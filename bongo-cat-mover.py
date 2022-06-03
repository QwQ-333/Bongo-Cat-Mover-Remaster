from webbrowser import BackgroundBrowser
import pyautogui
import pygame
import config 
import pen
from os import path
from pygame.locals import *
from sys import exit
import numpy as np


pygame.init()




window = pygame.display.set_mode((config.width, config.length))
clock = pygame.time.Clock()

img_dir = path.join(path.dirname("C:\\Users\\Brooks\\Desktop\\python2\\first_object\\final_project\\img"), "img")

bg = pygame.image.load(path.join(img_dir, "jueyunjian.jpg")).convert()
bg = pygame.transform.scale(bg, (config.width, config.length))
bg_rect = bg.get_rect()

bg_xiao = pygame.image.load(path.join(img_dir, "Bongo-cat.png")).convert_alpha()
bg_xiao = pygame.transform.scale(bg_xiao, (config.width, config.length))
bg_xiao = pygame.transform.scale(bg_xiao, (int(bg_xiao.get_width() / 2), int(bg_xiao.get_height() / 1.75)))

bg_rect_xiao = bg_xiao.get_rect()
bg_rect_xiao.x += 225
bg_rect_xiao.y += 75



# bg_rect = bg.get_rect(center = (config.width, config.length))
# rx = 1000 / config.width
# ry = 600 / config.length
# print(rx)
# print(ry)
# bg = pygame.transform.scale(bg, ((config.width*rx), (config.length*rx)))

pen_obj = pen.Pen()
sprite_group = pygame.sprite.Group()
sprite_group.add(pen_obj)



while True:
    clock.tick(144)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    sprite_group.update()
    pygame.display.update()




    p0 = 292,336
    #p1 = 60,15
    p1 = (pen_obj.rect.x,pen_obj.rect.y)
    p2 = 338,358
    
    handCoords = []
    
    x1 = 2*pen_obj.rect.x - 328 / 2 - 365 / 2
    y1 = 2*pen_obj.rect.y - 304 / 2 - 325 / 2
    x1y1 = (x1,y1)
    


    window.blit(bg, bg_rect)

    

    pygame.draw.polygon(window,config.white, [(0, config.length/2.25),(0, config.length),(config.width, config.length),(config.width, config.length*0.78)])
    pygame.draw.line(window, config.black, (0, config.length/2.25), (config.width, config.length*0.78), 3)
    window.blit(bg_xiao, bg_rect_xiao)
    for t in np.arange(0, 1, 0.001):
        px = p0[0]*(1-t)**2 + 2*(1-t)*t*x1y1[0] + p2[0]*t**2
        py = p0[1]*(1-t)**2 + 2*(1-t)*t*x1y1[1] + p2[1]*t**2       
        handCoords.append(( px, py ))
        pygame.draw.rect(window, (0, 0, 0), (px, py, 2, 3))

    #pygame.draw.polygon(window, (48, 38, 37), handCoords)


    
    sprite_group.draw(window)    
    #print (pyautogui.position())
    pygame.display.flip()
    pygame.display.update()