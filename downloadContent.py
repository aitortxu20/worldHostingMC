from googleapiclient.http import MediaIoBaseDownload
from quickstart import FILE_ID, PATH
import io
import os
import zipfile

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

    with zipfile.ZipFile(PATH + "FIALAND.ZIP", 'r') as zip_ref:
        zip_ref.extractall(PATH + "FIALAND")

    os.remove(PATH + "FIALAND.zip")