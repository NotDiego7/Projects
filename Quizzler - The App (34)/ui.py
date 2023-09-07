from tkinter import *

# --------------------------------- Constants -------------------------------- #
THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self, quiz):
        # ----------------------------------- Setup ---------------------------------- #

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, pady=25)

        self.quiz = quiz

        # -------------------------------- Load Images ------------------------------- #

        self.false_img = PhotoImage(file="images/false.png")
        self.true_img = PhotoImage(file="images/true.png")

        # ---------------------- Create Canvas and Inject Images --------------------- #

        self.canvas = Canvas(width= 450, height= 300, background= "white", highlightthickness= 0)
        self.displayed_query = self.canvas.create_text(225, 150, text="", font=("Bodoni MT", 19), width= 400)

        self.canvas.grid(column= 0, row= 1, columnspan= 2, padx= 25, pady= 35)
        
        # ----------------------------------- Score ---------------------------------- #

        self.score_label = Label(text= f"Score: {self.quiz.score}", background= THEME_COLOR, foreground= "white", font= ("Times New Roman", 17, "bold"))
        self.score_label.grid(column=1, row=0)

        # ---------------------------------- Buttons --------------------------------- #

        self.true_button = Button(width=100, height=100, background=THEME_COLOR, highlightthickness=0, command= self.true_button_functionality, image= self.true_img, border=0)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(width=100, height=100, background=THEME_COLOR, highlightthickness=0, command= self.false_button_functionality, image= self.false_img, border=0)
        self.false_button.grid(column=1, row=2)

        # ----------------------------- Get Initial Query ---------------------------- #

        self.get_query()


        self.window.mainloop()
 
    
    def get_query(self):
        self.canvas.config(background= "white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfigure(self.displayed_query, text= self.quiz.next_question())
        else:
            self.canvas.itemconfigure(self.displayed_query, text= f"You've exhausted your 10 questions.\nFeel free to open another session!\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state= "disabled")
            self.false_button.config(state= "disabled")


    def true_button_functionality(self):
        self.quiz.check_answer(user_answer= "True", canvas= self.canvas, score_label= self.score_label)
        self.canvas.after(ms= 1300, func= self.get_query)


    def false_button_functionality(self):
        self.quiz.check_answer(user_answer= "False", canvas= self.canvas, score_label= self.score_label)
        self.canvas.after(ms= 1300, func= self.get_query)