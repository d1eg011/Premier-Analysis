import pandas as pd

df_1 = pd.read_csv("/home/diego/Premier-Analysis/Daily_data/2025-07-11.csv", sep=';')
df_2 = pd.read_csv("/home/diego/Premier-Analysis/Daily_data/2025-07-12.csv", sep=';')

df_1.insert(0, "Date", "2025-07-11") # Add date column
df_2.insert(0, "Date", "2025-07-12") # Add date column

master_file = "/home/diego/Premier-Analysis/all_data.csv" # Master csv

df_combined = pd.concat([df_1, df_2], ignore_index=True)

print(df_combined.columns.tolist())

# Save updated master file
df_combined.to_csv(master_file, index=False, sep=';')




