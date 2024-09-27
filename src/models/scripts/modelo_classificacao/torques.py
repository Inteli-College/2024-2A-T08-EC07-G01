import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def preprocess_torque(df):
    '''
    Makes the pre-processement of the VALUE column in the torques dataset.

    Parameters:
    df: pandas DataFrame
    '''

    df["VALUE"] = df["VALUE"].str.strip()
    df["VALUE"] = df["VALUE"].replace('', pd.NA)
    df["VALUE"] = df["VALUE"].str.replace(',', '.', regex=False)
    df["VALUE"] = pd.to_numeric(df["VALUE"], errors='coerce') 
    return df.dropna(subset=["VALUE"])

def aggregate_by_knr_unit(df):
    '''
    Group the data by KNR and UNIT and pivot the data.

    Parameters:
    df: pandas DataFrame
    '''

    df_grouped = df.groupby(['KNR', 'UNIT'])['VALUE'].mean().reset_index()
    return df_grouped.pivot(index='KNR', columns='UNIT', values='VALUE').reset_index()

def normalize_columns(df, exclude_columns):
    '''
    Normalize the numeric columns of the DataFrame, and remove the UNIT and KNR columns.

    Parameters:
    df: pandas DataFrame
    exclude_columns: list of columns to exclude from normalization
    '''

    columns_to_normalize = df.columns.difference(exclude_columns)
    numeric_columns = df[columns_to_normalize].select_dtypes(include=[float, int]).columns
    scaler = MinMaxScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    return df

def execute(df):
    '''
    Main file script to preprocess the whole DataFrame.

    Parameters:
    df: pandas DataFrame
    '''
    
    df = df[df["UNIT"] != '          ']  # Remove onde UNIT tem espaços
    df["UNIT"] = df["UNIT"].str.strip() 
    df = preprocess_torque(df)

    df_pivot = aggregate_by_knr_unit(df)
    
    df_pivot.columns = df_pivot.columns.str.upper()

    df_pivot = normalize_columns(df_pivot, exclude_columns=['KNR', 'UNIT'])

    # Exemplo de como pode ser feito um merge, caso precise
    # df_resultados_final = df_merged.merge(df_pivot, on='KNR', how='left')

    return df_pivot

# Example function call
if __name__ == '__main__':
    file_path = 'resultados.csv' 
    df_torques = preprocess_data(file_path)
    df_torques.to_csv("df_torques", index=False)
    

