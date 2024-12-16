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
- **SQLAlchemy**: ORM (Object-Relational Mapper) para interagir com o banco de dados de forma eficiente.
- **SQLAlchemy-Utils**: Ferramentas adicionais para trabalhar com SQLAlchemy.
- **Psycopg2**: Conector PostgreSQL para Python.
- **Alembic**: Ferramenta de migração de banco de dados para SQLAlchemy.
- **Dotenv**: Carrega variáveis de ambiente a partir de um arquivo `.env`.
- **Pytest**: Framework de testes para garantir a qualidade do código.
- **HTTPX**: Cliente HTTP assíncrono para realizar testes de API.
- **Bcrypt**: Biblioteca de hashing para senhas, garantindo segurança no armazenamento de dados sensíveis.

### Explicação da Estrutura de pastas 📂

- **api/**: Contém o código principal da aplicação, incluindo a inicialização do FastAPI, modelos do banco de dados, controladores de endpoints e   lógica de negócio.
- **main.py**: Onde a aplicação FastAPI é configurada e os endpoints são definidos.
- **models.py**: Define os modelos do banco de dados, usando SQLAlchemy.
- **schemas.py**: Contém os schemas do Pydantic para validação de dados.
- **services/**: Lógica de negócio para manipulação de dados, como a criação, atualização e remoção de funcionários e cargos.
- **routers/**: Define os controladores que implementam as rotas da API.
- **utils/**: Funções auxiliares, como o gerenciamento de senhas (por exemplo, utilizando bcrypt).
  
- **migrations/**: Contém os arquivos de migração do banco de dados gerados pelo Alembic.
- **.env**: Armazena variáveis de ambiente, como a URL do banco de dados.
- **requirements.txt**: Arquivo com as dependências do projeto.

## Funcionalidades ⚙️

Esta API oferece os seguintes endpoints:

- **Criar Funcionário**: Cria um novo funcionário com informações como nome, código de registro, cargo, salário e senha.
- **Consultar Funcionário**: Permite buscar um funcionário pelo ID.
- **Atualizar Funcionário**: Atualiza informações de um funcionário, como salário, o líder e o cargo.
- **Excluir Funcionário**: Exclui um funcionário pelo ID.
- **Alterar Senha**: Atualiza a senha de um funcionário.
- **Alterar Status**: Modifica o status de contratação de um funcionário.

## Como Executar 🏃‍♂️


1. **Configurar Variáveis de Ambiente**: 

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

2. **Instalar Dependências**:

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
    
    - Clone o repositório e instale as dependências:

    ```bash
    git clone <url-do-repositorio>
    cd <diretorio-do-repositorio>
    pip install -r requirements.txt
    ```

    -logo após faça os passos abaixo dentro do seu ambiente virtual:
  
3. **Rodar as Migrations**: 
   - Execute as migrations do Alembic para configurar o banco de dados:

   ```bash 
   alembic upgrade head
   ```

4. **Rodar os Testes**: 
    
   - Para rodar os testes e garantir que tudo está funcionando corretamente, execute:

    ```bash 
    pytest api/tests/test_collaborator.py
   ```
    

