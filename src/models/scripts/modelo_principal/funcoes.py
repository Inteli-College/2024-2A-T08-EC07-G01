import pandas as pd

# Função para ler o DataFrame
def ler_arquivo(file_path):
    df = pd.read_csv(file_path) 
    return df

# Função para excluir NaN
def excluir_NaN(df):
    df = df.dropna()  # Tratamento de remoção de valores nulos
    return df