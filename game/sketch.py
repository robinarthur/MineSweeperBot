
# coding: utf-8

# In[29]:


import random
import numpy as np
from p5 import *
from cell import Cell


def make2DArray(cols, rows):
    #arr = np.array([range(cols) for row in range(rows)])
    #arr = np.zeros(shape = (rows,cols))
    arr = [[0 for _i in range(cols)] for _j in range(rows)]
    return arr

#var grid
#var cols
#var rows

#w = 20 # this is now in setup()

#totalBees = 30 # this is now in setup ()

def setup():
    w = 20
    totalBees = 30
    size(401, 401)
    cols = int(width / w)
    rows = int(height / w)
    grid = make2DArray(cols, rows)
    for col in range(cols):
        for row in range(rows):
            c = Cell(col, row, w)
            grid[col][row] = c
            
    # Pick totalBees spots
    options = []
    for col in range(cols):
        for row in range(rows):
            options.append([col, row])
            
    for n in range(totalBees):
        index = random.randint(0,len(options))
        choice = options[index]
        i = choice[0]
        j = choice[1]
        # Deletes that spot so it's no longer an option
        options.remove(choice)
        grid[i][j].bee = True
    
    for col in range(cols):
        for row in range(rows):
            print("grid[col][row]", grid[col][row])
            x = grid[col][row]
            print(x
            grid[col][row].countBees()
            

def gameOver():
    for col in range(cols):
        for row in range(rows):
            grid[col][row].revealed = true
        

def mousePressed():
    for col in range(cols):
        for row in range(rows):
            if grid[col][row].contains(mouseX, mouseY):
                grid[col][row].reveal()
                
                if grid[col][row].bee:
                    gameOver()

                    
def draw():
    background(255)
    for col in range(cols):
        for row in range(rows):
            grid[col][row].show()
            
run()

