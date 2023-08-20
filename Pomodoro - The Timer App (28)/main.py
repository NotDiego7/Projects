from tkinter import *
from math import floor
from playsound import playsound
# --------------------------------- Constants -------------------------------- #

BACKGROUND_COLOR = "#40435c"
BUTTON_COLOR = "#969590"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "√"
reps = 1
timer = None

# --------------------------------- Functions -------------------------------- #
def reset_timer():
    global reps
    canvas.after_cancel(timer)
    canvas.itemconfigure(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark_label.config(text="")
    reps = 1

def time_counter(seconds= WORK_MIN * 60):
    global reps, timer
    # ------------- Math to get seconds and minutes (and 0:00 format) ------------ #

    count_minutes = floor(seconds / 60)
    count_seconds = seconds % 60

    if count_seconds < 10 and count_seconds > 0:
        count_seconds = f"0{count_seconds}"
    if count_seconds == 0:
        count_seconds = "00"
    
    # ------------------------------- Rep mechanism ------------------------------ #
    
    if reps == 1:
        timer_label.config(text="Work Session", foreground="#8eedbe")
        playsound("Access-allowed-tone-2869.wav")
        reps += 1

    elif seconds == 0 and reps in [3, 5, 7]:
        seconds = WORK_MIN * 60
        timer_label.config(text="Work Session", foreground="#8eedbe")
        playsound("Access-allowed-tone-2869.wav")       
        reps += 1

    elif seconds == 0 and reps in [2, 4, 6]:
        seconds = SHORT_BREAK_MIN * 60
        timer_label.config(text="Short Break", foreground="#99ceff")
        playsound("Access-allowed-tone-2869.wav")
        
        # -------------------- Add Checkmark Post Work Session (1) ------------------- #

        check_mark_label.config(text= CHECKMARK * int(reps / 2))
        
        reps += 1

    elif seconds == 0 and reps == 8:
        seconds = LONG_BREAK_MIN * 60
        timer_label.config(text="Long Break", foreground="#c499ff")
        playsound("Access-allowed-tone-2869.wav")

        # -------------------- Add Checkmark Post Work Session (2) ------------------- #

        check_mark_label.config(text= CHECKMARK * int(reps / 2))

        reps += 1

    # ------------------------------ Timer mechanism ----------------------------- #

    if seconds > 0:
        timer = canvas.after(1000, time_counter, seconds - 1)

    # ----------------------------- Render on-screen ----------------------------- #

    canvas.itemconfigure(timer_text, text=f"{count_minutes}:{count_seconds}")

# ----------------------------- Main Window Setup ---------------------------- #

window = Tk()
window.wm_title("Pomodoro")
window.configure(padx=100, pady=50, background=BACKGROUND_COLOR)

# ---------------------------- Tomato Canvas Setup --------------------------- #

canvas = Canvas(width=200, height=224, background=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_image)
timer_text = canvas.create_text(100, 125, text="00:00", font=(FONT_NAME, 23), fill="white")
canvas.grid(column=1, row=1)

# ----------------------------- Label and Buttons ---------------------------- #

timer_label = Label(text="Timer", font=(FONT_NAME, 30), background=BACKGROUND_COLOR, foreground="white")
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", background=BUTTON_COLOR, foreground="white", command=time_counter)
start_button.config(width=10)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", background=BUTTON_COLOR, foreground="white", command=reset_timer)
reset_button.config(width=10)
reset_button.grid(column=2, row=2)

# -------------------------------- CheckMarks -------------------------------- #

check_mark_label = Label(text= "", font=(FONT_NAME, 15), background=BACKGROUND_COLOR, foreground="light green")
check_mark_label.grid(column=1, row=3)












window.mainloop()