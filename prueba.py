from __future__ import print_function

import getpass
import os, shutil
import os.path
import io

'''from dotenv import load_dotenv
load_dotenv()'''

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
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
                'credentials.json', SCOPES)
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


'''if __name__ == '__main__':
    downloadContent(getDriveService())
'''

from googleapiclient.http import MediaFileUpload
#from google.auth.transport.requests import Request
#from google.oauth2.credentials import Credentials
#from google_auth_oauthlib.flow import InstalledAppFlow
#from googleapiclient.discovery import build
from quickstart import FOLDER_ID, FILE_ID
import shutil, os
import time

def uploadContent(service, PATH):
    while True:
        zip = shutil.make_archive(f"{PATH}FIALAND", "zip", f"{PATH}FIALAND",)

        file_metadata = {'name': 'FIALAND.zip',
                         'parents': [FOLDER_ID]}

        media = MediaFileUpload(f'{PATH}FIALAND.zip',
                                mimetype='application/zip')
        # pylint: disable=maybe-no-member
        file = service.files().update(media_body=media,
                                      fileId=FILE_ID).execute()

        time.sleep(600)
        #return file.get('id')

from googleapiclient.http import MediaIoBaseDownload
from quickstart import FILE_ID, PATH
import io
import os
def downloadContent(service):
    file_id = FILE_ID

    request = service.files().get_media(fileId=file_id)
    file = io.BytesIO()
    downloader = MediaIoBaseDownload(file, request)
    done = False

    while done is False:
        status, done = downloader.next_chunk()
        print(F'Download {int(status.progress() * 100)}.')
    file.seek(0)

    with open(os.path.join(PATH, "FIALAND.zip"), "wb") as f:
        f.write(file.read())
        f.close()


import sys
import getpass
import os

from quickstart import getDriveService as service
from quickstart import PATH
from uploadContent import uploadContent
from downloadContent import downloadContent

