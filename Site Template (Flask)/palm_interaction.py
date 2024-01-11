from flask import Flask, request, jsonify
from google import generativeai
from flask_cors import CORS
from io import BytesIO
from PIL import Image
import requests, dropbox

APP_KEY = "bx9yg1jyu7zkj18"
APP_SECRET = "qmqy549b9wab3dk"
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

        temporary_link = request_data['temporaryLink']
        print(f'THIS IS IT: {temporary_link}')
        prompt = request_data['prompt']

        image = parse_and_open_image(temporary_link)

        generated_text = generate_ai_text(prompt, image)

        headers = {'Content-Type': 'application/json'}
        return jsonify({'text': generated_text}), 200, headers

    except Exception as e:
        raise Exception(f"{e}")


@app.route('/auth-step-one', methods=['GET'])
def auth_step_one():
    '''
    Fulfills GET requests.
    Responds with authorization URL (JSON).
    '''
    try:
        authorization_flow = dropbox.DropboxOAuth2FlowNoRedirect(
            consumer_key= APP_KEY, 
            consumer_secret= APP_SECRET, 
            token_access_type= 'legacy',
            timeout= 100.0
            )

        authorization_url = authorization_flow.start()
        headers = {'Content-Type': 'application/json'}

        return jsonify({'authorizationURL': authorization_url}), 200, headers

    except Exception as e:
        raise Exception(f'{e}')


@app.route('/auth-step-two', methods=['POST'])
def auth_step_two():
    '''
    Fulfills POST requests transporting authorization code.
    Responds with long-lived no-expiration access token (JSON).
    '''
    try:
        response_data = request.get_json()
        authorization_code = response_data['authorizationCode'].strip()
        oauth_result = finish_authorization(authorization_code)
        long_lived_access_token = oauth_result.access_token
        headers = {'Content-Type': 'application/json'}

        return jsonify({'longLivedAccessToken': long_lived_access_token}), 200, headers
    
    except Exception as e:
        raise Exception(f'{e}')


if __name__ == '__main__':
    app.run(debug=True)


# -------------------------- Gemini Pro Vision Flow -------------------------- #
def generate_ai_text(prompt, image_url):
    generativeai.configure(api_key= API_KEY)
    model = generativeai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([prompt, image_url])

    return response.text


def parse_and_open_image(temporary_link):
    image_bytes = requests.get(url= temporary_link).content
    image_data = BytesIO(image_bytes)
    image = Image.open(image_data)

    return image


# ---------------- Helper function to finish DBX authorization --------------- #
def finish_authorization(authorization_code):
    authorization_flow = dropbox.DropboxOAuth2FlowNoRedirect(
        consumer_key=APP_KEY,
        consumer_secret=APP_SECRET,
        token_access_type='legacy',
        timeout=100.0
    )
    return authorization_flow.finish(authorization_code)