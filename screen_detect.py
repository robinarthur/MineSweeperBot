"""

wird wohl nicht mehr gebraucht

"""

import autopy
import cv2
import numpy as np

ay = autopy
width, height = ay.screen.get_size()
img = ay.bitmap.capture_screen().save('screengrab.png')

print(width,height)
print(width)
print(height)

blue_MIN = np.array([255, 176, 98])
blue_MAX = np.array([255, 211, 128])
"""
for w_pixel in width:
    for h_pixel in height:
        pass


https://stackoverflow.com/questions/3586046/fastest-way-to-take-a-screenshot-with-python-on-windows?rq=1


import win32gui
import win32ui
windowname = "Microsoft Minesweeper"
hwnd = win32gui.FindWindow(None, windowname)
wDC = win32gui.GetWindowDC(hwnd)
dcObj=win32ui.CreateDCFromHandle(wDC)
cDC=dcObj.CreateCompatibleDC()
dataBitMap = win32ui.CreateBitmap()
dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
cDC.SelectObject(dataBitMap)
cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
# Free Resources
dcObj.DeleteDC()
cDC.DeleteDC()
win32gui.ReleaseDC(hwnd, wDC)
win32gui.DeleteObject(dataBitMap.GetHandle())
"""

import win32gui, win32ui, win32con
from PIL import Image



win_name='Microsoft Minesweeper'
class_name= "ApplicationFrameTitleBarWindow"
bmpfilenamename='1.bmp'
hWnd = win32gui.FindWindow(None, win_name)
print("hWnd", hWnd)
windowcor = win32gui.GetWindowRect(hWnd)
print("windowcor", windowcor)
w=windowcor[2]-windowcor[0]
h=windowcor[3]-windowcor[1]
wDC = win32gui.GetWindowDC(hWnd)
print("wDC", wDC)
dcObj=win32ui.CreateDCFromHandle(wDC)
cDC=dcObj.CreateCompatibleDC()
dataBitMap = win32ui.CreateBitmap()
dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
cDC.SelectObject(dataBitMap)
cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
bmpinfo = dataBitMap.GetInfo()
bmpstr = dataBitMap.GetBitmapBits(True)
im = Image.frombuffer(
    'RGB',
    (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
    bmpstr, 'raw', 'BGRX', 0, 1)


#dcObj.DeleteDC()
#cDC.DeleteDC()
#win32gui.ReleaseDC(hWnd, wDC)

#im=Image.open(bmpfilenamename)
im.load()
