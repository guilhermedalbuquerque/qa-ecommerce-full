# Criar classe "LoginPage" para representar página de login e reutilizar no teste.

class LoginPage:
    # Criar construtor daa classe, recebe o objeto do Playwright.
    def __init__(self,page):
        self.page = page
    
    # Função para acessar página de login.
    def go_to(self):
        self.page.goto("https://www.saucedemo.com/")
        
    #Função para efetuar login.
    def login(self,username,password):
        self.page.fill("#user-name",username)
        self.page.fill("#password",password)
        self.page.click("#login-button")