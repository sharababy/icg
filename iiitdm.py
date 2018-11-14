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

pygame.draw.polygon(screen, white,[(20+20,200+30),(720-20,200+30),(720-20,220+30),(20+20,220+30)])

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



center_x = 356
bottom_y = 400
roof_top_y = 220

brick = (72,7,0)
pygame.draw.polygon(screen,
					brick,
					[(center_x+20,roof_top_y),
					(center_x-20,roof_top_y),
					(center_x-20,bottom_y),
					(center_x+20,bottom_y)])

brick_wall_x = -center_x
pygame.draw.polygon(screen,
					brick,
					[(center_x+brick_wall_x+30,roof_top_y+80),
					(center_x+brick_wall_x-30,roof_top_y+80),
					(center_x+brick_wall_x-30,bottom_y),
					(center_x+brick_wall_x+30,bottom_y)])

brick_wall_x = -center_x + width - 49
pygame.draw.polygon(screen,
					brick,
					[(center_x+brick_wall_x+15,roof_top_y+80),
					(center_x+brick_wall_x-15,roof_top_y+80),
					(center_x+brick_wall_x-15,bottom_y),
					(center_x+brick_wall_x+15,bottom_y)])

support_x = -300
silver = (200,200,200)
pygame.draw.polygon(screen,
					silver,
					[(center_x+support_x+20,roof_top_y+20),
					(center_x+support_x-20,roof_top_y),
					(center_x+support_x-20,roof_top_y+80),
					(center_x+support_x+20,roof_top_y+80)])

support_x = 325
pygame.draw.polygon(screen,
					silver,
					[(center_x+support_x+20,roof_top_y),
					(center_x+support_x-20,roof_top_y+10),
					(center_x+support_x-20,roof_top_y+80),
					(center_x+support_x+20,roof_top_y+80)])



pillar_x = -200
pygame.draw.polygon(screen,
					white,
					[(center_x+pillar_x+20,roof_top_y),
					(center_x+pillar_x-20,roof_top_y),
					(center_x+pillar_x-20,bottom_y),
					(center_x+pillar_x+20,bottom_y)])

pillar_x = 200
pygame.draw.polygon(screen,
					white,
					[(center_x+pillar_x+20,roof_top_y),
					(center_x+pillar_x-20,roof_top_y),
					(center_x+pillar_x-20,bottom_y),
					(center_x+pillar_x+20,bottom_y)])


box_x = -300
pygame.draw.polygon(screen,
					white,
					[(center_x+box_x+30,roof_top_y+80),
					(center_x+box_x-30,roof_top_y+80),
					(center_x+box_x-30,bottom_y),
					(center_x+box_x+30,bottom_y)])

box_x = 300
pygame.draw.polygon(screen,
					white,
					[(center_x+box_x+30,roof_top_y+80),
					(center_x+box_x-30,roof_top_y+80),
					(center_x+box_x-30,bottom_y),
					(center_x+box_x+30,bottom_y)])


gate_line = (88,88,88)

gate_line_x = center_x - 180;
gate_line_y = roof_top_y + 100;
gate_line_width = 160
gate_line_height = 2

for x in range(0,10):
	y = x*9	
	pygame.draw.polygon(screen,
						gate_line,
						[(gate_line_x,gate_line_y+gate_line_height+y),
						(gate_line_x+gate_line_width,gate_line_y+gate_line_height+y),
						(gate_line_x+gate_line_width,gate_line_y+y),
						(gate_line_x,gate_line_y+y)])

gate_line_x = center_x + 20;
gate_line_y = roof_top_y + 100;
gate_line_width = 160
gate_line_height = 2

for x in range(0,10):
	y = x*9	
	pygame.draw.polygon(screen,
						gate_line,
						[(gate_line_x,gate_line_y+gate_line_height+y),
						(gate_line_x+gate_line_width,gate_line_y+gate_line_height+y),
						(gate_line_x+gate_line_width,gate_line_y+y),
						(gate_line_x,gate_line_y+y)])


window = (70,83,98)
box_x = -300
pygame.draw.polygon(screen,
					window,
					[(center_x+box_x+10,roof_top_y+120),
					(center_x+box_x-10,roof_top_y+120),
					(center_x+box_x-10,roof_top_y+150),
					(center_x+box_x+10,roof_top_y+150)])


box_x = 300
pygame.draw.polygon(screen,
					window,
					[(center_x+box_x+10,roof_top_y+120),
					(center_x+box_x-10,roof_top_y+120),
					(center_x+box_x-10,roof_top_y+150),
					(center_x+box_x+10,roof_top_y+150)])




road = (51,51,51)
pygame.draw.polygon(screen,road,[(0,bottom_y),(width,bottom_y),(width,height),(0,height)])


pos_x = 180
pos_y = 0
pygame.draw.polygon(screen,
					white,
					[(40+pos_x,bottom_y+50+pos_y),
					(45+pos_x,bottom_y+50+pos_y),
					(35+pos_x,bottom_y+80+pos_y),
					(30+pos_x,bottom_y+80+pos_y)])

pos_x = 160
pos_y = 60
pygame.draw.polygon(screen,
					white,
					[(40+pos_x,bottom_y+50+pos_y),
					(45+pos_x,bottom_y+50+pos_y),
					(35+pos_x,bottom_y+80+pos_y),
					(30+pos_x,bottom_y+80+pos_y)])



pos_x = 440
pos_y = 0
pygame.draw.polygon(screen,
					white,
					[(30+pos_x,bottom_y+50+pos_y),
					(35+pos_x,bottom_y+50+pos_y),
					(45+pos_x,bottom_y+80+pos_y),
					(40+pos_x,bottom_y+80+pos_y)])


pos_x = 460
pos_y = 60
pygame.draw.polygon(screen,
					white,
					[(30+pos_x,bottom_y+50+pos_y),
					(35+pos_x,bottom_y+50+pos_y),
					(45+pos_x,bottom_y+80+pos_y),
					(40+pos_x,bottom_y+80+pos_y)])


myfont = pygame.font.SysFont('helvetica', 16)
textsurface = myfont.render('INDIAN INSTITUTE OF INFORMATION TECHNOLOGY DESIGN AND MANUFACTURING', False, (0, 0, 0))
screen.blit(textsurface,(30,203))


pygame.display.update()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			running = 0
			sys.exit()
