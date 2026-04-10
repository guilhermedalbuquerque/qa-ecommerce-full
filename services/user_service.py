# Módulo para acessar repository.
class UserService:
    def __init__(self,repository):
        self.repository = repository
    
    def create_user(self,name,job):
        return self.repository.create_user(name,job)
        
    def get_user(self,name):
        return self.repository.get_user_by_name(name)
    
    def update_job(self,name,new_job):
        return self.repository.update_user(name,new_job)
    
    def delete_user(self,name):
        return self.repository.delete_user(name)