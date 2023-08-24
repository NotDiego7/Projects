from tkinter import *
from random import randint
import csv, linecache
# --------------------------------- Constants -------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------------- Functions -------------------------------- #

def get_random_row():
    #TODO: Pick random french word for both buttons when pressed
    with open(file= "data/french_words.csv", mode= "r") as file:
        rows_count = sum(1 for _ in file) - 1
    
    num_of_random_row = randint(2, rows_count)
    random_row = (linecache.getline(filename= "data/french_words.csv", lineno= num_of_random_row))
    random_french_word = random_row.strip().split(sep=",")[0]

    canvas.itemconfig(tagOrId= french_displayed_word, text=random_french_word)
    
# ----------------------------------- Setup ---------------------------------- #

window = Tk()
window.title("Flashy Cards")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

# -------------------------------- Load Images ------------------------------- #

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
image_wrong = PhotoImage(file="images/wrong.png")
image_right = PhotoImage(file="images/right.png")

# ---------------------- Create Canvas and Inject Images --------------------- #

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="French", font=("Times New Roman", 40, "italic"))
french_displayed_word = canvas.create_text(400, 263, text="trouve", font=("Times New Roman", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#TODO: Pending card_back inject

right_button = Button(width=100, height=100, background=BACKGROUND_COLOR, highlightthickness=0, command=get_random_row, image=image_right, border=0)
right_button.grid(column=0, row=1)

wrong_button = Button(width=100, height=100, background=BACKGROUND_COLOR, highlightthickness=0, command=get_random_row, image=image_wrong, border=0)
wrong_button.grid(column=1, row=1)


#NOTE: System Requirements: 11:54







window.mainloop()