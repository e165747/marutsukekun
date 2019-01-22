import sys
import os
import cv2
args = sys.argv

img_path = sys.argv[1]
resize_height = float(sys.argv[2])
img = cv2.imread(img_path)

# 画像の解像度を取得して、リサイズする高さを計算
img_height,img_width,_ = img.shape
resize_width = resize_height / img_height * img_width

# 画像をリサイズ
img = cv2.resize(img,(int(resize_width),int(resize_height)))

# リサイズした画像を(ファイル名-幅-高さ.拡張子)で保存
root, ext = os.path.splitext(img_path)
resize_img_path = "".join([root,"-%s-%s" % (int(resize_width),int(resize_height)),ext])
cv2.imwrite(resize_img_path,img)
