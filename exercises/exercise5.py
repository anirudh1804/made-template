import zipfile
import urllib.request
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float

# Downloading and unzipping data
zip = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
zippath = "GTFS.zip"
filename = "stops.txt"

urllib.request.urlretrieve(zip, zippath)
with zipfile.ZipFile(zippath, 'r') as zip_ref:
    zip_ref.extract(filename)

# Reshaping data - by using only columns : "stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"

columns = ["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"]

df = pd.read_csv(filename, usecols=columns)

# Filtering data
df = df[df["zone_id"] == 2001]

# Validating data
# Text validation for stop_name
df["stop_name"] = df["stop_name"].astype(str)

# Geographic coordinates validation for stop_lat and stop_lon
valid_coordinate_range = (-90, 90)
valid_lat_range = df["stop_lat"].between(*valid_coordinate_range)
valid_lon_range = df["stop_lon"].between(*valid_coordinate_range)
df = df[valid_lat_range & valid_lon_range]

# Use fitting SQLite types & Write data into SQLite database
engine = create_engine('sqlite:///gtfs.sqlite')
metadata = MetaData()
stops_table = Table('stops', metadata,
                    Column('stop_id', Integer, primary_key=True),
                    Column('stop_name', String),
                    Column('stop_lat', Float),
                    Column('stop_lon', Float),
                    Column('zone_id', Integer))

metadata.create_all(engine)

# Write datatype

df.to_sql('stops', con=engine, if_exists='replace', index=False, dtype={
    'stop_id': Integer,
    'stop_name': String,
    'stop_lat': Float,
    'stop_lon': Float,
    'zone_id': Integer
})