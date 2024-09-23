import pandas as pd
import models.scripts.funcoes as funcoes

def script1 (file_path):
    df = funcoes.ler_arquivo(file_path)
    df['FALHA'] = df['FALHA'].str.upper()
    # Remove todas as linhas com KNR repetido
    df = df.drop_duplicates(subset=['KNR'])
    df['FALHA'] = 1



# Exemplo de chamada da função
if __name__ == "__main__":
    file_path = 'nome_do_arquivo.csv'  # Caminho do arquivo de entrada
    df_falhas_trat1 = script1(file_path)
    df_falhas_trat1.to_csv("df_falhas_trat1", index=False)