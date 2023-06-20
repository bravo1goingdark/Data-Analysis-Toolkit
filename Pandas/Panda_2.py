# plot in pandas

import pandas as pd
import matplotlib.pyplot as plt


"""
The usage of the index_col and parse_dates parameters of the read_csv
function to define the first (0th) column as index of the resulting DataFrame 
and convert the dates in the column to Timestamp objects, respectively.

"""
air_qual = pd.read_csv("air.csv" , index_col=0 , parse_dates=True)
print(air_qual.head())
print(air_qual.plot())
print(plt.show())

print(air_qual["station_paris"].plot())
print(plt.show())

comp = air_qual.plot.scatter(x="station_london" , y="station_paris" , alpha = 0.5)
print(comp.plot())
print(plt.show())
print(air_qual.plot.box()) # returns box plot
print(plt.show())

axs = air_qual.plot.area(figsize = (12,14) , subplots = True)
print(plt.show())