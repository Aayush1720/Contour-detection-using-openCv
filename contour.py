import cv2
import numpy as np
from numpy.core.arrayprint import _object_format


def getContours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #print(len(contours))
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area > 500:
            cv2.drawContours(imgn, cnt, -1,(255,0,0),5)
            peri = cv2.arcLength(cnt, True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            objType = "not-defined"
            cv2.rectangle(imgn,(x,y),(x+w,y+h),(0,254,0),2)
            if objCor == 3: objType = "Triangle"
            if objCor == 4: objType = "quadrilateral"
            if objCor == 6: objType = "hexagon"
            if objCor > 6: objType = "circle"
            cv2.putText(imgn,objType, (x+ w//2-10, y + h//2-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)



path = 'sh.jpg'
img = cv2.imread(path)
imgn = img.copy()
imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(img)
getContours(imgCanny)
while True:
    cv2.imshow("original",img)
    cv2.imshow("canny", imgCanny)
    cv2.imshow("cont" , imgn)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


