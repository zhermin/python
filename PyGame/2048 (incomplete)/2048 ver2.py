import pygame
import random, math, sys
pygame.init()

# print(pygame.display.Info())

def events():
    keys = pygame.key.get_pressed()

    # Quit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()


# Display Attributes
W, H = 1920, 1080
HW, HH = int(W/2), int(H/2)
AREA = W + H

# Display Initialisation
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((HW, HH))
pygame.display.set_caption("2048")
FPS = 120

# Colors
black = (0,0,0,255)
white = (255,255,255,255)
red = (255,0,0,255)
green = (0,255,0,255)
blue = (0,0,255,255)


class rectangle(): # Class for Random Rectangles

    global white
    
    def __init__(self, x, y, w, h, id):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
        
        self.w = w
        self.h = h

        self.fillColor = white

        self.stained = False
        self.id = id

    def setXY(self, xy): # Obtain x1, y1 as xy and x2, y2
        self.x1, self.y1 = xy
        self.x2 = xy[0] + self.w
        self.y2 = xy[1] + self.h

    def getXY(self): # Returns (x1, y1) Tuple Coord
        return (self.x1, self.y1)

    def rect(self): # Pygame Rectangle Attributes : (x1, y1, w, h)
        return self.getXY() + (self.w, self.h)

    def coords(self): # Returns (x2, y2) Tuple Coord
        return self.getXY() + (self.x2, self.y2)

    def hasCollided(self, target): # Test if NO COLLISIONS with Target Rect
        tx1, ty1, tx2, ty2 = target.coords()

        if tx1 > self.x2 or tx2 < self.x1 or ty1 > self.y2 or ty2 < self.y1:
            return False # NO Collision
        else:
            return True # Collision

    def draw(self, surface = None):
        if not surface:
            surface = pygame.display.get_surface()
        
        pygame.draw.rect(surface, self.fillColor, self.rect(), 0)

    
# List of Randomly Generated Rectangles with [(0-ScreenWidth) x coord, (0-ScreenHeight) y coord, (20-40px) Width, (20-40px) Height], Looped 2000 Times
rectangles = list([rectangle(random.randint(0, W), random.randint(0, H), random.randint(20, 40), random.randint(20, 40), i) for i in range(0, 2000)])
rectangles[0].fillColor = green


# Main Loop
while True:
    events()

    mb = pygame.mouse.get_pressed() # mb[0] = Mouse Left Button, check if held down
    rectangles[0].setXY(pygame.mouse.get_pos()) # 1st Rect on Mouse Cursor Position

    for r in rectangles: # Iterating through 'rectangles' list
        if r.id == 0: # Skip 1st Rect (Cursor)
            continue
        
        r.draw() # Draw the Rectangles

        result = r.hasCollided(rectangles[0]) # For every instances of 'r', check if 'r' collided with cursor rect

        if result: # If result True, 'r' has collided
            r.fillColor = red # Turn that particular 'r' red

            if mb[0]: # If Mouse Button held down at time of collision, stain 'r' permanently red 
                r.stained = True
                
        else: # No Collision, but if not previously stained, 'r' set back to white
            if not r.stained:
                r.fillColor = white

    rectangles[0].draw()

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(black)











'''
class theValue():
    def __init__(self, value):
        self.value = value
        self.color = ""
        
        if self.value == 2:
            self.color = "red"
        elif self.value == 4:
            self.color = "blue"
        elif self.value == 8:
            self.color = "green"
        
        
two = theValue(2)
four = theValue(4)

print(two.value + four.value)
print(four.color)
'''





