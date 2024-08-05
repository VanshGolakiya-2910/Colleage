import pandas as pd
import numpy as np

# Read the CSV file
file_path = 'DMDW/pr1_imports-85.csv'
df = pd.read_csv(file_path)

# Helper function to check if the majority of the values in a column are numeric
def is_majority_numeric(column):
    # Replace '?' with NaN
    column = column.replace('?', np.nan)
    # Drop NaN values
    column = column.dropna()
    # Check if the majority of the values are numeric
    numeric_count = pd.to_numeric(column, errors='coerce').notnull().sum()
    return numeric_count > (len(column) / 2)

# Replace '?' with NaN in all columns
df.replace('?', np.nan, inplace=True)

# Create separate DataFrames for each replacement type
df_mean = df.copy()
df_median = df.copy()
df_mode = df.copy()

# Replacing NaN values with mean values
replacement_mean = {}
for col in df_mean.columns:
    if is_majority_numeric(df_mean[col]):
        df_mean[col] = pd.to_numeric(df_mean[col])
        replacement_mean[col] = df_mean[col].mean()
        df_mean[col].fillna(replacement_mean[col], inplace=True)

print("\n\nMean values for each column:", replacement_mean)
df_mean.to_csv('DMDW/output2_mean.csv', index=False)

# Replacing NaN values with median values
replacement_median = {}
for col in df_median.columns:
    if is_majority_numeric(df_median[col]):
        df_median[col] = pd.to_numeric(df_median[col])
        replacement_median[col] = df_median[col].median()
        df_median[col].fillna(replacement_median[col], inplace=True)

print("\n\nMedian values for each column:", replacement_median)
df_median.to_csv('DMDW/output2_median.csv', index=False)

# Replacing NaN values with mode values
replacement_mode = {}
for col in df_mode.columns:
    if is_majority_numeric(df_mode[col]):
        df_mode[col] = pd.to_numeric(df_mode[col])
        mode = df_mode[col].mode()
        if not mode.empty:
            replacement_mode[col] = mode[0]
            df_mode[col].fillna(replacement_mode[col], inplace=True)

print("\n\nMode values for each column:", replacement_mode)
df_mode.to_csv('DMDW/output2_mode.csv', index=False)
