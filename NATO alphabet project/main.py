import pandas as pd

# ------------------------------- Get DataFrame ------------------------------ #

NATO_data = pd.read_csv(filepath_or_buffer="nato_phonetic_alphabet.csv")
d_frame = pd.DataFrame(NATO_data)

# --------- Work with DataFrame to create key-value pairs for letters -------- #

data_dict = {row.letter: row.code for (index, row) in d_frame.iterrows()}

print(data_dict)

# ------------ Create list of phonetic NATO words = to user input ------------ #
finished = False
while finished == False:

    user_input = input("Enter the word/name: ").upper()
    try:
        phonetic_words_result = [data_dict[letter] for letter in user_input]
    except KeyError:
        print("You are only allowed to type letters.\nTry again")
    else:
        print(phonetic_words_result)
        finished = True