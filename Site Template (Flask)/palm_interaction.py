from flask import Flask, request, jsonify
from google import generativeai
from flask_cors import CORS
import os

# --------------------- Hook up Py file for HTTP requests -------------------- #
app = Flask(__name__)
CORS(app, origins= 'http://127.0.0.1:3000/ai.html')

@app.route('/home/NotDiego7/mysite/', methods=['POST'])
def generate_text_api():
    text = request.json['text']

    generatedText = generate_ai_text(text)

    headers = {
        'Access-Control-Allow-Origin': 'http://127.0.0.1:3000/ai.html',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type'
    }


    return jsonify({'text': generatedText}), 200, headers


if __name__ == '__main__':
    app.run(debug=True)


# ----------------------- Main Function to be executed ----------------------- #
def generate_ai_text(prompt):
    PALM_KEY = os.getenv('PALM_API_KEY')
    generativeai.configure(api_key= PALM_KEY)

    PaLMs_response = generativeai.chat(prompt= [prompt])


    return jsonify({'text': PaLMs_response})