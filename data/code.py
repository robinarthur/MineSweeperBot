#!/usr/bin/python2.7

# Python 2/3 compatibility
import sys
PY3 = sys.version_info[0] == 3

if PY3:
    xrange = range
else:
    pass

from glob import glob
import os
import time
from PIL import ImageOps, ImageGrab
import win32api, win32con
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd


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



# Bubble Sorting algorithm
def sort(List):
    for i in range(len(List)):
        for j in range(len(List) - 1, i, -1):
            if List[j] < List[j - 1]:
                List[j], List[j - 1] = List[j - 1], List[j]
    return List

def sort_squares():
    for fn in glob('full_snap.png'):
        img = cv2.imread(fn)
        squares = find_squares(img) # get a list of many numpy arrays with points in it

        flat_list = [item for row in squares for item in row]

        corners_list = []

        for corner in flat_list:
            corners_list.append(corner)

        df = pd.DataFrame([], columns=list('X','Y'))
        for point in corners_list:
            x = int(point[0])
            print(x)
            y = int(point[1])
            print(y)
            df2 = pd.DataFrame([x, y], columns=list('X', 'Y'))
            df = df.apply(df2, axis = 0, ignore_index=True)


        print("df")
        print(df)
#            print(point[0])
#            print(point[1])
#            x = point[0]
#            y = point[1]
#            one_point = [x,y]
#            point_list = point_list.append(one_point)

#        print("point_list")
#        print(point_list)
        break






        squaresnp = np.array(squares)
        print("squaresnp_shape + type of squares")
        print(squaresnp.shape)
        print(type(squares))
        print("squaresnpnp_ndim + typeof squaresnp")
        print(squaresnp.ndim)
        print(type(squaresnp))
        print(squares[0])
        print(type(squares[0]))
        print(squares[1])
        print("squaresnp")
        print(squaresnp[0])
#       print("_________")
        print(squares[0][0][0])
        print(type(squares[0][0]))
        print(squares[0][1][1])
        print(type(squares[0][1][1]))
        print(squares[0][2])
        print(squares[0][3])
        a = sorted(squares, key=lambda x:len(x))
        print(a)
        # thanks to stamaimer from stackoverflow
        # https://stackoverflow.com/a/45564147/7477664
        #sorted_list = sort(squares)
        #print(sorted_list)
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

def click_field(move_x, move_y):
    """Click one grid by given position."""
    field_status = info.map[move_x, move_y]

    # can only click blank region
    """ WARNING!!! The following made no sense for the bot """
    if field_status == 11:
        if self.mine_map[move_y, move_x] == 1:
            self.info_map[move_y, move_x] = 12
        else:
            # discover the region.
            self.discover_region(move_x, move_y)

def discover_region(move_x, move_y):
    """Discover region from given location."""
    field_list = deque([move_x, move_y])

    while len(field_list) != 0:
        field = field_list.popleft()

        (tl_idx, br_idx, region_sum) = get_region(field[1], field[0])
        if region_sum == 0:
            info_map[field[0], field[1]] = region_sum
            # get surrounding to queue
            region_mat = info_map[tl_idx[0]:br_idx[0]+1,
                                  tl_idx[1]:br_idx[1]+1]
            x_list, y_list = np.nonzero(region_mat == 11)

            for x_idx, y_idx in zip(x_list, y_list):
                field_temp = (x_idx + max(field[0]-1, 0),
                              y_idx + max(field[1]-1, 0))
                if field_temp not in field_list:
                    field_list.append(field_temp)
        elif region_sum > 0:
            info_map[field[0], field[1]] = region_sum

def get_region(move_x, move_y):
    """Get region around a location."""
    top_left = (max(move_x-1, 0), max(move_y-1, 0))
    bottom_right = (min(move_y+1, board_height-1),
                    min(move_x+1, board_width-1))
    region_sum = mine_map[top_left[0]:bottom_right[0]+1,
                          top_left[1]:bottom_right[1]+1].sum()

    return top_left, bottom_right, region_sum



def isDark():
    # check if the pixel is a dark pixel -> maybe background or border linewidth
    # a java example taken from:
    #   http://luckytoilet.wordpress.com/2012/12/23/2125/
    #
    #  static boolean isDark(int rgb){
    #    int red = (rgb >> 16) & 0xFF;
    #    int green = (rgb >> 8) & 0xFF;
    #    int blue = rgb & 0xFF;
    #    return red + green + blue < 120;
    #  }
    return None

    # get the RGB Values of each Pixel and store it in a numpy Array
def getRGB(img):
    RGB = np.array(img.getcolors())
    return RGB

