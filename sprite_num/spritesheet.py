import pygame as pg 
import json

class Spritesheet: 

    def __init__(self, filename, scale=1): 
        self.fn = filename
        self.sprite_sheet = pg.image.load(self.fn).convert() 
        self.scale = scale
        with open(filename[:-4]+'.json','r') as f: 
            self.json = json.load(f)

    def get_sprite(self, x, y, w, h): 
        sprite = pg.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet, (0,0), (x,y,w,h))
        sprite = pg.transform.scale(sprite, (int(w*self.scale), int(h*self.scale)))
        return sprite, w*self.scale, h*self.scale

    def load_sprite_name(self, name): 
        data = self.json['frames'][name]['frame']
        x,y,w,h = data['x'], data['y'], data['w'], data['h']
        return self.get_sprite(x,y,w,h)
