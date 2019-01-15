#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import random
import sys


args = sys.argv
"""
import pyocr
import pyocr.builders
from PIL import Image


tools = pyocr.get_available_tools()

if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

# The tools are returned in the recommended order of usage
tool = tools[0]
#print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
#print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
#print("Will use lang '%s'" % (lang))
# Ex: Will use lang 'fra'
# Note that languages are NOT sorted in any way. Please refer
# to the system locale settings for the default language
# to use.
"""

if __name__ == '__main__':

    # 対象画像を指定
    input_image_path = args[1]

    # 画像をグレースケールで読み込み
    gray_src = cv2.imread(input_image_path, 0)
    src_size = gray_src.shape
    print(src_size)

    # 前処理（平準化フィルターを適用した場合）
    # 前処理が不要な場合は下記行をコメントアウト
    blur_src = cv2.GaussianBlur(gray_src, (5, 5), 2)
    
    #blur_src = cv2.bitwise_not(blur_src)
    
    # 二値変換
    # 前処理を使用しなかった場合は、blur_srcではなくgray_srcに書き換えるする
    mono_src = cv2.threshold(blur_src,120, 255, cv2.THRESH_BINARY_INV)[1]
    #cv2.imshow("gray",gray_src)
    # ラベリング結果書き出し用に二値画像をカラー変換
    color_src01 = cv2.cvtColor(mono_src, cv2.COLOR_GRAY2BGR)
    color_src02 = cv2.cvtColor(mono_src, cv2.COLOR_GRAY2BGR)

    # ラベリング処理
    label = cv2.connectedComponentsWithStats(mono_src)

    # オブジェクト情報を項目別に抽出
    n = label[0] - 1
    data = np.delete(label[2], 0, 0)
    center = np.delete(label[3], 0, 0)
    #x3 = (data[0][0]+data[0][2])  - data[0][0]
    #y3 = (data[0][1]+data[0][3]) - data[0][1]
    #x0_org = data[0][0]
    #y0_org = data[0][1]
    #x1_org = data[0][0] + data[0][2]
    #y1_org = data[0][1] + data[0][3]

    # オブジェクト情報を利用してラベリング結果を画面に表示
    for i in range(1):
        
        #マスク用画像を生成
        mask = np.zeros_like(gray_src)
        mask_white = np.full_like(gray_src, 255)
        
        # 各オブジェクトの外接矩形を赤枠で表示
        x0 = data[i][0]
        y0 = data[i][1]
        x1 = data[i][0] + data[i][2]
        y1 = data[i][1] + data[i][3]
        cv2.rectangle(color_src01, (x0, 0), (x1,src_size[0]), (0, 0, 255))
        cv2.rectangle(mask, (x0, 0), (x1,src_size[0]), (255, 255, 255),-1)
        cv2.rectangle(mask_white, (x0, 0), (x1,src_size[0]), (0, 0,0),-1)
        
        img_masked = cv2.bitwise_and(gray_src,gray_src,mask=mask)

        # 各オブジェクトのラベル番号と面積に黄文字で表示
        cv2.putText(color_src01, "ID: " +str(i + 1), (x1 - 20, y1 + 15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))
        cv2.putText(color_src01, "S: " +str(data[i][4]), (x1 - 20, y1 + 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))

        # 各オブジェクトの重心座標をに黄文字で表示
        cv2.putText(color_src02, "X: " + str(int(center[i][0])), (x1 - 30, y1 + 15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))
        cv2.putText(color_src02, "Y: " + str(int(center[i][1])), (x1 - 30, y1 + 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))
        
        kiritori = cv2.bitwise_or(mask_white,img_masked)
        cv2.imwrite("test.png",kiritori)
        """
        txt = tool.image_to_string(
            Image.open("test.png"),
            lang="eng",
            builder=pyocr.builders.TextBuilder(tesseract_layout=6)
        )
        print( txt )
        """

    # 結果の表示
    #kiritori = cv2.bitwise_or(mask_white,img_masked)
    cv2.imshow("abc",kiritori)
    #cv2.imwrite("test.png",kiritori)
    cv2.imshow("masked",img_masked)
    cv2.imshow("mask",mask_white)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
