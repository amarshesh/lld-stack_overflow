import uuid
from entities.Answer import Answer
from entities.Question import Question
from entities.User import User
from entities.Votes import Vote, VoteType
from entities.Comments import Comment

class StackOverflow:

    def __init__(self):
        self.users = {}
        self.questions = {}
        self.user_questions = {}
        self.answers = {}
    def create_user(self, name, userId):
        user = User(name, userId)
        self.users[userId] = user
        self.user_questions[userId] = []    
        return user

    def create_question_post(self, title, description, user):
        question_id = str(uuid.uuid4())  # id yahan generate karo
        question = Question(question_id, title, description, user)
        self.questions[question_id] = question  # questions dict
        self.user_questions[user.get_id()].append(question)
        return question
    
    def create_answer_of_question(self, title, description, user, question_id):
        question = self.questions.get(question_id)
        if question is None:
            raise Exception("Question not found")
        answer_id = str(uuid.uuid4())  # () missing tha
        answer = Answer(answer_id, title, description, user, question)
        self.answers[answer_id] = answer 
        question.add_answer(answer)
        return answer
    
    def search_question_by_tag(self, tag_name):
        question_list = []
        for ques in self.questions.values():
            for tg in ques.tags:
                if tag_name == tg.get_name():
                    question_list.append(ques)
        return question_list
            

    def create_comment( self, description, user, target):
        comment_id = str( uuid.uuid4())
        comments = Comment( comment_id, description, user, target)
        target.add_comment(comments)
        return comments
    

    def vote(self, user, target, vote_type):
        # if already voted to same post 
        for v in target.get_votes():
            if v.get_user().get_id() == user.get_id():
                raise Exception("User has already voted to this post")
            
        if vote_type not in [VoteType.UPVOTE, VoteType.DOWNVOTE]:
            raise Exception("Invalid vote type")
        
        vote_id = str(uuid.uuid4())
        vote = Vote(vote_id, user, target, vote_type)
        target.add_vote(vote)
        target.created_by.update_reputation(10 if vote_type == VoteType.UPVOTE else -5)

    def get_top_k_questions(self, k):
        sorted_questions = sorted(self.questions.values(), key=lambda q: len(q.get_votes()), reverse=True)
        return sorted_questions[:k]
    def get_questions_by_user(self, user_id):
        return self.user_questions.get(user_id, [])
