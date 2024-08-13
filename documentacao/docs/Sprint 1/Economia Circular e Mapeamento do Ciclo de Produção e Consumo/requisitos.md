---
title: "Requisitos de Visualização"
index: 1
---

Os requisitos descritos a seguir têm como objetivo definir como os dados devem ser apresentados ao usuário final, abordando tanto as necessidades de visualização quanto as opções e funcionalidades de acesso dentro da nossa solução. Com isso, foram estabelecidos os seguintes requisitos:

1. **Dashboard**: É essencial a criação de um dashboard que exiba as informações das previsões realizadas. Este dashboard deve incluir o identificador do veículo, a indicação de ocorrência ou não de um problema (previsão), a natureza provável do problema, e a recomendação de teste a ser realizado para o problema identificado. A apresentação desses dados deve ser feita, preferencialmente, por meio de tabelas, que oferecem clareza e mantêm um formato familiar para os usuários.

2. **Sistema de Pesquisa**: Para facilitar e agilizar a consulta dos dados desejados, é importante integrar à solução um sistema de pesquisa. Este sistema permitirá que o usuário busque pelo identificador do veículo, filtrando os resultados exibidos no dashboard e proporcionando uma busca mais eficiente.

3. **Plataforma Web**: É necessária a construção de uma plataforma web que suporte toda a exibição e coleta de dados, incluindo o sistema de dashboard. A plataforma deve ser desenvolvida, preferencialmente, em um formato Desktop, subdividida em seções de Previsão e Treinamento. 

   - **Seção de Previsão**: A plataforma deve permitir a entrada de dados em formato .xlsx e, a partir disso, exibir o dashboard com as funcionalidades de pesquisa e paginação.

   - **Seção de Treinamento**: Deve ser possível inserir novos dados em formato .xlsx para o treinamento do modelo, que deve ser realizado mensalmente.

A implementação dos requisitos acima é fundamental para garantir uma experiência de usuário eficiente e intuitiva, permitindo que os dados sejam visualizados de forma clara e organizada. Com a criação do dashboard, o sistema de pesquisa e a plataforma web, os usuários terão acesso facilitado às informações relevantes, podendo realizar consultas e análises com maior agilidade. Essa estrutura robusta e bem planejada assegura que a solução atenda às necessidades de visualização de dados, contribuindo para tomadas de decisão mais informadas e precisas.
