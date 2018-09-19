# Assignment 5 , Submission by Vedant Bassi , Ced15i013

# C Curve


import sys, pygame, random as rndm, time
import numpy as np
import math

pygame.init()
pygame.font.init()

size = width, height = 1250, 750
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

def c_curve(x,y,l,a,n):

	if n>0:
		l = float(l/math.sqrt(2))
		c_curve(x,y,l,(a+45),n-1)
		x = x + (l*math.cos((a+45)*(pi/180)))
		y = y + (l*math.sin((a+45)*(pi/180)))

		c_curve(x,y,l,a-45,n-1)		

	elif n==0:
		pygame.draw.line(screen, color,[x, y], [x + (l*math.cos(a*(pi/180))), y + (l*math.sin(a*(pi/180)))], 1)


c_curve(300,200,450,0,13);

pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()    

