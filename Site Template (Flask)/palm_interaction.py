from flask import Flask, request, jsonify
from google import generativeai
from flask_cors import CORS
from PIL import Image
from io import BytesIO
import os, requests

from datetime import datetime, timedelta
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload

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
    PALM_KEY = "AIzaSyBfDMWMKteCfBPi4gXA2RYrV_G-ln7axj4"
    # ---------------------------------------------------------------------------- #
    """
    NEED TO CHANGE THIS HARDCODE METHOD!!!!!!
    """
    generativeai.configure(api_key= PALM_KEY)
    model = generativeai.GenerativeModel('gemini-pro-vision')
    # TODO Here we basically need to say, if user uploaded image, then attach image and prompt, else just prompt
    url = 'https://ia801404.us.archive.org/14/items/nhs-01-e-07/NHS01E01.jpg'
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






# ------------------------ Google Drive Functionality ------------------------ #
# Define your Google Drive credentials
SCOPES = ['https://www.googleapis.com/auth/drive.file']
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_console_flow()
drive_service = build('drive', 'v3', credentials=creds)

# Function to upload an image to Google Drive
def upload_image(image_path):
  with open(image_path, 'rb') as file:
    file_metadata = {
      'name': os.path.basename(image_path),
      'mimeType': 'image/jpeg'  # Adjust based on your image format
    }
    media = MediaFileUpload(file, mimetype='image/jpeg')
    return drive_service.files().create(body=file_metadata, media_body=media).execute()

# Upload the image
uploaded_file = upload_image('path/to/your/image.jpg')

# Schedule deletion for tomorrow
delete_date = datetime.now() + timedelta(days=1)

# Create a reminder to delete the file
reminder = drive_service.files().insert(body={
  'title': f'Delete {uploaded_file["name"]} on {delete_date.strftime("%Y-%m-%d")}',
  'parents': ['your-trash-folder-id']  # Replace with your actual trash folder ID
}).execute()

# Set up a scheduled task to execute the following code at the delete date
# (Replace with your preferred scheduling method)
def delete_file():
  drive_service.files().delete(uploaded_file['id']).execute()
  drive_service.files().delete(reminder['id']).execute()

# Replace this with your actual scheduling logic
# ...

# Print confirmation message
print(f"Image uploaded to Google Drive: {uploaded_file['id']}")
print(f"Scheduled for deletion on: {delete_date.strftime('%Y-%m-%d')}")

















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