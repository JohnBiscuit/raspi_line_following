import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    resize = cv2.resize(frame, (300, 300))
    resize = cv2.GaussianBlur(resize,(5,5),0)
    hsv = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([255, 255, 60])
    mask = cv2.inRange(hsv, lower_black, upper_black)
    _,contour,_ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if contour:
        c = max(contour, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        
        
        x1 = int((2*x+w+1)/2)
        y1 = int((2*y+h+1)/2)
             
        cv2.circle(resize, (x1, 0), 5, (255, 0, 255), -1)
    #print(x,y,w,h,x1,y1)    
    cv2.imshow('frame', mask)
    # cv2.imshow('frame2',erosion)
    cv2.imshow('closing', resize)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()


