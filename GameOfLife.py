
import pygame
import numpy as np
import time

WIDTH, HEIGHT = 1000, 1000
nX, nY = 80, 80
xSize = WIDTH/nX
ySize = HEIGHT/nY

pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT])

BG_COLOR = (10,10,10)
LIVE_COLOR = (255,255,255)
DEAD_COLOR = (128,128,128)
status = np.zeros((nX,nY))

pauseRun = False

running = True
while running:

    newStatus = np.copy(status)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pauseRun = not pauseRun

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            x, y = int(np.floor(posX/xSize)), int(np.floor(posY/ySize))
            newStatus[x,y] = not mouseClick[2]

    screen.fill(BG_COLOR) 

    for x in range(0,nX):
        for y in range(0,nY):


            if not pauseRun:

                nNeigh = status[(x-1)%nX,(y-1)%nY] + status[(x)%nX,(y-1)%nY] + \
                        status[(x+1)%nX,(y-1)%nY] + status[(x-1)%nX,(y)%nY] + \
                        status[(x+1)%nX,(y)%nY] + status[(x-1)%nX,(y+1)%nY] + \
                         status[(x)%nX,(y+1)%nY] + status[(x+1)%nX,(y+1)%nY]

                if status[x,y] == 0 and nNeigh==3:
                    newStatus[x,y] = 1

                elif status[x,y] == 1 and (nNeigh < 2 or nNeigh > 3):
                    newStatus[x,y] = 0


            poly = [(x*xSize,y*ySize),
                    ((x+1)*xSize,y*ySize),
                    ((x+1)*xSize,(y+1)*ySize),
                    (x*xSize,(y+1)*ySize)]

            if newStatus[x,y] == 1:
                pygame.draw.polygon(screen,LIVE_COLOR,poly,0)
            else:
                pygame.draw.polygon(screen,DEAD_COLOR,poly,1)

    status = np.copy(newStatus)
    time.sleep(0.1)
    pygame.display.flip()



pygame.quit()
