from PIL import ImageGrab
import os
import time

'''
Es wird als erstes ein Screenshot gemacht
'''

def screenGrab():
    box = (100,50,400,400)
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')

def main():
    screenGrab()


if __name__ == '__main__':
    main()
