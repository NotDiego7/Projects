from tkinter import *
from random import randint
import linecache, shutil
import pandas as pd
# --------------------------------- Constants -------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------------- Functions -------------------------------- #

def get_random_word():
    global french_word
    def flip_card():
        english_word = row.strip().split(sep=",")[1]

        canvas.itemconfig(card_image, image=card_back)
        canvas.itemconfig(language_title, text="English", fill="white")
        canvas.itemconfig(displayed_word, text=english_word, fill="white")
        canvas.after_cancel(timed_func)

    # ---------------------------------------------------------------------------- #

    try:
        with open(file="data/french_words_to_be_learned.csv", mode= "r") as file:
            rows_count = sum(1 for _ in file) - 1
    
    
    except FileNotFoundError:
        original_file = "data/french_words.csv"
        destination_file = "data/french_words_to_be_learned.csv"
        shutil.copy(src=original_file, dst=destination_file)

        # ---------------------------------------------------------------------------- #
        
        with open(file="data/french_words_to_be_learned.csv", mode= "r") as file:
            rows_count = sum(1 for _ in file) - 1

        num_of_row = randint(2, rows_count)
        row = (linecache.getline(filename= "data/french_words_to_be_learned.csv", lineno= num_of_row))
        french_word = row.strip().split(sep=",")[0]

        canvas.itemconfig(card_image, image=card_front)
        canvas.itemconfig(language_title, text="French", fill="black")
        canvas.itemconfig(displayed_word, text=french_word, fill="black")

        timed_func = canvas.after(ms=3200, func=flip_card)
        
        return french_word


    else:
        num_of_row = randint(2, rows_count)
        row = (linecache.getline(filename= "data/french_words_to_be_learned.csv", lineno= num_of_row))
        french_word = row.strip().split(sep=",")[0]

        canvas.itemconfig(card_image, image=card_front)
        canvas.itemconfig(language_title, text="French", fill="black")
        canvas.itemconfig(displayed_word, text=french_word, fill="black")

        timed_func = canvas.after(ms=3200, func=flip_card)
        
        return french_word


def get_random_word_green(): #NOTE: Green button logic/Get rid of known word
    content_to_drop = french_word
    dataframe = pd.read_csv(filepath_or_buffer="data/french_words_to_be_learned.csv")
    filtered_dataframe = dataframe[dataframe["French"] != content_to_drop]
    filtered_dataframe.to_csv(path_or_buf="data/french_words_to_be_learned.csv", index=False)
    get_random_word()


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
card_image = canvas.create_image(400, 263, image=card_front)
language_title = canvas.create_text(400, 150, text="", font=("Times New Roman", 40, "italic"))
displayed_word = canvas.create_text(400, 263, text="", font=("Times New Roman", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_button = Button(width=100, height=100, background=BACKGROUND_COLOR, highlightthickness=0, command=get_random_word_green, image=image_right, border=0)
right_button.grid(column=0, row=1)

wrong_button = Button(width=100, height=100, background=BACKGROUND_COLOR, highlightthickness=0, command=get_random_word, image=image_wrong, border=0)
wrong_button.grid(column=1, row=1)

# ---------------------------------------------------------------------------- #

get_random_word() #NOTE: Fetches a random FR word to start with & flips (EN side) after a given time






window.mainloop()