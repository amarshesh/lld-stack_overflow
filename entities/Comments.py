from datetime import datetime

class Comment:
    def __init__(self, id, description, user, target):
        self.id = id
        self.description = description
        self.created_by = user
        self.target = target
        self.created_at = datetime.now()

        target_id = getattr(target, 'id', None) or getattr(target, 'get_id', lambda: None)()
        print(f"Comment created: id={self.id} target={target.__class__.__name__}(id={target_id}) by {self.created_by.get_name()}")

    def get_id(self):
        return self.id
    
    def get_description(self):
        return self.description

    def get_user(self):
        return self.created_by  
    
    def get_target(self):
        return self.target