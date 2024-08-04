import pandas as pd
import numpy as np
def read_data():
    df=pd.read_csv("DMDW\pr2_DataSet.csv")
    df=df.sort_values(by=['Age'])
    return df
def create_bin(df):
    bin=[[0,10],[11,20],[21,30],[31,40],[41,50],[51,60],[61,70],[71,80]]
    bin_edges = [b[0] for b in bin] + [bin[-1][1]]
    df['Age_Bucket'] = pd.cut(df['Age'], bins=bin_edges, labels=False, include_lowest=True)
    return df
def save_to_excel(df, filename="DMDW/UpdatedDataSet.xlsx"):
    try:
        df.to_excel(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving the file: {e}")
def add_statistics(df):
    grouped = df.groupby('Age_Bucket').agg({'Age': ['mean', 'median']})
    grouped.columns = ['Mean_Age', 'Median_Age']
    grouped = grouped.reset_index()
    df = df.merge(grouped, on='Age_Bucket', how='left')
    return df
def save_to_mean_excle(df,filename="DMDW/meanDataSet.xlsx"):
    df['Age'] = df['Age_Bucket'].map(df.groupby('Age_Bucket')['Mean_Age'].first())
    try:
        df.to_excel(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving the file: {e}")
def save_to_median_excle(df,filename="DMDW/medianDataSet.xlsx"):
    df['Age'] = df['Age_Bucket'].map(df.groupby('Age_Bucket')['Median_Age'].first())
    try:
        df.to_excel(filename, index=False)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving the file: {e}")
def main():
    df=read_data()
    df=create_bin(df)
    df=add_statistics(df)
    save_to_excel(df)
    save_to_mean_excle(df)
    save_to_median_excle(df)
if __name__=='__main__':
    main()