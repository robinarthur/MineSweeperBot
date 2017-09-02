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
