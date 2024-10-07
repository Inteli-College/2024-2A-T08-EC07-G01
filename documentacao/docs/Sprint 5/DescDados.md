---

title: "Descrição do tratamento dos Dados" 
sidebar_position: 2

---

---

## Modelo Yes or No
### 1.1 Carregamento dos Dados Iniciais
Os dados são carregados a partir de arquivos CSV (por exemplo, df_falhas.csv), que contêm informações sobre resultados e falhas, respectivamente. Cada DataFrame é processado individualmente para preparar as informações para o modelo.

### 1.2 Remoção de Dados Inválidos e Tratamento de Valores Nulos

**DataFrame df_resultados:** Após o carregamento, `valores nulos` são removidos e a coluna `DATA` é convertida para o formato datetime.

**DataFrame df_falhas:** Os valores da coluna `FALHA` são convertidos para maiúsculas, `registros duplicados` com base na coluna KNR são removidos, e a coluna `FALHA` é preenchida com o valor 1 para indicar a presença de falhas.

### 2. Transformações e Limpeza de Dados

### 2.1 Remoção de Colunas Desnecessárias
Diversas colunas não utilizadas no modelo final são removidas dos DataFrames para reduzir dimensionalidade e otimizar o processamento como por exemplo as colunas `MODELO`, `COR`, `MOTOR`, `ESTACAO`, `USUARIO`, `HALLE`, e `DATA` são eliminadas do DataFrame de falhas. Já para o DataFrame de resultados, são removidas `UNIT`, `VALUE_ID` e `VALUE`.

### 2.2 Agregação de Dados por Identificador (ID)

Os dados são agregados com base na coluna `ID`, que indica diferentes tipos de falhas ou eventos. Esta etapa envolve o agrupamento por `KNR` e a criação de colunas específicas para cada ID totalizando 3 IDs diferentes, `ID1`, `ID2` e `ID718` onde cada uma possui colunas como `NAME`, `SOK (falhas bem-sucedidas)`, `SNOK (falhas mal-sucedidas)`, e `DATA`, representando contagens ou duração em dias de eventos específicos.

### 2.3 Unificação dos DataFrames e Preenchimento de Dados

Os DataFrames resultantes das agregações são mesclados por `KNR` para formar uma tabela consolidada, onde todas as colunas necessárias para o modelo são integradas. A função fillna(0) é utilizada para substituir valores nulos por zeros.

### 3. Normalização e Padronização
Para preparar os dados para o modelo de machine learning, as colunas resultantes da etapa anterior são normalizadas usando MinMaxScaler para garantir que todos os valores estejam na mesma escala. Essa etapa é essencial para melhorar o desempenho e a precisão do modelo.

---
## Modelo de classificação

###  1. Junção dos Dados de Torque e Falhas

A função execute `df_torques`, `df_falhas` faz a junção `merge` dos dados de torques e falhas com base na coluna KNR, preservando todos os registros de `df_torques` merge left. Isso permite analisar falhas associadas a cada torque.

### 2. Preparação e Limpeza do DataFrame de Falhas

O pipeline remove todas as `entradas nulas` para garantir a qualidade dos dados, filtra os registros com valores específicos na coluna `S_GROUP_ID` que poderiam indicar múltiplos valores e converte `S_GROUP_ID` para int. As colunas desnecessárias para o modelo `USUARIO`, `FALHA`, `MODELO`, `ESTACAO`, `HALLE`, `MOTOR`, `COR` são descartadas. Criação de variáveis `dummy` para `S_GROUP_ID` e garantia de que todas as categorias possíveis estão representadas.

### 3. Tratamento da Coluna VALUE nos Dados de Torque

Remoção de `espaços em branco` e substituição de strings vazias por NaN, substituição de vírgulas por pontos para padronizar os valores como floats e conversão dos valores para tipo numérico e remoção de valores nulos após a conversão.

### 4. Agrupamento e Pivotagem por KNR e UNIT

Os dados são agrupados por `KNR` e `UNIT` para calcular a média dos valores de torque depois o resultado é pivotado para transformar `UNIT` em colunas, facilitando a análise individual por unidade.

### 5. Normalização de Colunas Numéricas

As colunas numéricas, excluindo `KNR` e `UNIT`, são normalizadas para estarem em uma faixa padrão (0 a 1), o que facilita o treinamento do modelo.