# QA E-commerce Automation

![CI](https://github.com/guilhermedalbuquerque/qa-ecommerce-full/actions/workflows/tests.yml/badge.svg)

Projeto completo de automação de testes combinando **API + UI + Banco de Dados**, com execução em **CI/CD (GitHub Actions)** e geração de relatórios com **Allure Report**.

---

# Arquitetura do Projeto

O projeto evolui de testes simples para uma estrutura mais robusta com:

* Camada de **Service + Repository Pattern**
* Suporte a múltiplos bancos:

  * SQLite (em memória)
  * PostgreSQL (ambiente real)
* Separação de responsabilidades:

```
Teste → Service → Repository → Database
```

---

# Tecnologias utilizadas

* Python 3.12
* Pytest
* Playwright
* Requests
* Faker
* Allure Report
* GitHub Actions (CI/CD)
* SQLite
* PostgreSQL
* psycopg2
* Docker (ambiente local para banco)

---

# Relatório de Testes

Acesse o relatório online:

https://guilhermedalbuquerque.github.io/qa-ecommerce-full/

---

# Estrutura do Projeto

```
qa-ecommerce-full/
│
├── tests/
│   ├── api/
│   ├── ui/
│
├── repository/
│   ├── user_repository_sqlite.py
│   └── user_repository_postgres.py
│
├── services/
│   └── user_service.py
│
├── database/
│   ├── connection.py
│   └── connection_postgres.py
│
├── pages/
│   └── login_page.py
│
├── utils/
│   └── data_generator.py
│
├── docs/
│   └── images/
│
├── conftest.py
├── requirements.txt
└── pytest.ini
```

---

# Conceitos aplicados

* Page Object Model (POM)
* Fixtures do Pytest
* Geração de dados dinâmicos
* Testes positivos e negativos
* Integração contínua (CI)
* Variáveis de ambiente (.env)
* Execução headless (CI)
* Repository Pattern
* Separação de camadas (Service + Data Access)

---

# Variáveis de ambiente

Crie um arquivo `.env`:

```
API_KEY=your_api_key_here
```

---

# Como rodar o projeto

```
pip install -r requirements.txt
playwright install
pytest --alluredir=allure-results
allure serve allure-results
```

---

# Testes com Banco de Dados

Foram implementados testes completos de persistência utilizando dois bancos:

## SQLite (in-memory)

* Banco criado em memória durante o teste
* Execução rápida e isolada
* Ideal para testes unitários

## PostgreSQL

* Simula ambiente real
* Executado via Docker local
* Testes mais próximos de produção

## Operações testadas

* Criar usuário (INSERT)
* Buscar usuário (SELECT)
* Atualizar usuário (UPDATE)
* Deletar usuário (DELETE)

---

# Repository Pattern

O projeto utiliza o padrão **Repository Pattern** para abstrair o acesso ao banco.

### Benefícios:

* Baixo acoplamento
* Facilidade de manutenção
* Troca de banco sem impactar testes

## Estrutura

```
Test → Service → Repository → Database
```

## Implementações

* UserRepositorySQLite
* UserRepositoryPostgres

---

# Banco com Docker (opcional)

O PostgreSQL pode ser executado via Docker:

```
docker-compose up -d
```

---

# Testes de API

API utilizada:

👉 https://reqres.in/api

## Criar usuário

* Valida status 201
* Valida retorno do payload

![Create User](docs/images/faker-test-1.png)
![Create User 2](docs/images/faker-test-2.png)

---

## Atualizar usuário

* Valida status 200
* Confere alteração dos dados

![Update](docs/images/test-update.png)

---

## Deletar usuário

* Valida status 204

![Delete 1](docs/images/test-delete-1.png)
![Delete 2](docs/images/test-delete-2.png)

---

## Listar usuários

* Valida status 200
* Confere retorno da lista

![List](docs/images/test-example.png)

---

## Criar usuário sem API Key

* Teste negativo
* Espera status 401

![Negative](docs/images/test-negative.png)

---

## Execução dos testes API

![Run](docs/images/test-run.png)

---

# Testes de UI

Aplicação testada:
👉 https://www.saucedemo.com/

## Login com sucesso

* Preenche usuário e senha
* Valida redirecionamento

![UI Login 1](docs/images/ui-login-1.png)
![UI Login 2](docs/images/ui-login-2.png)

---

## Login inválido

* Valida mensagem de erro

![UI Negative 1](docs/images/ui-login-negative-1.png)
![UI Negative 2](docs/images/ui-login-negative-2.png)

---

## Page Object Model (POM)

Classe responsável por centralizar ações da página:

```
class LoginPage:
    def __init__(self, page):
        self.page = page

    def go_to(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")
```

![POM 1](docs/images/ui-pom-1.png)
![POM 2](docs/images/ui-pom-2.png)

---

## Execução dos testes UI

![UI Run 1](docs/images/ui-test-run-1.png)
![UI Run 2](docs/images/ui-test-run-2.png)

---

# CI/CD com GitHub Actions

Pipeline automatizado que:

* Instala dependências
* Executa testes
* Gera relatório Allure
* Publica no GitHub Pages

## Disparado em:

* Push
* Pull Request

## Exemplo do Workflow

```
- name: Rodar testes com Allure
  run: pytest --alluredir=allure-results
```

---

# Diferenciais do projeto

 -> Integração API + UI
 -> Testes com banco relacional (SQLite + PostgreSQL)
 -> Repository Pattern (arquitetura limpa)
 -> Docker para ambiente real
 -> Faker (dados dinâmicos)
 -> Allure Reports
 -> GitHub Actions (CI/CD)

---

#  Autor

Guilherme de Albuquerque Silva Azevedo

---

# Observações

Projeto desenvolvido com foco em simular um ambiente real de automação de testes, incluindo:

* Testes de API e UI
* Validação de persistência em banco de dados
* Arquitetura escalável
* Boas práticas de automação
