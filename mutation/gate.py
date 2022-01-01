import pygame as pg 

class Gate:
    
    def __init__(self, x, y, sprite): 
        self.x = x 
        self.y = y
        self.sprite, self.w, self.h = sprite
        self.GATE_SIZE, self.GATE_SIZE_H = self.w, self.w // 2

    def show(self, surface): 
        surface.blit(self.sprite, (self.x, self.y))