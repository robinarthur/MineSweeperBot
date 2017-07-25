#! C:\Users\tank\Anaconda3\python.exe

from PIL import ImageGrab, ImageOps
import os
import time
import win32api, win32con
import numpy

"""
All coordinates assume a screen resolution of 1366x768, and the App is "minimized"
to the top left corner.
x_pad = 99
y_pad = 49
Play area =  x_pad+1, y_pad+1, 301, 351
"""

# Globals
#------------
x_pad = 99
y_pad = 49

# bombingfield (x = rows, y = columns)
grid_rows = {'easy':10,
             'medium':10,
             'hard':10
}

grid_columns = {'easy':10,
                'medium':20,
                'hard':30
}

# pixel of the numbers to detect one pixel every number have
number_rows = {'1':11,
               '2':11,
               '3':,
               '4':,
               '5':
}

number_columns = {'1':17,
                  '2':17,
                  '3':,
                  '4':,
                  '5':



}

'''
Es wird als erstes ein Screenshot gemacht
'''

def screenGrab():
    bl = (x_pad + 1, y_pad + 1, x_pad + 301, y_pad + 351)
    im = ImageGrab.grab()

    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', 'PNG')
    return im


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print( "Click")    #completly optional. But nice for debugging purposes.

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print('left Down')

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('left release')

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x,y)

def startGame():
    #location of the dificulty level easy
    mousePos((112,96))
    leftClick()
    time.sleep(.1)
'''
    #location of dificulty level medium
    mousePos((121,115))
    leftClick()
    time.sleep(.1)

    #location of dificulty level hard
    mousePos((107,137))
    leftClick()
    time.sleep(.1)
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
