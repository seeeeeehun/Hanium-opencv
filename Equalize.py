import numpy as np
import cv2
while True:
    img = cv2.imread('pedestrian_img2_test2.png',0)
    img = cv2.resize(img, (400, 400))
    img2 = cv2.equalizeHist(img)
    #img = cv2.resize(img,(400,400))
    img2 = cv2.resize(img2,(400,400))
    img3 = cv2.imread('pedestrian_img2.png')
    dst = np.hstack((img,img2))
    cv2.imshow('img',dst)
    cv2.imshow('comparePhoto',img3)
    ch = 0xFF & cv2.waitKey(1)
    if ch == 27:
        break