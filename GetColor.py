import cv2
import numpy as np



def GetColor(source_img):

    chans = cv2.split(source_img)
    colors = ('b', 'g', 'r')
    features = []
    feature_data = ''
    counter = 1
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        elem = np.argmax(hist)

        if counter == 1:
            blue = str(elem)
            print(blue)
        elif counter == 2:
            green = str(elem)
            print(green)
        elif counter == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue
            print('red '+red)
            print(feature_data)
        counter = counter + 1

    with open('test.data', 'w') as myfile:
        myfile.write(feature_data)


#cap = cv2.imread('./training_dataset/pink/pink2.jpg')
#cap2 = cv2.imread('upper_script.png')
#GetColor(cap2)








