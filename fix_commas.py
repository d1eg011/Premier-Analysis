import pandas as pd

#Just apply this to any csv separated by ; to overwrite it

df = pd.read_csv("Daily_Data/2025-07-13.csv", sep=";")
df.to_csv("Daily_Data/2025-07-13.csv", index=False)  # Default separator is comma