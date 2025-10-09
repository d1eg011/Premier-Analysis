import pandas as pd

file_path = "/home/diego/Premier-Analysis/all_data.csv"

df = pd.read_csv(file_path)
df = df[df["Date"] != "2025-10-09"]
df.to_csv(file_path, index=False)
