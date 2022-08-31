# Calculadora de Aluguel



![GitHub repo size](https://img.shields.io/github/repo-size/alehkiz/Scraping-Aluguel?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/alehkiz/Scraping-Aluguel?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/alehkiz/Scraping-Aluguel?style=for-the-badge)
![Github open issues](https://img.shields.io/github/issues/alehkiz/Scraping-Aluguel?style=for-the-badge)


Sistema para predição de valores de aluguel para apartamentos extraídos do [Kaggle](https://www.kaggle.com/datasets/argonalyst/sao-paulo-real-estate-sale-rent-april-2019?resource=download).

* **A análise dos dados, incluindo as atividades de:**
  * Análise exploratórios;
  * Normalização;
  * Aplicação de `OrdinalEncoder`
  * Aplicação de `Principal Component Analysis`
  * Para criação do modelo utilizamos `GridSearchCV` para otimizar nossos hiperparamêtros;
  * Após identificar os melhores hiperparametros com o nosso modelo, criamos um `Pipeline` com Normalização aplicando o `StandardScaler`, em seguida o `PCA` e por fim o nosso modelo;
  * O score fica em torno de **0.65**
  * RMSE de **0.051**
* **Criamos nos aplicativo web:**
  * Baseado em **Flask** e **Postgresql**.
  * O aplicativo utiliza as variáveis que consideramos importantes em nossa análise, sendo elas: 
    * Quartos;
    * Banheiros;
    * Suites;
    * Vagas de estacionamento;
    * Area;
    * Bairro;
    * Mobiliado;
    * Piscina;
    * Elevador;
  * Utiliza uma API para envio do formulário via ajax.
* Os dados são persistidos em banco de dados para futura consulta.
* O usuário consegue salvar se o aluguel informado está de acordo com a sua pretenção de aluguel;
* Caso não esteja poderá informar o valor desejado.

### Melhorias futuras (Análise de dados):

- [X] Aplicar OrdinalEncoder
- [X] Aplicar PCA
- [X] Aplicar GridSearch
- [X] Aplicar Pipeline
- [X] Melhorar o modelo


### Melhorias futuras (Aplicativo Web):
- [x] Criar factory para o Flask
- [x] Criar factory para Blueprints
- [x] Criar formulário para aplicativo
- [x] Criar configuração de `desenvolvimento`, `produção`
- [x] Criar função para fazer o `predict` do modelo.
- [x] Criar javascript para tratar as requisições ajax.
- [x] Fazer o deploy no heroku

## 💻 Pré-requisitos

* versão mais recente de `python`
* Utilize um ambiente virtual: https://docs.python.org/3/tutorial/venv.html
* No ambiente virtual, instale as bibliotecas necessárias: `pip install -r requirements.txt`

## ☕ Subindo o servidor:

Para utilizar, siga estas etapas:

na raiz do repositórico, inicie o ambiente virual e instale os pacotes necessários, e rode flask run.

Lembre-se que utilizamos o postgres, logo, você deverá ter criado, além de criar o banco de dados com o nome `house_price` após criar o banco de dados, rode o comando `flask shell` e no terminal utilize o comando `db.create_all()`, saia e então rode `flask run`


## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

[⬆ Voltar ao topo](#Scraping-Aluguel)<br>
