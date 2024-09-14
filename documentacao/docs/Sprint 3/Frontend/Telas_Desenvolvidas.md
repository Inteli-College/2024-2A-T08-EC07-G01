---
title: "Telas desenvolvidas"
sidebar_position: 2
---

## Tela de Previsão de KNR

![Tela de Previsão de KNR](/img/previsaoKNR.jpg)

**Fonte:** Próprios autores

Esta tela permite que o usuário insira um KNR (Número de Registro de Veículo) e visualize as previsões de falhas associadas ao carro, indicando se há ou não uma falha prevista para aquele veículo. O resultado exibe um gráfico categorizando os tipos de falhas potenciais e seus status.


#### Campo de Busca  
O usuário digita o número de KNR desejado para realizar a busca das falhas previstas.  
- **Funcionalidade**: Após inserir o KNR e clicar no ícone de lupa, a tela busca o status do veículo relacionado ao KNR.

#### Indicação de Falha ou Não Falha  
Após a busca, a tela exibe uma indicação visual sobre a condição do veículo:
- **Carro sem falha prevista**: Caso um KNR válido seja inserido e o veículo não tenha falhas previstas, o usuário será redirecionado para a tela "Sem Falha Indicada".
- **Carro com falha prevista**: Se o KNR possuir uma falha associada, o usuário será redirecionado para a tela "Teste de Rodagem Indicado", que exibe os detalhes da falha.

**Modal de Previsão dos KNRs (sem Erros)**

![Modal de Previsão dos KNRs (sem Erros)](/img/previsaoModal1.jpeg)

**Fonte:** Próprios autores

**Modal de Previsão dos KNRs (com Erros)**

![Modal de Previsão dos KNRs (com Erros)](/img/previsaoModal2.jpg)

**Fonte:** Próprios autores

#### Mensagens de Erro  
Caso o KNR inserido seja inválido ou não retorne dados, a tela deverá exibir uma mensagem de erro ou de ausência de informações, solicitando um novo input.

---