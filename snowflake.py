# Assignment 6 , Submission by Vedant Bassi , Ced15i013

# Snowflake 

import sys, pygame, random as rndm, time
import numpy as np
import math

pygame.init()
pygame.font.init()

size = width, height =750, 750
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

r = (pi/180)

def midtri(x_s,y_s,x_e,y_e):
	sub = int(l/3)

	mid1 = 

	pygame.draw.line(screen,color,[x,y],[])
	pygame.draw.line(screen,color,[x,y],[x ,y])
	pygame.draw.line(screen,color,[x ,y],[x,y])



midtri(200,200,120,-45)

pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()    

