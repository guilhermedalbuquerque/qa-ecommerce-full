# teste de banco interno para testar persistência
# Importar classes service e repository para criação e manipulação da tabela de dados.
# importar função para geração de dados.

from repository.user_repository_sqlite import UserRepositorySQLite
from services.user_service import UserService

from utils.data_generator import  create_user_payload

# Função para validar criação, atualização e exclusão do usuário no banco.
def test_user_validate_db(db):
    repo = UserRepositorySQLite(db)
    service = UserService(repo)
    payload = create_user_payload()
   
    
    # Inserir no banco de dados.
    service.create_user(payload["name"],payload["job"])
    
    # Validar no banco de dados
    user_db = service.get_user(payload["name"])
    
    assert user_db is not None
    assert payload["name"] == user_db[1]
    assert payload["job"] == user_db[2]
    #---------------------------------------------------------------------------------------------------------------
    new_job= "QA Engineer"
    updated = service.update_job(payload["name"],new_job)
    
    assert updated == 1
    
    # Validar banco após atualização
    user_new_job = service.get_user(payload["name"])
    
    assert user_new_job is not None
    assert user_new_job[2] == new_job
    
    #---------------------------------------------------------------------------------------------------------------
    # Deletar usário do banco de dados.
    deleted = service.delete_user(payload["name"])
    assert deleted == 1
    
    # Validar banco após exclusão.
    user_after_delete = service.get_user(payload["name"])
    assert user_after_delete is None
    
    
    
    
    
    