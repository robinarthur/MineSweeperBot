#!/usr/bin/python2.7

# Python 2/3 compatibility
import sys
PY3 = sys.version_info[0] == 3

if PY3:
    xrange = range
else:
    pass
    #from Pillow import ImageOps, ImageGrab

from glob import glob
import os
import time
#from PIL import ImageOps, ImageGrab #only on windows
#import win32api, win32con # only on windows
import numpy as np
import cv2# funktioniert gerade nur unter python2.7
import matplotlib.pyplot as plt


# --- Globals ---
# All coordinates assume a screen resolution of 1366x768, and the App is the left
# half of the screen
# x_pad = 85
# y_pad = 142
# Play area =  x_pad+1, y_pad+1, 595, 654
# ---
# Globals
#------------
x_pad = 85
y_pad = 142

# bombingfield (x = rows, y = columns)
grid_rows = {'easy':9,
             'medium':16,
             'expert':30
}

grid_columns = {'easy':9,
                'medium':16,
                'hard':16
}


# Es wird als erstes ein Screenshot gemacht
#
#

def screenGrab():
    bl = (x_pad + 1, y_pad + 1, x_pad + 432, y_pad + 356)
    im = ImageGrab.grab()

    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', 'PNG')
    #return im

def Grab():
    box = (x_pad + 1, y_pad + 1, x_pad + 595, y_pad + 654)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = np.array(im.getcolors())
    a = a.sum()
    print(a)
    return a

def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def find_squares(img):
    img = cv2.GaussianBlur(img, (5, 5), 0)
    squares = []
    for gray in cv2.split(img):
        for thrs in xrange(0, 255, 26):
            if thrs == 0:
                bin = cv2.Canny(gray, 0, 50, apertureSize=5)
                bin = cv2.dilate(bin, None)
            else:
                retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)
            bin, contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                cnt_len = cv2.arcLength(cnt, True)
                cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
                if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
                    cnt = cnt.reshape(-1, 2)
                    max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
                    if max_cos < 0.1:
                        squares.append(cnt)
    return squares

def square_recognition():
    for fn in glob('full_snap.png'):
        img = cv2.imread(fn)
        squares = find_squares(img)
        cv2.drawContours( img, squares, -1, (0, 255, 255), 1 )
        cv2.imshow('squares', img)
        ch = cv2.waitKey()
        if ch == 27:
            break
    cv2.destroyAllWindows()

def sort_squares():
    for fn in glob('full_snap.png'):
        img = cv2.imread(fn)
        squares = find_squares(img)
        squaresnp = np.array(squares)
        print("squaresnp_shape")
        print(squaresnp.shape)
        print("squaresnpnp_ndim")
        print(squaresnp.ndim)
#        print(squares[0])
#        print(squares[1])
#        print("squaresnp")
#        print(squaresnp[0])
#        print("_________")
#        print(squares[0][0][0])
#        print(squares[0][1][1])
#        print(squares[0][2])
#        print(squares[0][3])
        # thanks to stamaimer from stackoverflow
        # https://stackoverflow.com/a/45564147/7477664

        flat_list = [item for row in squares for item in row]
        flat_list_np = np.array(flat_list)
        print("flat_list_np_shape")
        print(flat_list_np.shape)
        print("flat_list_np_ndim")
        print(flat_list_np.ndim)
#        print(flat_list[0])
#        print(flat_list[1])
#        print(flat_list[2])
#        print(flat_list[3])
#        print(flat_list[4])
#        print(flat_list[5])
#           plot of the points to see whats really inside

        x, y = flat_list_np.T
        plt.scatter(x,y,alpha = 0.5)
        #plt.xticks([]), plt.yticks([])# to hide tick values on X and Y axis
        plt.savefig('plot.png')
        plt.show()

        print("flat_list_np")
        print(flat_list_np)
        print("flat_list_sorted")
        flat_list_sorted = flat_list_np.sort()

        # If you want to reshape the 1d list with shape(1, 81, 2) to 2d list with shape(9, 9, 2)
        result = []
        temp = []
        count = 0

        for item in flat_list:
            temp.append(item)
            count += 1
            if count % 4 == 0:
                result.append(temp)
                temp = []
                count = 0

        # You also can use numpy to reshape flat_list to (9, 9, 2)

        result = np.array(flat_list).reshape(9, 9, 2)
        print("result" % result)
#
# its a bit difficult, because the game has a 3D effect, thats why the x-value of
# the flags are a bit lower then the number values. But, you have to click, before
# a flag is set. This could be stored before processing
#
# Flag = 22x25
# 2 = 15x24
#



# MOUSE Movements + differnt Clicks
# TO-DO: retype it with PyAutoGUI
#

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print('left Click')    #completly optional. But nice for debugging purposes.

def rightClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    print('right Click')

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print('left Down')

def rightDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(.1)
    print('right Down')

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('left release')

def rightUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    print('right release')

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x,y)

def startGame():
    #location of the dificulty level easy
    mousePos((103,212))
    leftClick()
    time.sleep(.1)

def helper():
    for fn1 in glob('full_snap.png'):
        for fn2 in glob('plot.png'):
# https://pythonprogramming.net/image-arithmetics-logic-python-opencv-tutorial/?completed=/image-operations-python-opencv-tutorial/
            # Load two images
            img1 = cv2.imread(fn1,cv2.IMREAD_GRAYSCALE)
            img2 = cv2.imread(fn2)

            # I want to put the second img on top-left corner,
            # So I create a ROI - Region of Image
            rows, cols, channels = img2.shape
            roi = img1[0:rows, 0:cols]

            # Now create a mask of img1 and create its inverse mask
            img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

            # add a threshold
            ret, mask = cv2.threshold(img2gray, 220, 255, cv2.TRESH_BINARY_INV)

            mask_inv = cv2.bitwise_not(mask)

            # Now black-out the area of img2 in ROI
            img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

            #take only region of logo from logo image
            img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

            dat = cv2.add(img1_bg,img2_fg)
            img1[0:rows, 0:cols] = dst

            cv2.imshow('res', img1)
            cv2.waitKey(0)
            cv2.destroyAllWindows()





            plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
            plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
            plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
            plt.show()
            #cv2.imwrite('watchgray.png',img)










def main():
    #helper()
    #img = "full_snap.png"
    helper()
    #sort_squares()
    #square_recognition() # funktioniert aktuell nur mit python2.7
    #pass

if __name__ == '__main__':
    main()
