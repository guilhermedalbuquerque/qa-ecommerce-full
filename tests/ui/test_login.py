# Importa a biblioteca para controle do navegador.

from pages.login_page import LoginPage


# Função para abrir e controlar página.
def test_login_sucess(page):
        
    login_page = LoginPage(page)
        
    login_page.go_to()
        
    # Preencher o login e Clica no botão login.
    login_page.login("standard_user","secret_sauce")
        
    # Valida se entrou na home
    assert "inventory" in page.url
    
        
    
        
    