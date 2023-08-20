#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_character = nr_letters + nr_symbols + nr_numbers

# --------------------------- Order not randomised: -------------------------- #

letters_total = ""
symbols_total = ""
numbers_total = ""

for letter in letters:
    if len(letters_total) != nr_letters:
        letters_total += random.choice(letters)
    else:
        break


for symbol in symbols:
    if len(symbols_total) != nr_symbols:
        symbols_total += random.choice(symbols)
    else:
        break

for number in numbers:
    if len(numbers_total) != nr_numbers:
        numbers_total += random.choice(numbers)
    else:
        break

# ---------------------- Order of characters randomised: --------------------- #

final_str = ""
character_list = list(f"{letters_total}{symbols_total}{numbers_total}")

random.shuffle(character_list)
final_str = "".join(character_list)


print(f"Your password is: {final_str}")