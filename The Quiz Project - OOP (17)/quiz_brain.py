class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}\n(True or False?): ").capitalize()
        self.check_answer(user_answer, current_question)


    def check_answer(self, user_answer, current_question):
        if user_answer == current_question.answer:
            self.user_score += 1
            print(f"You're right!\nThe correct answer was: {current_question.answer}.\nCurrent score: {self.user_score}/{self.question_number}")
        else:
            print(f"Wrong!\nThe correct answer was: {current_question.answer}\n Current score: {self.user_score}/{self.question_number}")