---
title: "Modelagem e implementação da I.A"
sidebar_position: 5
---

## **1.1** Introdução

Dado o escopo do projeto, de desenvolver um modelo preditivo para detectar falhas nos veículos da Volkswagen, foi escolhido um modelo de **Random Forest**, devido à sua capacidade de lidar com dados de alta dimensionalidade, flexibilidade, e bom desempenho em termos de **acurácia** e **recall**.

Além disso, a pipeline de dados foi implementado de forma robusta para manipular grandes volumes de informações e integrá-las de maneira eficiente ao modelo, permitindo que o sistema fosse flexível e escalável.

:::tip Info
Para ter uma visão melhor de como foi feito o pipeline de dados, veja a documentação de [Engenharia de Dados](/Sprint%205/eng)
:::

## **1.2** Lógica da implementação da Pipeline e escolha de Features

Aqui está o parágrafo corrigido para refletir a utilização de Random Forest:

## **1.2** Lógica da implementação da Pipeline e escolha de Features

Para a implementação do modelo de **Random Forest**, foi necessário seguir uma lógica de implementação que garantisse a eficiência e a precisão do modelo. A escolha das features foi feita com base na relevância para a detecção de falhas, garantindo que o modelo tivesse acesso a informações críticas para realizar as previsões.

### **1.2.1** Escolha do Modelo: Random Forest

A escolha do **Random Forest** foi feita devido à sua capacidade de lidar com grandes volumes de dados e identificar relações complexas entre as variáveis, sem a necessidade de supor dependências temporais como no caso de modelos de redes neurais. O **Random Forest** foi preferido em relação a outros modelos, como **Redes Neurais Recorrentes (RNN)** ou **LSTMs**, por sua flexibilidade, robustez contra overfitting, e eficiência computacional.

:::tip Info
**Random Forest** é um algoritmo de aprendizado de máquina que utiliza múltiplas árvores de decisão para melhorar a precisão e reduzir o risco de overfitting. Ele é eficiente e performa bem em uma ampla gama de problemas, sem a necessidade de modelar diretamente as dependências temporais.
:::

A principal razão para a escolha deste modelo foi o bom equilíbrio entre **acurácia** e **recall** nos testes, o que garantiu a capacidade do sistema de minimizar falsos negativos — falhas que não são detectadas. Isso é crucial, pois falhas não detectadas em veículos podem levar a consequências críticas.

### **1.2.2** Pipeline de Treinamento

A pipeline de treinamento foi cuidadosamente estruturado para garantir que os dados fossem corretamente manipulados antes de serem usados no modelo. As etapas incluem:

1. **Pré-processamento dos Dados**: Os dados são preparados por meio da função `preparacao_dados`, que separa as features e o target e transforma os dados em arrays NumPy.
2. **Estruturação do Modelo GRU**: A rede GRU é composta por duas camadas, cada uma com 50 unidades, seguidas por uma camada densa com ativação sigmoide para realizar a classificação binária (falha ou não).
3. **Treinamento e Avaliação**: Após o treinamento, o modelo é avaliado com base nas métricas de **acurácia**, **recall**, **f1_score** e **precisão**.

**Código do Modelo GRU:**

```python
def execute(df_merged):
    X_train, X_test, y_train, y_test = preparacao_dados(df_merged)

    model = Sequential()
    model.add(GRU(50, activation="relu", return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(GRU(50, activation="relu"))
    model.add(Dense(1, activation="sigmoid"))

    model.compile(optimizer="adam", loss="binary_crossentropy")

    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

    y_pred = model.predict(X_test)
    y_pred = (y_pred > 0.5).astype(int).flatten()

    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred)
    }
```

## **1.3** Consolidação do pipeline de dados com encapsulamento em classes e adequado para um deploy contínuo

Foi feita a consolidação do pipeline de dados em uma classe Python, permitindo que o processo de treinamento e avaliação do modelo GRU seja executado de forma modular e organizada. A classe encapsula as etapas de preparação dos dados, treinamento do modelo e avaliação, facilitando a reutilização e manutenção do código.

### **1.3.1** O Papel do Orquestrador

