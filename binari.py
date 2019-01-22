import cv2
import numpy as np
import random
import sys
args = sys.argv

input_image_path = args[1]

gray_src = cv2.imread(input_image_path, 0)
src_size = gray_src.shape
print(src_size)

mono_src = cv2.threshold(gray_src,220, 255, cv2.THRESH_BINARY)[1]

color_src = cv2.cvtColor(mono_src, cv2.COLOR_GRAY2BGR)

cv2.imwrite(args[1]+"_b.png",color_src)
