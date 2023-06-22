import numpy as np
import pandas as pd

air_quality_no2 = pd.read_csv("air_quality_long.csv",parse_dates=True)

air_quality_no2_all = air_quality_no2[["date.utc", "location","parameter", "value"]]

print(air_quality_no2_all.head())