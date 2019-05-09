#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:39:06 2019

@author: jediwattson
"""
import cv2

window_name = "hello"
img = cv2.imread('mario.png')

def hessianThreshold(val):
    
    surf = cv2.xfeatures2d.SURF_create(val)
    surf.setUpright(True)
    kp, des = surf.detectAndCompute(img, None)
    img2 = img
    cv2.drawKeypoints(img,kp,img2,(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG)
    cv2.imshow(window_name, img2)

hessianThreshold(4100)

cv2.waitKey(0)
cv2.destroyAllWindows()

