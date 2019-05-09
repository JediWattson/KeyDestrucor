import numpy as np
import cv2 as cv

cascade = cv.CascadeClassifier('../teachey/output/cascade.xml')
cap = cv.VideoCapture('smworld.webm')

last = (0,0,0,0)
skip = 0

while (cap.isOpened()):
    
    ret,frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    marios = cascade.detectMultiScale(gray, 1.04, 10)

    for x,y,h,w in marios:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv.imshow('frame',frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()