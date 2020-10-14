import cv2
import dropbox
import time
import random

start_time = time.time()

def TakeSnapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("Snapshot Taken!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def UploadFile(img_name):
    access_token = "Wsxy7icwLkIAAAAAAAAAAciwAZbWtY_SuyF1g5aIepgzk_-wYhwksHv5bc9_NSY5"
    file = img_name
    file_from = file
    file_to = "/Security/" + (img_name)
    dbx = dropbox.Dropbox(access_token)
    with (file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("Files Uploaded!")

def main():
    while (True):
        if ((time.time()-start_time) >=3 ):
            name = TakeSnapshot()
            UploadFile(name)

main()