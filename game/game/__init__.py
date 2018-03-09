# -*- coding: UTF-8 -*-

# Pygame-Modul importieren.
import pygame

# überprüfen, ob die optionalen Sound und Textmodule geladen werden können
if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden')

def main():
    # Initialisieren aller pygame Module und Fenster erstellen (wir bekommen eine
    # Oberfläche, die den Bildschirm repräsentiert).
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt
    # senden
    pygame.display.set_caption('Pygame-Tutorial: Grundlagen')
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)
    
    # Clock- Objekt erstellen, das wir benötigen um die Framerate zu begrenzen
    clock = pygame.time.Clock()
    
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


Class Cell:
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
        continue
        
    def countMines(self):
        continue
    
    def contains(self, x, y):
        pass
    
    def reveal(self):
        pass
    
    def floodFill(self):
        pass
    
    
    
    
    
    
    
    








if __name__ == '__main__':
    # unsere Main Funktion aufrufen.
    main()
