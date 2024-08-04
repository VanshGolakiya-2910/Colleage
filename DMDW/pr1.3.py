import pandas as pd
import numpy as np
def read_file(): #read the file 
    df=pd.read_csv(r'DMDW\pr1_imports-85.csv')
    return df
# num_of_column should be cleaned 
def num_of_col_clean():
    df=read_file()
    for i in  df['num-of-doors']:  # changing '?' with NaN
        if i == '?': 
            df['num-of-doors']=df['num-of-doors'].replace('?',np.nan)
    value_count=df['num-of-doors'].value_counts() # find the most occuring value 
    m_value=value_count.idxmax()
    df['num-of-doors']=df['num-of-doors'].replace(np.nan,m_value)  #replace the Nan with the most occuring value

# Fucntion to 
def create_group(df):
    grouped=df.groupby('num-of-doors')
    group_a=grouped.get_group('two')
    group_b=grouped.get_group('four')
    return group_a , group_b
def fill_values(df, column_name):
    d_types = df[column_name].apply(type)
    mode_type = d_types.mode()[0]
    
    # Replace '?' with NaN
    df[column_name] = df[column_name].replace('?', np.nan)
    
    if mode_type == str:
        # Find the most occurring value
        value_counts = df[column_name].value_counts()
        m_value = value_counts.idxmax()
        
        # Replace NaN with the most occurring value
        df[column_name] = df[column_name].fillna(m_value)
        
    elif mode_type in [int, float]:
        # Convert column to numeric to handle mixed data types
        df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
        
        # Fill NaN with the mean of the column (numeric only)
        df[column_name] = df[column_name].fillna(df[column_name].mean())
    
    return df

def group_change():
    df=read_file()
    group_a , group_b =create_group(df)
    for i in group_a:
        df=fill_values(df,i)
    for i in group_b:
        df=fill_values(df,i)

    group_a , group_b =create_group(df)
    
    print(group_a)
    print(group_b)
num_of_col_clean()
group_change()

    