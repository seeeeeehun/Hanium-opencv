import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


def color_histogram_of_training_image(img_name):

    if 'red' in img_name:
        data_source = 'red'
    elif 'yellow' in img_name:
        data_source = 'yellow'
    elif 'green' in img_name:
        data_source = 'green'
    elif 'orange' in img_name:
        data_source = 'orange'
    elif 'white' in img_name:
        data_source = 'white'
    elif 'black' in img_name:
        data_source = 'black'
    elif 'blue' in img_name:
        data_source = 'blue'
    elif 'violet' in img_name:
        data_source = 'violet'
    elif 'brown' in img_name:
        data_source = 'brown'
    elif 'gray' in img_name:
        data_source = 'gray'
    elif 'pink' in img_name:
        data_source = 'pink'

    image = cv2.imread(img_name)
    chans = cv2.split(image)

    colors = ('b', 'g', 'r')
    features =[]
    feature_data = ''
    counter = 0

    for (chan, color) in zip(chans, colors):
        counter = counter+1
        print(counter)
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)
        element = np.argmax(hist)
        print(element)
        if counter ==1:
            blue = str(element)
        elif counter==2:
            green = str(element)
        elif counter==3:
            red = str(element)
            feature_data = red +','+ green +','+ blue

    with open('training.data','a') as myfile:
        myfile.write(feature_data+','+data_source +'\n')


def training():

    for f in os.listdir('./training_dataset/brown'):
        color_histogram_of_training_image('./training_dataset/brown/'+f)
    for f in os.listdir('./training_dataset/red'):
        color_histogram_of_training_image('./training_dataset/red/'+f)
    for f in os.listdir('./training_dataset/yellow'):
        color_histogram_of_training_image('./training_dataset/yellow/'+f)
    for f in os.listdir('./training_dataset/green'):
        color_histogram_of_training_image('./training_dataset/green/'+f)
    for f in os.listdir('./training_dataset/orange'):
        color_histogram_of_training_image('./training_dataset/orange/'+f)
    for f in os.listdir('./training_dataset/white'):
        color_histogram_of_training_image('./training_dataset/white/'+f)
    for f in os.listdir('./training_dataset/black'):
        color_histogram_of_training_image('./training_dataset/black/'+f)
    for f in os.listdir('./training_dataset/blue'):
        color_histogram_of_training_image('./training_dataset/blue/'+f)
    for f in os.listdir('./training_dataset/gray'):
        color_histogram_of_training_image('./training_dataset/gray/'+f)
    for f in os.listdir('./training_dataset/pink'):
        color_histogram_of_training_image('./training_dataset/pink/'+f)


print('training data is being created . . .')
open('training.data','w')
training()
print('training data is ready!')



