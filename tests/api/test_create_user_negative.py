# Importar bibliote para realizar requisições HTML.
# Importar faker para gerar dados aleatorios.
import requests
from faker import Faker

fake = Faker("pt_BR")

# Teste para validar erro de autenticação (sem API Key)
def test_creat_user_no_key(base_url):
    
    # fake utilizado para não gerar valores fixos, simulando ambiente real.
    payload =  {
        "name": fake.name(),
        "job": fake.job()
    }
    
    response = requests.post(f"{base_url}/users", json=payload)
    print(response.status_code)
    print(response.text)
    
    # Valida que a API não permite criação de usuário sem autentação
    # Espera retorno HTTP 401 (Unauthorized)
    assert response.status_code == 401