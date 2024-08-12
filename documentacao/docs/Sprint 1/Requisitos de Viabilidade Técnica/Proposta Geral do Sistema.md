Esse projeto visa a construção de um sistema de manutenção preditiva para a linha de produção de carros T-Cross, um modelo da VolksWagen. O sistema visa prever quais carros na linha de produção têm maior probabilidade de possuir alguma falha, direcionando-os para os testes específicos a fim de realizar as manutenções de acordo.

Esse sistema desenvolvido será composto por uma **interface** acessível pelo usuário onde será possível visualizar as informações preditas, além de possibilitar o envio as informações adquiridas pelos sensores ao longo da produção dos carros, que serão utilizados para treinar o **modelo**, segunda parte desse sistema. O modelo será responsável por pegar as informações (os **inputs**), e devolver a classificação daquele carro correspondente, ou seja, se será necessário realizar o teste de rodagem ou não. 

Dentro da interface, além da classificação dos carros na linha de produção, também é possível acessar uma visualização dos dados a fim de permitir *insigths* aos gestores da linha de produção, ao conseguir visualizar numericamente quais são as falhas mais comuns, quais são as estações que costumam dar mais problemas, entre outros padrões identificados pelo modelo.



## Primeira Versão de Arquitetura do Sistema

Para uma melhor visualização da estrutura do sistema mencionado acima, é possível observar o diagrama de blocos abaixo, que ilustra como cada um dos componentes do sistema se comunica. 


<div align="center">

**Diagrama de Blocos**

![Diagrama de blocos](/img/Diagrama-de-blocos.png)

**Fonte:** Elaborado pela equipe Toretto 

</div>

### Frontend e Backend
Ambos constituem a formação da **interface**, sendo o Frontend a interface visual que o usuário consegue acessar e o Backend responsável por gerir as informações recebidas (tanto do modelo quanto do usuário), utilizando-se de APIs.
No **Frontend**, há a possibilidade de acessar tanto os **outputs** do modelo com a classificação dos carros, quanto realizar o upload de informações para o treinamento do modelo, ou dados sobre um carro específico para realizar uma classificação, ou seja, os **inputs**.

No **Backend**, os inputs recebidos pelo usuário serão ou repassados para o modelo para serem processados, ou serão armazenados para re-treinar o modelo posteriormente, atualizando-o com novos dados.

### Modelo
O **modelo** 


### Armazenamento de dados