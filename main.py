from stack_overflow import StackOverflow
from entities.Votes import VoteType
from entities.tags import Tag

so = StackOverflow()

# Users banao
alice = so.create_user("Alice", "u1")
bob = so.create_user("Bob", "u2")
print("Users bane:", alice.get_name(), bob.get_name())

# Question banao
q1 = so.create_question_post("Python kya hai?", "Python ek language hai", alice)
print("Question bana:", q1.get_title())

# Tag lagao
python_tag = Tag("t1", "python")
q1.add_tag(python_tag)
print("Tag laga:", q1.tags[0].get_name())

# Answer do
a1 = so.create_answer_of_question("Python easy hai", "Bahut acchi language", bob, q1.get_id())
print("Answer bana:", a1.get_title())

# Comment karo
so.create_comment("Accha sawaal hai", bob, q1)
print("Comments:", len(q1.get_comments()))

# Vote karo
so.vote(bob, q1, VoteType.UPVOTE)
print("Alice reputation after upvote:", alice.get_reputation())

# Search karo
results = so.search_question_by_tag("python")
print("Tag se mila:", results[0].get_title())

# User ke questions
user_qs = so.get_questions_by_user("u1")
print("Alice ke questions:", len(user_qs))

# Top questions
top = so.get_top_k_questions(1)
print("Top question:", top[0].get_title())