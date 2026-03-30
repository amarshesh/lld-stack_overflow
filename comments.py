

class Comment:
    def __init__( self, id, description, user, target):
        self.id = id
        self.description = description
        self.user = user
        self.target = target
        self.votes = []
        self.replies = []


    def get_id(self):
        return self.id
    
    def get_description(self):
        return self.description
    
    def add_vote(self, vote):
        self.votes.append(vote)

    def add_reply(self, comment):
        self.replies.append(comment)

    
    

