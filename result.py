import cv2
import numpy as np

#######   training part    ###############
samples = np.loadtxt('generalsamples.data',np.float32)
responses = np.loadtxt('generalresponses.data',np.float32)
responses = responses.reshape((responses.size,1))

model = cv2.ml.KNearest_create()
model.train(samples,cv2.ml.ROW_SAMPLE,responses)

############################# testing part  #########################

im = cv2.imread('problem/ta14.png')
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
            siki.append([x,string])
            siki.sort(key=lambda x:(x[0],x[1]))

l=len(siki)
ko=1
x=siki[0][0]
for i in range(l):
    if 0<siki[i]-x<50 and ko==1:
        one=siki[i-1][1]+siki[i][1]
    elif x-siki[i]>abs(50) and ko==1:
        ko=2
        x=siki[i][0]
    elif siki[i]-x<50 and ko==2:
        two=siki[i-1][1]+siki[i][1]
print(siki)
cv2.imshow('im',im)
cv2.imshow('out',out)
cv2.waitKey(0)
