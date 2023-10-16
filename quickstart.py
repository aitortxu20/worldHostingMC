from __future__ import print_function

import getpass
import os, shutil
import os.path
import io

from dotenv import load_dotenv
load_dotenv()

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload

import mimetypes

SCOPES = ['https://www.googleapis.com/auth/drive']
PATH = f"C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\.minecraft\\saves\\"
FOLDER_ID = os.getenv('FOLDER_ID')
FILE_ID = os.getenv('FILE_ID')


# If modifying these scopes, delete the file token.json.

def getDriveService():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials3.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)
        return service

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')
getDriveService()

'''if __name__ == '__main__':
    downloadContent(getDriveService())
'''

