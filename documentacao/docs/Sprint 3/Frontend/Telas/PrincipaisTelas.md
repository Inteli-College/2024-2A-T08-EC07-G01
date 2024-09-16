---
title: "Principais Telas do Frontend"
sidebar_position: 1
---

# **0.1** Introdução

O frontend deste projeto foi desenvolvido utilizando uma stack tecnológica moderna e eficiente, composta por **Nuxt.js**, **Vue.js**, **Tailwind CSS** e a biblioteca de componentes **shadcn/vue**.

## **1.1** Nuxt.JS com Vue.js

**Nuxt.js** é um framework progressivo baseado em Vue.js que simplifica o desenvolvimento de aplicações web poderosas e escaláveis. Ele oferece uma estrutura robusta para construir aplicações com renderização no lado do servidor (SSR), geração de sites estáticos (SSG) e suporte a Single Page Applications (SPA).

:::info Info
A escolha do Nuxt.js permite melhorar significativamente o desempenho e a otimização para mecanismos de busca `(SEO)` da aplicação.
:::

### **1.2** Benefícios do Nuxt.js

- **Renderização no Lado do Servidor (SSR)**: Melhora a performance e o SEO, entregando páginas pré-renderizadas aos usuários.
- **Geração de Sites Estáticos (SSG)**: Possibilita a exportação de todo o site em arquivos estáticos, aumentando a velocidade de carregamento.
- **Roteamento Automático**: Facilita a gestão de rotas através da estrutura de arquivos e pastas.
- **Modularidade e Extensibilidade**: Suporte a uma ampla gama de módulos que adicionam funcionalidades extras sem complicações.

Para projetos que exigem alta performance e escalabilidade, o Nuxt.js é uma excelente opção devido à sua flexibilidade e recursos avançados.

## **2.1** Tailwind CSS

Tailwind CSS é um framework CSS utilitário que permite criar interfaces de usuário customizadas de forma rápida e eficiente. Em vez de componentes pré-estilizados, o Tailwind fornece classes utilitárias de baixo nível que podem ser combinadas para construir qualquer design diretamente no seu HTML.

**Vantagens do Tailwind CSS**

- **Alta Produtividade**: Elimina a necessidade de escrever CSS personalizado para cada componente.
- **Customização Total**: Fácil de personalizar para atender às necessidades específicas do projeto, sem restrições de estilos pré-definidos.
- **Consistência Visual**: Garante uma aparência uniforme em toda a aplicação, facilitando a manutenção e escalabilidade.

:::tip Info
Foi utilizado o `Tailwind` em vez do `Bootstrap` pelo fato do mesmo ter um maior leque de opções, aumentando e melhorando a customização do projeto.
:::

## **3.1** Biblioteca de Componentes shadcn/vue

A **shadcn/vue** é uma biblioteca de componentes para Vue.js que oferece uma coleção de componentes acessíveis e personalizáveis, seguindo as melhores práticas de design e usabilidade. Inspirada na biblioteca shadcn/ui para React, ela traz para o ecossistema Vue uma série de componentes prontos para uso.

**Características da shadcn/vue**

- **Componentes Pré-Construídos**: Inclui botões, formulários, modais, menus e muito mais, agilizando o desenvolvimento.
- **Acessibilidade Incorporada**: Todos os componentes são desenvolvidos seguindo os padrões ARIA, garantindo que sejam utilizáveis por todos os usuários.
- **Estilização Flexível**: Integração perfeita com Tailwind CSS para customizar os estilos de acordo com o branding do projeto.

:::info
O foco em acessibilidade da shadcn/vue assegura que sua aplicação esteja em conformidade com as diretrizes de acessibilidade, melhorando a experiência para todos os usuários.
:::

## **4.1** Telas Principais do Frontend

A seguir, serão detalhadas as principais telas desenvolvidas no frontend, destacando suas funcionalidades e componentes utilizados.

### **4.2** Landing Page

A Landing Page é a porta de entrada do aplicativo, projetada para atrair e informar os usuários sobre as funcionalidades oferecidas.

**Funcionalidades:**

- **Apresentação do Produto**: Descrição clara e concisa dos principais recursos e benefícios.
- **Chamada para Ação (CTA)**: Botões e links que incentivam o usuário a explorar mais a fundo a aplicação.
- **Design Responsivo**: Layout adaptável para dispositivos móveis e desktops.

Utilizamos componentes de layout e tipografia da shadcn/vue, estilizados com Tailwind CSS, para criar uma interface atraente e moderna.

### **4.3** Histórico

Esta tela exibe um registro detalhado das falhas identificadas pelo sistema de inteligência artificial.

**Destaques:**

