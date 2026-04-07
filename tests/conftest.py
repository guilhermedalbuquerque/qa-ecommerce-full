# Fixture para evitar repetição nas requisições dos testes.
from playwright.sync_api import sync_playwright
import pytest
from dotenv import load_dotenv
import os

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