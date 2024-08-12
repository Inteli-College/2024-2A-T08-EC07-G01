Nesta documentação, apresentamos uma solução de tecnologia projetada para atender às necessidades específicas e requisitos da Volkswagen. A eficácia e o sucesso de qualquer solução tecnológica dependem em grande medida da clareza, precisão e compreensão de seus requisitos. Portanto, é fundamental definir e entender adequadamente os requisitos funcionais e não funcionais.

## Requisitos Funcionais

Os requisitos funcionais descrevem as funcionalidades específicas e as operações que a solução deve realizar. Eles são a base para o desenvolvimento e a implementação da solução, delineando as capacidades e os comportamentos esperados do sistema.

1. O sistema deve receber progressivamente as informações provenientes da planta e ir preenchendo as informações de montagem de cada um dos carros carros na linha de montagem.

2. O modelo já deve ter feito uma previsão em que seja possível identificar um provavel erro antes que o carro seja levado para o test-drive.

3. O modelo deve ter como saída as inconsistências mais prováveis para serem checadas durante o teste e informar qual tipo de teste é mais adequado para cada situação, de acordo com as informações de montagem dos carros.

4. O sistema deve possuir uma área destinada a um dashboard para fornecer informações importantes para o usuário como o status de cada carro registrado e por exemplo por quais processos ele já passou e se algum problema foi encontrado até então.

5. O sistema deve ter uma área destinada a receber mais dados para que ele possa adicioná-los ao seu banco de dados e ser retreinado com novas informações.

7. O sistema deve ter deploy na AWS.

## Requisitos Não Funcionais

Os requisitos não funcionais referem-se às características e qualidades do sistema que não estão diretamente relacionadas às funcionalidades específicas, mas que são cruciais para garantir seu desempenho, segurança, escalabilidade e usabilidade. Estes incluem aspectos como desempenho, confiabilidade, segurança, usabilidade e manutenibilidade.

1. O sistema deve apresentar uma predição após a submissão dos dados necessários em até 5 segundos.

2. O modelo deve apresentar uma precisão de no mínimo 95%.

3. O sistema deve apresentar Dashbords de entendimento claro e que sejam de boa visibilidade, trabalhando de maneira correta o contraste, espaçamento e como as informações são apresentadas.

4. Deve ser possível fazer a visualização de maneira clara do status de cada carro e ver os problemas encontrados até a etapa que o carro de encontra na linha de montagem.
