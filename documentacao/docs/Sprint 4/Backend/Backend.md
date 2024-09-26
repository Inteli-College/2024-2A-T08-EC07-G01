---
title: "Alterações Backend"
sidebar_position: 1
---

# **1.1** - Introdução

Durante a quarta Sprint, o projeto passou por uma série de aprimoramentos visando a implementação de novas funcionalidades. Um dos principais focos foi a inclusão da pipeline de treinamento e retreinamento do modelo, uma etapa fundamental para melhorar a eficiência e precisão das previsões realizadas. No entanto, para acomodar essa funcionalidade, foi necessário adaptar a estrutura do backend, garantindo que ele suportasse essas novas operações de forma eficiente.

As alterações realizadas no backend incluíram a adição de um novo roteador, um elemento crucial para organizar e direcionar as requisições relacionadas ao treinamento do modelo. Essa mudança foi cuidadosamente planejada para preservar a integridade das operações existentes, garantindo que a integração das novas funcionalidades não comprometesse o desempenho atual. Assim, foi possível assegurar que o backend continuasse funcionando corretamente, mesmo com a inclusão de funcionalidades mais complexas.

Além de atender às necessidades imediatas do projeto, essa reformulação do backend contribui para a escalabilidade a longo prazo. A inclusão de um roteador dedicado facilita a manutenção e a expansão futura do sistema, tornando-o mais adaptável a novas demandas. Dessa forma, as modificações realizadas não apenas aprimoram a funcionalidade atual, mas também preparam o projeto para futuras evoluções, assegurando um desenvolvimento sustentável.

## **2.1** - Novo repository de previsões

Para implementar essa funcionalidade, foi criado um `Predictions Repository`, responsável por armazenar as previsões geradas pelo modelo no banco de dados. Esse repositório centraliza o gerenciamento de previsões, facilitando seu armazenamento e acesso de forma organizada. A seguir, cada parte do código será detalhada para esclarecer seu funcionamento e propósito.

:::info 
Mais abaixo haverá o código completo desta parte afim de melhorar o entendimento.
:::

### **2.1.1** - Adquirir as previsões

Para adquirir as previsões, foi criado um método `get_all_predictions` que retorna todas as previsões armazenadas no banco de dados. Esse método é essencial para recuperar as previsões geradas pelo modelo, permitindo que sejam exibidas e utilizadas conforme necessário. A seguir, o código completo desse método será apresentado para ilustrar sua implementação.

```python
def get_all_predictions(self) -> List[Prediction]:
        documents = self.collection.find()
        return [Prediction(**document) for document in documents]
```

:::warning
A estrutura que ele retorna `Prediction` foi explicada anteriormente em [Base de Dados](/docs/).
:::

### **2.1.2** - Adicionar previsões

Para adicionar previsões, foi criado um método `create_prediction` que insere uma nova previsão no banco de dados. Esse método é fundamental para armazenar as previsões geradas pelo modelo, garantindo que estejam disponíveis para consulta posterior. A seguir, o código completo desse método será apresentado para ilustrar sua implementação.

```python
def create_prediction(self, prediction_info: Prediction) -> str:
        self.collection.insert_one(prediction_info.model_dump(by_alias=True))
        return str(prediction_info.KNR)
```

### **2.1.3** - Adquirir uma predição

Para adquirir uma previsão específica, foi criado um método `get_prediction` que retorna a previsão correspondente ao **KNR** fornecido. Esse método é essencial para recuperar previsões específicas, permitindo que sejam acessadas e utilizadas conforme necessário. A seguir, o código completo desse método será apresentado para ilustrar sua implementação.

```python
def get_prediction(self, knr_id: str) -> Optional[Prediction]:
        document = self.collection.find_one({"KNR": knr_id})
        return Prediction(**document) if document else None
```

### **2.1.4** - Atualizar uma previsão

Para atualizar uma previsão, foi criado um método `update_prediction` que modifica a previsão correspondente ao **KNR** fornecido. Esse método é fundamental para atualizar previsões existentes, garantindo que estejam sempre atualizadas e precisas. A seguir, o código completo desse método será apresentado para ilustrar sua implementação.

```python
def update_prediction(self, knr_id: str, prediction_info: PredictionUpdate) -> bool:
        result = self.collection.update_one(
            {"KNR": knr_id},
            {"$set": prediction_info.model_dump(exclude_unset=True, by_alias=True)},
        )
        return result.modified_count > 0
```

