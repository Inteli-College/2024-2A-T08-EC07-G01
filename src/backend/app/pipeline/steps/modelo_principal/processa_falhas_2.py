def execute(df):
    '''
    Remove columns from the DataFrame that are not present in vehicles that don't have failures.
    
    Parameters:
    df: pandas DataFrame
    '''
    colunas = ["MODELO", "COR", "MOTOR", "ESTACAO", "USUARIO", "HALLE", "DATA"]
    df = df.drop(columns=colunas, axis=1)
    return df


# Exemplo de chamada da função
if __name__ == "__main__":
    df = "df_falhas_trat1.csv"  # Caminho do arquivo de entrada
    df_falhas_trat2 = execute(df)
    df_falhas_trat2.to_csv("df_falhas_trat2", index=False)
