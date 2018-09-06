# Assignment 3 , Submission by Vedant Bassi , Ced15i013

# Draw a straight line using Bresenham's Circle Algorithm 

import sys, pygame, random as rndm, time
import numpy as np

pygame.init()
pygame.font.init()

size = width, height = 550, 550
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

patt = []

def demosaic():
	h = 0
	w = 0
	colors = []
	
	p = 0
	q = 0
	v = []

	sq_size = 25

	while h<height :
		while w<width:
			v.append(surf.get_at((w+10, h+10)))
			
			w += sq_size
		h += sq_size
		w=0
		colors.append(v)
		v = []

	h = 0
	w = 0

	for y in range(1,int(height/sq_size)-1):
		for x in range(1,int(width/sq_size)-1):

			r=b=g=0

			kernel = []
			
			kernel.append(patt[x-1][y-1])
			kernel.append(patt[x-1][y])
			kernel.append(patt[x-1][y+1])
			kernel.append(patt[x][y-1])
			kernel.append(patt[x][y])
			kernel.append(patt[x][y+1])
			kernel.append(patt[x+1][y-1])
			kernel.append(patt[x+1][y])
			kernel.append(patt[x+1][y+1])

			for k in range(9):

				if kernel[k] == 0:
					r+=1	
				elif kernel[k] == 1:
					g+=1
				elif kernel[k] == 2:
					b+=1

			kernel = []

			kernel.append(colors[x-1][y-1])
			kernel.append(colors[x-1][y])
			kernel.append(colors[x-1][y+1])
			kernel.append(colors[x][y-1])
			kernel.append(colors[x][y])
			kernel.append(colors[x][y+1])
			kernel.append(colors[x+1][y-1])
			kernel.append(colors[x+1][y])
			kernel.append(colors[x+1][y+1])			

			add = [0,0,0]
			for k in range(9):
				add[0] += int(kernel[k][0])
				add[1] += int(kernel[k][1])
				add[2] += int(kernel[k][2])


			add[0] = int(add[0]/r)
			add[1] = int(add[1]/g)
			add[2] = int(add[2]/b)

			c = (add[0],add[1],add[2])

			pygame.draw.rect(screen,c,[w+sq_size, h+sq_size, sq_size, sq_size], 0)
			w += sq_size


		h+=sq_size
		w = 0
	pygame.display.update()


def genColors():
	h = 0
	w = 0

	p = 0
	q = 0

	sq_size = 25

	while h<height :
		pa = []
		while w<width:	
			
			if p % 2 == 0:
				if q%2 == 0:
					color = (rndm.randint(0,255),0,0)
					pa.append(0)
					pygame.draw.rect(screen,color,[w, h, sq_size, sq_size], 0)		
				else:
					color = (0,rndm.randint(0,255),0)
					pa.append(1)
					pygame.draw.rect(screen,color,[w, h, sq_size, sq_size], 0)

			elif p % 2 != 0:
				if q%2 == 0:
					color = (0,rndm.randint(0,255),0)
					pa.append(1)
					pygame.draw.rect(screen,color,[w, h, sq_size, sq_size], 0)
				else:
					color = (0,0,rndm.randint(0,255))
					pa.append(2)
					pygame.draw.rect(screen,color,[w, h, sq_size, sq_size], 0)
			
			p += 1
			w += sq_size

		patt.append(pa)
		h += sq_size
		w=0
		q += 1
		p=0


genColors()
# print(np.asarray(patt))
pygame.display.update()




while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()    

		elif event.type == pygame.KEYDOWN:
			demosaic()






