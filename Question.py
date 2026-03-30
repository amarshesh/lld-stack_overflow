

from ast import List


class Question:
    def __init__(self, id, title, description, user):
        self.id = id
        self.title = title
        self.description = description
        self.user = user
        self.answers = []
        self.votes = []
        self.comments = []

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def add_answer(self, answer):
        self.answers.append(answer)

    def add_vote(self, vote):
        self.votes.append(vote)

    def add_comment(self, comment):
        self.comments.append(comment)
    

  