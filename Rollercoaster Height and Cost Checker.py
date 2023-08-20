print("We're first going to check if you're over the required height, which is 120cm.")
height = int(input("What is your height in cm.\n"))
if height >= 120:
    print("You're good on height.");
    print("Now we've got to check the price on your ticket - adults pay a little more - kids pay a little less.");
    age = int(input("Enter your age\n"))
    if age >= 45 and age <= 55:
        ticket = 0
        print(f"Your ticket is ${ticket}")
    elif age >= 18:
        ticket = 12
        print(f"Your ticket is ${ticket}")
        if input("Would you like a picture for $3?") == "yes":
                print(f"Great. You're ticket is {ticket + 3}")
        else:
                print(f"Okay. You're ticket is {ticket}")
    elif age >= 12 and age < 18:
            ticket = 7
            print(f"Your ticket is ${ticket}")
            if input("Would you like a picture for $3?") == "yes":
                 print(f"Great. You're ticket is {ticket + 3}")
            else:
                 print(f"Okay. You're ticket is {ticket}")
    elif age < 12:
          ticket = 5
          print(f"Your ticket is ${ticket}")
          if input("Would you like a picture for $3?") == "yes":
                 print(f"Great. You're ticket is {ticket + 3}")
else:
        print ("No, too short.")
