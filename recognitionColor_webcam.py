import cv2
import ScriptClothes_color
import boto3
import time

#s3 = boto3.client('s3')

colors = []
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap = cv2.VideoCapture('./test_movie/test_movie_1.mp4')
ret = cap.read()

while True:
    frame = None
    if(frame == ret):
        ret = cap.read()
        continue
    else:
        ret, frame = cap.read()
        time = time.time()
        #s3.upload_file( frame, 'webviedo', '%d.jpg'%time)
        found, w = hog.detectMultiScale(frame, winStride=(8, 8), padding=(32, 32), scale=1.05)
        for (x, y, w, h) in found:
            colors = ScriptClothes_color.ScriptClothoes_img(frame, x, y, w, h )
            with open('data.data','w') as myfile:
                myfile.write('position : '+str(x))
                myfile.write(', '+str(y))
                myfile.write(', width : '+str(w))
                myfile.write(', height : '+str(h))
                myfile.write('upper_color : '+colors[0])
                myfile.write(', lower_color : '+colors[1])



    ch = 0xFF & cv2.waitKey(1)
    if ch == 27:
        break
cv2.destroyAllWindows()



