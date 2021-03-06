import pygame
from math import hypot
from pygame.sprite import Sprite

class BadGuy(Sprite):
    def __init__(self):
        super(BadGuy,self).__init__()
        self.x = 400
        self.y = 400
        self.speed = 2
        self.rect = pygame.Rect(0,0,64,64)
        self.rect.centerx = self.x
        self.rect.centery = self.y
    
    def update_me(self, theHero):
        dx = self.x - theHero.x
        dy = self.y - theHero.y
        dist = hypot(dx, dy)
        dx = dx / dist
        dy = dy /dist
        self.x -= dx * self.speed
        self.y -= dy * self.speed
        self.rect.centerx = self.x
        self.rect.centery = self.y