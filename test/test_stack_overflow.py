from stack_overflow import StackOverflow
from entities.User import User
from entities.Votes import VoteType


def setup():
    so = StackOverflow()
    u1 = User("Alice", 1)
    u2 = User("Bob", 2)
    u3 = User("Charlie", 3)
    so.users.extend([u1, u2, u3])
    return so, u1, u2, u3


# ---- Post Question ----
def test_post_question():
    so, u1, u2, u3 = setup()
    q = so.post_question("What is Python?", "Explain in simple terms", u1)
    assert q.title == "What is Python?"
    assert q.description == "Explain in simple terms"
    assert q.user == u1
    assert q.id == 1
    assert q in so.questions
    print("PASS: test_post_question")


def test_post_multiple_questions():
    so, u1, u2, u3 = setup()
    q1 = so.post_question("Q1", "Desc1", u1)
    q2 = so.post_question("Q2", "Desc2", u2)
    q3 = so.post_question("Q3", "Desc3", u1)
    assert len(so.questions) == 3
    assert q1.id == 1 and q2.id == 2 and q3.id == 3
    print("PASS: test_post_multiple_questions")


# ---- Post Answer ----
def test_post_answer():
    so, u1, u2, u3 = setup()
    q = so.post_question("Q?", "Desc", u1)
    a = so.post_answer("My answer", u2, q)
    assert a.description == "My answer"
    assert a.user == u2
    assert a.question == q
    assert a in q.answers
    assert a in so.answers
    print("PASS: test_post_answer")


def test_multiple_answers_on_question():
    so, u1, u2, u3 = setup()
    q = so.post_question("Q?", "Desc", u1)
    a1 = so.post_answer("Ans1", u2, q)
    a2 = so.post_answer("Ans2", u3, q)
    assert len(q.answers) == 2
    assert a1 in q.answers and a2 in q.answers
    print("PASS: test_multiple_answers_on_question")


# ---- Post Comment ----
def test_comment_on_question():
    so, u1, u2, u3 = setup()
    q = so.post_question("Q?", "Desc", u1)
    c = so.post_comment("Nice question!", u2, q)
    assert c.description == "Nice question!"
    assert c.user == u2
    assert c in q.comments
    print("PASS: test_comment_on_question")


def test_comment_on_answer():
    so, u1, u2, u3 = setup()
    q = so.post_question("Q?", "Desc", u1)
    a = so.post_answer("Ans", u2, q)
    c = so.post_comment("Great answer!", u3, a)
    assert c in a.comments
    assert c.user == u3
    print("PASS: test_comment_on_answer")


# ---- Votes ----
def test_upvote():
    so, u1, u2, u3 = setup()
    q = so.post_question("Q?", "Desc", u1)
    a = so.post_answer("Ans", u2, q)
    so.upvote(u1, a)
    assert len(a.votes) == 1
    assert a.votes[0].vote_type == VoteType.UPVOTE
    assert a.votes[0].user == u1
    print("PASS: test_upvote")


def test_downvote():
    so, u1, u2, u3 = setup()
    q = so.post_question("Q?", "Desc", u1)
    a = so.post_answer("Ans", u2, q)
    so.downvote(u3, a)
    assert len(a.votes) == 1
    assert a.votes[0].vote_type == VoteType.DOWNVOTE
    print("PASS: test_downvote")


def test_vote_on_question():
    so, u1, u2, u3 = setup()
    q = so.post_question("Q?", "Desc", u1)
    so.upvote(u2, q)
    so.upvote(u3, q)
    assert len(q.votes) == 2
    print("PASS: test_vote_on_question")


# ---- Highest Voted Answer ----
def test_highest_voted_answer():
    so, u1, u2, u3 = setup()
    q = so.post_question("Q?", "Desc", u1)
    a1 = so.post_answer("Ans1", u2, q)
    a2 = so.post_answer("Ans2", u3, q)
    so.upvote(u1, a2)
    so.upvote(u2, a2)
    so.upvote(u1, a1)
    top = so.get_highest_voted_answer()
    assert top == a2, f"Expected a2 (2 votes), got {top.description}"
    print("PASS: test_highest_voted_answer")


