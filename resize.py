# resize.py
# coding:utf-8
import sys
import os
from PIL import Image

img_path = sys.argv[1]
resize_width = float(sys.argv[2])
img = Image.open(img_path)

# 画像の解像度を取得して、リサイズする高さを計算
img_width,img_height = img.size
resize_height = resize_width / img_width * img_height

# 画像をリサイズ
img = img.resize((int(resize_width),int(resize_height)))

# リサイズした画像を(ファイル名-幅-高さ.拡張子)で保存
root, ext = os.path.splitext(img_path)
resize_img_path = "".join([root,"-%s-%s" % (int(resize_width),int(resize_height)),ext])
img.save(resize_img_path)
