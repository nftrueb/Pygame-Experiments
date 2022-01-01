import pygame as pg 

class Crystal: 
    CRYSTAL_SIZE = 25
    CRYSTAL_SIZE_H = 12
    def __init__(self, x, y, new_type, sprite): 
        self.type = new_type 
        self.x = x
        self.y = y 
        self.rect = pg.Rect(x,y,self.CRYSTAL_SIZE,self.CRYSTAL_SIZE)
        self.active = True
        self.center = (x + self.CRYSTAL_SIZE_H, y + self.CRYSTAL_SIZE_H)
        self.sprite, self.w, self.h = sprite

    def show(self, surface): 
        if self.active: 
            surface.blit(self.sprite, (self.x, self.y))

    def get_attributes(self): 
        return self.center[0], self.center[1], self.type
