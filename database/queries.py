# Regras de acesso ao banco de dados.
# "?" usado para boas prática, evitando sql injection.
# Função para inserir usuário
def insert_user(con,name,job):
    
    exec = con.cursor()
    
    exec.execute("INSERT INTO users (name,job) VALUES (?, ?)", (name, job))
    
    con.commit()
    
    
# Função para fazer requisição de usuário pelo nome
def get_user_by_name(con,name):
    exec = con.cursor()
    
    # "," no parâmetro para não passar em formato de tupla.
    exec.execute("SELECT * FROM users  WHERE name  = ?", (name,))
    
    # retorna valor padronizado : "(id,name,job)".
    user = exec.fetchone()
    
    
    return user

# Função para atualizar registro do usuário.
def update_user(con,name, new_job):
    exec = con.cursor()
    
    exec.execute("UPDATE users SET job = ? WHERE name =?", (new_job, name))
    con.commit()
    updated_rows = exec.rowcount
    
    return updated_rows
    
def delete_user(con,name):
    exec = con.cursor()
    
    exec.execute("DELETE FROM users WHERE name = ?", (name,))
    con.commit()
    deleted_rows = exec.rowcount
    return deleted_rows