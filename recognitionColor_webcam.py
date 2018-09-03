import cv2
import ScriptClothes_color
import boto3
import time


colors = []
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap = cv2.VideoCapture(0)#람다에 함수들을 올렸을때 s3에서 바로 사진 받는걸로 바꿈


while True:

    ret, frame = cap.read()
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



