import pandas as pd
import csv

# Set the file path
file_path = 'DMDW/pr1_imports-85.csv'
df = pd.read_csv(file_path)

# Get the number of columns
no_columns = len(df.columns)

# Create a replacement dictionary
replacement = {}

for i, col in enumerate(df.columns):
    replacement[col] = f'nan{i+1}'

print(replacement)

# Replace '?' with the respective nan replacement
for col, replacement_value in replacement.items():
    df[col] = df[col].replace('?', replacement_value)

print(df)

# Save the updated DataFrame to a new CSV file
output_file_path = 'DMDW/output1a.csv'
df.to_csv(output_file_path, index=False)

print(f"File saved to {output_file_path}")
