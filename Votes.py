from enum import Enum

class VoteType(Enum):
    UPVOTE = 1
    DOWNVOTE = -1


# 1 vote bas 1 hi jgah diya jaa sakta hai brooooo
class Vote:
    def __init__(self, target, user, vote_type, id ):
        self.id = id
        self.target = target
        self.user = user
        self.vote_type = vote_type

    def get_id(self):
        return self.id
    
    def get_target(self):
        return self.target
    
    def get_user(self):
        return self.user
    
    def get_vote_type(self):
        return self.vote_type
    
    

