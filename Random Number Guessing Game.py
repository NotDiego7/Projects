import random

random_number = random.randint(1, 100)


print("Welcome to the Number Guessing Game.")
difficulty_level = input("Choose your difficulty level, please type 'easy' or 'hard': ")


if difficulty_level == "easy":
    tries_count_left = 10
elif difficulty_level == "hard":
    tries_count_left = 5
print(f"You have {tries_count_left} attempts remaining to guess the number.")


while tries_count_left > 0:
    user_guess = int(input("Make a guess: "))
    if user_guess > random_number:
        print("Too high\nGuess again")
        tries_count_left -= 1
        print(f"You have {tries_count_left} attempts remaining to guess the number.")
    elif user_guess < random_number:
        print("Too low\nGuess again")
        tries_count_left -= 1
        print(f"You have {tries_count_left} attempts remaining to guess the number.")
    else:
        print(f"You guessed the number!\nThe number was {random_number}.")
        tries_count_left = 0
else:
    print("Sorry. You ran out of attempts.")







