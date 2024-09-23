import pandas as pd
import models.scripts.funcoes as funcoes


def script1(file_path):
    df = funcoes.ler_arquivo(file_path)
    df= funcoes.excluir_NaN(df)
    df['DATA'] = pd.to_datetime(df['DATA'], errors='coerce')
    return df

# Exemplo de chamada da função
if __name__ == "__main__":
    file_path = 'arquivo_de_entrada.csv'  # Caminho do arquivo de entrada
    df_resultados_trat1 = script1(file_path)
    df_resultados_trat1.to_csv("df_resultados_trat1.csv", index=False)


