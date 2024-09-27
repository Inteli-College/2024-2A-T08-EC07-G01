import pandas as pd

def execute(file_path):
    '''
    Script to read a CSV file and return a DataFrame with the 'DATA' column converted to datetime and all NaN values removed.

    Parameters:
    file_path: str
    '''
    df = pd.read_csv(file_path)
    df= df.dropna() 
    df['DATA'] = pd.to_datetime(df['DATA'], errors='coerce')
    return df

# Exemplo de chamada da função
if __name__ == "__main__":
    file_path = 'arquivo_de_entrada.csv'  # Caminho do arquivo de entrada
    df_resultados_trat1 = execute(file_path)
    df_resultados_trat1.to_csv("df_resultados_trat1.csv", index=False)


