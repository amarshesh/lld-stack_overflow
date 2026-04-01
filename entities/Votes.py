from enum import Enum

from interfaces.Votable import Votable

class VoteType(Enum):
    UPVOTE = 1
    DOWNVOTE = -1

class Vote:
    def __init__(self, id, user, target, vote_type: VoteType):
        self.id = id
        self.created_by = user
        self.target = target  # Votable type hoga — baad mein samjhega
        self.vote_type = vote_type
        target_id = getattr(target, 'id', None) or getattr(target, 'get_id', lambda: None)()
        print(f"Vote created: id={self.id} type={self.vote_type} target={target.__class__.__name__}(id={target_id}) by {self.created_by.get_name()}")

    def get_id(self):
        return self.id
    
    def get_target(self):
        return self.target
    
    def get_user(self):
        return self.created_by
    
    def get_vote_type(self):
        return self.vote_type