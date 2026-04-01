from enum import Enum

class VoteType(Enum):
    UPVOTE = 1
    DOWNVOTE = -1

class Vote:
    def __init__(self, id, user, vote_type: VoteType, target: Votable): 
        self.id = id
        self.created_by = user
        self.vote_type = vote_type
        self.target = target  # Votable type hoga — baad mein samjhega

    def get_id(self):
        return self.id
    
    def get_target(self):
        return self.target
    
    def get_user(self):
        return self.created_by
    
    def get_vote_type(self):
        return self.vote_type