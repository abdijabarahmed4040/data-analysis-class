import pandas as pd 

data = pd.read_csv("Train.csv")
#loading data
print(data.info())
#print(data.tail())
#(data.head())
print(data.describe())
#checking out the data -
#cleaning
# head and tail 
# deascribe info
#cleanig
print(data.isnull().sum())


@#data dropna(subset["Age"], inplace=true)

data["Age"] = date["age"].fillna(date["Age"].mean())
print(data.info)

#data - 1. numerical numbers 2.catogorical object

catagoricak = data.dtypes[data.dtypes == "object"].index
print(data[catogarical].describe())


print(catagorical)







