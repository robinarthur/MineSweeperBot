import cv2
import numpy as np
import pandas as pd
import imutils

f = 'full_snap.png'
img = cv2.imread(f)
cv2.imshow("test",img)
"""
some of my blue pixels
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
"""

# find the blue pixels and save it in frame_threshed
frame_threshed = cv2.inRange(img, blue_MIN, blue_MAX)

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

# check if the length of cnts are euqal to the number of rows/ number of tiles
# then go further

# TODO
"""
    mine_map :
        the column that defines the minearea
        0 is empty
        1 is mine
    info_map :
        the column that presents to the gamer from the Game
        0-8 is number of mines in sorrounding.
        9 is flagged field.
        10 is questioned field.
        11 is undiscovered field.
        12 is a mine field
"""
d = []
# info_map - tiles are undiscovered == 11 in the initialize routine
undiscovered = 11
# mine_map - tile are undiscovered (mine_map == empty == 0) in the initialize
# routine
no_bomb = 0
# checked - change the value to 1, to show if the tile is checked once, could be
# useless, because its the same like info_map !== 11 or so...
checked = 0
print("d", d)
print(type(d))


for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])

	# fill the data with the coords
	d.append({'tilenumber': i, 'X-Value': cX, 'Y-Value': cY,
		'info_map': undiscovered, 'mine_map': no_bomb, 'checked': checked})

	# decrease i to go backwards, because tile number 81 is the first contour
	i-=1
	# draw the center of the shape on the image
	cv2.circle(img, (cX, cY), 1, (255, 255, 255), -1)

df = pd.DataFrame(d)
df = df.set_index('tilenumber')

# only for debugging
print("x,y dataframe", df)
cv2.imshow("Image_with_contours",img)

# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()
