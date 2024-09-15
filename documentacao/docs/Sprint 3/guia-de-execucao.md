---
sidebar_position: 1
custom_edit_url: null
---

# Execução com o Docker


## Preparação do ambiente 

Para ter um ambiente que interaja com docker, é necessário realizar a instalação do mesmo. Esse tutorial a seguir estava funcionando para linux quando o projeto foi desenvolvido. Caso tenha algum problema, consulte a [documentação do docker](https://docs.docker.com/compose/install/) 

1. Instale o Docker e o Docker compose: 

```bashrc
sudo apt install docker docker-compose-v2
```

Após a execução, deve ser utilizado o comando:

```bashrc
sudo apt-get update
```

## Executando o projeto

Agora, para a execução do projeto é necessário abrir um terminal na pasta do projeto e executar os seguintes comandos:

```bashrc
$ cd src
$ docker compose up
```

Depois da execução do comando, o projeto estará funcionando. 
Os serviços estão localizados nas seguintes portas:

**FrontEnd**: (http://localhost:3000)[http://localhost:3000]
**BackEnd**: (http://localhost:8000)[http://localhost:8000]
**Docs do Backend**: (http://localhost:8000/docs)[http://localhost:8000/docs]