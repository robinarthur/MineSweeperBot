from p5 import *
from game import Cell
from cell import grid, rows
import random



def make2DArray(cols, rows):
    #arr = np.array([range(cols) for row in range(rows)])
    #arr = np.zeros(shape = (rows,cols))
    arr = [[0 for _i in range(cols)] for _j in range(rows)]
    return arr




def setup():
    global w
    global totalMines
    global grid
    global rows
    global cols
    
    w = 20
    totalMines = 30
    width = 401
    height = 401
    size(width+100,height+100)
    
    cols = int(width / w)
    rows = int(height / w)
    
    grid = make2DArray(cols, rows)
    
    # fill every "cell" with a cell object
    for col in range(len(grid)):
        for row in range(len(grid[0])):
            grid[col][row] = Cell(col, row, w)
    
    
    # Pick totalMines spots
    options = []
    for i in range(cols):
        for j in range(rows):
            options.append([i, j])
            
    
    for n in range(totalMines):
        index = int(random.randint(0, len(options)))
        i = choice[0]
        j = choice[1]
        # Delete that spot so its no longer an option
        options.remove(choice)
        grid[i][j] = True
        
        
    for i in range(cols):
        for j in range(rows):
            grid[i][j].countMines()
       
    
def draw():
    background(255)
    
    for i in range(cols):
        for j in range(rows):
            grid[i][j].show()


def gameOver():
    pass

    
    
    
    
    ###### to be continued here

def mousePressed():
    pass



class Cell:
    def __init__(self, i, j, w):
        self.__i = i
        self.__j = j
        self.__x = i * w
        self.__y = j * w
        self.__w = w
        self.__neighborCount = 0
        
        self.__mine = False
        self.__revealed = False
        
    def show(self):
        stroke(0)
        noFill()
        rect(self.__x, self.__Y, self.__w, self.__w)
        if self.__revealed:
            if self.__mine:
                fill(127)
                ellipse(self.__x + self.__w * 0.5, self.__y + self.__y * 0.5, self.__w * 0.5)
                pass
            else:
                fill(200)
                rect(self.__x, self.__y, self.__w, self.__w)
                if self.__neighborCount > 0:
                    textAlign(CENTER)
                    fill(0)
                    text(self.__neighborCount, self.__x + self.__w *0.5, self.__y + self.__w - 6)
                    pass

    
    
run()