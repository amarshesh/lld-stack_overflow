from entities.Answer import Answer
from entities.Question import Question
from entities.User import User
from entities.Votes import Vote, VoteType
from comments import Comment

class StackOverflow:
    def __init__(self):
        self.users = []
        self.questions = []
        self.answers = []
        self.user_questions = {}   # 
        self.user_answer = {}      # user_id -> list of answers
        self.question_description = {}  # question description -> answers
        

    def post_question( self,  title, description, user):
        question_id =  len(self.questions) + 1
        question = Question(question_id, title, description, user)
        if user not in self.user_questions:
            self.user_questions[user] = []
        self.user_questions[user].append(question)
        self.questions.append(question)
        return question
    
    def post_answer( self, description, user, question):
        answer_id = len(self.answers) + 1
        answer = Answer(answer_id, description, user, question)
        self.answers.append(answer)

        if question.description not in self.question_description:
            self.question_description[question.description] = []
        self.question_description[question.description].append(answer)
        question.add_answer(answer)

        if user not in self.user_answer:
            self.user_answer[user] = []
        self.user_answer[user].append(answer)
        return answer
    
    def post_comment( self, description, user, target):
        comment_id = len(target.comments) + 1
        comment = Comment(comment_id, description, user, target)
        target.add_comment(comment)
        return comment

    def get_highest_voted_answer(self):
         if not self.answers:
             return None
         self.answers.sort(
             key=lambda x: sum(1 if v.vote_type == VoteType.UPVOTE else -1 for v in x.votes),
             reverse=True
         )
         return self.answers[0]

    def upvote(self, user, target):
        vote_id = len(target.votes) + 1
        vote = Vote(target, user, VoteType.UPVOTE, vote_id)
        target.add_vote(vote)
    
    def downvote( self, user, target):
        vote_id = len(target.votes) + 1
        vote = Vote(target, user, VoteType.DOWNVOTE, vote_id)
        target.add_vote(vote)
    
    def get_question_by_user(self, user):
        return self.user_questions.get(user, [])
    
    def get_answer_by_user(self, user):
        return self.user_answer.get(user, [])
    
    def get_answer_by_question_description(self, description):
        return self.question_description.get(description, [])
    