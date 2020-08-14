import numpy as np
import pandas as pd
import datetime as date
from sklearn.preprocessing import LabelEncoder

x=pd.read_csv(r"C:\Users\ravi\Desktop\datasets/weatherHistory.csv")

print(x.info())
x["new_dates"]=pd.to_datetime(x["Formatted Date"])


print(x["Formatted Date"].head())


x["Formatted Date"]=x["Formatted Date"].str.split().map(lambda x:x[0])

x["new_dates"]=pd.to_datetime(x["Formatted Date"])

x["year"]=x["new_dates"].dt.year
x["month"]=x["new_dates"].dt.month
x["day"]=x["new_dates"].dt.day

le=LabelEncoder()

x["new_summary"]=le.fit_transform(x["Summary"])

print(x["Temperature "].mean(),x["Temperature "].median(),x["Temperature "].mode())

x.drop(x.index[20:41:10],inplace=True)

x.drop("Precip Type",axis=1,inplace=True)

print(x.info())