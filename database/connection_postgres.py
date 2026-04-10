# Camada de conexão com banco de dados utilizano postgres.
import psycopg2

# Função de inicialização
def get_connection_pg():
    return psycopg2.connect(host ="localhost",database="qa_db",user="qa_user",password="qa_pass",port=5432)

# Criar tabela do banco de dados

def create_table_pg(con):
    exec = con.cursor()
    
    exec.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                name TEXT,
                job TEXT
            )
                 
                 """)
    con.commit()