from abc import ABC, abstractmethod
from interfaces.Commentable import Commentable
from interfaces.Votable import Votable

class Post(Commentable, Votable, ABC):
    def __init__(self, id, title, description, user):
        self.id = id
        self.title = title
        self.description = description
        self.created_by = user
        self.comments = []
        self.votes = []
        print(f"Post created: {self.__class__.__name__} id={self.id} title={self.title}")

    def add_comment(self, comment):
        self.comments.append(comment)
    
    def get_comments(self):
        return self.comments

    def add_vote(self, vote):
        self.votes.append(vote)
    
    def get_votes(self):
        return self.votes
    
    def get_id(self):
        return self.id
    
    @abstractmethod
    def get_title(self):
        pass

