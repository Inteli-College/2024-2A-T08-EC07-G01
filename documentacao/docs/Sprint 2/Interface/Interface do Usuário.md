---
sidebar_position: 1
custom_edit_url: null
---

# Aplicação web

Uma aplicação web é um tipo de software que é acessado e executado através de um navegador, utilizando a internet como meio de comunicação entre o usuário e o servidor. Ao contrário de programas tradicionais que necessitam de instalação no dispositivo do usuário, as aplicações web operam em um ambiente distribuído, onde os dados e a lógica de aplicação são armazenados em servidores remotos. Isso permite que os usuários acessem e utilizem a aplicação de qualquer lugar, desde que possuam uma conexão à internet e um navegador compatível.

Essas aplicações são construídas utilizando tecnologias como HTML, CSS e JavaScript no lado do cliente, enquanto no lado do servidor podem utilizar diversas linguagens de programação e frameworks, como Python com Django, JavaScript com Node.js, ou PHP. A comunicação entre o cliente e o servidor geralmente é feita através de protocolos HTTP ou HTTPS, e os dados são frequentemente transmitidos em formatos como JSON ou XML. Além disso, as aplicações web modernas podem interagir com bancos de dados, APIs, e outros serviços para oferecer funcionalidades dinâmicas e personalizadas aos usuários.

Em resumo, uma aplicação web é uma solução tecnológica flexível e escalável, que permite a criação de interfaces interativas e acessíveis para uma vasta gama de usuários. Devido à sua natureza centralizada, as atualizações e manutenções são simplificadas, uma vez que as alterações no código ou na estrutura da aplicação precisam ser feitas apenas no servidor. Isso, combinado com a facilidade de acesso e a crescente popularidade de dispositivos conectados à internet, faz das aplicações web uma escolha ideal para uma ampla variedade de projetos.

## **1.1.** Tecnologias utilizadas

Para garantir a responsividade e interatividade da aplicação web, foram utilizadas diversas tecnologias que contribuíram para a criação de uma interface moderna e eficiente. Abaixo estão as principais tecnologias empregadas:

- **Nuxt**: O Nuxt.js é um framework de código aberto baseado em Vue.js que facilita a criação de aplicações web modernas e escaláveis. Ele fornece uma arquitetura de aplicação pré-configurada, que inclui funcionalidades como roteamento, renderização do lado do servidor, e gerenciamento de estado. Além disso, o Nuxt.js oferece uma série de plugins e módulos que permitem a integração com outras tecnologias e serviços, como APIs RESTful, GraphQL, e CMSs.

- **Vue**: O Vue.js é uma biblioteca JavaScript de código aberto para a construção de interfaces de usuário reativas e dinâmicas. Ele fornece uma sintaxe simples e intuitiva para a criação de componentes reutilizáveis, que podem ser combinados para formar interfaces complexas e interativas.

:::tip Informação
O Vue.js oferece um sistema de reatividade eficiente, que atualiza **automaticamente** a interface do usuário sempre que os dados subjacentes são modificados.
:::

- **Tailwind**: O Tailwind CSS é um framework de design de componentes CSS que oferece uma abordagem de estilo utilitário para a criação de interfaces de usuário. Em vez de fornecer classes CSS pré-definidas para estilizar elementos, o Tailwind permite que os desenvolvedores criem estilos personalizados usando classes utilitárias, que podem ser combinadas e reutilizadas para estilizar qualquer elemento HTML.

- **ShadCN**: O ShadCN é uma biblioteca de componentes pré-produzidos para o Vue.js, que oferece uma série de componentes reutilizáveis e personalizáveis para a criação de interfaces de usuário.

:::info 
O ShadCN inclui componentes para botões, formulários, modais, e muito mais, que podem ser **facilmente integrados** em qualquer aplicação Vue.js, bastando apenas instalar o ShadCN dentro de seu package-lock, para saber mais a respeito do mesmo clique [aqui](https://www.shadcn-vue.com/).
:::

## **2.1.** Modelagem da interface

Ao modelar a interface, foi pensado sempre na iteratividade do usuário com a plataforma e o que a mesma iria agregar de valor. A interface foi pensada para ser intuitiva e fácil de usar, com elementos visuais claros e bem organizados. 

### **2.1.1.** Design intuitivo

Ao modelar a interface, consideramos essencial a interação contínua e intuitiva do usuário com a plataforma, visando sempre agregar valor prático ao processo. O foco principal foi criar uma interface que facilitasse a identificação rápida e eficiente de informações cruciais, como a detecção de falhas no veículo antes da fase de testes de rodagem.

Priorizamos um design intuitivo, com elementos visuais organizados de maneira clara e acessível, garantindo que os técnicos e engenheiros da Volkswagen possam navegar facilmente pelo sistema sem a necessidade de treinamento extenso.

### **2.1.2.** Eficiência e responsividade

A interface foi desenvolvida com base em princípios de usabilidade para maximizar a eficiência das interações e minimizar possíveis erros. Incorporamos padrões de design responsivo, assegurando que a aplicação funcione de maneira fluida tanto em desktops quanto em dispositivos móveis.

Além disso, a interface foi projetada para se adaptar a diferentes tamanhos de tela e resoluções, garantindo uma experiência consistente e agradável para todos os usuários, independentemente do dispositivo que estiverem utilizando.

### **2.1.3.** Integração com a I.A. para Detecção de Falhas

Dado que o projeto envolve uma Inteligência Artificial para identificar falhas nos veículos antes dos testes de rodagem, cada detalhe da interface foi projetado para complementar essa funcionalidade. O sistema foi desenhado para fornecer dados relevantes e insights de maneira rápida e precisa, facilitando a tomada de decisões e permitindo a detecção precoce de problemas.

Elementos como gráficos e painéis interativos foram cuidadosamente dispostos para destacar possíveis falhas identificadas pela I.A., de forma visualmente atraente e de fácil interpretação.

O resultado é uma interface que não apenas atende às necessidades dos usuários, mas também se alinha com os objetivos da Volkswagen de garantir a qualidade e a segurança dos veículos antes de entrarem em fase de testes.

## **3.1** Protótipo de alta fidelidade ( Figma )

Para a criação do protótipo de alta fidelidade, foi utilizado a ferramenta Figma, que é uma plataforma de design colaborativo baseada na nuvem. O Figma permite a criação de interfaces de usuário interativas e responsivas, que podem ser compartilhadas e visualizadas por toda a equipe de desenvolvimento.

Abaixo será apresentado o protótipo de alta fidelidade da aplicação web, que inclui as principais telas e elementos da interface, como a página inicial, o painel de controle, e os gráficos de falhas detectadas.