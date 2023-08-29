import smtplib, datetime, linecache
from random import randint


with open(file="quotes.txt", mode="r") as file:
    lines_total = sum(1 for line in file)

quote = linecache.getline(filename="quotes.txt", lineno=randint(1, lines_total))

# ---------------------------------------------------------------------------- #

now = datetime.datetime.now()
day_of_week = now.isoweekday()

if day_of_week == 1:
    my_email = "Diego007lopez@gmail.com"
    recipient = "Lopez.d9@outlook.com"

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as host_connection:
        host_connection.starttls()
        host_connection.login(user= my_email, password= "grxdhlzlwiflpyru") 
        host_connection.sendmail(from_addr=my_email, to_addrs=recipient, msg=f"Subject: Quote of the Day\n\n{quote}")