def test_highest_voted_with_downvotes():
    so, u1, u2, u3 = setup()
    q = so.post_question("Q?", "Desc", u1)
    a1 = so.post_answer("Ans1", u2, q)
    a2 = so.post_answer("Ans2", u3, q)
    so.upvote(u1, a1)
    so.upvote(u2, a1)     # a1: +2
    so.upvote(u1, a2)
    so.downvote(u2, a2)   # a2: +1 -1 = 0
    top = so.get_highest_voted_answer()
    assert top == a1
    print("PASS: test_highest_voted_with_downvotes")


def test_highest_voted_no_answers():
    so, u1, u2, u3 = setup()
    assert so.get_highest_voted_answer() is None
    print("PASS: test_highest_voted_no_answers")


# ---- Lookup by User ----
def test_get_questions_by_user():
    so, u1, u2, u3 = setup()
    so.post_question("Q1", "D1", u1)
    so.post_question("Q2", "D2", u2)
    so.post_question("Q3", "D3", u1)
    alice_qs = so.get_question_by_user(u1)
    assert len(alice_qs) == 2
    assert all(q.user == u1 for q in alice_qs)
    print("PASS: test_get_questions_by_user")


def test_get_questions_by_user_empty():
    so, u1, u2, u3 = setup()
    assert so.get_question_by_user(u3) == []
    print("PASS: test_get_questions_by_user_empty")


def test_get_answers_by_user():
    so, u1, u2, u3 = setup()
    q = so.post_question("Q?", "Desc", u1)
    so.post_answer("A1", u2, q)
    so.post_answer("A2", u2, q)
    so.post_answer("A3", u3, q)
    bob_ans = so.get_answer_by_user(u2)
    assert len(bob_ans) == 2
    assert all(a.user == u2 for a in bob_ans)
    print("PASS: test_get_answers_by_user")


# ---- Lookup by Description ----
def test_get_answers_by_question_description():
    so, u1, u2, u3 = setup()
    q = so.post_question("Q?", "Explain Python", u1)
    a1 = so.post_answer("A1", u2, q)
    a2 = so.post_answer("A2", u3, q)
    results = so.get_answer_by_question_description("Explain Python")
    assert len(results) == 2
    assert a1 in results and a2 in results
    print("PASS: test_get_answers_by_question_description")


def test_get_answers_by_description_not_found():
    so, u1, u2, u3 = setup()
    assert so.get_answer_by_question_description("nonexistent") == []
    print("PASS: test_get_answers_by_description_not_found")


# ---- Tags ----
def test_add_tag_to_question():
    so, u1, u2, u3 = setup()
    q = so.post_question("Q?", "Desc", u1)
    q.add_tag("python")
    q.add_tag("oop")
    assert "python" in q.tags
    assert "oop" in q.tags
    assert len(q.tags) == 2
    print("PASS: test_add_tag_to_question")


# ---- Comment Replies ----
def test_reply_to_comment():
    so, u1, u2, u3 = setup()
    q = so.post_question("Q?", "Desc", u1)
    c1 = so.post_comment("First comment", u2, q)
    from comments import Comment
    reply = Comment(99, "This is a reply", u3, c1)
    c1.add_reply(reply)
    assert len(c1.replies) == 1
    assert c1.replies[0].description == "This is a reply"
    print("PASS: test_reply_to_comment")


# ---- Run All ----
if __name__ == "__main__":
    test_post_question()
    test_post_multiple_questions()
    test_post_answer()
    test_multiple_answers_on_question()
    test_comment_on_question()
    test_comment_on_answer()
    test_upvote()
    test_downvote()
    test_vote_on_question()
    test_highest_voted_answer()
    test_highest_voted_with_downvotes()
    test_highest_voted_no_answers()
    test_get_questions_by_user()
    test_get_questions_by_user_empty()
    test_get_answers_by_user()
    test_get_answers_by_question_description()
    test_get_answers_by_description_not_found()
    test_add_tag_to_question()
    test_reply_to_comment()
    print("\n--- ALL TESTS PASSED ---")
