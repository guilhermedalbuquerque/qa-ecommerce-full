# Camada de conexão do banco de dados.
# Função para inicialização.
def create_table(con):
    
    # Variavél para executar comandos sql.
    exec = con.cursor()
    
    exec.execute("""
                 CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 job TEXT
                 )
                 """)
    con.commit()
    
    
    