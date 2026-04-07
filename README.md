# QA E-commerce Automation

![CI](https://github.com/guilhermedalbuquerque/qa-ecommerce-full/actions/workflows/tests.yml/badge.svg)

Projeto completo de automação de testes combinando **API + UI**, com execução em **CI/CD (GitHub Actions)** e geração de relatórios com **Allure Report**.

---

## Tecnologias utilizadas

* Python 3.12
* Pytest
* Playwright
* Requests
* Faker
* Allure Report
* GitHub Actions (CI/CD)

---

## Relatório de Testes

Acesse o relatório online:

https://guilhermedalbuquerque.github.io/qa-ecommerce-full/

---

## Estrutura do Projeto

```
qa-ecommerce-full/
│
├── tests/
│   ├── api/
│   ├── ui/
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

## Conceitos aplicados

* Page Object Model (POM)
* Fixtures do Pytest
* Geração de dados dinâmicos
* Testes positivos e negativos
* Integração contínua (CI)
* Variáveis de ambiente (.env)
* Execução headless (CI)

---

## Variáveis de ambiente

Crie um arquivo `.env`:

```
API_KEY=your_api_key_here
```

---

## Como rodar o projeto

```
pip install -r requirements.txt
playwright install
pytest --alluredir=allure-results
allure serve allure-results
```

---

# Testes de API

### Criar usuário

* Valida status 201
* Valida retorno do payload



![Create User](docs/images/faker-test-1.png)
![Create User 2](docs/images/faker-test-2.png)

---

### Atualizar usuário

* Valida status 200
* Confere alteração dos dados



![Update](docs/images/test-update.png)

---

### Deletar usuário

* Valida status 204



![Delete 1](docs/images/test-delete-1.png)
![Delete 2](docs/images/test-delete-2.png)

---

### Listar usuários

* Valida status 200
* Confere retorno da lista



![List](docs/images/test-example.png)

---

### Criar usuário sem API Key

* Teste negativo
* Espera status 401



![Negative](docs/images/test-negative.png)

---

### Execução dos testes API



![Run](docs/images/test-run.png)

---

# Testes de UI

Aplicação testada:
    https://www.saucedemo.com/

---

### Login com sucesso

* Preenche usuário e senha
* Valida redirecionamento

📸

![UI Login 1](docs/images/ui-login-1.png)
![UI Login 2](docs/images/ui-login-2.png)

---

### Login inválido

* Valida mensagem de erro

📸

![UI Negative 1](docs/images/ui-login-negative-1.png)
![UI Negative 2](docs/images/ui-login-negative-2.png)

---

### Page Object Model (POM)

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

### Execução dos testes UI

📸

![UI Run 1](docs/images/ui-test-run-1.png)
![UI Run 2](docs/images/ui-test-run-2.png)

---

# CI/CD com GitHub Actions

Pipeline automatizado que:

* Instala dependências
* Executa testes
* Gera relatório Allure
* Publica no GitHub Pages

---

## Disparado em:

* Push
* Pull Request

---

## Exemplo do Workflow

```
- name: Rodar testes com Allure
  run: pytest --alluredir=allure-results
```

---

# Diferenciais do projeto

✔ Integração API + UI
✔ Uso de Faker (dados dinâmicos)
✔ Segurança com `.env`
✔ Execução headless no CI
✔ Relatório Allure automatizado
✔ Deploy com GitHub Pages

---

#  Autor

Guilherme de Albuquerque Silva Azevedo

---

#  Observações

Projeto desenvolvido com foco em simular um ambiente real de automação de testes, incluindo validações completas de API e interface, boas práticas de organização e integração contínua.
