import pandas as pd
import io
import re
from sqlalchemy import create_engine

# Step 1: Train stops data Extraction from provided CSV File
csv_url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"


# Step 2: Train stops CSV Data Transformation
df = pd.read_csv(csv_url, delimiter=';')

# Requirement 1: Drop the "Status" column
del df["Status"]

# Requirement 2: Drop rows with invalid values
valid_verkehr = {"FV": None, "RV": None, "nur DPN": None}

# Requirement 3: Drop rows with invalid values
df = df.dropna(axis=0, how='any')  # Drop rows with any empty cells
df = df.query("Verkehr in @valid_verkehr")

# Requirement 4: Validate IFOPT values based on the specified pattern
pattern = re.compile(r"^\w{2}:\d+:\d+(?::\d+)?$")
valid_ifopt = df["IFOPT"].astype(str).str.contains(pattern, regex=True)
df = df.loc[valid_ifopt]

# Replacing , with . 

df['Laenge'] = df['Laenge'].str.replace(r',', '.')
df['Breite'] = df['Breite'].str.replace(r',', '.')

df['Laenge'] = df['Laenge'].astype(float)
df = df.query("-90 <= Laenge <= 90")

df['Breite'] = df['Breite'].astype(float)
df = df.query("-90 <= Breite <= 90")


# Step 3: Data Loading
#db_engine = create_engine("sqlite:///trainstops.sqlite")
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
# Create table and insert data
df.to_sql(table_name, 'sqlite:///trainstops.sqlite', if_exists="replace", index=False)
