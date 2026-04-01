from Post import Post
class Answer(Post):
    def __init__(self, id, title, description, user, question):
        super().__init__(id, title, description, user)
        self.question = question
        self.is_accepted = False

    def get_title(self):
        return self.title 

    def get_question(self):
        return self.question