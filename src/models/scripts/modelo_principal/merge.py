import pandas as pd


def execute(df_resultados, df_falhas):
    '''
    Script to merge the results and failures DataFrames.

    Parameters:
    df_resultados: str
    df_falhas: str
    '''

    # !!!TODO: Should have been a DataFrame, not a file path (takes time to read the .csv again)!!!

    resultados = pd.read_csv(df_resultados)
    falhas = pd.read_csv(df_falhas)
    merged_df = pd.merge(resultados, falhas, on='KNR', how='left')
    # Adiciona 0 em todos os NaN
    merged_df = merged_df.fillna(0)
    return merged_df
    
# Exemplo de chamada da função
if __name__ == "__main__":
    df_resultados = 'df_resultados_trat2.csv'  # Caminho do arquivo de entrada
    df_falhas = "df_falhas_trat2.csv"
    merged_df= execute(df_resultados, df_falhas)
    merged_df.to_csv("df_merge", index=False)