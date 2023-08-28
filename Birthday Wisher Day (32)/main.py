import smtplib

my_email = "Diego007lopez@gmail.com"
recipient = "erikitasan99@gmail.com"

host_connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
host_connection.starttls()
host_connection.login(user= my_email, password= "grxdhlzlwiflpyru") 
host_connection.sendmail(from_addr=my_email, to_addrs=recipient, msg="Subject: Erika es...\n\nculooooooooooooo")
host_connection.close()