
# coding: utf-8

# In[1]:


import numpy as np
from p5 import *
#from sketch import *

class Cell(object):
    def __init__(self, i, j, w):
        self.__i = i
        self.__j = j
        self.__x = i * w
        self.__y = j * w
        self.__w = w
        self.__neighborCount = 0
    
        self.__bee = False
        self.__revealed = False
        

    def show(self):
        stroke(0)
        noFill()
        rect(self.__x, self.__y, self.__w, self.__w)
        if self.__revealed:
            if self.__bee:
                fill(127)
                ellipse(self.__x + self.__w * 0.5, self.__y + self.__y * 0.5, self.__w * 0.5)
            else:
                fill(200)
                rect(self.__x, self.__y, self.__w, self.__w)
                if self.__neighborCount > 0:
                    textAlign(CENTER)
                    fill(0)
                    text(self.__neighborCount, self.__x + self.__w *0.5, self.__y + self.__w - 6)
                    
    def countBees(self):
        if self.__bee:
            self.__neighborCount = -1
            return
        
        total = 0
        for xoff in range(-1,2):
            i = self.__i + xoff
            if i < 0 or i >= cols:
                pass
            for yoff in range(-1,2):
                j = self.__y + yoff
                if j < 0 or j >= rows:
                    pass
                neighbor = grid[i][j]
                if neighbor.__bee:
                    total =+ 1
        self.__neighborCount = total
    
    def contains(self, x, y):
        return x > self.__x and x < self.__x + self.__w and y > self.__y and y < self.__y + self.__w
    
    def reveal(self):
        self.__revealed = True
        if self.__neighborCount == 0:
            # flood fill time
            self.floodFill()
    
    def floodFill(self):
        for xoff in range(-1, 2):
            i = self.__i + xoff
            if i < 0 or i >= cols:
                pass
            for yoff in range(-1, 2):
                j = self.__y + yoff
                if j < 0 or j >= rows:
                    pass
                
                neighbor = grid[i][j]

        

        
        
        
        


# In[19]:


cols = 10
rows = 10
w = 40
# function to print the grid row-wise
def p(o):
    for index, i in enumerate(o):
        print(o[index])
    print("")

# make an empty grid with zeros
grid = [[0 for x in range(cols)] for y in range(rows)]
p(grid)
# fill every element of the grid with a cell object
for col in range(cols):
    for row in range(rows):
        c = Cell(col, row, w)
        grid[col][row] = c    

        
p(grid)


# In[20]:


t = grid[5][5]
print(t.reveal)

