def execute(df_torques, df_falhas):
    '''
    Merges both the torques and fails datasets, using the KNR column as the key.

    Parameters:
    df_torques: pandas DataFrame of torques
    df_falhas: pandas DataFrame of fails
    '''
    df_merged = df_torques.merge(df_falhas, on="KNR", how="left")
    return df_merged
