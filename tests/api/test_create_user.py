# Importar bibliote para realizar requisições HTML.
# Importar faker para gerar dados aleatorios.
import requests
from utils.data_generator import create_user_payload



# Função para criar um usuario via API.
def test_create_user(base_url,api_key):
    
    # Header para informar chave para autenticação da API.
    # Declarando tipo de connteúdo para requisição (JSON).
    headers = { 
        "x-api-key":api_key, 
        "Content-Type": "application/json"
        }
    
    # Dados para a criação do usuário.
    
    payload = create_user_payload()
    print("Payload enviado:")
    print(payload)
     
    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    print(response.status_code)
    print(response.text)
    
    # Valida criação (201 Created).
    assert response.status_code == 201
    
    body = response.json()
    
    # Validar retorno da API.
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    