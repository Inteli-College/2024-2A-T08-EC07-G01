from sklearn.preprocessing import MinMaxScaler

def merge2(df_merge1):
    
    # Selecionando apenas as colunas específicas para normalização
    colunas_normalizacao = ['ID1NAME','ID1SOK', 'ID1SNOK', 'ID1DATA', 'ID2NAME', 'ID2SOK', 'ID2SNOK', 'ID2DATA', 'ID718NAME', 'ID718SOK', 'ID718SNOK', 'ID718DATA']

    # Inicializando o MinMaxScaler
    scaler = MinMaxScaler()

    # Aplicando a normalização
    merged_df[colunas_normalizacao] = scaler.fit_transform(merged_df[colunas_normalizacao])
    return merged_df
    
# Exemplo de chamada da função
if __name__ == "__main__":
    df_merge1 = 'df_merge1.csv'  # Caminho do arquivo de entrada
    merged_df= merge2(df_merge1)
    merged_df.to_csv("df_final", index=False)