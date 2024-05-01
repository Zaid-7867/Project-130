import pandas as pd
import csv
df=pd.read_csv("total_stars.csv")
print(df.head())
df.columns
df.drop(["Unnamed: 0","Unnamed: 6","Star_name.1","Distance.1","Radius.1","Luminosity"],axis=1,inplace=True)
print(df)