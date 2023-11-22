import pandas as pd
import io
import re
from sqlalchemy import create_engine

#exttract train data from csv file
csv_url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"

# transform and seperate the data
df = pd.read_csv(csv_url, delimiter=';')

#drop the status column
del df["Status"]

#sort data
#keep valid data
valid_verkehr = {"FV": None, "RV": None, "nur DPN": None}

# drop invalid values
df = df.dropna(axis=0, how='any')  # Drop rows with any empty cells
df = df.query("Verkehr in @valid_verkehr")

#Validate IFOPT values 
pattern = re.compile(r"^\w{2}:\d+:\d+(?::\d+)?$")
valid_ifopt = df["IFOPT"].astype(str).str.contains(pattern, regex=True)
df = df.loc[valid_ifopt]

# Replacing , with . 
df['Laenge'] = df['Laenge'].str.replace(r',', '.')
df['Breite'] = df['Breite'].str.replace(r',', '.')

#geography coordinates system 
df['Laenge'] = df['Laenge'].astype(float)
df = df.query("-90 <= Laenge <= 90")

df['Breite'] = df['Breite'].astype(float)
df = df.query("-90 <= Breite <= 90")


#create the table
table_name = "trainstops"

# Define column data types
column_types = {
    "DS100": str,
    "EVA_NR": int,
    "Laenge": float,
    "Breite": float,
    "Verkehr": str,
    "IFOPT": str,
    "NAME": str,
    "Betreiber_Name": str,
    "Betreiber_Nr": int
    
    
}
df = df.astype(column_types)
# insert data into sqlite
df.to_sql(table_name, 'sqlite:///trainstops.sqlite', if_exists="replace", index=False)
