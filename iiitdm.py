# Assignment 8 , Submission by Vedant Bassi , Ced15i013

# Man Dancing

import sys, pygame, random as rndm, time
import numpy as np
import math

pygame.init()
pygame.font.init()

size = width, height =750, 550
bgcolor = 255, 255, 255
color = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

white = (255,255,255)

sky = (217,235,237)
cream = (232, 208,187)
screen = pygame.display.set_mode(size)
surf=pygame.display.get_surface()
screen.fill(sky)


pygame.draw.polygon(screen, white,[(20,200),(720,200),(720,220),(20,220)])

roof_y_start = 220
roof_y_end = 240

center = 356

b_width = 50
l_width = 40
s_width = 22

pygame.draw.polygon(screen, cream,[(center-(6.5*b_width),roof_y_start),(center-(6.5*b_width)+s_width,roof_y_start),(center-(6.5*l_width),roof_y_end),(center-(6.5*l_width)-s_width,roof_y_end)])
pygame.draw.polygon(screen, cream,[(center-(5.5*b_width),roof_y_start),(center-(5.5*b_width)+s_width,roof_y_start),(center-(5.5*l_width),roof_y_end),(center-(5.5*l_width)-s_width,roof_y_end)])
pygame.draw.polygon(screen, cream,[(center-(4.5*b_width),roof_y_start),(center-(4.5*b_width)+s_width,roof_y_start),(center-(4.5*l_width),roof_y_end),(center-(4.5*l_width)-s_width,roof_y_end)])
pygame.draw.polygon(screen, cream,[(center-(3.5*b_width),roof_y_start),(center-(3.5*b_width)+s_width,roof_y_start),(center-(3.5*l_width),roof_y_end),(center-(3.5*l_width)-s_width,roof_y_end)])
pygame.draw.polygon(screen, cream,[(center-(2.5*b_width),roof_y_start),(center-(2.5*b_width)+s_width,roof_y_start),(center-(2.5*l_width),roof_y_end),(center-(2.5*l_width)-s_width,roof_y_end)])
pygame.draw.polygon(screen, cream,[(center-(1.5*b_width),roof_y_start),(center-(1.5*b_width)+s_width,roof_y_start),(center-(1.5*l_width),roof_y_end),(center-(1.5*l_width)-s_width,roof_y_end)])
pygame.draw.polygon(screen, cream,[(center-(0.5*b_width),roof_y_start),(center-(0.5*b_width)+s_width,roof_y_start),(center-(0.5*l_width),roof_y_end),(center-(0.5*l_width)-s_width,roof_y_end)])
pygame.draw.polygon(screen, cream,[(center+(0.5*b_width),roof_y_start),(center+(0.5*b_width)+s_width,roof_y_start),(center+(0.5*l_width),roof_y_end),(center+(0.5*l_width)-s_width,roof_y_end)])
pygame.draw.polygon(screen, cream,[(center+(1.5*b_width),roof_y_start),(center+(1.5*b_width)+s_width,roof_y_start),(center+(1.5*l_width),roof_y_end),(center+(1.5*l_width)-s_width,roof_y_end)])
pygame.draw.polygon(screen, cream,[(center+(2.5*b_width),roof_y_start),(center+(2.5*b_width)+s_width,roof_y_start),(center+(2.5*l_width),roof_y_end),(center+(2.5*l_width)-s_width,roof_y_end)])
pygame.draw.polygon(screen, cream,[(center+(3.5*b_width),roof_y_start),(center+(3.5*b_width)+s_width,roof_y_start),(center+(3.5*l_width),roof_y_end),(center+(3.5*l_width)-s_width,roof_y_end)])
pygame.draw.polygon(screen, cream,[(center+(4.5*b_width),roof_y_start),(center+(4.5*b_width)+s_width,roof_y_start),(center+(4.5*l_width),roof_y_end),(center+(4.5*l_width)-s_width,roof_y_end)])
pygame.draw.polygon(screen, cream,[(center+(5.5*b_width),roof_y_start),(center+(5.5*b_width)+s_width,roof_y_start),(center+(5.5*l_width),roof_y_end),(center+(5.5*l_width)-s_width,roof_y_end)])
pygame.draw.polygon(screen, cream,[(center+(6.5*b_width),roof_y_start),(center+(6.5*b_width)+s_width,roof_y_start),(center+(6.5*l_width),roof_y_end),(center+(6.5*l_width)-s_width,roof_y_end)])



myfont = pygame.font.SysFont('helvetica', 16)
textsurface = myfont.render('INDIAN INSTITUTE OF INFORMATION TECHNOLOGY DESIGN AND MANUFACTURING', False, (0, 0, 0))
screen.blit(textsurface,(30,203))


pygame.display.update()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			running = 0
			sys.exit()
