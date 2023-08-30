##################### Extra Hard Starting Project ######################
import datetime, smtplib, os
import pandas as pd
from random import choice

# 1. Update the birthdays.csv
with open("Birthday Wisher Automization Final/birthdays.csv", mode="r+") as file:
    lines_list = file.readlines()
    lines_list[-1] = "Terry,Lopez.d9@outlook.com,1997,08,30"
    file.seek(0)
    file.writelines(lines_list)

# 2. Check if today matches a birthday in the birthdays.csv
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day

dataframe = pd.read_csv("Birthday Wisher Automization Final/birthdays.csv")
day_bool = any(dataframe["day"] == current_day)
month_bool = any(dataframe["month"] == current_month)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if day_bool and month_bool:
    file_list = [file for file in os.listdir(path="Birthday Wisher Automization Final\letter_templates")]
    letter = choice(file_list)
    letter_path = os.path.join("Birthday Wisher Automization Final\letter_templates", letter)
    # ---------------------------------------------------------------------------- #
    with open(letter_path, mode="r+") as file:
        letter = file.read()
        new_letter = letter.replace("[NAME]", "Yeica")
        file.seek(0)
        file.write(new_letter)

# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP(host="smtp.gmail.com", port=587) as host_connection:
    host_connection.starttls()
    host_connection.login("Diego007lopez@gmail.com", "grxdhlzlwiflpyru")
    host_connection.sendmail(from_addr="Diego007lopez@gmail.com", to_addrs="Lopez.d9@outlook.com", msg=f"Subject: Happy Birthday!\n\n{new_letter}")




