from p5 import *
import random, pygame


def make2DArray(boardwidth, boardheight):
    #arr = np.array([range(boardwidth) for row in range(boardheight)])
    #arr = np.zeros(shape = (boardheight,boardwidth))
    arr = [[0 for _i in range(boardwidth)] for _j in range(boardheight)]
    return arr


def setup():
    global cellsize
    global totalMines
    global grid
    global boardheight
    global boardwidth
    global boardrects
    global windowheight
    global windowwidth
    
    cellsize = 20
    totalMines = 30
    windowwidth = 600
    windowheight = 600
    
    size(windowwidth, windowheight)
    
    boardwidth = int(windowwidth // cellsize)
    boardheight = int(windowheight // cellsize)
    
    xmargin = int((windowwidth - cellsize * boardwidth) / 2)
    ymargin = int((windowwidth - cellsize * boardheight) / 2)
    
    #grid = make2DArray(boardwidth, boardheight)
    
    # fill every "cell" with a cell object
    #for col in range(len(grid)):
    #    for row in range(len(grid[0])):
    #        grid[col][row] = Cell(col, row, cellsize)
    # Create pygame.Rect objects for each board space to
    # do board-coordinate-to-pixel-coordinate conversions.
    grid = []
    for x in range(boardwidth):
        grid.append([])
        for y in range(boardheight):
            r = pygame.Rect((xmargin + (x*cellsize),
                             ymargin + (y*cellsize),
                             cellsize,
                             cellsize))
            grid[x].append(r)
    
    
    
    
    # Pick totalMines spots
    options = []
    for i in range(boardwidth):
        for j in range(boardheight):
            options.append([i, j])
            
    
    for n in range(totalMines):
        index = int(random.randint(1, len(options)+1))
        print("index", index)
        choice = options[index]
        print("choice", choice)
        print("index", index)
        
        i = choice[0]
        j = choice[1]
        # Delete that spot so its no longer an option
        options.remove(choice)
        grid[i][j].__mine = True
        
    for i in range(boardwidth):
        for j in range(boardheight):
            c = grid[i][j]
            c.countMines()
       
    
def draw():
    background(255)
    
    for i in range(boardwidth):
        for j in range(boardheight):
            grid[i][j].show()


def gameOver():
    for i in range(boardwidth):
        for j in range(boardheight):
            grid[i][j].__revealed == True


def mousePressed():
    for i in range(boardwidth):
        for j in range(boardheight):
            if grid[i][j].contains(mouse_x, mouse_y):
                grid[i][j].reveal()
                
                if grid[i][j].mine:
                    gameOver()



class Cell:
    def __init__(self, i, j, cellsize):
        self.__i = i
        self.__j = j
        self.__x = i * cellsize
        self.__y = j * cellsize
        self.__cellsize = cellsize
        self.__neighborCount = 0
        
        self.__mine = False
        self.__revealed = False
        
    def show(self):
        stroke(0)
        fill.enabled = False
        #nofill()
        _rect_mode = 'CENTER'
        print(self.__x, self.__y)
        rect(self.__x, self.__y, self.__cellsize, self.__cellsize) #removed , self.__cellsize, self.__cellsize from the parantheses
        if self.__revealed:
            if self.__mine:
                fill(127)
                ellipse(self.__x + self.__cellsize * 0.5, self.__y + self.__y * 0.5, self.__cellsize * 0.5)
            else:
                fill(200)
                rect(self.__x, self.__y, self.__cellsize, self.__cellsize)
                if self.__neighborCount > 0:
                    # textAlign is not integrated yet in p5.py 
                    textAlign(CENTER)
                    fill(0)
                    # text is not integrated yet in p5.py
                    text(self.__neighborCount, self.__x + self.__cellsize *0.5, self.__y + self.__cellsize - 6)


    def countMines(self):
        if self.__mine:
            self.__neighborCount = -1
            return
        
        total = 0
        for xoff in range(-1, 2):
            i = self.__i + xoff
            if i < 0 or i >= boardwidth:
                continue
            for yoff in range(-1, 2):
                j = self.__y + yoff
                if j < 0 or j >= boardheight:
                    continue
                neighbor = grid[i][j]
                if neighbor.__mine:
                    total =+1
        self.__neighborCount = total
                      
    
    def contains(self, x, y):
        return x > self.__x and x < self.__x + self.__cellsize and y > self.__y and y < self.__y + self.__cellsize
    
    
    def reveal(self):
        self.__revealed = True
        if self.__neighborCount == 0:
            # floodFill time
            self.floodFill()
    
    def floodFill(self):
        for xoff in range(-1, 2):
            i = self.__i + xoff
            if i < 0 or i >= boardwidth:
                continue
            for yoff in range(-1, 2):
                j = self.__y + yoff
                if j < 0 or j >= boardheight:
                    continue
                
                neighbor = grid[i][j]
                if not neighbor.__revealed:
                    neighbor.reveal()



    ###### to be continued here  
    
run()