if sys.argv[1] == "--help":
    print(f"""
    ----------------------------------------------------------------
                    Bienvenido {getpass.getuser()} a la ayuda!
    ----------------------------------------------------------------

        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⠞⠛⣿⠉⠉⠉⠉⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠁⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⠉⠉⠙⠒⠒⣲⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⢠⡶⠲⠿⠀⠀⠀⠀⠀⢸⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⡇⠀⢸⡷⠿⡾⠾⣧⠀⠀⠀⣤⠤⢤⡤⣾⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⡇⠀⢸⣷⣀⣧⣀⣿⠀⠀⠀⣿⣀⣼⣅⣿⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⡇⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⣧⠀⢸⠀⠀⠀⠀⣿⣷⣿⡟⣶⠀⠀⠀⢺⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣄⣸⣧⣀⡀⠀⢀⣿⡀⢸⡆⠀⠀⠀⢉⣋⣋⡛⠉⠀⢀⢀⣽⠀⣿⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⠿⣶⣴⠟⠛⢿⢳⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⢿⡆⠀⠀⠈⠉⠉⢻⣻⠟⠛⠻⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⡿⠿⣿⣟⣻⣤⠶⠶⠿⣦⣠⡾⠛⠉⠀⠀⠀⠈⣧⣄⣨⢷⢿⣆⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⠏⢸⣇⠀⠀⠀⠀⠀⢸⣿⡁⠀⠀⠀⠠⡶⢾⣷⠀⠀⠀⣴⠶⠿⠇⠀⣿⡏⠉⠀⠀⠠⢼⣯⡁⠀⠀⠀⠀⢀⣠⡠⣛⡋⠀⠀⠈⢹⡟⣆⠀⠀
⠀⠀⠀⠀⠀⣼⢻⠃⠀⣻⣀⣀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⡇⠀⠿⠤⠤⠤⠾⠀⠀⠀⠀⣿⣇⣀⣀⣤⠼⣯⣭⣦⠀⣀⡴⣞⣿⡿⠿⠟⢳⡄⠀⠀⠀⢻⡻⡆⠀
⠀⠀⠀⢀⡾⠃⠘⡆⣰⠏⠉⠉⠉⠉⠉⣳⣿⡄⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣸⡿⣍⠀⠀⠉⠉⠹⠿⠷⢿⣯⣿⠁⣠⡀⣸⢿⣄⠀⠀⠈⢷⢻⡄
⠀⠀⢀⡾⠃⠀⠀⣿⣃⣀⠀⠀⠀⠀⣰⡟⢹⡁⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠙⢦⠀⠀⠀⠀⠀⠀⢸⡇⠀⢀⣸⠙⣿⣿⢿⡄⠀⠀⣨⣿⣿
⠀⢠⡿⠁⠀⢀⡼⠁⠀⠈⠉⠉⠉⣹⣿⠀⢸⠉⠉⣷⣀⣴⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢻⠀⠀⠀⠱⣄⠀⠀⠀⢸⡟⠃⠀⢻⡿⣿⠟⠋⠈⢿⣶⣏⣉⣿⡗
⢠⡟⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⣰⠏⣿⠀⢸⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡀⠀⠀⠀⠘⢧⡀⢸⣟⠛⠀⢶⠚⣿⣿⣆⠀⠀⠈⠁⠘⠛⠋⠀
⢸⡇⠀⢠⠟⠀⠀⠀⠀⠀⠀⣼⠏⠀⡟⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡈⢻⣄⠀⠀⠀⠀⠙⣿⠗⠀⣶⠚⢳⡾⡇⠻⣦⡀⠀⠀⠀⠀⠀⠀
⢸⡇⣰⠋⠀⠀⠀⠀⠀⠀⣴⠇⠀⢀⡇⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠹⣦⡀⠀⠠⣾⡏⠀⣶⠾⢦⣼⠟⠛⠉⣻⠃⠀⠀⠀⠀⠀⠀
⠘⣷⡇⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⢸⡇⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠈⢻⣶⣴⡿⠀⢠⠜⢂⣴⠿⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠉⠉⠛⠛⠛⠛⠓⠞⠃⠀⠀⠀⢸⣇⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠠⣽⣷⠀⢀⡸⠦⣼⡷⠀⠀⢀⣾⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣏⠙⡷⠶⠶⠶⠶⠶⠶⠶⠒⠒⠒⠒⠒⠒⠋⠉⠉⣿⡇⠀⠀⠀⠀⠹⣯⣀⣸⣧⣤⣿⠶⠶⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣶⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡤⠤⠤⠶⢶⡿⠇⠀⠀⠀⠀⠀⠙⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣸⡄⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⠀⢾⢷⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⣧⠀⠀⠀⠀⠀⠀⠀⢸⣏⣷⠤⠤⠤⠤⠤⠤⢴⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣼⠀⠀⠀⠀⠀⠀⠀⠈⣿⠏⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢸⡄⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡅⣧⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⡄⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⣇⠀⠀⠀⠀⠀⠀⠀⢿⣦⣤⣤⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⣿⣤⣤⣤⣤⣤⣤⣤⣼⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡾⢻⡀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢈⡷⠶⠤⠶⠶⠶⠴⢤⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡏⠀⠀⠀⠀⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

    Parámetros de los que dispongo:

    -ul/--upload:   Cada 10 minutos se actualiza el server/mundo en la nube.
    --------------------------------------------------------------------------------------------
    -dl/--download: Descarga instantánea del último estado del server/mundo guardado en la nube. 

    """)

elif sys.argv[1] == "--upload" or sys.argv[1] == "-ul":
    uploadContent(service(), PATH)

elif sys.argv[1] == "--download" or sys.argv[1] == "-dl":
    downloadContent(service())
else:
    print("\n[!] Uknown Command\nEscribe --help para saber que parámetos utilizar")