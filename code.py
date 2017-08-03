#! C:\Users\ckr\Anaconda3\python.exe

from PIL import ImageGrab, ImageOps
import os
import time
import win32api, win32con
import numpy as np
#import cv2

"""
All coordinates assume a screen resolution of 1366x768, and the App is the left
half of the screen
x_pad = 85
y_pad = 142
Play area =  x_pad+1, y_pad+1, 595, 654
"""

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


'''
Es wird als erstes ein Screenshot gemacht
'''

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

def grid_recognition():
    img = cv2.imread(screenGrab())
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imwrite('houghlines3.jpg', img)
    print('Grid detected')


'''
if get_square_one_one() == 11404 then blue/ not known
if get_square_one_one() == 5606/5605 then white/ no bombs nearby
if get_square_one_one() == 29749 then white with 1 / 1 bomb is nearby
'''


'''
its a bit difficult, because the game has a 3D effect, thats why t x-value of
the flags are a bit lower then the number values. But, you have to click, before
a flag is set. This could be stored before processing

Flag = 22x25
2 = 15x24
'''
def get_square_one_one():
    box = (x_pad+18,y_pad+12,x_pad+40,y_pad+37)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = np.array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() +  '\\square_1_1__' + str(int(time.time())) + '.png', 'PNG')
    return a
''' funktioniert nicht'''
def get_square_one_two():
    box = (x_pad+78,y_pad+15,x_pad+93,y_pad+39)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = np.array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() +  '\\square_1_2__' + str(int(time.time())) + '.png', 'PNG')
    return a
''''''
def get_square_two_one():
    box = (x_pad+18,y_pad+69,x_pad+40,y_pad+94)
    im = ImageGrab.grab(box)
    a = np.array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() +  '\\square_2_1__' + str(int(time.time())) + '.png', 'PNG')
    return a


'''
MOUSE Movements + differnt Clicks
'''

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
'''
bezieht sich noch auf das alte Spiel
'''
class Cord:
    #how many bombs remaining
    m_Bombs = (254, 16)
    m_Smiley = (144, 16)
    bomb_field_1_1 = (15, 69)
    bomb_field_1_10 = (281, 69)
    bomb_field_10_1 = (19, 344)
    bomb_field_10_10 = (281, 344)
    background = (452, 477)




def main():
    pass

if __name__ == '__main__':
    main()
