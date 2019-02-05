import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import math

#画像をリサイズする関数
def resize(img,resize_height):
    img_height,img_width = img.shape
    resize_width = resize_height / img_height * img_width
    return cv2.resize(img,(int(resize_width),int(resize_height)))

args = sys.argv
img = cv2.imread(args[1],0)
#画像をリサイズして縦の長さを合わせる
#resize_height = 50
#img = resize(img,50)

#cv2.imshow("img",img)
#cv2.waitKey()
img2 = img.copy()
#template = cv2.imread(args[2],0)
#print(args[2])
#w, h = template.shape[::-1]

tempfile = ['../match_data/plus.png', '../match_data/minus.png', '../match_data/times.png',
            '../match_data/divide.png']
#最大類似度
t_o_m = []
for temp in tempfile:
    template = cv2.imread(temp,0)
    w, h = template.shape[::-1]
    img = img2.copy()
    #method = eval("cv2.TM_CCOEFF_NORMED")

    # Apply template Matching
    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print('max value: {},min_value: {}, position: {}'.format(max_val,min_val,max_loc))

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    #if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    #    top_left = min_loc
    #else:
    #    top_left = max_loc
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 0, 2)
    t_o_m.append(max_val)
    if max(t_o_m) >= 0.999:
        print(max(t_o_m))

    #出力
    plt.subplot(221),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.subplot(223),plt.imshow(template,cmap = 'gray')
    plt.title('number_data'), plt.xticks([]), plt.yticks([])
    plt.suptitle(temp)

    plt.show()
