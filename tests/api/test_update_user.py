# Importar bibliote para realizar requisições HTML.
from utils.data_generator import create_user_payload
import requests


# Função para atualizar usuário (PUT).
def test_update_user(base_url,api_key):
    # ID para exemplo da API.
    user_id = 2 
    
    headers = {
        "x-api-key":api_key,
        "Content-Type": "application/json"
        }
    
    payload = create_user_payload()

    response = requests.put(f"{base_url}/users/{user_id}", json=payload, headers=headers)
    print("payload enviado:")
    print(payload)
    
    print("resposta:")
    print(response.text)
    
    # Valida Sucesso no status code (200)
    assert response.status_code == 200
    
    body = response.json()
    
    # Valida se os dados foram atualizados
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    
