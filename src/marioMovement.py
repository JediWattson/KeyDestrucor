import numpy as np
import cv2 as cv

cascade = cv.CascadeClassifier('brains/cascade.xml')
cv.namedWindow("mario", cv.WINDOW_NORMAL)

cap = cv.VideoCapture('smworld.webm')


while (cap.isOpened()):
    
    ret,frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    marios = cascade.detectMultiScale(gray, 1.04, 10)

    for x,y,h,w in marios:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv.imshow('mario',frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()