
class User:
    def __init__( self, name, user_id):
        self.name = name
        self.reputation = 0
        self.id = user_id  
    
    def get_name(self):
        return self.name

    def get_reputation(self):
        return self.reputation
    
    def get_id(self):
        return self.id
    
    def increase_reputation(self):
        rep = self.get_reputation() 
        self.reputation = rep + 1
        return self.reputation

    
    