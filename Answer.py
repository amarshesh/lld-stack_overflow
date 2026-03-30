class Answer:
    def __init__(self, id, description, user, question):
        self.id = id
        self.description = description
        self.user = user
        self.question = question
        self.comments = []
        self.votes = []

    def add_vote(self, vote):
        self.votes.append(vote)

    def add_comment(self, comment):
        self.comments.append(comment)
    

  