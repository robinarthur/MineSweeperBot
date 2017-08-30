import cv2
import numpy as np
import imutils
import pandas as pd

img = cv2.imread('full_snap.png')
"""
R: between 98 and 128
G: between 176 and 211
B: between 255

h: between 210 and 200
s: between 100 and 48
v: between 68 and 100

hsv/2 in opencv and opencv uses BGR not RGB
"""

blue_MIN = np.array([255, 176, 98])
blue_MAX = np.array([255, 211, 128])
"""
https://pythonprogramming.net/color-filter-python-opencv-tutorial/

lower_red = np.array([30,150,50])
lower_red = cv2.cvtColor(lower_red,cv2.COLOR_BGR2HSV)
upper_red = np.array([255,255,180])
upper_red = cv2.cvtColor(upper_red,cv2.COLOR_BGR2HSV)
"""

#hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

frame_threshed = cv2.inRange(img, blue_MIN, blue_MAX)
#frame_threshed2 = cv2.inRange(frame_threshed, lower_red, upper_red)
#out = cv2.cvtColor(frame_threshed,cv2.COLOR_HSV2BGR)
cv2.imshow("input", img)
#cv2.imshow("hsv_img", hsv_img)
#cv2.imshow("frame_treshed", frame_threshed)
#cv2.imshow("frame_threshed2", frame_threshed2)
#cv2.imshow('out',out)

# find contours in the thresholded image
cnts = cv2.findContours(frame_threshed.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

#print("cnts", cnts)
i = len(cnts)
print("i", i)

# we know we're gonna have x rows of data, where x is the product of
# board_width * board_height
numberOfRows = 81
# create dataframe
df = pd.DataFrame(index=np.arange(numberOfRows, 0), columns=('x', 'y'))

print("df", df)


for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	# fill the dataframe with the coords

	i-=1
	# draw the contour and the center of the shape on the image
	#cv2.drawContours(img, [c], -1, (255, 255, 255), 2)
	cv2.circle(img, (cX, cY), 1, (255, 255, 255), -1)
	#print("Durchgang: %5d ,X: %6d ,Y: %6d" (str(i),str(cX),str(cY)))

cv2.imshow("Image_with_contours",img)
print("cX", cX)
print("cY", cY)
print("i_end", i)


cv2.waitKey(0)
# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()
