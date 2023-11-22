#!/bin/bash
python3 /project/pipeline.py

#import data for temperatures

import pandas as pd
tempdf = pd.read_csv(r"D:\FAU\Semester 3\MADE\Datasets\temp\temperatures.csv")
tempdf.head()

#remove unwanted columns from 1901 until 2009
#sort the dataset in ascending order of year - keep data from last decade
#remove rows before 2010
tempdf = tempdf.sort_values("YEAR", ascending=False)
tempdf = tempdf[0:8]
#remove columns with quarterly records
tempdf = tempdf.drop(tempdf.loc[:, 'JAN-FEB':'OCT-DEC'].columns, axis=1)
tempdf.head(20)

selected_columns = tempdf[['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']]

# Add the values of the data across the selected columns
#average temperature through 2010 to 2017
tempdf["Avg Temp"] = selected_columns.sum(axis=1)/8
tempdf.head(20)


#import data for CO2 emissions

import pandas as pd
codf = pd.read_csv(r"D:\FAU\Semester 3\MADE\Datasets\co2_emission.csv")
codf.head()

#sort the data
codf = codf.sort_values(by='Entity', ascending=True)
#only select the data for India between 2010 and 2017
codf = codf[(codf["Entity"] == "India") & (codf["Year"] >= 2010)]
codf = codf.drop(['Code'], axis=1)
# Rename the 'Entity' column to 'Country'
codf.rename(columns={'Entity': 'Country'}, inplace=True)
codf.head(10)
