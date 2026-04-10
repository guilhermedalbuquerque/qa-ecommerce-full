# Módulo repository para fazer o acesso ao banco SQlite.
class UserRepositorySQLite:
    def __init__(self,connection):
        self.con= connection
        
    def create_user(self,name,job):
        exec = self.con.cursor()
        
        exec.execute("INSERT INTO users (name,job) VALUES (?,?)", (name,job))
        
        self.con.commit()
        
    def get_user_by_name(self,name):
        exec = self.con.cursor()
        
        exec.execute("SELECT * FROM users WHERE name = ?", (name,))
        
        return exec.fetchone()
    
    def update_user(self,name,new_job):
        exec = self.con.cursor()
        
        exec.execute("UPDATE users SET job = ? WHERE name= ?", (new_job,name))
        
        self.con.commit()
        return exec.rowcount
    
    def delete_user(self,name):
        exec = self.con.cursor()
        
        exec.execute("DELETE FROM users WHERE name = ?", (name,))
        
        self.con.commit()
        return exec.rowcount