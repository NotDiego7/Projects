from flask import Flask, request, jsonify
from google import generativeai
from flask_cors import CORS
from io import BytesIO
from PIL import Image
import requests, base64

API_KEY = "AIzaSyDh-DlmCVoUAHDT3GA5N20pRF668pWZnxk"

# -------------------------------- WebApp API -------------------------------- #
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def home():
    """
    Fulfills POST requests.
    Responds with Google (AI) Gemini generated text (JSON).
    """
    try:
        request_data = request.get_json()

        image_base64 = request_data['imageBase64']
        prompt = request_data['prompt']

        image = parse_and_open_image(image_base64)

        generated_text = generate_ai_text(prompt, image)

        headers = {'Content-Type': 'application/json'}
        return jsonify({'text': generated_text}), 200, headers

    except Exception as e:
        raise Exception(f"{e}")



if __name__ == '__main__':
    app.run(debug=True)


# -------------------------- Gemini Pro Vision Flow -------------------------- #
def generate_ai_text(prompt, image_url):
    generativeai.configure(api_key= API_KEY)
    model = generativeai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([prompt, image_url])

    return response.text


def parse_and_open_image(image_base64):
    image_blob = base64.b64decode(image_base64)
    image_data = BytesIO(image_blob)
    image = Image.open(image_data)
    return image
