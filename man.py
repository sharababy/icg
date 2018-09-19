# Assignment 8 , Submission by Vedant Bassi , Ced15i013

# Man Dancing

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

y = 0
dire = 1
running = 1
h1x = 170
h2x = 330

l1y = 500
l2y = 500

leg = 0
leg1 = 0
leg2 = 0

shy = 350


pygame.display.update()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			running = 0
			sys.exit()

	screen.fill(bgcolor)

	
	# Face
	pygame.draw.circle(screen, color, (250,250), 50, 1)
	
	# Body
	pygame.draw.line(screen, color, (250, 300),(250, 450))

	# arms
	pygame.draw.line(screen, color, (250, shy),(h1x, 300))
	pygame.draw.line(screen, color, (250, shy),(h2x, 300))

	# hands
	pygame.draw.line(screen, color,(h1x, 300),(h1x-30,300))
	pygame.draw.line(screen, color,(h2x, 300),(h2x+30,300))

	# legs
	pygame.draw.line(screen, color, (250, 450),(200, l1y))
	pygame.draw.line(screen, color, (250, 450),(300, l2y))

	# pygame.draw.line(screen, color, (0, y), (width-1, y))

	if dire == 1:
		h1x +=1
		h2x +=1
	elif dire == 0:
		h1x -= 1
		h2x -=1

	if h1x > 200:
		dire = 0
	elif h1x < 140:
		dire = 1

	
	if leg == 0:
		if leg1 == 1:
			l1y += 1
		elif leg1 == 0:
			l1y -= 1

		if l1y > 510:
			leg1 = 0
			leg = 1
			
		elif l1y < 470:
			leg1 = 1
			
	elif leg == 1:
		if leg2 == 1:
			l2y += 1
		elif leg2 == 0:
			l2y -= 1

		if l2y > 510:
			leg2 = 0
			leg = 0
		elif l2y < 470:
			leg2 = 1
			


	pygame.display.flip()




