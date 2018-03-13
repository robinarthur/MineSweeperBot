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
    global width
    global height
    
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
        index = int(random(1, len(options)+1))
        print("index", index)
        choice = options[index]
        print("choice", choice)
        print("index", index)
        
        i = choice[0]
        j = choice[1]
        # Delete that spot so its no longer an option
        options.remove(choice)
        grid[i][j].__mine = True
        
    for i in range(cols):
        for j in range(rows):
            c = grid[i][j]
            c.countMines()
    
    
def draw():
    background(255)
    
    for i in range(cols):
        for j in range(rows):
            grid[i][j].show()


def gameOver():
    for i in range(cols):
        for j in range(rows):
            grid[i][j].__revealed == True


def mousePressed():
    for i in range(cols):
        for j in range(rows):
            if grid[i][j].contains(mouseX, mouseY):
                grid[i][j].reveal()
                
                if grid[i][j].__mine:
                    gameOver()



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
        #nofill()
        _rect_mode = 'CENTER'
        print(self.__x, self.__y)
        rect(self.__x, self.__y, self.__w, self.__w)
        if self.__revealed:
            if self.__mine:
                fill(127)
                ellipse(self.__x + self.__w * 0.5, self.__y + self.__y * 0.5, self.__w * 0.5)
            else:
                fill(200)
                rect(self.__x, self.__y, self.__w, self.__w)
                if self.__neighborCount > 0:
                    textAlign(CENTER)
                    fill(0)
                    text(self.__neighborCount, self.__x + self.__w *0.5, self.__y + self.__w - 6)


    def countMines(self):
        if self.__mine:
            self.__neighborCount = -1
            return
        
        total = 0
        for xoff in range(-1, 2):
            i = self.__i + xoff
            if i < 0 or i >= cols:
                continue
            for yoff in range(-1, 2):
                j = self.__y + yoff
                if j < 0 or j >= rows:
                    continue
                neighbor = grid[i][j]
                if neighbor.__mine:
                    total =+1
        self.__neighborCount = total
                    
    
    def contains(self, x, y):
        return x > self.__x and x < self.__x + self.__w and y > self.__y and y < self.__y + self.__w
    
    
    def reveal(self):
        self.__revealed = True
        if self.__neighborCount == 0:
            # floodFill time
            self.floodFill()
    
    def floodFill(self):
        for xoff in range(-1, 2):
            i = self.__i + xoff
            if i < 0 or i >= cols:
                continue
            for yoff in range(-1, 2):
                j = self.__y + yoff
                if j < 0 or j >= rows:
                    continue
                
                neighbor = grid[i][j]
                if not neighbor.__revealed:
                    neighbor.reveal()


