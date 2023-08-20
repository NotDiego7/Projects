rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

possible_choices = ["r", "p", "s"]
game_images = [rock, paper, scissors]

human_choice = input(f"Go ahead, type the first letter of your option of choice {possible_choices}.")
human_choice = human_choice.lower()
computer_choice = random.choice(possible_choices)

if human_choice not in possible_choices:
    print("Not a valid choice.")
elif computer_choice == "r" and human_choice == "s" or human_choice == "r" and computer_choice == "s":
    print(f"{game_images[0]}\n{game_images[2]}\nRock wins.")
elif computer_choice == "p" and human_choice == "r" or human_choice == "p" and computer_choice == "r":
    print(f"{game_images[1]}\n{game_images[0]}\nPaper wins.")
elif computer_choice == "s" and human_choice == "p" or human_choice == "s" and computer_choice == "p":
    print(f"{game_images[2]}\n{game_images[1]}\nScissors wins.")
elif computer_choice == human_choice and computer_choice == "r":
    print(f"{game_images[0]}\n{game_images[0]}\nTie.")
elif computer_choice == human_choice and computer_choice == "p":
    print(f"{game_images[1]}\n{game_images[1]}\nTie.")
elif computer_choice == human_choice and computer_choice == "s":
    print(f"{game_images[2]}\n{game_images[2]}\nTie.")