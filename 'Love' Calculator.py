# 🚨 Don't change the code below 👇
print("Welcome to the 'Love' Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combo_name = name1.lower() + name2.lower()

combo_name_count1 = combo_name.count("t"), combo_name.count("r"), combo_name.count("u"), combo_name.count("e")
combo_name_count2 = combo_name.count("l"), combo_name.count("o"), combo_name.count("v"), combo_name.count("e")

total_count = (str(sum(combo_name_count1)) + str(sum(combo_name_count2)))

total_count = int(total_count)

if total_count < 10 or total_count > 90:
    print(f"Your score is {total_count}, you go together like coke and mentos.")
elif total_count > 40 and total_count < 50:
    print(f"Your score is {total_count}, you are alright together.")
else:
    print(f"Your score is {total_count}.")
