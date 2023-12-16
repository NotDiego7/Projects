from flask import Flask, request, jsonify
from google import generativeai
from flask_cors import CORS
from PIL import Image
from io import BytesIO
import os, requests


# ---------------------------------- Gemini ---------------------------------- #
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
    # PALM_KEY = os.getenv('PALM_API_KEY')
    # print(PALM_KEY)
    """
    NEED TO CHANGE THIS HARDCODE METHOD!!!!!!
    """
    # ---------------------------------------------------------------------------- #
    PALM_KEY = "AIzaSyByeZrXmwsZsIz5MNtSqqwnt1ZWHBtuaY8"
    # ---------------------------------------------------------------------------- #
    """
    NEED TO CHANGE THIS HARDCODE METHOD!!!!!!
    """
    generativeai.configure(api_key= PALM_KEY)
    model = generativeai.GenerativeModel('gemini-pro-vision')
    # TODO Here we basically need to say, if user uploaded image, then attach image and prompt, else just prompt
    url = 'https://archive.org/download/as17-140-21391/as17-140-21391.jpg'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Cookie": "PHPSESSID=242a10656e1779cac246145de54684aa",
    }
    response = requests.get(url= url, headers= headers)
    image_data = BytesIO(response.content)
    image = Image.open(image_data)
    response = model.generate_content([prompt, image])
  
    return response.text













# ----------------------------- Chat Based System ---------------------------- #


# from flask import Flask, request, jsonify
# from google import generativeai
# from flask_cors import CORS
# from time import sleep
# from datetime import datetime
# import os



# # --------------------- Hook up Py file for HTTP requests -------------------- #
# app = Flask(__name__)
# CORS(app)

# @app.route('/', methods=['POST'])
# def generate_text_api():
#     text = request.json['text']

#     generatedText = generate_ai_text(text)

#     headers = {
#         'Access-Control-Allow-Origin': '*',
#         'Access-Control-Allow-Methods': '*',
#         'Access-Control-Allow-Headers': '*'
#     }


#     return jsonify({'text': generatedText}), 200, headers


# if __name__ == '__main__':
#     app.run(debug=True)

# # ----------------------- Main Function to be executed ----------------------- #
# def generate_ai_text(prompt):
#     # PALM_KEY = os.getenv('PALM_API_KEY')
#     # print(PALM_KEY)
#     """
#     NEED TO CHANGE THIS HARDCODE METHOD!!!!!!
#     """
#     # ---------------------------------------------------------------------------- #
#     PALM_KEY = "AIzaSyCzeG9tUGbeeODMYCvrY9btm8UQupprjb8"
#     # ---------------------------------------------------------------------------- #
#     """
#     NEED TO CHANGE THIS HARDCODE METHOD!!!!!!
#     """

#     generativeai.configure(api_key= PALM_KEY)

#     PaLMs_response = generativeai.chat(prompt= [prompt])
#     print(PaLMs_response.candidates[0]['content'])

#     if len(PaLMs_response.candidates) > 0:
#         generated_text = PaLMs_response.candidates[0]['content']
#         print(generated_text)
#     else:
#         generated_text = "No response candidates were returned by the Google API."

#     return generated_text