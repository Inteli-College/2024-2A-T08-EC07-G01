import pandas as pd

def merge1(df_resultados, df_falhas):
    merged_df = pd.merge(df_resultados, df_falhas, on='KNR', how='left')
    # Adiciona 0 em todos os NaN
    merged_df = merged_df.fillna(0)
    return merged_df
    
# Exemplo de chamada da função
if __name__ == "__main__":
    df_resultados = 'df_resultados_trat2.csv'  # Caminho do arquivo de entrada
    df_falhas = "df_falhas_trat2.csv"
    merged_df= merge1(df_resultados, df_falhas)
    merged_df.to_csv("df_merge1", index=False)