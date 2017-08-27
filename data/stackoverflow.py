"""this is the next approach with the help of stackoverflow
https://stackoverflow.com/questions/45860131/opencv-python-how-can-i-get-the-coordinates-of-detected-areas-after-image-proc
1. treshold the blue - check, maybe improve the blue range
http://www.geeksforgeeks.org/detection-specific-colorblue-using-opencv-python/
2. found contour in the range of blue - contour_img, the contours are in contour
http://docs.opencv.org/3.2.0/d4/d73/tutorial_py_contours_begin.html
3. found thier centers
4. They were all separated by some 55-57 pixels (both x,y coordinates). Rest is simple.

for i in range(len(coords)):
np_arr[int(coords[i][1]/57)][int(coords[i][0]/57)]=0

The blue tile coordinates are stored in coords, np_arr is my array.
"""
import numpy as np
import cv2
import imutils
import pandas as pd

initial = np.arange(81).reshape(9, 9)
print("initial_array"'{0}'.format(initial))

img = cv2.imread("full_snap.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# https://stackoverflow.com/questions/23811638/convert-hsv-to-grayscale-in-opencv
# https://stackoverflow.com/questions/34712144/merge-hsv-channels-under-opencv-3-in-python
h, s, v = cv2.split(hsv)# gray is in the v-channel
lower_red = np.array([100,80,50])
upper_red = np.array([130,255,255])

# Here we are defining range of bluecolor in HSV
# This creates a mask of blue coloured
# objects found in the frame.
mask = cv2.inRange(hsv, lower_red, upper_red)

# The bitwise and of the frame and mask is done so
# that only the blue coloured objects are highlighted
# and stored in res
res = cv2.bitwise_and(img,img, mask= mask)
cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
# This displays the frame, mask
# and res which we created in 3 separate windows.

im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contour_img = cv2.drawContours(img, contours, -1, (255,255,255), -1)
cv2.imshow('contour_img', contour_img)

# find contours in the thresholded image
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

"""
print("cnts'{0}'".format(cnts))
i = 0
# loop over the contours
for c in cnts:
    # compute the center of the contour
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    i=+1
    # draw the contour and center of the shape on the image
    cv2.drawContours(contour_img, [c], -1, (0, 255, 0), 2)
    cv2.circle(contour_img, (cX, cY), 7, (255, 255, 255), -1)
    print("Durchgang: %5d ,X: %6d ,Y: %6d" (i,cX,cY)

	cv2.imshow("Image", contour_img)
    cv2.waitKey(0)
"""
# loop over the contours
for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])

	# draw the contour and center of the shape on the image
	cv2.drawContours(contour_img, [c], -1, (0, 255, 0), 2)
	cv2.circle(contour_img, (cX, cY), 7, (255, 255, 255), -1)

	# show the image
	cv2.imshow("Image", contour_img)
	cv2.waitKey(0)


# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()
