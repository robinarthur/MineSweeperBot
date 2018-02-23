import numpy as np
from p5 import *

class Cell:
    def __init__(self, i, j, w):
        self.i = i
        self.j = j
        self.x = i * w
        self.y = j * w
        self.w = w
        self.neighborCount = 0
    
        self.bee = False
        self.revealed = False

    def show(self):
        stroke(0)
        noFill()
        rect(self.x, self.y, self.w, self.w)
        if self.revealed:
            if self.bee:
                fill(127)
                ellipse(self.x + self.w * 0.5, self.y + self.y * 0.5, self.w * 0.5)
            else:
                fill(200)
                rect(self.x, self.y, self.w, self.w)
                if self.neighborCount > 0:
                    textAlign(CENTER)
                    fill(0)
                    text(self.neighborCount, self.x + self.w *0.5, self.y + self.w - 6)
                    
    def countBees(self):
        if self.bee:
            self.neighborCount = -1
            return
        total = 0
        for xoff in range(-1,2):
            i = self.i + xoff
            if i < 0 or i >= cols:
                pass
            for yoff in range(-1,2):
                j = self.y + yoff
                if j < 0 or j >= rows:
                    pass
                neighbor = grid[i][j]
                if neighbor.bee:
                    total =+ 1
        self.neighborCount = total
    
    def contains(self, x, y):
        return x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.w
    
    def reveal(self):
        self.revealed = True
        if self.neighborCount == 0:
            # flood fill time
            self.floodFill()
    
    def floodFill(self):
        for xoff in range(-1, 2):
            i = self.i + xoff
            if i < 0 or i >= cols:
                pass
            for yoff in range(-1, 2):
                j = self.y + yoff
                if j < 0 or j >= rows:
                    pass
                
                neighbor = grid[i][j]
