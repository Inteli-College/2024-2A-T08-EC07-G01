Esse projeto visa a construção de um sistema de manutenção preditiva para a linha de produção de carros T-Cross, um modelo da VolksWagen. O sistema visa prever quais carros na linha de produção têm maior probabilidade de possuir alguma falha, direcionando-os para os testes específicos a fim de realizar as manutenções de acordo.

Esse sistema desenvolvido será composto por uma **interface** acessível pelo usuário onde será possível visualizar as informações preditas, além de possibilitar o envio as informações adquiridas pelos sensores ao longo da produção dos carros, que serão utilizados para treinar o **modelo**, segunda parte desse sistema. O modelo será responsável por pegar as informações (os **inputs**), e devolver a classificação daquele carro correspondente, ou seja, se será necessário realizar o teste de rodagem ou não. 

Dentro da interface, além da classificação dos carros na linha de produção, também 



## Primeira Versão de Arquitetura do Sistema

<div align="center">

**Diagrama de Blocos**

![Diagrama de blocos](/img/Diagrama-de-blocos.png)

**Fonte:** Elaborado pela equipe Toretto 

</div>