#TODO
#
# put the different recognitions together
# (sort_squares + canny_edge)
# ask on stackoverflow for the best "clickable" solution
#
# look into the opencv examples!
# def digits():
#
# def digits_adjust():
#
# def digits_video():
#




def canny_edge():
        # taken from:
        # https://pythonprogramming.net/canny-edge-detection-gradients-python-opencv-tutorial/
        for fn in glob('full_snap.png'):
            img = cv2.imread(fn)
            while(1):
                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

                lower_red = np.array([30,150,50])
                upper_red = np.array([255,255,180])

                mask = cv2.inRange(hsv, lower_red, upper_red)
                res = cv2.bitwise_and(img, img, mask= mask)

                laplacian = cv2.Laplacian(img, cv2.CV_64F)
                edges = cv2.Canny(img,100,200)

                cv2.imshow('Original', img)
                cv2.imshow('Edges', edges)
                cv2.imshow('Laplacian', laplacian)

                # just for debugging:
                print("Original'{0}'".format(img))
                print("edges'{0}'".format(edges))
                print("laplacian'{0}'".format(laplacian))


                k = cv2.waitKey(5) & 0xFF
                if k == 27:
                    break
            cv2.destroyAllWindows()

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

def clone_game(board_width, board_height):
    """this function clones the game and puts the information in it,
    wich already known.

    Parameters:
    -----------

    board_height : int
    board_width : int
    mine_map : numpy.ndarray
        the map that defines the minearea
        0 is empty
        1 is mine
    info_map : numpy.ndarray
        the map that presents to the gamer from the Game
        0-8 is number of mines in sorrounding.
        9 is flagged field.
        10 is questioned field.
        11 is undiscovered field.
        12 is a mine field
    """

    mine_map = np.zeros((board_height, board_width),
                        dtype = np.uint8)

    info_map = np.ones((board_height, board_width),
                       dtype = np.uint8)*11

    print("mine_map'{0}'".format(mine_map))
    print("info_map'{0}'".format(info_map))



def check_board(self):
    """Check the board status and give feedback."""
    num_mines = np.sum(info_map == 12)
    num_undiscovered = np.sum(info_map == 11)
    num_questioned = np.sum(info_map == 10)
    if num_mines > 0:
        return 0
    elif np.array_equal(info_map == 9, mine_map):
        return 1
    elif num_undiscovered > 0 or num_questioned > 0:
        return 2




def main():
    #helper()
    #img = "full_snap.png"
    #helper()
    #sort_squares()
    #square_recognition() # funktioniert aktuell nur mit python2.7
    #pass
    #read_pic()
    #corner_detection()
    #gradient()
    #canny_edge()
    clone_game(9,9)

if __name__ == '__main__':
    main()


####### doesnt work, but its too early to remove it ###
def read_pic():
    # powered by:
    # https://github.com/robinarthur/OpenCV2-Python/blob/master/OpenCV_Python_Blog/sudoku_v_0.0.6/sudoku.py
    for fn in glob('sudoku.jpg'):
        img = cv2.imread(fn)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print("gray1'{0}'".format(gray))
        gray = cv2.bilateralFilter(gray, 11, 17, 17)
        print("gray2'{0}'".format(gray))

        tresh = cv2.adaptiveThreshold(gray, 255,1,1,5,2)
        contours, hierarchy = cv2.findContours(tresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        image_area = gray.size # this is the area of the image_area

        # the following print statements are for Debugging only
        print("img'{0}'".format(img))
        print("gray'{0}'".format(gray))
        print("tresh'{0}'".format(tresh))
        print("image_area'{0}'".format(image_area))

        for i in contours:
            if cv2.contourArea(i)> image_area/2:
                # if area of box > half of image,
                # it is possibly the biggest blob
                peri = cv2.arcLength(i, True)
                approx = cv2.approxPolyDP(i, 0.02*peri, True)
                # cv2.drawContours(img,[approx],0,(0,255,0),2,cv2.CV_AA)
                break

        # the following print statements are for Debugging only
        print("peri'{0}'".format(peri))
        print("approx'{0}'".format(approx))

def corner_detection():
    # taken from:
    # https://pythonprogramming.net/corner-detection-python-opencv-tutorial/
    for fn in glob('full_snap.png'):
        img = cv2.imread(fn)
        grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = np.float32(grayimg)

        corners = cv2.goodFeaturesToTrack(gray, 40, 0.01, 400)
        corners = np.int0(corners)

        for corner in corners:
            x,y = corner.ravel()
            cv2.circle(grayimg, (x,y), 3, 255, -1)

        cv2.imshow('Corner', grayimg)
        cv2.waitKey() # this line doesn't appear in the source

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
