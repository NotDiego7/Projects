import time

# def log_execution_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
#         return result
#     return wrapper

# @log_execution_time
# def my_function(n):
#     for i in range(n):
#         print(i)

# my_function(100)

# class Lavaral(object):
#     def __init__(self, affected_function):
#         self.affected_function = affected_function

#     def decorator(self):
#         time.sleep(10.0)
#         def wrapper():
#             return self.affected_function
                

def decorator(affected_function):
    def wrapper():
        print('Here we go...')
        time.sleep(1.0)
        print(3)
        time.sleep(1.0)
        print(2)
        time.sleep(1.0)
        print(1)
        time.sleep(2.5)
        affected_function()
        return
    return wrapper

# ---------------------------------------------------------------------------- #
@decorator
def my_function():
    num = 1
    for i in range(11):
        print(f'\n\n\n{num}. Dan the Man...\n\n\n')
        num += 1

decorated_function = my_function()
decorated_function()
# lavaral_instance = Lavaral(my_function)
# lavaral_instance()