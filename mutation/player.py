import pygame as pg 
import numpy as np

class Player: 
    # PLAYER_SIZE = 31
    # PLAYER_SIZE_H = PLAYER_SIZE // 2
    PLAYER_H = 32
    PLAYER_W = 32

    speeds = {
        'human' : 2,
        'kangaroo' : 2, 
        'eagle' : 2
    }

    jumps = {
        'human' : 10, 
        'kangaroo' : 13, 
        'eagle' : 5
    }

    gravities = {
        'human' : .4, 
        'kangaroo' : .4, 
        'eagle' : .1
    }

    colors = {
        'human' : (200,0,0), 
        'kangaroo' : (190,190,0), 
        'eagle' : (210,50,130)
    }

    def __init__(self, x, y, idle, running): 
        self.type = 'human'
        self.rect = pg.Rect(x,y,self.PLAYER_W,self.PLAYER_H)
        self.x = x 
        self.y = y
        self.left_down = False
        self.right_down = False
        self.velocity = 0
        self.types = list(self.speeds.keys())

        self.animations = {'idle' : {}, 'running' : {}}
        self.animations['idle']['human'] = idle[0]
        self.animations['idle']['kangaroo'] = idle[1]
        self.animations['idle']['eagle'] = idle[2]
        self.animations['running']['human'] = running[0]
        self.animations['running']['kangaroo'] = running[1]
        self.animations['running']['eagle'] = running[2]

        self.running_idx = 0
        self.counter = 0
        self.facing = 'right'

    def update(self, ground, crystals): 

        #set stats based on current type
        speed = self.speeds[self.type]
        
        #update horizontal position
        if self.left_down and not self.horiz_colliding(ground,speed,0):   #left
            self.x -= speed
            self.facing = 'left'
        if self.right_down and not self.horiz_colliding(ground,speed,1): #right
            self.x += speed
            self.facing = 'right'

        #update vertical position
        self.velocity += self.gravities[self.type]
        dir = 0
        if self.velocity >= 0: 
            dir = 1
        if not self.vert_colliding(ground, self.velocity, dir): 
            self.y += self.velocity
        else: 
            self.velocity = 0

        if self.y > 480: 
            self.respawn(100,50)
            for crystal in crystals: 
                crystal.active = True 
            return

        #check colliding with crystals 
        for crystal in crystals: 
            if crystal.active:
                x,y,t = crystal.get_attributes()
                if np.sqrt((x-self.x)**2 + (y-self.y)**2) <= crystal.CRYSTAL_SIZE_H + self.PLAYER_W: 
                    crystal.active = False
                    self.type = t

        self.rect.x = self.x 
        self.rect.y = self.y

        if False: 
            print('X: {x}  Y: {y}'.format(x=self.x, y=self.y))
            print('Vel: {v}'.format(v=self.velocity))
            print('LEFT: {l}   RIGHT: {r}'.format(l=self.left_down, r=self.right_down))

    def vert_colliding(self, ground, speed, dir): 
        for g in ground: 
            x,y,w,h = g.get_attributes()

            #checking x coords overlap
            if self.x + self.PLAYER_H <= x or self.x >= x + w: 
                continue

            if dir == 0: #up 
                if self.y + speed >= y and self.y + speed <= y + h:
                    return True
            else: #down 
                if self.y + speed + self.PLAYER_H >= y and self.y - speed + self.PLAYER_H <= y + h: 
                    return True 

        return False

    def horiz_colliding(self, ground, speed, dir): 
        for g in ground: 
            x,y,w,h = g.get_attributes()

            if not (self.y >= y - self.PLAYER_W and self.y <= y + h):
                continue 

            if dir == 0:  
                if self.x - speed >= x and self.x - speed <= x + w:
                    return True
            else: 
                if self.x + speed + self.PLAYER_W >= x and self.x + speed + self.PLAYER_W <= x + w:
                    return True

        return False

    def jump(self): 
        speed = 0
        if self.type == 'eagle': 
            speed = self.jumps['eagle']
        else:
            speed = self.jumps[self.type]
            if self.velocity != 0: 
                return 

        self.velocity = -1 * speed

    def show(self, surface): 
        # color = self.colors[self.type]
        # pg.draw.rect(surface, color, self.rect)
        if self.counter >= 40: 
            self.running_idx = (self.running_idx + 1) % 2
            self.counter = 0 
        else: 
            self.counter += 1

        if self.velocity == 0 and not(self.left_down or self.right_down): 

            if self.facing == 'right': 
                sprite = self.animations['idle'][self.type]
            else: 
                sprite = pg.transform.flip(self.animations['idle'][self.type], True, False)
        else: 
            if self.facing == 'right': 
                sprite = self.animations['running'][self.type][self.running_idx]
            elif self.facing == 'left': 
                sprite = pg.transform.flip(self.animations['running'][self.type][self.running_idx], True, False)

        surface.blit(sprite, (self.x,self.y))

    def respawn(self, x,y): 
        self.x = x 
        self.y = y
        self.rect.x = x 
        self.rect.y = y
        self.type = 'human'
