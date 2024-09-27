import pandas as pd

def execute(df):
    # TODO: Change the function, to also input the columns to remove
    '''
    Remove columns from the DataFrame that are not present in vehicles that don't have failures.

    Parameters:
    df: pandas DataFrame
    '''
    colunas = ['MODELO', 'COR', 'MOTOR', 'ESTACAO', 'USUARIO', 'HALLE', 'DATA']
    df = df.drop(columns=colunas, axis=1)
    return df


# Exemplo de chamada da função
if __name__ == "__main__":
    df = 'df_falhas_trat1.csv'  # Caminho do arquivo de entrada (??????) Deveria ser o DF nao caminho do DF
    df_falhas_trat2 = execute(df)
    df_falhas_trat2.to_csv("df_falhas_trat2", index=False)