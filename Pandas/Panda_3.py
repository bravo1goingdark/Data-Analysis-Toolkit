import pandas as pd
import matplotlib.pyplot as plt

air_qual = pd.read_csv("air.csv" , parse_dates=True , index_col= 0)
air_qual["london_mg_per_cubic"] = air_qual["station_london"]
print(air_qual.head())
air_qual["ratio_paris_antwerp"] = (air_qual["station_paris"] / air_qual["station_antwerp"])
print(air_qual.head())

air_quality_renamed = air_qual.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
"""
The rename() function can be used for both row labels and column labels.
Provide a dictionary with the keys the current names and the values the new names to update the corresponding names.

"""
print(air_quality_renamed.head())

# calculate summary statistics

titanic = pd.read_csv("titanic.csv")
titpd = titanic.agg(
    {
        "age" : ["min" , "max" , "median" , "skew"],
        "fare" : ["min" , "max" , "median" , "mean"]
    }
)
print(titpd)

"""
As our interest is the average age for each gender, a subselection on these two columns is made first:
titanic[["Sex", "Age"]]. Next, the groupby() method is applied on the Sex column to make a group per category.
The average age for each gender is calculated and returned

"""
group = titanic[["sex" , "age"]].groupby("sex").mean()
print(group)

groupti = titanic.groupby("sex").mean(numeric_only=True)
print(groupti)

# Count number of records by category
"""
The value_counts() method counts the number of records for each category in a column.

"""
cou = titanic["pclass"].value_counts()
print(cou)

num = titanic.groupby("pclass")["pclass"].count()
print(num)