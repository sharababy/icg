# Class Assignment , Submission by Vedant Bassi , Ced15i013

# Rainbow

import sys, pygame, random as rndm, time
import numpy as np
import math

pygame.init()
pygame.font.init()

size = width, height =700, 700
bgcolor = 255, 255, 255
color = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen = pygame.display.set_mode(size)
surf=pygame.display.get_surface()
screen.fill(bgcolor)

# myfont = pygame.font.SysFont('Comic Sans MS', 25)
# textsurface = myfont.render('Bayers Demosaicing', False, (0, 0, 0))
# screen.blit(textsurface,(150,10))

pi = (22.0/7.0)


v = (148, 0, 211)
i =(75, 0, 130)
b = (0, 0, 255)
g = (0, 255, 0)
y = (255, 255, 0)
o = (255, 127, 0)
r = (255, 0 , 0)


pygame.draw.arc(screen,v,[250,300,150,150], 0, pi + 0.01, 10)
pygame.draw.arc(screen,i,[240,290,170,170], 0, pi + 0.01, 10)
pygame.draw.arc(screen,b,[230,280,190,190], 0, pi + 0.01, 10)
pygame.draw.arc(screen,g,[220,270,210,210], 0, pi + 0.01, 10)
pygame.draw.arc(screen,y,[210,260,230,230], 0, pi + 0.01, 10)
pygame.draw.arc(screen,o,[200,250,250,250], 0, pi + 0.01, 10)
pygame.draw.arc(screen,r,[190,240,270,270], 0, pi + 0.01, 10)


pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()    

