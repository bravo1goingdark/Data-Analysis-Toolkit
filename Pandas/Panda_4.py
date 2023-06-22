import pandas as pd
import matplotlib.pyplot as plt


# reshape the layout of table

titanic = pd.read_csv("titanic.csv", index_col="age")
print(titanic.head())

airq = pd.read_csv("air_quality_long.csv" , index_col="date.utc" , parse_dates=True)
print(airq.head())

"""
With DataFrame.sort_values(), the rows in the table are sorted according to the defined column(s). 
The index will follow the row order.

"""

print(titanic.sort_values(by="age").head())
print(titanic.sort_values(by=["age" , "pclass"], ascending=False).head())


no2 = airq[airq["parameter"] == "no2"]
print(no2.head())
no2_subset = no2.sort_index().groupby(["location"]).head(2)
print(no2_subset)

# The pivot() function is purely reshaping of the data: a single value for each index/column combination is required.
# (long to wide format)
piv = no2_subset.pivot(columns="location" , values="value")
print(piv.head())

pivplot = no2.pivot(columns="location" , values="value").plot()
print(plt.show())

# The pandas.melt() method on a DataFrame converts the data table from wide format to long format. 
# The column headers become the variable names in a newly created column.
#(wide to long format)
new = piv.melt(id_vars="date.utc")
print(new)