import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
#What is a Series
a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
#Labels
print(myvar[0])
#Create Labels
myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
#Key/Value Objects as Series
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
#DataFrames
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 
#refer to the row index:
print(df.loc[0])
#use a list of indexes:
print(df.loc[[0, 1]])
#Named Indexes
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
#refer to the named index:
print(df.loc["day2"])
#Load Files Into a DataFrame
df1 = pd.read_csv('data.csv')

print(df1) 
#max_rows
print(pd.options.display.max_rows) 
#Read JSON
df2 = pd.read_json('data.json')

print(df2.to_string()) 
#Viewing the Data
print(df1.head(10))
print(df2.head(10))
#Info About the Data
print(df1.info()) 
print(df2.info()) 
#Checking Pandas Version
print(pd.__version__)