# Importar API para realizar requisição HTML.
# Importar funções para criação e manipulação da tabela de dados.
# importar função para geração de dados.
import requests
from database.queries_postgres import (
    insert_user_pg,
    get_user_by_name,
    update_user,
    delete_user
    )

from utils.data_generator import  create_user_payload

# Função para validar criação, atualização e exclusão do usuário no banco.
def test_user_validate_db_postgres(base_url,api_key,db_postgres):
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }

    payload = create_user_payload()

    response = requests.post(f"{base_url}/users", json=payload, headers=headers)
    assert response.status_code == 201
    
    # Inserir usário no banco de dados
    insert_user_pg(db_postgres,payload["name"],payload["job"])
    
    # Validar no banco de dados
    user_db = get_user_by_name(db_postgres,payload["name"])
    
    assert payload["name"] == user_db[1]
    assert payload["job"] == user_db[2]
    #-----------------------------------------------------------------------------------------------------------------
    # Atualiza usuário no banco de dados.
    new_job = "QA Engineer Senior"
    
    updated = update_user(db_postgres,payload["name"],new_job)
    assert updated == 1
    
    # Validar banco após atualização
    user_updated= get_user_by_name(db_postgres,payload["name"])
    
    assert user_updated is not None
    assert user_updated[2] == new_job
#---------------------------------------------------------------------------------------------------------------------
    # Deletar usário do banco de dados.
    deleted = delete_user(db_postgres,payload["name"])
    
    assert deleted == 1
    
    user_after_delete = get_user_by_name(db_postgres,payload["name"])
    assert user_after_delete is None
    
    
    
    
    