O **Orchestrator** é a peça central do pipeline de dados, responsável por executar e coordenar dinamicamente cada etapa do processamento de forma organizada e modular. Ele permite a execução de várias fases do pipeline de forma automática, garantindo que o fluxo de dados ocorra sem interrupções.

Um dos principais benefícios do **Orchestrator** é que ele pode carregar scripts de processamento dinamicamente de um sistema de arquivos distribuído, como o **GridFS**, permitindo que as etapas do pipeline sejam atualizadas ou modificadas sem que seja necessário interromper o sistema.

### **1.3.2** Explicação Detalhada do Código do Orquestrador

O **Orchestrator** foi projetado para oferecer flexibilidade e escalabilidade ao pipeline. Suas principais funcionalidades incluem:

- **Configuração Dinâmica**: O pipeline é configurado por meio de um arquivo JSON, que especifica cada etapa de processamento, como o nome dos módulos, os arquivos de script e os DataFrames envolvidos.
- **Execução Modular**: Cada etapa do pipeline é encapsulada em um módulo Python separado. O orquestrador executa esses módulos em sequência, injetando os DataFrames necessários em cada etapa, garantindo a integridade dos dados ao longo do processo.
- **Carregamento de Scripts**: A função `fetch_script_from_gridfs` carrega dinamicamente os scripts do GridFS, permitindo que o pipeline seja atualizado sem interrupções no fluxo.

**Código do Orquestrador:**

```python
class Orchestrator:
    def __init__(self, pipeline_steps, dataframes, mongo_uri, db_name):
        self.pipeline_steps = pipeline_steps
        self.dataframes = dataframes  # Dictionary to store DataFrames
        self.logs = []
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.fs = gridfs.GridFS(self.db)

    def run_dynamic_pipeline(self):
        for step in self.pipeline_steps:
            module_name = step["name"]
            file_path = step["file_path"]
            kwargs = step.get("kwargs", {}).copy()

            dataframes_needed = step.get("dataframes", [])
            for df_name in dataframes_needed:
                if df_name in self.dataframes:
                    kwargs[df_name] = self.dataframes[df_name]
                else:
                    raise ValueError(f"DataFrame '{df_name}' not found for step '{module_name}'.")

            script_content = self.fetch_script_from_gridfs(file_path)
            module = self.load_module_from_file(module_name, script_content)

            result = self.execute_step(step["name"], module, **kwargs)

            output_df_name = step.get("output_dataframe")
            if output_df_name:
                self.dataframes[output_df_name] = result

        return self.dataframes
```

### **1.3.3** Exemplo de Execução de Múltiplas Etapas

O pipeline processa e normaliza os dados de entrada antes de serem alimentados no modelo GRU. As principais etapas incluem:

1. **Processamento dos Resultados**: A função `drop_colunas` remove colunas desnecessárias, enquanto a função `agregar_por_id` agrega os dados por identificadores (ID).
2. **Normalização**: As colunas relevantes são normalizadas utilizando o **MinMaxScaler**, preparando os dados para o modelo.
3. **Treinamento e Predição**: O modelo GRU é treinado com os dados processados, e as predições subsequentes são geradas.

O orquestrador garante que cada uma dessas etapas seja executada de forma ordenada e sem interrupções, registrando logs para facilitar a auditoria e o debugging.

:::info

Para saber mais do Orquestrador, clique [aqui](/Sprint%204/Pipelines/Orquestrador)
:::

## **2.1** Conclusão

O pipeline de machine learning para predição de falhas em veículos foi projetado para ser modular, escalável e eficiente. A escolha do modelo **GRU** proporcionou o melhor equilíbrio entre **acurácia** e **recall**, sendo crucial para garantir que falhas não sejam negligenciadas pelo sistema, reduzindo o risco de falsos negativos.

O **Orchestrator** desempenha um papel vital na execução do pipeline, facilitando a orquestração dinâmica de múltiplas etapas de processamento, permitindo atualizações contínuas e assegurando que o sistema esteja sempre operando de forma eficiente. Este pipeline é uma solução robusta e preparada para escala, oferecendo flexibilidade para futuras expansões e melhorias.
