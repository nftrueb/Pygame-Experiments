import pygame as pg 

class Ground: 

    def __init__(self, x, y, width, height, sprite): 
        self.rect = pg.Rect(x,y,width,height)
        self.sprite, self.w, self.h = sprite
        self.x = x * self.w 
        self.y = y * self.h
        self.width = width * self.w
        self.height = height * self.h

    def show(self, surface): 
        for i in range(self.width // self.w): 
            surface.blit(self.sprite, (self.x + self.w * i, self.y))

    def get_attributes(self): 
        return self.x, self.y, self.width, self.height