import pygame, sys, random, time
from pygame.locals import *

pygame.init()                    
pygame.display.set_caption("Atari Breakout")
screen = pygame.display.set_mode((640, 650))

# 미사일 class
class Missile:
      def __init__(self,x):
            self.x = x
            self.y = 574

def draw(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

def fire(self):
    missiles.append(Missile(self.x+50))

            
    pygame.draw.line(screen, (r,g,b),(self.x, self.y), (self.x,self.y+8), 6)

missiles = []

Missile.fire()

clock = pygame.time.Clock()
while 1:
    clock.tick(60)
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        # 미사일
        
        
        
        i = 0
        while i < len(missiles):
            missiles[i].draw()
            i =+ 1


    screen.fill((0,0,0))
    
    pygame.display.update()

        
