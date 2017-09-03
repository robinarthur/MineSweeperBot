import autopy
import opencv

ay = autopy
width, height = ay.screen.get_size()
img = ay.bitmap.capture_screen().save('screengrab.png')

print(width,height)
print(width)
print(height)

blue_MIN = np.array([255, 176, 98])
blue_MAX = np.array([255, 211, 128])

for w_pixel in width:
    for h_pixel in height:
        pass

"""
https://stackoverflow.com/questions/3586046/fastest-way-to-take-a-screenshot-with-python-on-windows?rq=1

"""
import win32gui
import win32ui

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
