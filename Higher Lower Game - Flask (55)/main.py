from flask import Flask
import requests

main = Flask(__name__)

@main.route('/')
def home_page():
    return '<p>Hello World</p>'

@main.route('/<username>')
def username():
    return f'<h1> Aurabuar {username} </h1>'

if __name__ == '__main__':
    main.run(debug= True)