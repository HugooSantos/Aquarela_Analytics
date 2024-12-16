# API de Funcionários ![Logo](./logo.png)

## Descrição

Este projeto é uma API desenvolvida utilizando **FastAPI** para gerenciar dados de funcionários. A API permite realizar operações como criar, consultar, atualizar e excluir funcionários, com foco em alta performance e escalabilidade.

## Estrutura do Banco de Dados 🗄️

Abaixo, a estrutura do banco de dados que foi utilizada no projeto, incluindo as tabelas `roles` e `collaborators`:

![Estrutura do Banco de Dados](./sql.png)

### Tabela: **roles**
- `role_id` (bigint) - Chave primária, autoincremento.
- `name` (varchar(40)) - Nome do cargo.
- `role_code` (varchar(40)) - Código do cargo.
- `can_lead` (boolean) - Indica se o cargo pode liderar.

### Tabela: **collaborators**
- `collaborator_id` (bigint) - Chave primária, autoincremento.
- `first_name` (varchar(50)) - Primeiro nome do colaborador.
- `last_name` (varchar(50)) - Sobrenome do colaborador.
- `registration_code` (varchar(40)) - Código de registro do colaborador.
- `leader_name` (varchar(40)) - Nome do líder do colaborador.
- `leader_code` (varchar(40)) - Código do líder do colaborador.
- `role_id` (bigint) - Chave estrangeira, referencia o `role_id` da tabela `roles`.
- `salary` (decimal(10, 2)) - Salário do colaborador.
- `password` (varchar(255)) - Senha do colaborador.
- `status_hired` (boolean) - Indica se o colaborador está contratado.
- `created_at` (timestamp) - Data de criação do registro.
- `updated_at` (timestamp) - Data da última atualização do registro.


## Tecnologias e Bibliotecas Utilizadas 🛠️

As principais bibliotecas e tecnologias utilizadas para o desenvolvimento desta API são:

- **FastAPI**: Framework moderno e rápido para a construção de APIs RESTful.
- **Uvicorn**: Servidor ASGI rápido para rodar a aplicação.
- **SQLAlchemy**: ORM para interagir com o banco de dados.
- **SQLAlchemy-Utils**: Ferramentas adicionais para trabalhar com SQLAlchemy.
- **Psycopg2**: Conector PostgreSQL para Python.
- **Alembic**: Ferramenta de migração de banco de dados para SQLAlchemy.
- **Dotenv**: Carrega variáveis de ambiente a partir de um arquivo `.env`.
- **Pytest**: Framework de testes.
- **HTTPX**: Cliente HTTP assíncrono para realizar testes de API.
- **Bcrypt**: Biblioteca de hashing para senhas, garantindo segurança no armazenamento de dados sensíveis.
- **PostgreSQL 15**: Foi o banco de dados proposto para essa API.

### Explicação da Estrutura de pastas 📂

- **api/**: Contém o código principal da aplicação, incluindo a inicialização do FastAPI, modelos do banco de dados, controladores de endpoints e lógica de negócio.
  - **main.py**: Onde a aplicação FastAPI é configurada e os endpoints são definidos.
  - **models.py**: Define os modelos do banco de dados, usando SQLAlchemy.
  - **schemas.py**: Contém os schemas do Pydantic para validação de dados. É utilizado para garantir que as requisições e respostas estejam no formato correto.
  - **services/**: Contém a lógica de negócios para manipulação de dados, como a criação, atualização e remoção de colaboradores e cargos.
  - **routers/**: Define os controladores que implementam as rotas da API.
  - **utils/**: Funções auxiliares para tarefas complementares.
  - **repositories/**: Contém as classes responsáveis pela interação direta com o banco de dados. A camada de repositório abstrai as consultas e operações no banco.
- **migrations/**: Contém os arquivos de migração do banco de dados gerados pelo Alembic.
  
- **.env**: Armazena variáveis de ambiente, como a URL do banco de dados e chaves secretas.
  
- **requirements.txt**: Arquivo que contém as dependências do projeto.



## Funcionalidades ⚙️

Esta API oferece os seguintes endpoints:

- **Criar Funcionário**: Cria um novo funcionário com informações como nome, código de registro, cargo, salário e senha.
- **Consultar Funcionário**: Permite buscar um funcionário pelo ID.
- **Atualizar Funcionário**: Atualiza informações de um funcionário, como salário, o líder e o cargo.
- **Excluir Funcionário**: Exclui um funcionário pelo ID.
- **Alterar Senha**: Atualiza a senha de um funcionário.
- **Alterar Status**: Modifica o status de contratação de um funcionário.



## Validações Adicionadas 🛡️
Foram implementadas diversas validações para garantir a consistência e a integridade dos dados relacionados aos colaboradores e suas funções no sistema. Veja abaixo as principais validações realizadas:

- **Validação de Colaborador Existente**:

    Verifica se o colaborador existe no sistema antes de realizar qualquer operação. Caso contrário, retorna um erro com a mensagem "Collaborator not found".

- **Validação de Líderes**:

    Verifica se o código do líder informado é válido.

    Garante que o líder possui permissões de liderança antes de ser atribuído a um colaborador.

- **Validação de Permissão para Liderança**:

    Confirma que colaboradores sem um código de líder possuem a função adequada para liderar (role_code precisa ser TL).

- **Promoção de Salário**:

    Garante que, em caso de promoção, o novo salário seja maior do que o salário atual.
    Promoção de Cargo:

    Verifica se o código do novo cargo representa uma posição hierarquicamente superior ao cargo atual.

## Como Executar 🏃‍♂️


    
1. **Clonar e Instalar Dependências**
    
    via ssh:
    ```bash
    git clone git@github.com:HugooSantos/Aquarela_Analytics.git
    ```
    via https:

    ```bash
    git clone https://github.com/HugooSantos/Aquarela_Analytics.git
    ```
    
    entre no diretorio:

    ```bash
    cd Aquarela_Analytics
    ```

2. **Configurar Variáveis de Ambiente**: 

   Copie o arquivo .env.example para um novo arquivo .env e adicione as informações do seu banco de dados:
   ```bash
   cp .env.example .env
   ```

   No arquivo .env, adicione as variáveis do seu banco de dados:
   ```bash
   POSTGRES_USER=seu_usuario
   POSTGRES_PASSWORD=sua_senha
   POSTGRES_DB=nome_do_banco
   POSTGRES_HOST=localhost
   POSTGRES_PORT=sua porta (normalmente é 5432) 
   ```

3. **Instalar Dependências**:

   - Primeiro, crie e ative seu ambiente virtual:

    **No Windows**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
    **No macOS/Linux**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    - instale as Dependências

    ```bash
    pip install -r requirements.txt
    ```

    agora rode: 
    ```bash
    python create_database.py
    ```
    
    Aqui você criara o seu banco de dados.

    -logo após faça os passos abaixo dentro do seu ambiente virtual:
  
4. **Rodar as Migrations**: 
   - Execute as migrations do Alembic para configurar o banco de dados:

   ```bash 
   alembic upgrade head
   ```

5. **Rodar os Testes**: 
    
   - Para rodar os testes e garantir que tudo está funcionando corretamente, execute:

    ```bash 
    pytest api/tests/test_collaborator.py
   ```
    

6. **Ver Openapi**: 
    
   - Para ver o seu openapi rode no terminal com a venv ativa

    ```bash 
    uvicorn api.main:app --reload
    ```
   - acesse:

    ```bash 
    http://localhost:8000/docs
    ```


