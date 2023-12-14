from flask import Flask, request, jsonify
from google import generativeai
from flask_cors import CORS
from time import sleep
from datetime import datetime
import os



# --------------------- Hook up Py file for HTTP requests -------------------- #
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def generate_text_api():
    text = request.json['text']


    generatedText = generate_ai_text(text)

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': '*',
        'Access-Control-Allow-Headers': '*'
    }


    return jsonify({'text': generatedText}), 200, headers


if __name__ == '__main__':
    app.run(debug=True)


# ----------------------- Main Function to be executed ----------------------- #
def generate_ai_text(prompt):
    PALM_KEY = os.getenv('PALM_API_KEY')
    generativeai.configure(api_key= PALM_KEY)

    PaLMs_response = generativeai.chat(prompt= [prompt])
    print(PaLMs_response)


    return jsonify({'text': PaLMs_response})