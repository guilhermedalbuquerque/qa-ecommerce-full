from pages.login_page import LoginPage


# Função para abrir e controlar página.
def test_login_failed(page):
    
    login_page = LoginPage(page)
        
    login_page.go_to()
        
    # Preencher o login falso e Clica no botão login.
    login_page.login("standard_user","senha_errada")
        
    # Valida mensagem de erro
    # Captura mensagem de erro exibido na tela e valida retornao o erro esperado.
    error_message = page.locator("[data-test='error']")
    assert error_message.is_visible()
    assert "Username and password do not match" in error_message.text_content()
        