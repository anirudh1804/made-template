#!/usr/bin/env python
# coding: utf-8

# In[4]:


#import data for temperatures

import pandas as pd
tempdf=pd.read_csv("../data/temperatures.csv")
tempdf.head()

#remove unwanted columns from 1901 until 2009
#sort the dataset in ascending order of year - keep data from last decade
#remove rows before 2010
tempdf.rename(columns={'YEAR': 'Year'}, inplace=True)
df = tempdf.sort_values("Year", ascending=False)
new_df = df[0:8]
#remove columns with quarterly records
df1 = new_df.drop(new_df.loc[:, 'JAN-FEB':'OCT-DEC'].columns, axis=1)
df1.head(20)

# In[5]:

#import co2 emissions

import pandas as pd
import matplotlib.pyplot as plt
df2 = pd.read_csv("../data/co2_emission.csv")
df2.head()
#sort the data
df2 = df.sort_values(by='Entity', ascending=True)
#only select the data for India between 2010 and 2017
df2 = df[(df["Entity"] == "India") & (df["Year"] >= 2010)]
df2 = df.drop(['Code'], axis=1)
# Rename the 'Entity' column to 'Country'
df2.rename(columns={'Entity': 'Country'}, inplace=True)
df2.rename(columns={'Annual CO₂ emissions (tonnes )': 'emmissionslarge'}, inplace=True)
df2.head(10)

# Assuming you have two DataFrames: temperature_df and co2_emissions_df

# Merge the two DataFrames
merged_df = pd.merge(df1, df2, left_on='ANNUAL', right_on='emmissionslarge', how='inner')

# Save the merged DataFrame to an SQLite file
sqlite_file_path = 'merged_data.db'
merged_df.to_sql('merged_data', sqlite_file_path, index=False, if_exists='replace')

print("Merged data saved to SQLite file:", sqlite_file_path)