### **2.1.5** - Deletar uma previsão

Para deletar uma previsão, foi criado um método `delete_prediction` que remove a previsão correspondente ao **KNR** fornecido. Esse método é essencial para excluir previsões indesejadas, garantindo que o banco de dados permaneça organizado e atualizado. A seguir, o código completo desse método será apresentado para ilustrar sua implementação.

```python
def delete_prediction(self, knr_id: str) -> bool:
        result = self.collection.delete_one({"KNR": knr_id})
        return result.deleted_count > 0
```

### **2.1.6** - Código completo

A seguir, o código completo da classe `PredicitionsRepository` será apresentado para ilustrar sua implementação. Esse código reúne todos os métodos criados para gerenciar as previsões, garantindo que estejam armazenadas e acessíveis conforme necessário.

```python
class PredictionsRepository:
    def __init__(self, db: MongoDB):
        self.db = db
        self.collection = db.get_collection("predictions")

    def get_all_predictions(self) -> List[Prediction]:
        documents = self.collection.find()
        return [Prediction(**document) for document in documents]

    def create_prediction(self, prediction_info: Prediction) -> str:
        self.collection.insert_one(prediction_info.model_dump(by_alias=True))
        return str(prediction_info.KNR)

    def get_prediction(self, knr_id: str) -> Optional[Prediction]:
        document = self.collection.find_one({"KNR": knr_id})
        return Prediction(**document) if document else None

    def update_prediction(self, knr_id: str, prediction_info: PredictionUpdate) -> bool:
        result = self.collection.update_one(
            {"KNR": knr_id},
            {"$set": prediction_info.model_dump(exclude_unset=True, by_alias=True)},
        )
        return result.modified_count > 0

    def delete_prediction(self, knr_id: str) -> bool:
        result = self.collection.delete_one({"KNR": knr_id})
        return result.deleted_count > 0
```

