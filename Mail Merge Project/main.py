
# --------------- Get names only (no special characters, etc.) --------------- #

edited_names = []
with open(file=r"C:\Users\Lopez\Desktop\Mail Merge Project Start\Input\Names\invited_names.txt") as file:
    names = file.readlines()
    for i in names:
        edited_names.append(i.replace("\n", ""))
    
# print(edited_names)

# ------------------------ Create empty letters (DONE) ----------------------- #

# for i in edited_names:
#     with open(file=f"Output/ReadyToSend/{i}.txt", mode="w") as letter:
#         letter.write("")

# ------------------------ Get starting_letter content ----------------------- #

with open(file=r"C:\Users\Lopez\Desktop\Mail Merge Project Start\Input\Letters\starting_letter.txt") as template:
    template = template.readlines()

# print(template)

# ------------------------------- Make letters ------------------------------- #

for i in edited_names:
    with open(file=f"Output/ReadyToSend/{i}.txt", mode="w") as final_letter:
        template[0] = template[0].replace("[name]", i)
        final_letter.writelines(template)
        template[0] = template[0].replace(i, "[name]")