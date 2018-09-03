import time
import cv2
import boto3
import os



cap = cv2.VideoCapture(0)
counter = 0
timestamp=''
s3 = boto3.client('s3')
while (cap.isOpened()):
    now = time.localtime()
    timestamp = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    if((counter%20)==0):
        _, frame = cap.read()

        cv2.imwrite('./test_movie/'+ timestamp +'.jpg',frame)
        s3.upload_file('./test_movie/' + timestamp + '.jpg', 'webviedo', timestamp + '.jpg')
        os.remove('./test_movie/'+ timestamp +'.jpg')

    counter = counter+1


    ch = 0xFF & cv2.waitKey(1)
    if ch == 27:
        break


cv2.destroyAllWindows()







