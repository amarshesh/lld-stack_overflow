
from abc import ABC, abstractmethod

class Votable(ABC):
    @abstractmethod
    def add_vote(self, vote):
        pass
    
    @abstractmethod
    def get_votes(self):
        pass