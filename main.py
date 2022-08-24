import csv
import pandas as pd

df = pd.read_csv("merged.csv")
print(df.columns)

del df ["lum"]
del df ["star_name"]
del df ["distance.1"]
del df ["mass.1"]
del df ["radius.1"]
del df ["Unnamed: 0"]
del df ["Unnamed: 6"]
print(df.columns)
df.to_csv("main.csv")