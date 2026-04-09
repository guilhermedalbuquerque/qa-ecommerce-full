# Importar API para realizar requisição HTML.
# Importar funções para criação e manipulação da tabela de dados.
# importar função para geração de dados.
import requests
from utils.data_generator import create_user_payload

from database.queries import insert_user, get_user_by_name, delete_user, update_user

# Função para validar criação, atualização e exclusão do usuário no banco.
def test_user_validate_db(base_url,api_key,db):
    
    headers = {
        "x-api-key" : api_key,
        "Content-Type":"application/json"
        }
    
    payload = create_user_payload()
    
    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    assert response.status_code == 201
    
    # Inserir no banco de dados.
    insert_user(db,payload["name"],payload["job"])
    
    # Validar no banco de dados
    user_db = get_user_by_name(db,payload["name"])
    
    assert user_db is not None
    assert payload["name"] == user_db[1]
    assert payload["job"] == user_db[2]
    #---------------------------------------------------------------------------------------------------------------
    new_job= "QA Engineer"
    updated = update_user(db,payload["name"],new_job)
    
    assert updated == 1
    
    # Validar banco após atualização
    user_new_job = get_user_by_name(db,payload["name"])
    
    assert user_new_job is not None
    assert user_new_job[2] == new_job
    
    #---------------------------------------------------------------------------------------------------------------
    deleted = delete_user(db,payload["name"])
    assert deleted == 1
    
    # Validar banco após exclusão.
    user_after_delete = get_user_by_name(db,payload["name"])
    assert user_after_delete is None
    
    
    
    
    
    