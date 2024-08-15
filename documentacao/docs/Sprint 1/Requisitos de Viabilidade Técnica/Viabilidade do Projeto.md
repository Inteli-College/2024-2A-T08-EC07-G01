## Estudo da viabilidade

A indústria automotiva está cada vez mais orientada por dados e inteligência artificial, com o objetivo de otimizar processos e melhorar a qualidade dos veículos produzidos. Nesse contexto, a Volkswagen busca inovar em seus processos de controle de qualidade, propondo o desenvolvimento de um modelo preditivo capaz de avaliar, de maneira antecipada, a necessidade de testes de rodagem nos veículos logo após saírem da linha de produção.

Este estudo de viabilidade tem como objetivo principal avaliar se a equipe de desenvolvimento dispõe dos recursos e insumos necessários para construir um modelo robusto e eficiente. Tal modelo preditivo visa identificar a probabilidade de falhas potenciais nos veículos, permitindo a tomada de decisões mais assertivas quanto à necessidade de testes adicionais, garantindo assim a qualidade dos produtos entregues ao consumidor final.

A seguir, será apresentada uma análise detalhada dos dados disponíveis e das variáveis *(features)* selecionadas para treinar o modelo, com o intuito de verificar sua capacidade preditiva e precisão em identificar possíveis falhas.

## Análise exploratória dos dados

Para a primeira versão do modelo preditivo, as bibliotecas utilizadas foram o [pandas](https://pandas.pydata.org/docs/), o [numpy](https://numpy.org/), e o [sklearn](https://scikit-learn.org/stable/). O parceiro disponibilizou uma variedade de tabelas, entre elas as tabelas de resultados (que contém atualizações de status do carro, quanto tempo ele passou em cada procedimento, entre outras coisas que descrevem o que aconteceu ao longo da linha de produção) e de falhas (que contém as falhas encontradas em cada carro). São essas tabelas que serão utilizadas para a construção da nossa solução, porque saber o que aconteceu na linhas de produção irá impactar diretamente nas falhas que serão encontradas.

Para uma análise mais detalhada do código utilizado para a exploração dos dados, é possível acessar o notebook na pasta **notebooks** dentro de **src** do nosso [GitHub](https://github.com/Inteli-College/2024-2A-T08-EC07-G01), com o nome **main.ipynb**. 

### Importação das bibliotecas

Primeiramente, é realizada a importação das bibliotecas mencionadas acima, que serão utilizadas para auxiliar a modificação e vizualização dos dados, a fim de melhorar os inputs para o modelo processar. 

### Inicializar os dados e arrumar erros de conversão

Depois, as tabelas são carregadas, e há a necessidade (no caso apresentado) de arrumar os indexs pois ao converter de xlsx (formato que o parceiro disponibilizou) para csv, algumas colunas com o nome "unnamed" surgem, pois o index não é reconhecido. 

### Preparação dos dados

- **Remoção de linhas com dados nulos:** Como há uma grande quantidade de dados, o drop (método que funciona como um "deletar") das linhas com dados nulos não representa grande perda. 

- **Conversão de csv para parquet:** Para um processamento mais rápido, os dados foram convertidos para *parquet.

- **Drop de colunas que não serão usadas para treinar o modelo:** Na tabela **Resultados**, as colunas 'UNIT', 'VALUE_ID' e 'VALUE' são apagadas, para diminuir o tamanho da tabela e assim dando mais ênfase para as *features* mais importantes, como o 'KNR' (que é um código que identifica cada carro), o 'STATUS' (que avalia se o carro está "ok" ou "não ok" naquele checkpoint), e a 'DATA' (que representa o momento em que aquela avaliação foi feita). 
Já na tabela de **Falhas**, as colunas retiradas foram todas exceto as que tem os KNRs (para identificar os carros) e as descrições das falhas (com mais de 2000 tipos de falhas únicas).

#### Mudanças nas tabelas de resultados

- **Concatenar tabelas de resultados:** Para termos mais volume de dados, juntamos duas tabelas de resultados referentes a dois meses do ano de 2023.

- **Converter a coluna de datas de *object* para o *datetime* do pandas:** Ao usar a função `describe` do pandas, foi mostrado que todos as colunas estavam com o tipo *object*, o que para uma análise temporal não é muito útil. Por essa razão, convertemos o tipo da coluna 'DATA' para *datetime*.

- **Feature engineering:**

#### Mudanças na tabela de falhas

- **Remover os KNRs repetidos:**

- **Mudar as especificações das falhas para 1:**

#### Juntando a tabela de resultados com a de falhas

- **Se há falha com aquele KNR, 1, senão, 0:**

- **Normalização dos dados:**

- **Drop das colunas KNR e Falha (que é o target):**

#### Primeiro modelo utili\ado 

Acurácia do treinamento : 88
Do teste 81.7



