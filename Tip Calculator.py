#Tip Calculator
print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill?\n"))
number_of_people = int(input("How many people to split the bill?\n"))
tip_percentage = int(input("What percentage of a tip would you like to give?\n"))
#The following is a numerical way of getting the percentage
tip_percentage = tip_percentage / 100
tipAmount = total_bill * tip_percentage
pay_per_person = (total_bill + tipAmount) / number_of_people
pay_per_person = round(pay_per_person, 2)
pay_per_person = "{:.2f}".format(pay_per_person)
print(f"Each person should pay {pay_per_person}")

