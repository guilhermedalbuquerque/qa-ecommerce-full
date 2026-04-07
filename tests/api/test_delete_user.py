# Importar bibliote para realizar requisições HTML.
import requests

# Função para deletar usuário (DELETE)
def test_delete_user(base_url):
    
    # ID de exemplo para á API
    user_id = 2
    
    headers = {"x-api-key":"pub_58acb8b41634808136010a9b7bf9e612" }
    
    response = requests.delete(f"{base_url}/users/{user_id}", headers=headers)
    
    print("Status : ", response.status_code)
    
    # Valida se a remoção foi efetuada com sucesso (204)
    assert response.status_code == 204
    