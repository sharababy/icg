# Assignment 1 , Submission by Vedant Bassi , Ced15i013

# Draw a straight line using DDA algorithm


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
textsurface = myfont.render('DDA Algorithm', False, (0, 0, 0))
screen.blit(textsurface,(200,10))


x1 = 100.0
y1 = 100.0

x2 = 280.0
y2 = 150.0


slope = ( y2 - y1 ) / ( x2 - x1 )

y = 0.0

for x in range(0,int(x2-x1)):

    y += slope
    # print(y,round(y))
    surf.set_at((round(x+x1), round(y+y1)), color)


pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()    





