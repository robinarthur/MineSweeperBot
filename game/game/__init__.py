# -*- coding: UTF-8 -*-


# import some Modules
import random
import numpy as np


# Pygame-Modul importieren.
import pygame

# p5.py from http://github.com/p5py/p5 Modul importieren
from p5 import *
from cell import rows




# überprüfen, ob die optionalen Sound und Textmodule geladen werden können
if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden')


# the array is the template for the grid
def make2DArray(cols, rows):
    #arr = np.array([range(cols) for row in range(rows)])
    #arr = np.zeros(shape = (rows,cols))
    arr = [['false' for _i in range(cols)] for _j in range(rows)]
    return arr


def main():
    # Initialisieren aller pygame Module und Fenster erstellen (wir bekommen eine
    # Oberfläche, die den Bildschirm repräsentiert).
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt
    # senden
    pygame.display.set_caption('p5.py - Minesweeper')
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)
    
    # Clock- Objekt erstellen, das wir benötigen um die Framerate zu begrenzen
    clock = pygame.time.Clock()
    
    
    # setup from p5
    w = 20
    totalMines = 30
    size(401, 401)
    
    
    global cols 
    global rows
    cols = int(width / w)
    rows = int(height / w)
    
    
    grid = make2DArray(cols, rows)
    for col in range(cols):
        for row in range(rows):
            c = Cell(col, row, w)
            grid[col][row] = c
    
    # Pick the spots of totalMines
    options = []
    for col in range(cols):
        for row in range(rows):
            options.append([col, row])
            
    for n in range(totalMines):
        index = random.randint(0, len(options))
        print(index)
        choice = options[index]
        i = choice[0]
        j = choice[1]
        # delete that spot so its no longer an option
        options.remove(choice)
        grid[i][j].__mine = True
    
    for col in range(cols):
        for row in range(rows):
            print("grid[col][row]", grid[col][row])
            x = grid[col][row]
            #print[x]
            print(type(grid))
            
            grid[col][row].countMines()
    
    
    
    
    
    # die Schleife und damit unser Spiel, läuft solange running == True
    running = True
    while running:
        # Framerate auf 30 pro Sekunde beschränken
        # Pygame wartet, falls das Programm schneller läuft
        clock.tick(30)
        
        # screen.surface mit schwarz (RGB = 0, 0, 0) füllen
        screen.fill((0, 0, 0))
        
        # Alle aufgelaufenen Events holen und abarbeiten
        for event in pygame.event.get():
            # Spiel beenden, wenn wir ein Quit-Event finden.
            if event.type == pygame.QUIT:
                running = False
            
            # wir interessieren uns auch für "Taste gedrückt"-Events.
            if event.type == pygame.KEYDOWN:
                # Wenn Escape gedrückt wird, posten wir ein QUIT-Event in Pygames Event
                # Warteschlange
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
        
        
        # Inhalt vom Screen anzeigen:
        pygame.display.flip()


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


    def copyGrid():
        # copy the Grid to flag the mines with True
        pass
    
    
    def mark_mines():
        # mark the spots of the mines with True
        pass
    
    def countMines(self):
        # count the Trues of the neighbors
        pass
        
    
    
    
    
    def countMinesold(self,grid, col, row):
        if self.__mine:
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
                print("i,j, self.__i, col, row", i , j, self.__i, col, row)
                neighbor = grid[i+col][j+row]
                if neighbor.__mine:
                    total =+ 1
        self.__neighborCount = total
        pass
    
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

        pass
    
    
    
    
    
    
    
    








if __name__ == '__main__':
    # unsere Main Funktion aufrufen.
    main()
