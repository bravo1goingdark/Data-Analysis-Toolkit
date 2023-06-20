import pandas as pd

"""
A DataFrame is a 2-dimensional data structure that can store data of different types 
(including characters, integers, floating point values, categorical data and more) in columns.

Each column in Dataframe is Series
When selecting a single column of a pandas DataFrame, the result is a pandas Series. 
To select the column, use the column label in between square brackets [].

"""

df = pd.DataFrame(
    {
        "Name" : ["don" , "heroicmayank" , "Habibs" , "Master"],
        "Age" : [18 , 10 ,17 , 19],
        "Gender" : ["male" , "male" , "male" , "male"]
    }
    , 
)

print(df)
series = df["Age"]
print(series)
ser = pd.Series([10,15,20] , name="Age")
print(ser)

# Do something with a DataFrame or Series

max = df["Age"].max()
print(max)
maxx = ser.max()
print(maxx)

des = df.describe() # describe about data stored in dataframe such as count , mean , standard deviation , min , max
print(des)


# read and write tabular data

"""
read_csv() function to read data stored as a csv file into a pandas DataFrame. 
pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), 
each of them with the prefix read_*.

1--> .head(n) : will show first n number of rows and column
2--> .dtypes : will show all datatypes of variable 
3--> .info() : will show technical information about requested data
4--> .tail(n) : will show last n number of rows and column
"""


read = pd.read_csv("titanic.csv")
print(read.describe())
print(read.head(8)) 
print(read.dtypes)
read = read.to_excel("titanic.xlsx" , sheet_name= "passanger") ## convert diffrent file format extension to excel
excel = pd.read_excel("titanic.xlsx" , sheet_name="passanger") ## to read excel sheet

print(excel.head())

print(excel.info())


# subset of a DataFrame

ages = pd.read_csv("titanic.csv")
titanic = ages["name"] # selecting only name from the csv
print(titanic.head())
print(titanic.shape) # return number of rows in a dataframe/data table
age_20 = ages[ages["age"] < 20]
print(age_20.head(10))
print(age_20.shape)

cabin_23 = ages[(ages["cabin"] == 2) | (ages["cabin"] == 3)]
print(cabin_23.head())
shape = ages[["age" , "name"]].shape
print(shape)

# filter specific rows from a DataFrame

above_35  = ages[ages["age"] > 60]
print(above_35)
# from_ind = ages[ages["home.dest"]]
# print(from_ind)

# select specific rows and columns from a DataFrame
"""
The loc/iloc operators are required in front of the selection brackets [].
 When using loc/iloc, the part before the comma is the rows you want, 
and the part after the comma is the columns you want to select.

"""
adult_names = ages.loc[ages["age"] > 35, "name"]
print(adult_names)

col = ages.iloc[9:25, 2:5] #rows 10 till 25 and columns 3 to 5.
print(col)