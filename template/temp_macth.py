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
resize_height = 50
img = resize(img,50)

#cv2.imshow("img",img)
#cv2.waitKey()
img2 = img.copy()
template = cv2.imread(args[2],0)
print(args[2])
w, h = template.shape[::-1]


# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print('max value: {},min_value: {}, position: {}'.format(max_val,min_val,max_loc))

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 0, 2)

    #出力
    plt.subplot(221),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.subplot(223),plt.imshow(template,cmap = 'gray')
    plt.title('number_data'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()
