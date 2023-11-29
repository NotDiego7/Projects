# ----------------------------------- Flask ---------------------------------- #
# from flask import Flask
# import requests

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# if __name__ == "__main__":
#     app.run()

# ---------------------------- Decorator Exercise ---------------------------- #
import time
current_time = time.time()
# print(current_time)

def speed_calc_decorator(function_to_decorate):
    def wrapper():

        before_execution_time = time.time()
        function_to_decorate()
        after_execution_time = time.time()
        
        execution_time = after_execution_time - before_execution_time
        return execution_time

    return wrapper




@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_execution_time = round(fast_function(), 2)
slow_execution_time = round(slow_function(), 2)
print(f'The fast_function execution time was {fast_execution_time} secs, while the slow_function execution time was {slow_execution_time} secs.\nThe fast_function was {slow_execution_time - fast_execution_time} secs faster.\n')