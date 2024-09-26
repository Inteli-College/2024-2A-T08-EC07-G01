# Estrutura de Pastas e Documentação dos Scripts

Para a automatização da preparação dos dados, foram desenvolvidos dois diretórios principais, cada um contendo scripts relacionados ao pré-processamento de dados e construção de modelos, além de um script global, que depois serão chamados numa pipeline orquestradora. A seguir, uma explicação de cada pasta e o que cada arquivo faz.

## Estrutura de Pastas

```bash
- modelo_classificacao
    |_ falhas.py
    |_ merge_torques_falhas.py
    |_ modelo.py
    |_ torques.py
- modelo_principal
    |_ falhas.py
    |_ falhas2.py
    |_ merge.py
    |_ modelo.py
    |_ resultado.py
    |_ resultado2.py
- preparacao.py 
```

### Descrição dos Arquivos

#### 1. Pasta `modelo_classificacao`

- **falhas.py**
    - Este script realiza o pré-processamento dos dados de falhas, removendo registros nulos, aplicando a codificação one-hot e agregando colunas para posterior uso nos modelos. Ele inclui tratamento específico para a coluna `S_GROUP_ID` (que é a coluna que armazena o tipo de falha) e gera um DataFrame pronto para análise e modelagem.

- **torques.py**
    - Este script realiza o pré-processamento dos dados de torque, incluindo a limpeza dos valores, agregação por `KNR` e `UNIT`, e normalização dos dados numéricos. Ele também implementa um pipeline completo de pré-processamento para uso em modelos de classificação.

- **merge_torques_falhas.py**
    - Realiza a junção (merge) dos dados de falhas com os dados de torque a partir de uma chave comum (`KNR`). O objetivo é ter todas as informações a respeito dos KNRS que possuem falhas em um único DataFrame para os modelos de classificação de falha.

- **modelo.py**
    - Contém a lógica para a construção e treinamento de um modelo de rede neural recorrente (GRU). Ele utiliza dados preparados para treinamento e validação, definidos no arquivo `preparacao.py`, e constrói um modelo sequencial com camadas GRU e uma camada final densa com ativação sigmoide.

#### 2. Pasta `modelo_principal`

- **falhas.py**
    - Faz a leitura de um arquivo CSV de falhas e aplica transformações, como remoção de registros duplicados baseados na coluna `KNR` e conversão da coluna `FALHA` para valores binários.

- **falhas2.py**
    - Remove colunas irrelevantes para a análise de falhas e retorna o DataFrame simplificado.

- **merge.py**
    - Faz o merge entre dois arquivos CSV: um contendo resultados e outro contendo falhas, unindo as informações a partir da coluna `KNR` e preenchendo valores nulos com zero.

- **modelo.py**
    - Similar ao script de `modelo_classificacao`, este arquivo também constrói um modelo de rede neural GRU para previsão, utilizando os dados já processados e prontos para modelagem.

- **resultado.py**
    - Realiza o pré-processamento dos dados de resultados, removendo valores nulos e convertendo a coluna `DATA` para o tipo datetime. O resultado é salvo em um novo arquivo CSV.

- **resultado2.py**
    - Faz o pré-processamento adicional dos dados, agregando-os por ID e aplicando normalização. As colunas de interesse são calculadas a partir de valores específicos de `ID`, e o resultado final é um DataFrame com essas informações normalizadas e agregadas.

#### 3. Script global `preparacao.py`

- **preparacao.py**
    - Este script contém uma função para preparar os dados antes de serem utilizados nos modelos. Ele realiza a separação entre features (`X`) e target (`y`), e faz a divisão dos dados em conjuntos de treino e teste. Além disso, ele reestrutura os dados de entrada para o formato adequado para redes neurais recorrentes (3 dimensões: `n_samples`, `n_features`, `1`).
