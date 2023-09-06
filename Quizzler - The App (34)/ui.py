from tkinter import *

# --------------------------------- Constants -------------------------------- #
THEME_COLOR = "#375362"

class QuizUI():
    def __init__(self):
        # ----------------------------------- Setup ---------------------------------- #

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)

        # -------------------------------- Load Images ------------------------------- #

        self.false_img = PhotoImage(file="images/false.png")
        self.true_img = PhotoImage(file="images/true.png")

        # ---------------------- Create Canvas and Inject Images --------------------- #

        self.canvas = Canvas(width= 300, height= 250, background= "gray", highlightthickness= 0)
        self.false_button_image = self.canvas.create_image(100, 97, image= self.false_img)
        self.true_button_image = self.canvas.create_image(300, 97, image= self.true_img)
        self.displayed_query = self.canvas.create_text(250, 300, text="", font=("Times New Roman", 20, "italic"))

        self.canvas.grid(column= 0, row= 0, columnspan= 2)
        
        # ---------------------------------- Buttons --------------------------------- #

        self.true_button = Button(width=100, height=100, background=THEME_COLOR, highlightthickness=0, command=self.true_button_functionality, image=self.true_button_image, border=0)
        self.true_button.grid(column=0, row=1)

        self.false_button = Button(width=100, height=100, background=THEME_COLOR, highlightthickness=0, command=self.false_button_functionality, image=self.false_button_image, border=0)
        self.false_button.grid(column=1, row=1)



        self.window.mainloop()

    

    def true_button_functionality(self):
        pass


    def false_button_functionality(self):
        pass