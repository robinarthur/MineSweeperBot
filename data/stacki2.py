import cv2
import numpy as np

img = cv2.imread('full_snap.png')

blue_MIN = np.array([95, 50, 83],np.uint8)
blue_MAX = np.array([105, 61, 100],np.uint8)

hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

frame_threshed = cv2.inRange(hsv_img, blue_MIN, blue_MAX)
cv2.imshow('output2.jpg', frame_threshed)


cv2.waitKey(0)
# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()
