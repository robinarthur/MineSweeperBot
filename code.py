#! C:\Users\tank\Anaconda3\python.exe

from PIL import ImageGrab
import os
import time
import win32api, win32con

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


'''
Es wird als erstes ein Screenshot gemacht
'''

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+301, y_pad+351)
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')

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

def main():
    pass

if __name__ == '__main__':
    main()
