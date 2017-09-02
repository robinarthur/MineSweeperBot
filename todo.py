""" This file is my actual TODO list...
"""


"""
f_clickable
    check if the given tile id have 'the number to click'

f_cvt_tilenumber2info_map(tilenumber)

"""

def is_clickable(tilenumber):
    i,j = cvt_tilenumber2info_map(tilenumber)
    if info_map[i][j] == 11:
        return True
    else:
        return False

def cvt_tilenumber2info_map(tilenumber):
    pass


"""
screen_detect.py
-------
get screenshots:
1. - the hole screen
2. - only one tile
