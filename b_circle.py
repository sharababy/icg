# Assignment 2 , Submission by Vedant Bassi , Ced15i013

# Draw a straight line using Bresenham's Circle Algorithm 

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
textsurface = myfont.render('Bresenhams Circle Algorithm', False, (0, 0, 0))
screen.blit(textsurface,(150,10))



def Circle(X, Y, P, Q):

	surf.set_at((X + P, Y + Q),color)
	surf.set_at((X - P, Y + Q),color)
	surf.set_at((X + P, Y - Q),color)
	surf.set_at((X - P, Y - Q),color)
	surf.set_at((X + Q, Y + P),color)
	surf.set_at((X - Q, Y + P),color)
	surf.set_at((X + Q, Y - P),color)
	surf.set_at((X - Q, Y - P),color)


rad = 50
x = 250
y = 250

p = 0
q = rad

d = 3 - (2*rad)

while p <= q:

	Circle(x, y, p, q)
	p+=1

	if d<0:
		d = d + (4*p) + 6
	else:
		q = q - 1
		d = d + 4*(p-q) + 10

	Circle(x, y, p, q)


pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()    





