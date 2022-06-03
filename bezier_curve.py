import pygame
from pygame.locals import *
from sys import exit
import numpy as np

pygame.init()
screen = pygame.display.set_mode((1200, 600))

run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    
    p0 = 30,30
    #p1 = 60,15
    p1 = pygame.mouse.get_pos()
    p2 = 30,190
    
    screen.fill(0)
    for p in [p0, p1, p2]:
        pygame.draw.circle(screen, (255, 255, 255), p, 5)
    for t in np.arange(0, 1, 0.01):
        px = p0[0]*(1-t)**2 + 2*(1-t)*t*p1[0] + p2[0]*t**2
        py = p0[1]*(1-t)**2 + 2*(1-t)*t*p1[1] + p2[1]*t**2
        pygame.draw.rect(screen, (255, 255, 0), (px, py, 1, 1))

    pygame.display.update()

pygame.quit()
exit()