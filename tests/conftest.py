# Fixture para evitar repetição nas requisições dos testes.
from playwright.sync_api import sync_playwright
from database.conection import create_table
from database.connection_postgres import get_connection_pg, create_table_pg
import pytest
from dotenv import load_dotenv
import os
import sqlite3

# Carrega variaveis do arquivo ".env".
load_dotenv()


# Fixture para API
@pytest.fixture
def base_url():
    return "https://reqres.in/api"

# API KEY segura
@pytest.fixture
def api_key():
    return os.getenv("API_KEY")

# Fixture para UI
@pytest.fixture
def page():
    with sync_playwright() as p: # Abre o navegador e fecha assim que o bloco terminar.
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        yield page # Entrega a página para o teste
        
        browser.close()
        
# Fixture para banco de dados.
@pytest.fixture
def db():
    # Criar banco na mémoria
    connect = sqlite3.connect(":memory:")
    create_table(connect) # Criar a tabela do banco de dados.
    
    # Entrega banco para o teste.
    yield connect 
    
    connect.close()
    
# Fixture para banco de dados Postgres.
@pytest.fixture
def db_postgres():
    connect = get_connection_pg()
    create_table_pg(connect)
    
    # Entrega banco para o teste.
    yield connect
    
    # Limpa banco a cada teste
    exec = connect.cursor()
    exec.execute("DELETE FROM users")
    connect.commit()
    connect.close()
    