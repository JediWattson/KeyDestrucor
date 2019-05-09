"""
    I pretty much copied this from the git
    https://github.com/opencv/opencv/blob/master/samples/python/tutorial_code/ImgTrans/canny_detector/CannyDetector_Demo.py

"""

from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse

max_lowThreshold = 130
window_name = 'Edge Map'
title_trackbar = 'Min Threshold:'
ratio = 3
kernel_size = 7

def CannyThreshold(val):
    low_threshold = val
    img_blur = cv.blur(src_mask, (3,3))
    detected_edges = cv.Canny(img_blur, low_threshold, low_threshold*ratio, kernel_size)
    mask = detected_edges != 0
    dst = src * (mask[:,:,None].astype(src.dtype))
    cv.imshow(window_name, dst)

parser = argparse.ArgumentParser(description='Code for Canny Edge Detector tutorial.')
parser.add_argument('--input', help='Path to input image.', default='fruits.jpg')
args = parser.parse_args()

src = cv.imread(args.input)
if src is None:
    print('Could not open or find the image: ', args.input)
    exit(0)

# Convert BGR to HSV
hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
src_mask = cv.bitwise_and(src,src, mask= mask)

cv.imshow("hello", mask)

cv.namedWindow(window_name)
cv.createTrackbar(title_trackbar, window_name , 0, max_lowThreshold, CannyThreshold)

CannyThreshold(0)
cv.waitKey(0)