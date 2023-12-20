from datetime import datetime, timedelta
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload

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

