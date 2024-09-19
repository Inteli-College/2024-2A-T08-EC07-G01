import pandas as pd

def script2(df):
    colunas = ['MODELO', 'COR', 'MOTOR', 'ESTACAO', 'USUARIO', 'HALLE', 'DATA']
    df = df.drop(columns=colunas, axis=1)


# Exemplo de chamada da função
if __name__ == "__main__":
    file_path = 'nome_do_arquivo.csv'  # Caminho do arquivo de entrada
    df_falhas_trat2 = script2(file_path)
    df_falhas_trat2.to_csv("df_falhas_trat2", index=False)