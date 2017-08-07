from PIL import ImageGrab
import os
import time

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

def main():
    screenGrab()


if __name__ == '__main__':
    main()
