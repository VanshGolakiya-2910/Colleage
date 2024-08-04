import pandas as pd 
import numpy as np  
import shutil
df=pd.read_csv(r"DMDW\pr1_imports-85.csv")
df.iloc[:, 1:] = df.iloc[:, 1:].replace('?', np.nan)
# df['normalized-losses']=df['normalized-losses'].astype(float)
# mean2=df['normalized-losses'].mean()
# df['normalized-losses'].fillna(mean2,inplace=True)
# print(df['normalized-losses'])


for col in df.columns:
    if df[col].isnull().any():
        mode_dtype = df[col].apply(lambda x: type(x).__name__).mode()[0]
        if mode_dtype == 'str':
            mode_value=df[col].mode()
            df[col].fillna(mode_value, inplace=True)       
        else:
            df[col] = pd.to_numeric(df[col], errors='coerce').astype(float)
            mean_value = df[col].mean(skipna=True)
            df[col].fillna(mean_value, inplace=True)
print(df)


# Write the modified DataFrame back to the original CSV file
df.to_csv(r"imports-85-pr2-modified.csv", index=False)

# Write the modified DataFrame back to the original CSV file
# df.to_csv(r"imports-85-pr2.csv", index=False)
