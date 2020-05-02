# Trabalho de Processamento de Informação

## Objetivo

Pretende-se criar um módulo extrator que permita obter informação a partir da Web, de forma automatizada, 
relativamente a uma temática informacional previamente definida.

### Linhas de orientação para o trabalho:

1. O módulo poderá ser desenvolvido em qualquer linguagem de programação à escolha de cada grupo de trabalho.
2. O módulo deverá permitir obter um conjunto de url’s válidos e extrair informação a partir destes. 
Por url’s entende-se aqueles cujo conteúdo das suas páginas corresponde à unidade de informação selecionada 
para a prova de conceito.
3. O conjunto de dados a obter deverá ser superior a 200.000 registos e não deverá ultrapassar os 4Gb de informação.
4. O mecanismo criado deverá permitir a atualização da informação e a extração desta através de um processo 
intervalado.
 
### Regras

Para este momento de avaliação são requeridos grupos de trabalho entre 2 a 3 alunos.
O trabalho implica uma demonstração/explicação presencial a realizar em sala de aula com todos os membros do grupo.
Cada grupo terá que explorar um tema diferente dos demais.
Todos os grupos terão que validar o tema escolhido com o docente.

## Resultados

### Método escolhido

O site escolhido para a recolha de informação foi o: https://transparency.entsoe.eu/
Trata-se de um site com informação diversa sobre o estado da rede eléctrica em vários paises, actualizado a cada hora.

Pretende-se reunir informação de consumo e tipos de produçáo de energia para 5 países (Portugal, Espanha, Itália, 
Alemanha e Irlanda).
Os elementos em estudo são os seguintes:

#### Informação sobre consumo (previsão e observado) 
https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show

#### Imformação sobre os tipos de produção
https://transparency.entsoe.eu/generation/r2/installedGenerationCapacityAggregation/show

### Instalação

Para correr este software deverá ter instalado o python3, posicionar-se na raíz do programa e
 de seguida instalar as bibliotecas necessárias:

1. `pip install -r requirements.txt `
2. Para correr o software deverá executar o ficheiro **main.py** (certifique-se que dispõe de uma base de dados e que as 
condições de acesso se encontram correctamente definidas (caso contrário verificar o ponto seguinte): `python main.py`

### Base de dados MySQL

O projecto necessita de uma base de dados MYSQL operacional. Poderá usar os seguintes métodos para criação e gestão
de uma instância MySQL.

Na pasta ```/dump``` do projecto encontra-se um ficheiro que pode ser usado para importar a informação na base de dados.
Dessa forma evita-se a necessidade de extrair a informação do site, que poderá levar algumas horas. 

#### Docker

1. docker run --name mysql-server -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 -d mysql:latest

#### Base de dados existente

Caso já disponha de uma instância MySQL deverá alterar as condições de acesso no ficheiro: *models/MyModel.py* 
nomeadamente o *username, password e host*.

```python
engine = create_engine('mysql+mysqlconnector://root:password@localhost')  # connect to server
```

### Objectivos do 2º Momento

Pretende-se criar um módulo de armazenamento permita alojar a informação obtida através do módulo extrator criado no 
TP1. A passagem dos dados para o módulo de armazenamento poderá ser feita diretamente a partir da web ou a partir 
dos dados previamente armazenados durante o desenvolvimento do TP1.

#### Resultados

O objectivo deste 2º momento é armazenar a informação trabalhada no 1º momento em um SGBD.

Posteriormente para o 3º momento o objectivo é avaliar com base na informação recolhida o seguinte:

#### Consumo:

1.  Avaliar o erro de previsão da plataforma para a previsão de consumo. Verificar a média do erro para todos os países 
e retirar algumas conclusões se possivel. 
2. Determinar o dia em que foi observado o maior erro para cada país. Tentar justificar se possivel com 
algum acontecimento de ordem imprevisivel. Por exemplo o erro da previsão de consumo no dia em que foi estado de emergência.
3. Avaliar através dos valores observados, os meses ou dias onde a carga foi mais elevada. 
Determinar também o ano/periodo onde existiu um máximo e mínimo de carga. Tentar explicar e retirar conclusões.
4. Avaliar o impacto de pontes nos valores observados para os diferentes países.
5. Avaliar o impacto que o COVID-19 teve na carga/consumo de energia nos diferentes países no mês de Março e Abril 
em comparação com anos anteriores.  

#### Tipos de Produção

6. Através de um gráfico, verificar a evolução das energias renováveis para os diferentes países.
7. Através de um gráfico, Verificar a evolução na diminuição de combustiveis fosseis nos diferentes países.
