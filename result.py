import cv2
import numpy as np
import sys

args = sys.argv
#######   training part    ###############
samples = np.loadtxt('generalsamples.data',np.float32)
responses = np.loadtxt('generalresponses.data',np.float32)
responses = responses.reshape((responses.size,1))

model = cv2.ml.KNearest_create()
model.train(samples,cv2.ml.ROW_SAMPLE,responses)

############################# testing part  #########################

im = cv2.imread('problem/ta4.png')
out = np.zeros(im.shape,np.uint8)
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)

#輪郭抽出
image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

siki=[]
one = 0
two = 0

for cnt in contours:
    #輪郭の囲む面積
    if cv2.contourArea(cnt)>40:
        [x,y,w,h] = cv2.boundingRect(cnt)
        if  h>52:
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
            roi = thresh[y:y+h,x:x+w]
            roismall = cv2.resize(roi,(10,10))
            roismall = roismall.reshape((1,100))
            roismall = np.float32(roismall)
            retval, results, neigh_resp, dists = model.findNearest(roismall, k = 1)
            string = str(int((results[0][0])))
            cv2.putText(out,string,(x,y+h),0,1,(0,255,0))

            #配列に突っ込む

            #siki.insert(0,int(string))
            siki.append([x,string])
            siki.sort(key=lambda x:(x[0],x[1]))

result = []
x_place =  siki[0][0]
x_str = siki[0][1]


#数字をまとめる
for n in siki[1:]:
    if abs(x_place - n[0]) <= 50:
        x_str += n[1]
        print("if")
    else:
        result.append(x_str)
        x_str = n[1]
        print("else")
    x_place = n[0]

result.append(x_str)
print(result)
#print(siki)
cv2.imshow('im',im)
cv2.imshow('out',out)
cv2.waitKey(0)
