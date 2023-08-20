# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small_pizza = 2
pepperoni_medium_large_pizza = 3
total = 0

if size == "M" or size == "L":
    total += large_pizza
    if size == "M":
        total -= 5
elif size == "S":
    total += small_pizza

if add_pepperoni == "Y":
    if size == "M" or size == "L":
        total += pepperoni_medium_large_pizza
    elif size == "S":
        total += pepperoni_small_pizza

if extra_cheese == "Y":
    total += 1

print(f"Your final bill is ${total}.")