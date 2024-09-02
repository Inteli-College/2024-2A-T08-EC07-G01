# Modelo de Classificação por S_Group_ID

## Ideia Inicial 

Após a Sprint 1 a Volkswagen enviou uma tabela de falhas contendo a coluna S_GROUP_ID, a qual representa a classe de um determinado tipo de falha. Com isso, o grupo percebeu a oportunidade de prever tanto se haverá falha, como em que categoria de falha ela se encaixaria. Dessa forma, foram discutidas diferentes abordagens para a realização do problema. A primeira solução que o grupo imaginou foi a criação de dois modelos, um prevendo o acontecimento de falhas e outro que preveria o S_GROUP_ID, caso o resultado do primeiro seja de falha.

Todavia, essa ideia foi descartada após perceber que seria complexo acertar exatamente a classe que a falha pertenceria, além do fato de que permitiria um *KNR* ter somente um único tipo de falha. 

## Modelo

Para conseguir prever de maneira correta e abranger todos os tipos de falhas possíveis, o grupo optou por agrupar as falhas por KNR e utilizar a técnica do OneHotEncode. e da criação de um modelo para cada coluna gerada. Dessa maneira, para cada valor único do S_GROUP_ID há uma coluna com valores 0 ou 1, dependendo se havia algum registro daquele tipo de falha no dataframe. Esse processamento foi feito para que pudesse haver vários modelos, com cada modelo tendo como target uma coluna diferente. Assim, possibilitaria prever os diferentes tipos de falha existentes, além de possivelmente garantir mais estabalidade nas previsões.

## Pré-processamento S_GROUP_ID 

Na tabela enviada, a variável S_GROUP_ID possui 19 registros únicos, porém diversos deles eram idênticos, mas com diferenças de tipo. Dessa forma o grupo buscou tratar e colocar todos em `lowercase` para conseguir ter um melhor controle da tabela.

