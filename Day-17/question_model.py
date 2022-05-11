class QuestionModel:
    def __init__(self, textSoal, answerSoal):
        self.text = textSoal
        self.answer = answerSoal
        
obj_question = QuestionModel("Hello","True")
print(obj_question.text)
print(obj_question.answer)
