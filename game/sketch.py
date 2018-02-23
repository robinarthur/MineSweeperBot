
# coding: utf-8

# In[2]:


import numpy as np
from p5 import *
import cell.py


def make2DArray(cols, rows):
    arr = np.array([range(cols) for row in range(rows)])
    return arr

#var grid
#var cols
#var rows

w = 20

totalBees = 30

def setup():
    size(401, 401)
    cols = int(width / w)
    rows = int(height / w)
    grid = make2DArray(cols, rows)
    for col in range(cols):
        for row in range(rows):
            grid[col][row] = Cell(col, row, w)
            
    # Pick totalBees spots
    options = []
    for col in range(cols):
        for row in range(rows):
            options.append([col, row])
            
    
    for n in range(totalBees):
        index = int(random(len(options)))
        choice = options[index]
        i = choice[0]
        j = choice[1]
        # Deletes that spot so it's no longer an option
        options.remove(index, 1)
        grid[i][j].bee = true
    
    
    for col in range(cols):
        for row in range(rows):
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

