import cv2
import ScriptClothes_color

colors = []
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap = cv2.imread('fullbody.jpg')

found, w = hog.detectMultiScale(cap, winStride=(8, 8), padding=(32, 32), scale=1.05)
for (x, y, w, h) in found:
    colors = ScriptClothes_color.ScriptClothoes_img(cap, x, y, w, h )
    with open('data.data','w') as myfile:
        myfile.write('position : '+str(x))
        myfile.write(', '+str(y))
        myfile.write(', width : '+str(w))
        myfile.write(', height : '+str(h))
        myfile.write('upper_color : '+colors[0])