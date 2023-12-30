from flask import Flask, request, jsonify
from google import generativeai
from flask_cors import CORS
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
from dropbox import DropboxOAuth2FlowNoRedirect
import requests, json

# -------------------------------- WebApp API -------------------------------- #
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def generate_text_endpoint():
    try:
        request_data = request.get_json()

        temporary_link = request_data['temporaryLink']
        prompt = request_data['prompt']

        image = parse_preview_page_link(temporary_link)

        generated_text = generate_ai_text(prompt, image)

        headers = {'Content-Type': 'application/json'}
        return jsonify({'text': generated_text}), 200, headers

    except Exception as e:
        raise Exception(f"{e}")

@app.route('/dbxtkn', methods=['GET'])
def drop_box_oauth2_token_endpoint():
    APP_KEY = "bx9yg1jyu7zkj18"
    APP_SECRET = "qmqy549b9wab3dk"

    try:
        # TODO: Here, we need OAuth2
        auth_endpoint = "https://api.dropboxapi.com/2/auth/token/from_oauth1"

        headers = {
            "Authorization": "Basic <APP_KEY>:<APP_SECRET>",
            "Content-Type": "application/json"
        }

        data = {
            "oauth1_token": "bx9yg1jyu7zkj18",
            "oauth1_token_secret": "qmqy549b9wab3dk"
        }
        with requests
        r = requests.post(auth_endpoint, headers=headers, data=json.dumps(data))


        # Store the access token securely (database or encrypted file)
        # TODO: (Implement storage method)

        headers = {'Content-Type': 'application/json'}
        return jsonify({'access_token': access_token}), 200, headers

    except Exception as e:
        raise Exception(f'Error: {e}')
        



if __name__ == '__main__':
    app.run(debug=True)

# ---------------------- Gemini Pro Vision Main Function --------------------- #
def generate_ai_text(prompt, image_url):
    API_KEY = "AIzaSyDh-DlmCVoUAHDT3GA5N20pRF668pWZnxk"
    
    generativeai.configure(api_key= API_KEY)
    model = generativeai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([prompt, image_url])

    return response.text


def parse_preview_page_link(temporary_link) -> str:
    image_bytes = requests.get(url= temporary_link).content
    image_data = BytesIO(image_bytes)
    image = Image.open(image_data)

    return image

    






























# ----------------------- JS -> Py -> dbx/Gemini -> JS ----------------------- #


# from flask import Flask, request, jsonify
# from google import generativeai
# from flask_cors import CORS
# from PIL import Image
# from io import BytesIO
# import os, requests, dropbox

# # -------------------------------- WebApp API -------------------------------- #
# app = Flask(__name__)
# CORS(app)

# @app.route('/', methods=['POST'])
# def generate_text_api():
#     try:
#         print(f"1. This is the request size: {request.content_length}")

#         image_bytes = request.get_data()

#         image_bytes_io = BytesIO(image_bytes)

#         # Save image temporarily and process
#         with open('new_image.jpg', 'wb') as f:
#             f.write(image_bytes_io)

#         with open('/tmp/image.jpg', 'rb') as f:
#             image_bytes_io = f.read()

#         print(2)
#         image_url = drop_box_logic(image_bytes_io)
#         print(3)
#         text = request.form.get('text')
#         print(4)
#         generated_text = generate_ai_text(text, image_url)
#         print(5)

#         headers = {'Content-Type': 'application/json'}
#         return jsonify({'text': generated_text}), 200, headers

#     except Exception as e:
#         raise Exception(f"Error processing request: {e}")


# if __name__ == '__main__':
#     app.run(debug=True)

# # ---------------------- Gemini Pro Vision Main Function --------------------- #
# def generate_ai_text(prompt, image_url= None):
#     PALM_KEY = ""
#     generativeai.configure(api_key=PALM_KEY)
#     model = generativeai.GenerativeModel('gemini-pro-vision')

