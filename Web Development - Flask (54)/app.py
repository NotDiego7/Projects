# from flask import Flask
# import requests

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# if __name__ == "__main__":
#     app.run()

def outer():
    print('I am the outer function.')

    def inner():
        print('I am the inner function.')

    inner()

outer()