:::warning
No código acima está apenas a classe, os imports foram **omitidos** para melhor entendimento. Caso queira analisar o código inteiro, acesse o [repositório](https://github.com/Inteli-College/2024-2A-T08-EC07-G01)
:::

## **3.1** - Novo serviço de previões

Foram desenvolvidos tanto um serviço para previsões quanto um repositório para armazená-las. O serviço gerencia todas as operações relacionadas às previsões, assegurando que elas sejam realizadas de maneira eficiente e segura. Este serviço atua como uma interface central para o processamento de previsões, facilitando a organização e a execução correta das tarefas. A seguir, serão detalhadas as partes do código, destacando seu funcionamento e propósito.

Além disso, foi implementado um Singleton para garantir que apenas uma instância do serviço seja criada. Essa abordagem evita duplicações e assegura a consistência das operações, prevenindo possíveis conflitos e melhorando a eficiência geral do sistema. Essa escolha arquitetural é essencial para manter a integridade dos dados e a confiabilidade do serviço.

Por fim, cada componente do código será analisado em detalhes, oferecendo uma visão abrangente de seu papel e funcionamento. Essa explicação permitirá compreender o fluxo completo das previsões, desde sua geração até o armazenamento no repositório.

### **3.1.1** - Serviço adquirir previsões

Para adquirir previsões, foi criado um método `get_all_predictions` que retorna todas as previsões armazenadas no repositório. Esse método é essencial para recuperar as previsões geradas pelo modelo, permitindo que sejam exibidas e utilizadas conforme necessário. A seguir, o código completo desse método será apresentado para ilustrar sua implementação.

```python
def get_all_predictions(self) -> List[Prediction]:
        return self.predict_repo.get_all_predictions()
```

### **3.1.2** - Serviço pegar uma previsão

Para pegar uma previsão específica, foi criado um método `get_prediction` que retorna a previsão correspondente ao **KNR** fornecido. Esse método é essencial para recuperar previsões específicas, permitindo que sejam acessadas e utilizadas conforme necessário. A seguir, o código completo desse método será apresentado para ilustrar sua implementação.

```python
def get_prediction(self, knr: str) -> Optional[Prediction]:
        return self.predict_repo.get_prediction(knr)
```

### **3.1.3** - Serviço adicionar uma previsão

# TODO

### **3.1.4** - Serviço atualizar uma previsão

Para atualizar uma previsão, foi criado um método `update_prediction` que modifica a previsão correspondente ao **KNR** fornecido. Esse método é fundamental para atualizar previsões existentes, garantindo que estejam sempre atualizadas e precisas. A seguir, o código completo desse método será apresentado para ilustrar sua implementação.

```python
def update_prediction(self, knr: str, prediction: PredictionUpdate) -> bool:
        return self.predict_repo.update_prediction(knr, prediction)
```

### **3.1.5** - Serviço deletar uma previsão

Para deletar uma previsão, foi criado um método `delete_prediction` que remove a previsão correspondente ao **KNR** fornecido. Esse método é essencial para excluir previsões indesejadas, garantindo que o repositório permaneça organizado e atualizado. A seguir, o código completo desse método será apresentado para ilustrar sua implementação.

```python
def delete_prediction(self, knr: str) -> bool:
        return self.predict_repo.delete_prediction(knr)
```

### **3.1.6** - Código completo

A seguir, o código completo da classe `PredictionsService` será apresentado para ilustrar sua implementação. Esse código reúne todos os métodos criados para gerenciar as previsões, garantindo que estejam armazenadas e acessíveis conforme necessário.

```python
class PredictionService:
    def __init__(self, predict_repo: PredictionsRepository):
        self.predict_repo = predict_repo

    def get_all_predictions(self) -> List[Prediction]:
        return self.predict_repo.get_all_predictions()

    def get_prediction(self, knr: str) -> Optional[Prediction]:
        return self.predict_repo.get_prediction(knr)

    def predict(self, knr: KNR) -> Prediction:
        # TODO: call the predictions function
        return Prediction(knr.KNR)

    def update_prediction(self, knr: str, prediction: PredictionUpdate) -> bool:
        return self.predict_repo.update_prediction(knr, prediction)

    def delete_prediction(self, knr: str) -> bool:
        return self.predict_repo.delete_prediction(knr)
```

### **3.1.7** - Singleton

Para garantir que apenas uma instância do serviço seja criada, foi implementado um Singleton. Essa abordagem evita duplicações e assegura a consistência das operações, prevenindo possíveis conflitos e melhorando a eficiência geral do sistema. A seguir, o código completo do Singleton será apresentado para ilustrar sua implementação.

```python
class PredictionsServiceSingleton:
    _instance: Optional[PredictionService] = None

    def __init__(self, *args, **kwargs):
        raise RuntimeError("Call get_instance() instead")

    def __new__(cls, *args, **kwargs):
        raise RuntimeError("Call get_instance() instead")

    @classmethod
    def initialize(cls, predict_repo: PredictionsRepository):
        if cls._instance is None:
            cls._instance = PredictionService(predict_repo)

    @classmethod
    def get_instance(cls) -> PredictionService:
        if cls._instance is None:
            raise Exception(
                "ModelServiceSingleton is not initialized. Call initialize() first."
            )

        return cls._instance
```

:::info
Foi utilizado o padrão Singleton para garantir que apenas uma instância do serviço seja criada. Isso evita duplicações e assegura a consistência das operações, prevenindo possíveis conflitos e melhorando a eficiência geral do sistema.
:::

## **4.1** - Conclusão

As mudanças realizadas no backend durante a quarta Sprint desempenharam um papel fundamental na implementação da pipeline de treinamento e retreinamento do modelo. A inclusão de um novo roteador e um repositório dedicado para previsões foi uma medida estratégica que permitiu integrar essas funcionalidades de maneira eficiente e organizada. Com isso, foi possível aprimorar a estrutura do projeto, tornando o backend mais robusto e preparado para lidar com a complexidade das operações de previsão.

Além dessas alterações, a implementação de um serviço centralizado para gerenciar as operações relacionadas às previsões foi essencial para garantir a escalabilidade e a manutenibilidade do sistema. Essa abordagem permitiu um melhor gerenciamento dos dados e das operações, evitando redundâncias e promovendo um fluxo mais eficiente de informações. O uso de uma arquitetura bem planejada favoreceu a preparação do sistema para futuras demandas, reforçando sua flexibilidade e adaptabilidade.

Portanto, as mudanças realizadas no backend durante a quarta Sprint representam um avanço significativo para o projeto. A estruturação cuidadosa do código e a organização das operações não só melhoraram a funcionalidade atual, mas também estabeleceram uma base sólida para o desenvolvimento futuro. Dessa forma, o projeto se encontra mais bem preparado para evoluções contínuas e aprimoramentos necessários, mantendo o foco em um desenvolvimento sustentável e eficiente.

