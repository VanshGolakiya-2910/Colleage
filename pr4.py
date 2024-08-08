import csv
import pandas as pd
import statistics

def add_data():
    print("Adding data to 'health_records.csv'...")
    age = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
    fat_per = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

    data = {'age': age, 'fat_per': fat_per}

    with open("health_records.csv", 'w', newline='') as csvfile:
        fieldnames = ['age', 'fat_per']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in zip(age, fat_per):
            writer.writerow({'age': row[0], 'fat_per': row[1]})

    print("Data successfully added to 'health_records.csv'.\n")

def read_data(data_path):
    print(f"Reading data from '{data_path}'...")
    df = pd.read_csv(data_path)
    print("Data successfully read.\n")
    return df

def mean_dev():
    print("Calculating mean, median, mode, and standard deviation for 'age' and 'fat_per'...")
    df = read_data("health_records.csv")

    age_mean = df['age'].mean()
    age_median = df['age'].median()
    age_mode = df['age'].mode().iloc[0]
    fat_per_mean = df['fat_per'].mean()
    fat_per_median = df['fat_per'].median()
    fat_per_mode = df['fat_per'].mode().iloc[0]
    age_dev = statistics.stdev(df['age'])
    fat_per_dev = statistics.stdev(df['fat_per'])

    df['age_mean'] = age_mean
    df['age_median'] = age_median
    df['age_mode'] = age_mode
    df['fat_per_mean'] = fat_per_mean
    df['fat_per_median'] = fat_per_median
    df['fat_per_mode'] = fat_per_mode
    df['age_dev'] = age_dev
    df['fat_per_dev'] = fat_per_dev

    df.to_csv('health_records_with_stats.csv', index=False)
    print("Statistics added to 'health_records_with_stats.csv'.\n")

def z_score():
    print("Calculating Z-scores for 'age' and 'fat_per'...")
    df = read_data("health_records.csv")
    
    def calculate_z_score(mean, stdev, col):
        z_col = [(i - mean) / stdev for i in df[col]]
        return z_col
    
    df['age_z_score'] = calculate_z_score(df['age'].mean(), statistics.stdev(df['age']), 'age')
    df['fat_per_z_score'] = calculate_z_score(df['fat_per'].mean(), statistics.stdev(df['fat_per']), 'fat_per')

    df.to_csv('health_records_with_z_score.csv', index=False)
    print("Z-scores added to 'health_records_with_z_score.csv'.\n")

def decimal_scaling_normalization():
    print("Performing decimal scaling normalization for 'age' and 'fat_per'...")
    df = read_data("health_records.csv")
    
    def calculate_decimal_scaling_normalization(col):
        max_val = max(abs(df[col].min()), abs(df[col].max()))
        scaling_factor = 10 ** len(str(int(max_val)))
        return df[col] / scaling_factor
    
    df['age_deci_norm'] = calculate_decimal_scaling_normalization('age')
    df['fat_deci_norm'] = calculate_decimal_scaling_normalization('fat_per')

    df.to_csv('health_records_with_decimal_norm.csv', index=False)
    print("Decimal scaling normalization complete. Results saved to 'health_records_with_decimal_norm.csv'.\n")

if __name__ == "__main__":
    add_data()  # Make sure the data is added first
    mean_dev()  # Calculate mean, median, mode, and standard deviation
    z_score()  # Calculate Z-scores
    decimal_scaling_normalization()  # Perform decimal scaling normalization
