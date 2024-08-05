import csv
import pandas as pd 
import numpy as np
import statistics

def add_data():
    age = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
    fat_per = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
    
    data = {'age': age, 'fat_per': fat_per}
    
    with open("health_records.csv", 'w', newline='') as csvfile:
        fieldnames = ['age', 'fat_per']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in zip(age, fat_per):
            writer.writerow({'age': row[0], 'fat_per': row[1]})
def read_data(data_path):
    df=pd.read_csv(data_path)
    return df
def mean_dev():
    df=read_data("D:\ET22BTCO039\health_records.csv")
    age_mean=df['age'].mean()
    age_median=df['age'].median()
    age_mode=df['age'].mode().iloc[0]
    fat_per_mean=df['fat_per'].mean()
    fat_per_median=df['fat_per'].median()
    fat_per_mode=df['fat_per'].mode().iloc[0]
    age_dev=statistics.stdev(df['age'])
    fat_per_dev=statistics.stdev(df['fat_per'])

    df['age_mean']=age_mean
    df['age_median']=age_median
    df['age_mode']=age_mode

    df['fat_per_mean']=fat_per_mean
    df['fat_per_median']=fat_per_median
    df['fat_per_mode']=fat_per_mode

    df['age_dev']=age_dev
    df['fat_per_dev']=fat_per_dev
    df.to_csv('health_records_with_stats', index=False)
def z_score():
    df=read_data("D:\ET22BTCO039\health_records.csv")
    def calculate_z_score(mean,stdev,col):
        z_col=[]
        for i in df[col]:
           value=(i-mean)/stdev
           z_col.append(value)
        return z_col
    for i in df:
        mean=df[i].mean()
        stdev=statistics.stdev(df[i])
        if i=='age':
            df['age_z_score']=calculate_z_score(mean,stdev,i)
        else:
            df['fat_per_z_score']=calculate_z_score(mean,stdev,i)

    df.to_csv('health_records_with_z_score', index=False)       
def decimal_scaling_normalization():
    df = read_data("D:\ET22BTCO039\health_records.csv")
    
    def calculate_decimal_scaling_normalization(col):
        decimal_norm = [i / 10**2 for i in df[col]]
        return decimal_norm
    
    df['age_deci_norm'] = calculate_decimal_scaling_normalization('age')
    df['fat_deci_norm'] = calculate_decimal_scaling_normalization('fat_per')
    
    df.to_csv('health_records_with_decimal_norm.csv', index=False)
decimal_scaling_normalization()
