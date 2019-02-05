import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import math

args = sys.argv
img = cv2.imread(args[1],0)
img2 = img.copy()

#マッチングさせる記号ファイルがある場所
tempfile = ['../match_data/plus.png', '../match_data/minus.png', '../match_data/times.png',
            '../match_data/divide.png']
#出力させる記号の配列
sign = ["+","-","*","/"]
max_sign = 0
#最大類似度の場所
place = 0
#最大類似度
t_o_m = [0]
for temp in tempfile:
    template = cv2.imread(temp,0)
    w, h = template.shape[::-1]
    img = img2.copy()
    #method = eval("cv2.TM_CCOEFF_NORMED")

    # Apply template Matching
    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print('max value: {},min_value: {}, position: {}'.format(max_val,min_val,max_loc))

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 0, 2)

    #類似度を元に文字を判定
    if max_val >= max(t_o_m) and max_val >= 0.8:
        place = tempfile.index(temp)
        print(tempfile.index(temp))
        max_sign = sign[place]

    t_o_m.append(max_val)
    print(max_sign)
    #出力
    plt.subplot(221),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.subplot(223),plt.imshow(template,cmap = 'gray')
    plt.title('number_data'), plt.xticks([]), plt.yticks([])
    plt.suptitle(temp)

    plt.show()
