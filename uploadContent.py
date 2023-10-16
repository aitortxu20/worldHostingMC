from googleapiclient.http import MediaFileUpload
#from google.auth.transport.requests import Request
#from google.oauth2.credentials import Credentials
#from google_auth_oauthlib.flow import InstalledAppFlow
#from googleapiclient.discovery import build
from quickstart import FOLDER_ID, FILE_ID
import shutil, os
import time
from datetime import datetime

def uploadContent(service, PATH):

    shutil.rmtree(f"{PATH}pruebas")
    shutil.copytree(f"{PATH}FIALAND", f"{PATH}pruebas")

    for file in os.listdir(f"{PATH}pruebas"):
        if file == "playerdata":
            shutil.rmtree(f"{PATH}pruebas\\{file}")

    try:
        while True:

            try:

                zip = shutil.make_archive(f"{PATH}FIALAND", "zip", f"{PATH}pruebas")

                file_metadata = {'name': 'FIALAND.zip',
                                 'parents': [FOLDER_ID]}

                media = MediaFileUpload(f'{PATH}FIALAND.zip',
                                        mimetype='application/zip')
                # pylint: disable=maybe-no-member
                file = service.files().update(media_body=media,
                                              fileId=FILE_ID).execute()

                now = datetime.now()
                currentTime = now.strftime("%H:%M:%S")

                print(f"\n[+] File Uploaded! at {currentTime}")
                time.sleep(600)


            except PermissionError:

                file_metadata = {'name': 'FIALAND.zip',
                                 'parents': [FOLDER_ID]}

                media = MediaFileUpload(f'{PATH}FIALAND.zip',
                                        mimetype='application/zip')
                # pylint: disable=maybe-no-member
                file = service.files().update(media_body=media,
                                              fileId=FILE_ID).execute()

                now = datetime.now()
                currentTime = now.strftime("%H:%M:%S")

                print(f"\n[+] File Uploaded! at {currentTime}")
                time.sleep(600)


    except KeyboardInterrupt:
        print("\n[!] Saliendo...\n")

