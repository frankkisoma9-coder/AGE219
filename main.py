import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 1. Load the merged data
print("Loading data...")
df = pd.read_csv("merged_FAOSTAT.csv")

# 2. Clean the data (Phase 3.1)
# Drop completely empty or unneeded helper code columns
columns_to_drop = ['Sex Code', 'Source Code', 'Source']
cleaned_df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

# Remove rows where the critical numeric 'Value' or 'Year' is missing
cleaned_df = cleaned_df.dropna(subset=['Value', 'Year'])

print("\n--- Cleaned Data Columns ---")
print(cleaned_df.columns)
print("\n--- Data Preview ---")
print(cleaned_df.head())

