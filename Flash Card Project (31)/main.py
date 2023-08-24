from tkinter import *
from random import randint
import csv, linecache
# --------------------------------- Constants -------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
# ----------------------------------- Setup ---------------------------------- #
window = Tk()
window.title("Flashy Cards")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)
# -------------------------------- Load Images ------------------------------- #
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
wrong = PhotoImage(file="images/wrong.png")
right = PhotoImage(file="images/right.png")
# ---------------------- Create Canvas and Inject Images --------------------- #
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="French", font=("Times New Roman", 40, "italic"))
canvas.create_text(400, 263, text="trouve", font=("Times New Roman", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#TODO: Pending card_back inject

right_button_canvas = Canvas(width=100, height=100, background=BACKGROUND_COLOR, highlightthickness=0)
right_button_canvas.create_image(50, 50, image=right)
right_button_canvas.grid(column=0, row=1)

wrong_button_canvas = Canvas(width=100, height=100, background=BACKGROUND_COLOR, highlightthickness=0)
wrong_button_canvas.create_image(50, 50, image=wrong)
wrong_button_canvas.grid(column=1, row=1)

#TODO: Read CSV data
with open(file="data/french_words.csv", mode= "r") as data:
    data = csv.reader(data)
    x = linecache.getline(filename= data, lineno= 1)
    print(x)

#NOTE: System Requirements: 11:54







window.mainloop()