#     # Conditionally use image if provided
#     if image_url:
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#             "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
#             "Cookie": "PHPSESSID=242a10656e1779cac246145de54684aa",
#         }
#         response = requests.get(url= image_url, headers= headers)
#         image_data = BytesIO(response.content)
#         image = Image.open(image_data)
#         response = model.generate_content([prompt, image])
#     else:
#         response = model.generate_content([prompt])

#     return response.text






# # -------------------------- Dropbox as Temp Storage ------------------------- #
# def drop_box_logic(image_bytes_io):
#     access_token = ""  # TODO: Replace with your Dropbox access token
    
#     try:
#         print("Bout to try opening the image...")
#         image = Image.open(image_bytes_io)
#         print("well the damn image opened... Now we gonna check if it's all good by running the verify method on it...")
#         image.verify()  # Check image integrity
#         for i in range(11):
#             print(f"Damn image opened successfully!")

#         with dropbox.Dropbox(oauth2_access_token=access_token) as dbx:
#             uploaded_file = dbx.files_upload(image_bytes_io.read(), "/image.jpg")  # Read from BytesIO for upload
#             shared_link_url = dbx.sharing_create_shared_link_with_settings(
#                 uploaded_file.path_lower
#             ).url
#             return shared_link_url

#     except Exception as e:
#         raise Exception(f"Error uploading image: {e}")






# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #





































































# 1. Temporary File Storage:

# Store the image temporarily on the server using request.files['imageData'].save('/tmp/image.jpg').
# Access the image bytes from this temporary file using with open('/tmp/image.jpg', 'rb') as f: image_bytes = f.read().
# Remember to delete the temporary file after processing: os.remove('/tmp/image.jpg'). 


# # ------------------------ Google Drive Functionality ------------------------ #
# from datetime import datetime, timedelta
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.http import MediaFileUpload

# # Define your Google Drive credentials
# SCOPES = ['https://www.googleapis.com/auth/drive.file']
# flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
# creds = flow.run_console_flow()
# drive_service = build('drive', 'v3', credentials=creds)

# # Function to upload an image to Google Drive
# def upload_image(image_path):
#   with open(image_path, 'rb') as file:
#     file_metadata = {
#       'name': os.path.basename(image_path),
#       'mimeType': 'image/jpeg'  # Adjust based on your image format
#     }
#     media = MediaFileUpload(file, mimetype='image/jpeg')
#     return drive_service.files().create(body=file_metadata, media_body=media).execute()

# # Upload the image
# uploaded_file = upload_image('path/to/your/image.jpg')

# # Schedule deletion for tomorrow
# delete_date = datetime.now() + timedelta(days=1)

# # Create a reminder to delete the file
# reminder = drive_service.files().insert(body={
#   'title': f'Delete {uploaded_file["name"]} on {delete_date.strftime("%Y-%m-%d")}',
#   'parents': ['your-trash-folder-id']  # Replace with your actual trash folder ID
# }).execute()

# # Set up a scheduled task to execute the following code at the delete date
# # (Replace with your preferred scheduling method)
# def delete_file():
#   drive_service.files().delete(uploaded_file['id']).execute()
#   drive_service.files().delete(reminder['id']).execute()

# # Replace this with your actual scheduling logic
# # ...

# # Print confirmation message
# print(f"Image uploaded to Google Drive: {uploaded_file['id']}")
# print(f"Scheduled for deletion on: {delete_date.strftime('%Y-%m-%d')}")

















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
        










# ------------------------ Get access_token via OAuth1 ----------------------- #
# import dropbox
# from dropbox import DropboxOAuth2FlowNoRedirect

# APP_KEY = "d5jldlgvwbaop3f"
# APP_SECRET = "3xek9a87iujkkal"

# auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

# authorize_url = auth_flow.start()
# print("1. Go to: " + authorize_url)
# print("2. Click \"Allow\" (you might have to log in first).")
# print("3. Copy the authorization code.")
# auth_code = input("Enter the authorization code here: ").strip()

# try:
#     oauth_result = auth_flow.finish(auth_code)
# except Exception as e:
#     print('Error: %s' % (e,))
#     exit(1)
# ---------------------------------------------------------------------------- #