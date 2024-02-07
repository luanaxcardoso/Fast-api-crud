python -m venv .venv # Cria um ambiente virtual

.venv\Scripts\activate # Ativa o ambiente virtual

pip install "fastapi[all]" # Instala o FastAPI e suas dependências como o Uvicorn

uvicorn app:app --reload # Inicia o servidor

métodos HTTP: GET, POST, PUT, DELETE

---------------------------------------------------------------------------------------------------

Estrutura do Usuário
Cada usuário possui os seguintes atributos:

id: Um identificador único (UUID) para o usuário.
first_name: O primeiro nome do usuário.
last_name: O sobrenome do usuário.
email: O endereço de e-mail do usuário.
role: O papel do usuário, que é uma lista de roles.
Estrutura do Role
Cada role possui os seguintes atributos:

role_1: Descrição do primeiro tipo de papel.
role_2: Descrição do segundo tipo de papel.
role_3: Descrição do terceiro tipo de papel.
Modelos
O código define dois modelos:

User: Representa a estrutura de dados de um usuário.
Role: Representa a estrutura de dados de um papel.
Funcionalidades Adicionais
O código inclui tratamento de erros básico para lidar com casos em que um usuário não é encontrado ou uma operação de exclusão falha.
Um endpoint de raiz (/) que retorna uma mensagem "Hello World" para verificar se o servidor está ativo.
Execução Local
Clone este repositório.
Instale as dependências do projeto com pip install -r requirements.txt.
Execute o servidor FastAPI com uvicorn main:app --reload.
Acesse os endpoints fornecidos para interagir com a API de gerenciamento de usuários.