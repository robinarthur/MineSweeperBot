# import the necessary packages
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
"""This function is actually a test for my dtection section to get the right
coordinates from my detected rectangles, to give them to my click function
taken from: http://www.pyimagesearch.com/2015/09/21/opencv-track-object-movement/
"""

#construct the argument parse and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
                help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=32,
                help="max buffer size")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the "green"
# ball in the HSV color space
# for my grid i need the boundaries for the color blue

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
blueLower1 = (25, 50, 50) # i have to test wich blud fits better
blueUpper1 = (32, 255, 255)
blueLower2 = (100, 150, 0)
blueUpper2 = (140, 255, 255)

# initialize the list of tracked points, the frame counter.
# and the coordinate deltas
pts = deque(maxlen=args["buffer"])
counter = 0
(dX, dY) = (0, 0)
direction = ""

# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
    camer = cv2.VideoCapture(0)

# otherwise, grab a referance to the video file
else:
    camera = cv2.VideoCapture(args["video"])
