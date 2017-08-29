import cv2
import numpy as np

img = cv2.imread('full_snap.png')

blue_MIN = np.array([80, 50, 83])
blue_MAX = np.array([105, 61, 100])
"""
https://pythonprogramming.net/color-filter-python-opencv-tutorial/
"""
lower_red = np.array([30,150,50])
lower_red = cv2.cvtColor(lower_red,cv2.COLOR_BGR2HSV)
upper_red = np.array([255,255,180])
upper_red = cv2.cvtColor(upper_red,cv2.COLOR_BGR2HSV)

hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

frame_threshed = cv2.inRange(hsv_img, blue_MIN, blue_MAX)
frame_threshed2 = cv2.inRange(frame_threshed, lower_red, upper_red)
#out = cv2.cvtColor(frame_threshed,cv2.COLOR_HSV2BGR)
cv2.imshow("input", img)
cv2.imshow("hsv_img", hsv_img)
cv2.imshow("frame_treshed", frame_threshed)
cv2.imshow("frame_threshed2", frame_threshed2)
#cv2.imshow('out',out)


cv2.waitKey(0)
# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()
