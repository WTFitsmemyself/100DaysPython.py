from data import question_data
max_question = len(question_data)
class quiz:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        
    def next_question(self):
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            ans = input(f"Q.{self.question_number}: {current_question.text}")
             
