from tkinter import *
from tkinter import messagebox
from password_generator import get_random_password
import json, pprint

# --------------------------------- Constants -------------------------------- #
FONT = ("Times New Roman", 12, )
ENTRY_DEFAULT_COLOR = "#9a9c9b"
ENTRY_DAFAULT_FOREGROUND_COLOR = "#ebedec"
# --------------------------------- Functions -------------------------------- #
def save_data():
    website_data = website_entry.get().title()
    email_data = email_entry.get()
    password_data = password_entry.get()

    new_data_dict = {
        website_data: {
            "email": email_data,
            "password": password_data,
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(title= "Empty fields", message= "Please fill in empty fields.")
    else:
        if messagebox.askyesno(title= "Confirmation", message= "Are you sure you want to save?"):
            try:
                with open(file= "Password Manager Data.json", mode= "r") as file:
                    loaded_data = json.load(fp= file)
                    loaded_data.update(new_data_dict)
            except json.decoder.JSONDecodeError:
                with open(file= "Password Manager Data.json", mode= "w") as file:    
                    json.dump(obj= new_data_dict, fp= file, indent= 4)
            else:
                with open(file= "Password Manager Data.json", mode= "w") as file:    
                    json.dump(obj= loaded_data, fp= file, indent= 4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    with open(file= "Password Manager Data.json", mode= "r") as file:
        loaded_dict = json.load(fp= file)
        website_data = website_entry.get().title()

        if website_data in loaded_dict:
            messagebox.showinfo(title= website_data.title(), message= f"Email: {loaded_dict[website_data]['email']}\nPassword: {loaded_dict[website_data]['password']}")
        else:
            messagebox.showwarning(title= website_data.title(), message= f"{website_data.title()} is not in the database.")

# ---------------------------- PASSWORD GENERATOR ---------------------------- #
def generate_password():
    password_entry.delete(0, END)
    password_entry.insert(0, get_random_password())
# --------------------------------- UI SETUP --------------------------------- #
window = Tk()
window.title("Password Manager")
window.configure(padx= 30, pady= 40)
window.tk_setPalette(background= "#d4d4d4", foreground= "#3c423e")
# ---------------------------------------------------------------------------- #
logo = PhotoImage(file= "logo.png")
canvas = Canvas(width=160, height=200)
canvas.create_image(100, 100, image= logo)
canvas.grid(column= 1, row= 0)
# ---------------------------------------------------------------------------- #
website_label = Label(text="Website:", font= FONT)
website_label.grid(column= 0, row= 1)

website_entry = Entry(width= 48, background= ENTRY_DEFAULT_COLOR, foreground= ENTRY_DAFAULT_FOREGROUND_COLOR)
website_entry.focus()
website_entry.grid(column= 1, row= 1, columnspan= 2)
# ---------------------------------------------------------------------------- #
email_label = Label(text="Email/Username:", font= FONT)
email_label.grid(column= 0, row= 2)

email_entry = Entry(width= 48, background= ENTRY_DEFAULT_COLOR, foreground= ENTRY_DAFAULT_FOREGROUND_COLOR)
email_entry.insert(0, "Example@example.com")
email_entry.grid(column= 1, row= 2, columnspan= 2)
# ---------------------------------------------------------------------------- #
password_label = Label(text="Password:", font= FONT)
password_label.grid(column= 0, row= 3)

password_entry = Entry(width= 48, background= ENTRY_DEFAULT_COLOR, foreground= ENTRY_DAFAULT_FOREGROUND_COLOR)
password_entry.grid(column= 1, row= 3, columnspan= 2)
# ---------------------------------------------------------------------------- #
generate_password_button = Button(text="Generate", font= ("Times New Roman", 11), width=10, command= generate_password)
generate_password_button.grid(column= 3, row= 3)
# ---------------------------------------------------------------------------- #
add_button = Button(text="Add", font= FONT, width= 33, command= save_data)
add_button.grid(column= 1, row= 4, columnspan= 2)
# ---------------------------------------------------------------------------- #
search_button = Button(text="Search", font= ("Times New Roman", 11), width= 10, command= search)
search_button.grid(column= 3, row= 1)












#TODO: To show our inputed password data, we need a switch of sorts and we could simply pass on the grid functions of either the main input page or our data page






window.mainloop()