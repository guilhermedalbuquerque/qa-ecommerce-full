# Importar faker para gerar dados aleatorios.
from faker import Faker

# fake utilizado para não gerar valores fixos, simulando ambiente real.
fake = Faker("pt_BR")

# Cria um payload dinâmico para criação do usuário.
def create_user_payload():
    return {
        "name" : fake.name(),
        "job" : fake.job()
    }