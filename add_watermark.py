import datetime
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from apikey import apikey
from googleapiclient.http import MediaFileUpload
CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_console()
youtube = build('youtube', 'v3', credentials=credentials)
request = youtube.watermarks().set(
        channelId="UCiBfuUreTbKvBKtQbb6SIWQ",
        body={
          "position": { "type": "corner", "cornerPosition": "bottomRight" },
               "timing": { "type": "offsetFromStart", "offsetMs": 60 }
        },
        media_body=MediaFileUpload("test2.jpg")
    )
request.execute()
