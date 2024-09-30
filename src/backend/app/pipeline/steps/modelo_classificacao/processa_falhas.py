import pandas as pd

def execute(df):
    """
    Function to prepare the data for the classification model, using the fails dataset (i.e., the dataset after the main model is run).

    Parameters:
    df: pandas DataFrame
    """
    df_brute = df.dropna()

    df = df_brute[df_brute["S_GROUP_ID"] != "#MULTIVALUE"].copy()

    df["S_GROUP_ID"] = df["S_GROUP_ID"].astype(int)

    df = df.drop(["USUARIO", "FALHA", "MODELO", "ESTACAO", "HALLE", "MOTOR", "COR"], axis=1)

    df_one_hot = pd.get_dummies(df, columns=["S_GROUP_ID"])

    s_group_columns = [
        "S_GROUP_ID_-2",
        "S_GROUP_ID_1",
        "S_GROUP_ID_2",
        "S_GROUP_ID_4",
        "S_GROUP_ID_5",
        "S_GROUP_ID_133",
        "S_GROUP_ID_137",
        "S_GROUP_ID_140",
        "S_GROUP_ID_9830946",
    ]

    for col in s_group_columns:
        if col not in df_one_hot.columns:
            df_one_hot[col] = 0

    df_one_hot[s_group_columns] = df_one_hot[s_group_columns].astype(int)

    grouped_df = (
        df_one_hot.groupby("KNR")
        .agg({col: "sum" for col in s_group_columns})
        .reset_index()
    )

    grouped_df[s_group_columns] = grouped_df[s_group_columns].astype(bool)

    return grouped_df
