import datetime as datetime

class Orquestrator:
    def __init__(self, pipeline):
        self.pipeline = pipeline
        self.logs = []

    def log(self, message: str, error: bool = False):
        '''
        Loga uma mensagem.

        Parameters:
        message (str): Mensagem a ser logada.
        error (bool): Indica se a mensagem é um erro, default é False.
        '''
        log_type = "ERROR" if error else "INFO"
        self.logs.append(f"[{log_type}] {message}")
        if error:
            self.save_logs()

    def execute_step(self, step_name: str, step_func: function):
        '''
        Executa um passo do pipeline e loga o resultado.

        Parameters:
        step_name (str): Nome do passo a ser executado.
        step_func (function): Função a ser executada.
        '''
        try:
            self.log(f"{step_name}...")
            step_func()
            self.log(f"{step_name} concluído com sucesso.")
        except Exception as e:
            self.log(f"Erro ao {step_name}: {e}", error=True)
            raise

    def run_etl(self):
        '''
        Roda apenas o etl do pipeline.
        '''
        self.execute_step("Extraindo dados", self.pipeline.extract)
        self.execute_step("Transformando dados", self.pipeline.transform)
        self.execute_step("Carregando dados", self.pipeline.load)

    def run_model_training(self, model_type: str = 'Main'):
        '''
        Realiza o treinamento do modelo principal ou de classificação.

        Parameters:
        model_type (str): Tipo de modelo a ser utilizado. Pode ser 'Main' ou 'Class', default é 'Main'.
        '''
        if model_type == 'Main':
            self.execute_step("Treinando modelo principal", self.pipeline.trainMain)
        elif model_type == 'Class':
            self.execute_step("Treinando modelo de classificação", self.pipeline.trainClass)

    def run_predictions(self, model_type: str = 'Main'):
        '''
        Retorna as previsões do modelo principal ou de classificação.

        Parameters:
        model_type (str): Tipo de modelo a ser utilizado. Pode ser 'Main' ou 'Class', default é 'Main'.
        '''
        if model_type == 'Main':
            self.execute_step("Fazendo previsões principais", self.pipeline.predictMain)
        elif model_type == 'Class':
            self.execute_step("Fazendo previsões de classificação", self.pipeline.predictClass)

    def save_logs(self):
        '''
        Salva os logs em um arquivo de texto com o timestamp atual.
        '''
        timestamp = datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
        with open(f"logs_{timestamp}.txt", "a") as f: 
            for log in self.logs:
                f.write(log + "\n")
        self.logs.clear() 


    def execute_full_pipeline(self):
        '''
        Executa o pipeline completo, incluindo ETL, treinamento e previsões com ambos os modelos de classificação e se tem ou não falha.

        '''
        try:

            self.run_etl()  # ETL
            self.run_model_training(model_type='Main') 
            self.run_predictions(model_type='Main')  
            self.run_model_training(model_type='Class') 
            self.run_predictions(model_type='Class') 
        except Exception as e:
            self.log(f"Erro durante execução do pipeline completo: {e}", error=True)
