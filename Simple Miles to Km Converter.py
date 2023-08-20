from tkinter import *
# ------------------------------ Create objects ------------------------------ #

window = Tk()

# ---------------------------- Display Properties ---------------------------- #

window.config(padx=55, pady=65)
window.wm_title("Miles to Kilometers Converter")
window.wm_minsize(250, 250)

# --------------------------------- Functions -------------------------------- #

def get_conversion():
    miles = float(text_entry.get())
    km = round(miles * 1.60934, ndigits=2)
    conversion_result.config(text=km)

# ---------------------------------------------------------------------------- #
#                                    Widgets                                   #
# ---------------------------------------------------------------------------- #

# ------------------------------------- 0 ------------------------------------ #

is_equal_to = Label(text="is equal to:", font=("Times New Roman", 15))
# is_equal_to.config(padx=2, pady=2)
is_equal_to.grid(column=0, row=1)

# ------------------------------------- 1 ------------------------------------ #

text_entry = Entry(font=("Times New Roman", 14), width=10)
text_entry.grid(column=1, row=0)

# ------------------------------------- 2 ------------------------------------ #

conversion_result = Label(font=("Times New Roman", 14)) #TODO need to add text argument from get_conversion function
# conversion_result.config(padx=2, pady=2)
conversion_result.grid(column=1, row=1)

# ------------------------------------- 3 ------------------------------------ #

button = Button(foreground="purple", text="Calculate", font=("Times New Roman", 14), command=get_conversion, )
# button.config(padx=2, pady=2)
button.grid(column=1, row=2)

# ------------------------------------- 4 ------------------------------------ #

miles_label = Label(text="Miles", font=("Times New Roman", 14))
# miles_label.config(padx=2, pady=2)
miles_label.grid(column=2, row=0)

# ------------------------------------- 5 ------------------------------------ #

km_label = Label(text="Km", font=("Times New Roman", 14))
# km_label.config(padx=2, pady=2)
km_label.grid(column=2, row=1)









window.mainloop()