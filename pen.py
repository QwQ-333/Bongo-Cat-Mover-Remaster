import pyautogui
import pygame
import config
import math

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

class Pen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 1))
        self.image.fill(config.black)
        # give us a 30 by 40 rectangle that we can control the coordinates
        self.rect = self.image.get_rect() 
        self.rect.x = 0
        self.rect.y = 0
    
    def update(self):
        # get our mouse position
        # update the pen's position to be the same as our mouse's position
        
        self.rect.x = map_range(pyautogui.position()[0], 0, config.monitor_width, 0, config.width)
        self.rect.y = map_range(pyautogui.position()[1], 0, config.monitor_height, 0, config.length)
        # self.rect.x = self.rect.x - 15
        # self.rect.y = self.rect.y - 20
        
        # prevX & prevY is the coordinates before the rotation
        prevX = self.rect.x
        prevY = self.rect.y
        t = math.radians(167)
        self.rect.x = prevX * math.cos(t) + prevY * math.sin(t)
        self.rect.y = -prevX * math.sin(t) + prevY * math.cos(t)
        self.rect.x = self.rect.x / 10
        self.rect.y = self.rect.y / 10
        self.rect.x = self.rect.x + 310
        self.rect.y = self.rect.y + 423