- **Listagem das Falhas**: Exibição de falhas com detalhes como data, descrição e classe.
- **Filtros e Pesquisa**: Possibilidade de filtrar falhas por data, tipo, classe ou knr, e pesquisar por palavras-chave.
- **Visualização Detalhada**: O usuário poderá ter uma visão geral sobre todas as falhas que já ocorreram

A implementação desta tela aproveita componentes de tabela e modais da shadcn/vue para uma experiência de usuário intuitiva.

### **4.4** Dashboard com Gráficos

O dashboard fornece visualizações gráficas das falhas detectadas, tendências e outras métricas importantes.

**Recursos Incluídos:**

- **Gráficos Interativos**: Utilização de componenentes de gráfico do ShadCN para exibir dados de forma clara e compreensível.
- **Atualização em Tempo Real**: Dados atualizados dinamicamente conforme novas falhas são detectadas.
- **Personalização**: Opção para o usuário selecionar quais métricas deseja visualizar nos gráficos.

A integração dos gráficos do ShadCN com o Tailwind CSS permite criar visualizações atraentes e informativas para o usuário.

:::warning
Garantir que os gráficos sejam acessíveis, fornecendo alternativas textuais e garantindo contraste adequado de cores.
:::

### **4.5** Adicionar Arquivo para Treino

Esta tela permite que o usuário faça upload de arquivos para treinar o modelo de inteligência artificial.

**Funcionalidades:**

- **Upload Seguro de Arquivos**: Suporte a formatos específicos e validação no lado do cliente.
- **Feedback Imediato**: Indicação do progresso do upload e confirmação de melhoria ou piora no próximo modelo.
- **Instruções Claras**: Orientações sobre os requisitos do arquivo e passos para concluir o processo.

Está tela tem por objetivo ser simples e interativa para o usuário final, com feedbacks claros e instruções fáceis de seguir.

### **4.6** Adicionar Arquivo para Predição

Nesta tela, o usuário pode enviar arquivos para que o sistema realize predições com base no modelo treinado.

**Características:**

- **Interface Simples**: Processo de upload direto, com minimização de etapas para facilitar o uso.
- **Resultados Rápidos**: Exibição dos resultados da predição logo após o processamento.
- **Histórico de Predições**: Registro dos arquivos enviados e resultados obtidos para referência futura.

Utilizamos componentes de upload e notificações da shadcn/vue para melhorar a experiência do usuário.

### **4.7** Healthcheck de Todos os Componentes

A tela de Healthcheck fornece um status em tempo real dos componentes essenciais do sistema: frontend, backend e base de dados.

**Funcionalidades:**

- **Indicadores de Status**: Exibição visual do status atual de cada componente (operacional, degradado, offline).
- **Detalhes Técnicos**: Informações adicionais como tempo de resposta, última verificação e logs de erro.
- **Notificações**: Alertas para o usuário em caso de falhas críticas ou necessidade de intervenção.

Esta funcionalidade é crucial para monitorar a saúde do sistema e garantir a disponibilidade contínua dos serviços.

## **5.1** Considerações Finais

A escolha das tecnologias **Nuxt.js**, **Vue.js**, **Tailwind CSS** e **shadcn/vue** proporcionou uma base sólida para o desenvolvimento de uma aplicação frontend moderna, performática e acessível.

O Vue.js, com sua sintaxe intuitiva e abordagem reativa, permitiu a criação de interfaces de usuário dinâmicas e escaláveis. Sua componentização facilitou a reutilização de código e a manutenção do projeto a longo prazo.

Integrando o Nuxt.js, aproveitamos os benefícios da renderização no lado do servidor (SSR) e da geração de sites estáticos. Isso não apenas melhorou o desempenho da aplicação, mas também otimizou para mecanismos de busca (SEO), garantindo que o conteúdo fosse facilmente indexado e acessível para um público mais amplo.

O Tailwind CSS acelerou o processo de estilização com sua abordagem utilitária. Com classes pré-definidas, pudemos criar designs consistentes e responsivos sem escrever CSS personalizado extensivo. Isso aumentou a eficiência do desenvolvimento e garantiu uma experiência visual coesa em todas as páginas.

Adicionando o shadcn/vue, incorporamos um conjunto de componentes de UI acessíveis e personalizáveis. Baseado em padrões de design modernos, este recurso permitiu que construíssemos interfaces de usuário ricas enquanto mantínhamos a acessibilidade e a usabilidade no centro do processo de design.

Em conjunto, essas tecnologias permitiram desenvolver uma aplicação que não é apenas moderna e performática, mas também centrada no usuário. A combinação dessas ferramentas garantiu que pudéssemos entregar uma experiência de alta qualidade, atendendo às necessidades de um público diversificado e alinhando-nos com as melhores práticas atuais do desenvolvimento web.

:::info Continuar investindo em testes automatizados e monitoramento para manter a qualidade e confiabilidade da aplicação ao longo do tempo.
:::