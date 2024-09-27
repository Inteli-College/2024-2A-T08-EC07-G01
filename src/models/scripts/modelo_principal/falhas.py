import pandas as pd

def execute (file_path):
    '''
    Reads a CSV file and returns a DataFrame with the 'FALHA' column converted to 1 and all duplicates removed.

    Parameters:
    file_path: str
    '''
    df = pd.read_csv(file_path)
    df['FALHA'] = df['FALHA'].str.upper()
    # Remove todas as linhas com KNR repetido
    df = df.drop_duplicates(subset=['KNR'])
    df['FALHA'] = 1

    return df


# Exemplo de chamada da função
if __name__ == "__main__":
    file_path = 'nome_do_arquivo.csv'  # Caminho do arquivo de entrada
    df_falhas_trat1 = execute(file_path)
    df_falhas_trat1.to_csv("df_falhas_trat1", index=False)