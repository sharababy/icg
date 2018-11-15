import sys, pygame
import random as rand

pygame.init()
pygame.font.init()

size = width, height = 800, 800
bgcolor = 255, 255, 255
color = (0,0,0)

screen = pygame.display.set_mode(size)
surf=pygame.display.get_surface()
screen.fill(bgcolor)

myfont = pygame.font.SysFont('Arial', 15)
# textsurface = myfont.render('100 Non Intersecting Disjoint Circles', False, (0, 0, 0))
# screen.blit(textsurface,(10,10))


offset = 32
radius = offset-5
x = offset
y = offset

for d in range(0,100):
		x+=(offset*2)
		if x>width-radius:
			y+=(offset*2)
			x = offset
		
		pygame.draw.circle(surf,color,(x,y),radius,1)
		textsurface = myfont.render(str(d+1), False,(0, 0, 0))
		screen.blit(textsurface,(x-3,y-3))


pygame.display.update()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()    

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_ESCAPE:
				running = False
