import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os

tempdf=pd.read_csv(r'C:\\Users\\zucky\\OneDrive\\Desktop\\made-template\\data\\temperatures.csv', delimiter=',')
print(tempdf)
tempdf.rename(columns={'YEAR': 'Year'}, inplace=True)
df = tempdf.sort_values("Year", ascending=False)
new_df = df[0:8]
df1 = new_df.drop(new_df.loc[:, 'JAN-FEB':'OCT-DEC'].columns, axis=1)
print(df1.head(20))


df2 = pd.read_csv(r'C:\\Users\\zucky\\OneDrive\Desktop\\made-template\data\\co2_emission.csv', delimiter=',')
print(df2.head(5))
df2 = df2.sort_values(by='Entity', ascending=True)
df2 = df2[(df2["Entity"] == "India") & (df2["Year"] >= 2010)]
df2 = df2.drop(['Code'], axis=1)
df2.rename(columns={'Entity': 'Country'}, inplace=True)
df2.rename(columns={'Annual CO₂ emissions (tonnes )': 'emmissionslarge'}, inplace=True)
print(df2.head(10))

# Merge DataFrames
merged_df = pd.merge(df1, df2, left_on='Year', right_on='Year', how='inner')

# SQLite Connection
sqlite_file_path = 'merged_data.sqlite'
sqlite_connection_string = f'sqlite:///{sqlite_file_path}'
engine = create_engine(sqlite_connection_string)

# Save to SQLite database
merged_df.to_sql('merged_data', engine, index=False, if_exists='replace')

print("Merged data saved to SQLite file:", sqlite_file_path)

