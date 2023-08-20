import random
from GAME_DATA import data
from GAME_ART import logo, vs
score = 0


def get_output_message(answer_validation_param, end_game_param):
    """Prints out if user was right or wrong and their respective score."""
    if answer_validation_param == "You're right!":
        print(f"{answer_validation_param} Current score: {score}")
    elif answer_validation_param == "You're wrong!":
        print(f"Sorry. {answer_validation_param} Final score: {score}")
        end_game_param = True
        return end_game_param



def get_instagram_users():
    """Returns two different IG users and their data."""
    instagram_user_one = random.choice(data)
    instagram_user_two = random.choice(data)

    while instagram_user_one == instagram_user_two:
        instagram_user_two = random.choice(data)
    return instagram_user_one, instagram_user_two



def score_count(answer_validation_param):
    """Returns how many rounds the user has answered correctly."""
    global score
    if answer_validation_param == "You're right!":
        score += 1



def get_comparison(user_one_param, user_two_param):
    """Prints the information used to compare two different IG users & game art (vs)."""
    print(f"Compare the following:\nA: {user_one_param.get('name')}, a {user_one_param.get('description')} from {user_one_param.get('country')}")
    print(vs), print(f"B: {user_two_param.get('name')}, a {user_two_param.get('description')} from {user_two_param.get('country')}")



def check_answer(user_one_param, user_two_param, answer):
    """Checks user's answer and prints out if their right or wrong."""
    user_one_count = user_one_param.get('follower_count')
    user_two_count = user_two_param.get('follower_count')

    if answer == 'a' and user_one_count > user_two_count:
        return "You're right!"
    elif answer == 'a' and user_one_count < user_two_count:
        return "You're wrong!"
    elif answer == 'b' and user_one_count < user_two_count:
        return "You're right!"
    elif answer == 'b' and user_one_count > user_two_count:
        return "You're wrong!"



def main():
    """Executes all parameters for functionality."""
    end_game = False
    while end_game == False:
        print(logo)
        
        if score > 0:
           end_game = get_output_message(answer_validation, end_game)
           if end_game:
            return

        instagram_user_one, instagram_user_two = get_instagram_users()
        
        get_comparison(instagram_user_one, instagram_user_two)

        user_answer = input("Who do you think has more followers, A or B? ").lower()
        answer_validation = check_answer(instagram_user_one, instagram_user_two, user_answer)

        score_count(answer_validation)
        
#This is to catch the first round wrong answers and print the results
        if score == 0:
            print(f"Sorry. {answer_validation} Final score: {score}")
            end_game = True

        


    
    

main()