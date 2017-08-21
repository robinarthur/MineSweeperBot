"""
This file contains some functions from Adrianus Kleemans:
https://github.com/robinarthur/bejeweled-bot

"""

import autopy as ap
import Quartz.CoreGraphics as CG
import struct
import pygame
import time
import sys

### Constans - dont know if i use this for my bot... ###
SLEEPING_TIME = 0.02
MAX_MOVES = 5
DRAW_CANVAS = False
MAX_TIME = 75

### input helpers ###

def left_down():
    pass

def left_up():
    pass

def move_mouse(x, y):
    pass

def click(x, y):
    pass
    
def move_fields(x0, y0, x1, y1):
    global moves

### screen helpers ###

def capture():
    global screenshot_width
    global screenshot_data
    region = CG.CGRectInfinite
    # Create screenshot as CGImage
