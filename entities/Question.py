from Post import Post

class Question(Post):
    
    def __init__(self, id, title, description, user):
        super().__init__(id, title, description, user)
        self.answers = []
        self.tags = []
        self.accepted_answer = None 

    def get_title(self):
        return self.title

    def add_answer(self, answer):
        self.answers.append(answer)

    def get_answers(self):
        return self.answers

    def add_tag(self, tag):
        self.tags.append(tag)

    def get_tags(self):
        return self.tags

    def accept_answer(self, answer):
        self.accepted_answer = answer
        answer.is_accepted = True