import pandas as pd
import numpy as np

def read_data():
    df = pd.read_csv(r"DMDW\pr2_DataSet.csv")
    df = df.sort_values(by=['Age'])
    return df

def create_equal_freq_bin(df, bin_size):
    bins = np.array_split(df['Age'], len(df) // bin_size)
    df['Equal_Freq_Bin'] = np.concatenate([np.full(len(bin), i) for i, bin in enumerate(bins)])
    return df

def create_equal_width_bin(df, num_bins):
    bin_edges = np.linspace(df['Age'].min(), df['Age'].max(), num_bins + 1)
    df['Equal_Width_Bin'] = np.digitize(df['Age'], bin_edges, right=True) - 1
    return df

def add_statistics(df, bin_column):
    grouped = df.groupby(bin_column)['Age'].agg(['mean', 'median'])
    grouped.columns = ['Mean_Age', 'Median_Age']
    grouped = grouped.reset_index()
    df = df.merge(grouped, on=bin_column, how='left')
    return df

def smoothing_by_bin_means(df, bin_column):
    df[f'{bin_column}_Mean_Smoothed'] = df.groupby(bin_column)['Age'].transform('mean')
    return df

def smoothing_by_bin_medians(df, bin_column):
    df[f'{bin_column}_Median_Smoothed'] = df.groupby(bin_column)['Age'].transform('median')
    return df

def smoothing_by_bin_boundaries(df, bin_column):
    def boundary_smoothing(group):
        min_val = group.min()
        max_val = group.max()
        return group.apply(lambda x: min_val if abs(x - min_val) <= abs(x - max_val) else max_val)
    
    df[f'{bin_column}_Boundary_Smoothed'] = df.groupby(bin_column)['Age'].transform(boundary_smoothing)
    return df

def main():
    df = read_data()
    
    # Equal Frequency Binning
    df = create_equal_freq_bin(df, bin_size=10)
    df = add_statistics(df, 'Equal_Freq_Bin')
    df = smoothing_by_bin_means(df, 'Equal_Freq_Bin')
    df = smoothing_by_bin_medians(df, 'Equal_Freq_Bin')
    df = smoothing_by_bin_boundaries(df, 'Equal_Freq_Bin')
    
    # Create final DataFrame for Equal Frequency Binning
    df_equal_freq = df[['Age', 'Equal_Freq_Bin', 'Equal_Freq_Bin_Mean_Smoothed', 'Equal_Freq_Bin_Median_Smoothed', 'Equal_Freq_Bin_Boundary_Smoothed']]
    
    # Equal Width Binning
    df = create_equal_width_bin(df, num_bins=8)
    df = add_statistics(df, 'Equal_Width_Bin')
    df = smoothing_by_bin_means(df, 'Equal_Width_Bin')
    df = smoothing_by_bin_medians(df, 'Equal_Width_Bin')
    df = smoothing_by_bin_boundaries(df, 'Equal_Width_Bin')

    # Create final DataFrame for Equal Width Binning
    df_equal_width = df[['Age', 'Equal_Width_Bin', 'Equal_Width_Bin_Mean_Smoothed', 'Equal_Width_Bin_Median_Smoothed', 'Equal_Width_Bin_Boundary_Smoothed']]

    # Save results to Excel
    with pd.ExcelWriter(r"DMDW\Binned_and_Smoothed_Data.xlsx") as writer:
        df_equal_freq.to_excel(writer, sheet_name='Equal_Freq_Binning', index=False)
        df_equal_width.to_excel(writer, sheet_name='Equal_Width_Binning', index=False)
    
    print("The data has been successfully binned, smoothed, and saved to 'Binned_and_Smoothed_Data.xlsx'.")

if __name__ == "__main__":
    main()
