# 🚨 Don't change the code below 👇
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
crossroad_direction = input("You're at a crossroad, where do you want to go? Left of right?\n").lower()

if crossroad_direction == "right":
    print("As you start heading right, a bandit jumps out of the bushes and traps you into a corner — slaying you.\nGame Over.")
elif crossroad_direction == "left":
    swim_or_wait = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if swim_or_wait == "swim":
        print("You started swimming when all of a sudden a shark swam across and started circling you — suddenly striking you.\nGame Over.")
    elif swim_or_wait == "wait":
        three_coloured_door_choice = input("A kind fisherman arrives and takes you across the lake, where you find yourself in front of three huge gates — one is red, the other is yellow and the last is blue. Which one will you choose?\n").lower()
        if (three_coloured_door_choice == "red") or (three_coloured_door_choice == "blue"):
            print("Both the red and blue doors lead to a mysterious dark void, and once the gate shut close behind you, you were trapped in pitch-black forever.\nGame Over.")
        elif three_coloured_door_choice == "yellow":
            print("You found yourself going through the bright-yellow gate. On the other side was a utopian-like world, and on top of a hill was it — the treasure of all treasures.\nThe End.")



