import cv2
import GetColor
import KNNclassifier as KNN


def ScriptClothoes_img(img,x,y,w,h):

        pad_w, pad_h = int(0.4 * w), int(0.1 * h)
        cv2.rectangle(img, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 0, 255), 2)
        #cv2.putText(img, 'person%d' %n, (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

        co_w = int(w / 5)
        co_h = int(h / 16)
        #print(x, y, w, h)

        img_upper = img[(y + 6 * co_h):(y + 7 * co_h), (x + 2 * co_w):(x + 3 * co_w)]
        #cv2.rectangle(img, (x + 2 * co_w, y + 6 * co_h), (x + 3 * co_w, y + 7 * co_h), (255, 0, 0), 2)
        cv2.imwrite('upper_script.png',img_upper)
        GetColor.GetColor(img_upper)
        upper_color = KNN.main('training.data', 'test.data')
        print('upper_clothes_color is ' + upper_color + '\n')

        img_lower = img[(y + 9 * co_h):(y + 10 * co_h), (x + 2 * co_w):(x + 3 * co_w)]
        #cv2.rectangle(img, (x + 2 * co_w, y + 9 * co_h), (x + 3 * co_w, y + 10 * co_h), (0, 255, 0), 2)
        cv2.imwrite('lower_script.png', img_lower)
        GetColor.GetColor(img_lower)
        lower_color = KNN.main('training.data', 'test.data')
        print('lower_clothes_color is ' + lower_color + '\n')

        return upper_color, lower_color


#cap = cv2.imread('fullbody.jpg')
#ScriptClothoes_img(cap)










