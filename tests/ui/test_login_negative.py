# Importa a biblioteca para controle do navegador.
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


# Função para abrir e controlar página.
def test_open_page():
    with sync_playwright() as p: # Abre o navegador e fecha assim que o bloco terminar.
        broswer = p.chromium.launch(headless=False, slow_mo=2000) # Abre Navegador.
        page = broswer.new_page()
        
        login_page = LoginPage(page)
        
        login_page.go_to()
        
        # Preencher o login falso e Clica no botão login.
        login_page.login("standard_user","senha_errada")
        
        # Valida mensagem de erro
        #Caaptura mensagem de erro exibido na tela e valida retornao o erro esperado.
        error_mensage = page.locator("[data-test='error']").text_content()
        assert "Username and password do not match" in error_mensage
        broswer.close()