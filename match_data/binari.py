import cv2
import numpy as np
import sys
import os

args = sys.argv

img_path = args[1]

gray_src = cv2.imread(img_path, 0)
#src_size = gray_src.shape
#print(src_size)

mono_src = cv2.threshold(gray_src,30, 255, cv2.THRESH_OTSU)[1]

color_src = cv2.cvtColor(mono_src, cv2.COLOR_GRAY2BGR)

root, ext = os.path.splitext(img_path)
rename_img_path = "".join([root,"b",ext])
cv2.imwrite(rename_img_path,color_src)
