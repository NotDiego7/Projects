import time           

# def decorator(affected_function):
#     def wrapper():
#         print('Here we go...')
#         time.sleep(1.0)
#         print(3)
#         time.sleep(1.0)
#         print(2)
#         time.sleep(1.0)
#         print(1)
#         time.sleep(2.5)
#         affected_function()
#         return
#     return wrapper

# # ---------------------------------------------------------------------------- #
# @decorator
# def my_function():
#     num = 1
#     for i in range(11):
#         print(f'\n\n\n{num}. Dan the Man...\n\n\n')
#         num += 1

# decorated_function = my_function()
# decorated_function()

def add_user_interactive_question(function_to_decorate):
    def wrapper():
        time.sleep(0.2)
        user_response = input(f'{player_id.title()}, are you ready? ') # TODO Need to pass player_id into this
        if user_response.title() == 'Yes':
            return function_to_decorate()
        else:
            return
    return wrapper


@add_user_interactive_question
def first():
    words_to_output = ['Ready...', 'Set!', 'Gooooo!']
    for i in range(0, 3):
        time.sleep(1.2)
        print(words_to_output[i])


player_id = input('Enter your name: ')
first()