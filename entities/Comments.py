from datetime import datetime

class Comment:
    def __init__(self, id, description, user, target):
        self.id = id
        self.description = description
        self.created_by = user
        self.target = target
        self.created_at = datetime.now()

    def get_id(self):
        return self.id
    
    def get_description(self):
        return self.description

    def get_user(self):
        return self.created_by  
    
    def get_target(self):
        return self.target