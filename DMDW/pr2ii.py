import pandas as pd
import numpy as np

file_path = 'DMDW\pr1_imports-85.csv'
df = pd.read_csv(file_path)

# Helper function to check if the mode of a column is int or float
def is_mode_numeric(column):
    mode = column.mode()
    if not mode.empty:
        return pd.api.types.is_numeric_dtype(mode)
    return False

# Replace '?' with NaN if the mode of the column is numeric
for col in df.columns:
    if is_mode_numeric(df[col]):
        df[col] = pd.to_numeric(df[col], errors='coerce')
    else:
        df[col] = df[col].replace('?', np.nan)

# Replacing '?' with mean values
replacement_mean = {}
for col in df.columns:
    if df[col].dtype in [np.float64, np.int64]:
        replacement_mean[col] = df[col].mean()
        df[col] = df[col].fillna(replacement_mean[col])  # Direct assignment

print("\n\nMean values for each column:", replacement_mean)
df.to_csv('DMDW\\output2_mean.csv', index=False)

# Replacing '?' with median values
replacement_median = {}
for col in df.columns:
    if df[col].dtype in [np.float64, np.int64]:
        replacement_median[col] = df[col].median()
        df[col] = df[col].fillna(replacement_median[col])  # Direct assignment

print("\n\nMedian values for each column:", replacement_median)
df.to_csv('DMDW\\output2_median.csv', index=False)

# Replacing '?' with mode values
replacement_mode = {}
for col in df.columns:
    if df[col].dtype in [np.float64, np.int64]:
        mode = df[col].mode()
        if not mode.empty:
            replacement_mode[col] = mode[0]
            df[col] = df[col].fillna(replacement_mode[col])  # Direct assignment

print("\n\nMode values for each column:", replacement_mode)
df.to_csv('DMDW\\output2_mode.csv', index=False)