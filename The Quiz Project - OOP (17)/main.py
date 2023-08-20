from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def main_flow():
    # ----------------- Get object from question_data dictionary ----------------- #

    question_bank = []
    for i in range(len(question_data)):
        question = Question(question_data[i]["question"], question_data[i]["correct_answer"])
        question_bank.append(question)

    # ----------------- Create objects from classes & return vars ---------------- #

    quiz_brain = QuizBrain(question_bank)

    # ----- Check if we still have questions in question_list & check answers ---- #
    
    while quiz_brain.still_has_questions():
        quiz_brain.next_question()
    else:
        print(f"You've completed the quiz.\nYour final score: {quiz_brain.user_score}/{quiz_brain.question_number}")



main_flow()