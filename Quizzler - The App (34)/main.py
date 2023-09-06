from ui import QuizUI
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from html import unescape

question_bank = []
for question in question_data:
    question_text = unescape(question["question"])
    question_answer = unescape(question["correct_answer"])
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

front_end = QuizUI()

quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
