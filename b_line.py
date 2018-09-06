# Assignment 2 , Submission by Vedant Bassi , Ced15i013

# Draw a straight line using Bresenham's Algorithm 

import sys, pygame


pygame.init()
pygame.font.init()

size = width, height = 530, 500
bgcolor = 255, 255, 255
color = (0,0,0)

screen = pygame.display.set_mode(size)
surf=pygame.display.get_surface()
screen.fill(bgcolor)

myfont = pygame.font.SysFont('Comic Sans MS', 25)
textsurface = myfont.render('Bresenhams Algorithm', False, (0, 0, 0))
screen.blit(textsurface,(200,10))

x0 = 100.0
y0 = 100.0

x1 = 280.0
y1 = 150.0

surf.set_at((int(x0),int(y0)), color)


dx=x1-x0;
dy=y1-y0;

x=x0;
y=y0;

p=2*dy-dx;

while(x<x1):

	if p>=0 :
		surf.set_at((int(x),int(y)), color)
		y=y+1
		p=p+2*dy-2*dx
	
	else:
	
		surf.set_at((int(x),int(y)), color)
		p=p+2*dy
	
	x=x+1


pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()    





