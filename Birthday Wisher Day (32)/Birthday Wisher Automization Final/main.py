##################### Extra Hard Starting Project ######################
import datetime, smtplib, os
import pandas as pd
from random import choice

# 1. Update the birthdays.csv
with open("Birthday Wisher Automization Final/birthdays.csv", mode="r+") as file:
    lines_list = file.readlines()
    lines_list[-1] = "Terry,Lopez.d9@outlook.com,1997,08,29"
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
    os.listdir(path="Birthday Wisher Automization Final\letter_templates")

# 4. Send the letter generated in step 3 to that person's email address.




