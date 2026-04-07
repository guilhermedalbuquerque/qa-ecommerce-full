# Importar biblioteca para relizar requisições HTML
import requests

# Função para listar usurios e conferir status code e estrutura
def test_list_users(base_url,api_key):
    
    # Header de autenticação, utilizando API key, Necessário para endpoints protegidos
    headers = { 
        "x-api-key": api_key
            }
    response = requests.get(f"{base_url}/users?page=2", headers= headers)
    
    # LOG da resposta para debug
    print(response.status_code)
    print(response.text)
    
    # Valida se a API respondeu corretamente(status code = 200)
    assert response.status_code == 200, f"Esperado 200, Resposta foi: {response.status_code}"
    
    # Valida se no corpo da resposta está a chave "data", garantindo a estrutura correta.
    body = response.json()
    
    assert "data" in body
    assert isinstance(body["data"],list )
    
    # Valida que a lista não está vazia
    
    assert len (body["data"]) > 0
    
    # Valida campos obrigatórios do usuário
    
    user = body["data"][0]
    assert "id" in user
    assert "email" in user
    
    