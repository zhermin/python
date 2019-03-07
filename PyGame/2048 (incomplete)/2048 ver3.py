import pygame
import random, math, sys, time
from pygame.locals import *
pygame.init()

# print(pygame.display.Info())

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



class rectangle(): # Class for Random Rectangles
    
    def __init__(self, k_x, k_y, color):

        self.k_x = k_x
        self.k_y = k_y
        
        self.x1 = scnW/4
        self.y1 = scnH/4

        self.final_x1 = self.x1 * self.k_x + 10
        self.final_y1 = self.y1 * self.k_y + 10

        self.w = self.x1 - 15
        self.h = self.y1 - 15

        self.final_x2 = self.w + self.final_x1
        self.final_y2 = self.h + self.final_y1

        self.color = color
        #self.id = id

        self.rectx = None
        self.recty = None
        self.current = (self.rectx, self.recty)

    def size(self):
        return (self.final_x1, self.final_y1, self.w, self.h)

    def draw(self):      
        pygame.draw.rect(surface, self.color, self.size(), 0)

'''
    def pos(self):
        
        self.draw()

        if self.final_x1 == 10:
            self.rectx = 0

        if self.final_y1 == 10:
            self.recty = 0

        if self.final_x1 == 160:
            self.rectx = 1

        if self.final_y1 == 160:
            self.recty = 1

        if self.final_x1 == 310:
            self.rectx = 2

        if self.final_y1 == 310:
            self.recty = 3

        if self.final_x1 == 460:
            self.rectx = 3

        if self.final_y1 == 460:
            self.recty = 3

        #self.current = ((self.rectx, self.recty))
        #print(self.current)

        

        # print(self.final_x1, self.final_y1)
'''

        



#r1 = rectangle(1, 1, red)
#r2 = rectangle(2, 1, blue)




# GLOBAL

maingrid = {
    (1, 1): 0, (2, 1): 0, (3, 1): 0, (4, 1): 0,
    (1, 2): 0, (2, 2): 0, (3, 2): 0, (4, 2): 0,
    (1, 3): 0, (2, 3): 0, (3, 3): 0, (4, 3): 0,
    (1, 4): 0, (2, 4): 0, (3, 4): 0, (4, 4): 0
    }

'''
for k, v in maingrid.items():
    
    xcoord = k[0]
    ycoord = k[1]
    value = maingrid[(xcoord, ycoord)]
'''

# END OF GLOBAL


def spawn():

    global maingrid
    
    while True:
        
        rcoord = random.choice(list(maingrid.keys())) # can be removed
        color = None
        print(rcoord, maingrid[rcoord])
        print(rcoord[0], rcoord[1])
        
        if maingrid[rcoord] == 0:
            maingrid[rcoord] += 2
            color = red
            break
        else:
            continue

    return rcoord[0], rcoord[1], color




spawnrect = list([rectangle(random.randint(0,3), random.randint(0,3), red, i) for i in range(0, 4)])
#print(spawnrect)


# Main Loop
while True:
    events()
    keys = pygame.key.get_pressed()
 
    for k_x in range(0, 4):
        
        for k_y in range(0, 4):
            
            pygame.draw.rect(surface, white, (scnW/4 * k_x + 5, scnH/4 * k_y + 5, scnW/4 - 5, scnH/4 - 5), 0)

    #r1.move()
    #r2.move()

    for spwn in spawnrect:
        
        spwn.draw()

            
        if keys[pygame.K_LEFT] and spwn.final_x1 > 10:
            spwn.final_x1 -= 75
        
        if keys[pygame.K_RIGHT] and spwn.final_x1 < 460:
            spwn.final_x1 += 75
            
        if keys[pygame.K_UP] and spwn.final_y1 > 10:
            spwn.final_y1 -= 75
            
        if keys[pygame.K_DOWN] and spwn.final_y1 < 460:
            spwn.final_y1 += 75



    
    
    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(black)









