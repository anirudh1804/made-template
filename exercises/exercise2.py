#import libraries 
import sqlite3
import pandas as pd

#read data
df = pd.read_csv(r"D:\FAU\Semester 3\MADE\Exercise 2\D_Bahnhof_2020_alle.csv")


#create connection sqlite
conn = sqlite3.connect('trainstops.sqlite')
c = conn.cursor()
c.execute('''CREATE TABLE trainstops (EVA_NR INT, DS100 VARCHAR, IFOPT TEXT, NAME TEXT, Verkehr TEXT, Laenge FLOAT, Breite FLOAT, Betreiber_Name TEXT, Betreiber_Nr INT)''')
datatypes = {
            "EVA_NR": int,
            "DS100": str,
            "IFOPT": str,
            "NAME": str,
            "Verkehr": str,
            "Laenge": float,
            "Breite": float,
            "Betreiber_Name": str,
            "Betreiber_Nr": int,
        }

#sort out invalid data
#drop the Status column
df = df.drop(['Status'], axis=1)

#Valid "Verkehr" values are "FV", "RV", "nur DPN"
valid_verkehr_values = ['FV', 'RV', 'nur DPN']
df = df[df['Verkehr'].isin(valid_verkehr_values)]

#Valid "Laenge", "Breite" values are geographic coordinate system values between and including -90 and 90
df = df[(df['Laenge'] >= -90.0) & (df['Laenge'] <= 90.0)]
df = df[(df['Breite'] >= -90.0) & (df['Breite'] <= 90.0)]

#Valid "IFOPT" pattern in regex
regex = r"^[a-zA-Z]{2}:\d+:\d+(:\d+)?$"
df = df[df['IFOPT'].str.extract(regex)]

#Empty cells are considered invalid
df = df.dropna(inplace=False)
df = df.astype(datatypes)

#create sqlite
df.to_sql('trainstops', conn, if_exists='replace', index=False)