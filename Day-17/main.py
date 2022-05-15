from question_model import QuestionModel
from quiz_brain import quiz
from data import question_data

Question_Bank = []


def question_bank():
    for i in range(0, len(question_data)-1):
        obj_question = QuestionModel(question_data[i]["text"], question_data[i]["answer"])
        Question_Bank.append(obj_question)

question_bank()
obj_quiz = quiz(Question_Bank)
obj_quiz.next_question()

