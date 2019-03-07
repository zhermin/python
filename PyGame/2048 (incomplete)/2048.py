import pygame
import random, math, sys, time
from pygame.locals import *
pygame.init()


# Quit Game
def events():
    keys = pygame.key.get_pressed()

    # Quit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()


# Display Attributes
scnW = scnH = 600

# Display Initialisation
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((scnW + 5, scnH + 5))
pygame.display.set_caption("2048")
FPS = 120

# Colors
black = (0,0,0,255)
white = (255,255,255,255)
red = (255,0,0,255)
green = (0,255,0,255)
blue = (0,0,255,255)
yellow = (255,255,0,255)

# Window Surface to Draw On
surface = pygame.display.get_surface()


# Class for Random Rectangles
class rectangle():
    
    def __init__(self, times_x, times_y, v):

        self.times_x = times_x
        self.times_y = times_y
        
        self.x1 = scnW/4 * self.times_x + 10
        self.y1 = scnH/4 * self.times_y + 10

        self.w = scnW/4 - 15
        self.h = scnH/4 - 15

        self.x2 = self.x1 + self.w
        self.y2 = self.y1 + self.h

        self.v = v

        if 8 in self.v:
            self.color = green
        elif 4 in self.v:
            self.color = blue
        elif 2 in self.v:
            self.color = red
        else:
            self.color = white

        self.getx = None
        self.gety = None

    def getpos(self):        

        if self.x1 == 10:
            self.getx = 1

        if self.y1 == 10:
            self.gety = 1

        if self.x1 == 160:
            self.getx = 2

        if self.y1 == 160:
            self.gety = 2

        if self.x1 == 310:
            self.getx = 3

        if self.y1 == 310:
            self.gety = 3

        if self.x1 == 460:
            self.getx = 4

        if self.y1 == 460:
            self.gety = 4

        return self.getx, self.gety


    def size(self):
        return (self.x1, self.y1, self.w, self.h)

    def draw(self, ):      
        pygame.draw.rect(surface, self.color, self.size(), 0)


# Maingrid
class thegrid():

    def __init__(self):
        
        self.grid = {
                (1, 1): [], (2, 1): [], (3, 1): [], (4, 1): [],
                (1, 2): [], (2, 2): [], (3, 2): [], (4, 2): [],
                (1, 3): [], (2, 3): [], (3, 3): [], (4, 3): [],
                (1, 4): [], (2, 4): [], (3, 4): [], (4, 4): []
                }

        

maingrid = thegrid()


# Spawn a Rectangle
def spawn():
    
    while True:
        
        rcoord = random.choice(list(maingrid.grid.keys())) # returns tuple
        print(rcoord, maingrid.grid[rcoord])
        
        if maingrid.grid[rcoord] == []:            
            maingrid.grid[rcoord].append(2)
            break

        else:
            continue


# Main Loop
while True:
    
    events()
    keys = pygame.key.get_pressed()


    if all(v == [] for v in maingrid.grid.values()): # Game Start with all Empty Squares        
        spawn()
        spawn()
        spawn()
        spawn()        

    elif all(v != [] for v in maingrid.grid.values()): # Game Over if all Squares are filled. Needs to add "if still moveable"
        print("GAME OVER!!!")
        #pygame.quit()
    
    for k, v in maingrid.grid.items(): # Coloring every Square one by one
        pygame.draw.rect(surface, white, (scnW/4 * (k[0] - 1) + 5, scnH/4 * (k[1] - 1) + 5, scnW/4 - 5, scnH/4 - 5), 0)
        

    for k, v in maingrid.grid.items():

        if v != []:

            isDiff = None
            
            r = rectangle((k[0] - 1), (k[1] - 1), v)

            num = v[0]

            if len(maingrid.grid[(r.getpos()[0], r.getpos()[1])]) == 2:

                item1 = maingrid.grid[(r.getpos()[0], r.getpos()[1])][0]
                item2 = maingrid.grid[(r.getpos()[0], r.getpos()[1])][1]

                if item1 == item2: # if [2, 2] : 2 == 2
                
                    print("same!")
                       
                    added = item1 + item2
                    maingrid.grid[(r.getpos()[0], r.getpos()[1])].clear()
                    maingrid.grid[(r.getpos()[0], r.getpos()[1])].append(added)
                    print(maingrid.grid[(r.getpos()[0], r.getpos()[1])])

                    isDiff = False
                    
                    break

                else:

                    print("different!")

                    isDiff = True


                        
                    
            if keys[pygame.K_LEFT] and r.x1 > 10:

                if not isDiff:

                    print(r.getpos()[0], r.getpos()[1], maingrid.grid[r.getpos()[0], r.getpos()[1]])
                    maingrid.grid[(r.getpos()[0], r.getpos()[1])].clear()

                    r.x1 -= r.w + 15
                                
                    maingrid.grid[(r.getpos()[0], r.getpos()[1])].append(num)
                    print(r.getpos()[0], r.getpos()[1], maingrid.grid[r.getpos()[0], r.getpos()[1]])
                    print("")

                else:
                    break
            
            if keys[pygame.K_RIGHT] and r.x1 < 460:
             
                if not isDiff:

                    print(r.getpos()[0], r.getpos()[1], maingrid.grid[r.getpos()[0], r.getpos()[1]])
                    maingrid.grid[(r.getpos()[0], r.getpos()[1])].clear()
                    
                    r.x1 += r.w + 15

                    maingrid.grid[(r.getpos()[0], r.getpos()[1])].append(num)
                    print(r.getpos()[0], r.getpos()[1], maingrid.grid[r.getpos()[0], r.getpos()[1]])
                    print("")

                else:
                    break
                
            if keys[pygame.K_UP] and r.y1 > 10:
          
                if not isDiff:

                    print(r.getpos()[0], r.getpos()[1], maingrid.grid[r.getpos()[0], r.getpos()[1]])
                    maingrid.grid[(r.getpos()[0], r.getpos()[1])].clear()
                
                    r.y1 -= r.h + 15

                    maingrid.grid[(r.getpos()[0], r.getpos()[1])].append(num)
                    print(r.getpos()[0], r.getpos()[1], maingrid.grid[r.getpos()[0], r.getpos()[1]])
                    print("")

                else:
                    break
                
            if keys[pygame.K_DOWN] and r.y1 < 460:
 
                if not isDiff:

                    print(r.getpos()[0], r.getpos()[1], maingrid.grid[r.getpos()[0], r.getpos()[1]])
                    maingrid.grid[(r.getpos()[0], r.getpos()[1])].clear()
                
                    r.y1 += r.h + 15

                    maingrid.grid[(r.getpos()[0], r.getpos()[1])].append(num)
                    print(r.getpos()[0], r.getpos()[1], maingrid.grid[r.getpos()[0], r.getpos()[1]])
                    print("")

                else:
                    break
                    

            r.draw()

    
    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(black)	



    



    





