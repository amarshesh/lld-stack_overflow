from Answer import Answer
from Question import Question
from User import User
from comments import Comment

class StackOverflow:
    def __init__(self):
        self.users = []
        self.questions = []
        self.answers = []

    def post_question( self,  title, description, user):
        question_id =  len(self.questions) + 1
        question = Question(question_id, title, description, user)
        self.questions.append(question)
        return question
    
    def post_answer( self, description, user, question):
        answer_id = len(self.answers) + 1
        answer = Answer(answer_id, description, user, question)
        self.answers.append(answer)
        question.add_answer(answer)
        return answer
    
    def post_comment( self, description, user, target):
        comment_id = len(target.comments) + 1
        comment = Comment(comment_id, description, user, target)
        target.add_comment(comment)
        return comment

#examples 

stackoverflow = StackOverflow()
user1 = User("user1", 1)
stackoverflow.users.append(user1)
user2 = User("user2", 2)
stackoverflow.users.append(user2)
question1 = stackoverflow.post_question("What is Python?", "I want to know about Python programming language.", user1)
answer1 = stackoverflow.post_answer("Python is a high-level programming language.", user2, question1)

comment1 = stackoverflow.post_comment("Thanks for the answer!", user1, answer1)
print("Question:", question1.title)
for ans in question1.answers:
    print("Answer:", ans.description)
    print("Answered by:", ans.user.get_name())
    for com in ans.comments:
        print("Comment:", com.description)
        print("Commented by:", com.user.get_name())
