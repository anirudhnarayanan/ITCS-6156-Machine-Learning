import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

#!tail -30 weatherAUS.csv
df = pd.read_csv("weatherAUS.csv")
print(df.columns[df.isna().any()].tolist())

#print df.iat[3,6] == df.iat[5953,6]
#print pd.isnull(df["Evaporation"][5955:5960]).all()
for item in list(df.columns.values):
    na_len = df[item].isna().sum()
    total_len = df[item].count()
    
    if na_len > 0.7*total_len:
        del df[item]


columns = list(df.columns.values)
col = 0
for index,row in df.iterrows():
    removed = False
    col = 0
    while col < len(columns) and removed == False:
        if row[columns[col]] != row[columns[col]]:
            df.drop(index, inplace=True)
            removed = True
        col = col+1
        
print df.shape
