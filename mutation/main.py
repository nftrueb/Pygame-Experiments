import pygame as pg
from pygame.constants import K_a, K_d
from pygame.sprite import Sprite
from player import Player
from ground import Ground
from crystal import Crystal
from gate import Gate
from spritesheet import Spritesheet

class Application: 

    def __init__(self, title, width, height, cell): 
        pg.init()
        self.width, self.height = width, height
        self.screen = pg.display.set_mode((width,height))
        pg.display.set_caption(title)
        self.running = True 
        self.clock = pg.time.Clock()
        self.clock.tick(20)
        self.cell = cell

        #sprite_sheet = Spritesheet(fn) # pass to player, ground, crystal, etc
        cell_size_ss = Spritesheet('./assets/Sprite-0006.png',2)
        idle = [cell_size_ss.load_sprite_name('Sprite-0006 1.png')[0], cell_size_ss.load_sprite_name('Sprite-0006 4.png')[0],
                cell_size_ss.load_sprite_name('Sprite-0006 7.png')[0]]
        run_sprite = [(cell_size_ss.load_sprite_name('Sprite-0006 2.png')[0], cell_size_ss.load_sprite_name('Sprite-0006 3.png')[0]),
                        (cell_size_ss.load_sprite_name('Sprite-0006 5.png')[0], cell_size_ss.load_sprite_name('Sprite-0006 6.png')[0]),
                        (cell_size_ss.load_sprite_name('Sprite-0006 7.png')[0], cell_size_ss.load_sprite_name('Sprite-0006 8.png')[0])]
        self.player = Player(100,100, idle, run_sprite)

        ground_sprite = cell_size_ss.load_sprite_name('Sprite-0006 0.png')
        self.ground = [[Ground(2, 6, 3, 1, ground_sprite), 
                        Ground(5, 7, 1, 1, ground_sprite),
                        Ground(6, 6, 3, 1, ground_sprite),
                        Ground(9, 12, 3, 1, ground_sprite),
                        Ground(15, 6, 4, 1, ground_sprite)]]


        crystal_sprite_sheet = Spritesheet('./assets/crystal.png')
        k_crystal_sprite = crystal_sprite_sheet.load_sprite_name('crystral 0.png')
        e_crystal_sprite = crystal_sprite_sheet.load_sprite_name('crystral 1.png')
        self.crystals = [[  Crystal(250, 150, 'kangaroo', k_crystal_sprite), 
                            Crystal(350, 350, 'eagle', e_crystal_sprite)]]

        gate_ss = Spritesheet('./assets/crystal.png', 2)
        gate_sprite = gate_ss.load_sprite_name('crystral 2.png')
        self.gates = [Gate(550,125,gate_sprite)]

        self.curr_level = 0

    def mainloop(self): 
        while self.running: 
            for event in pg.event.get(): 
                if event.type == pg.QUIT: 
                    self.running = False 

                if event.type == pg.MOUSEBUTTONDOWN: 
                    print(event)
                    print('X: {x}   Y: {y}'.format(x=event.pos[0]//self.cell, y=event.pos[1]//self.cell))

                if event.type == pg.KEYDOWN: 
                    if event.key == pg.K_ESCAPE: 
                        self.running = False 

                    elif event.key == pg.K_RSHIFT: 
                        print(self.player.type)

                    elif event.key == pg.K_a or event.key == pg.K_LEFT: 
                        self.player.left_down = True

                    elif event.key == pg.K_d or event.key == pg.K_RIGHT: 
                        self.player.right_down = True

                    elif event.key == pg.K_w or event.key == pg.K_SPACE or event.key == pg.K_UP: 
                        self.player.jump()

                if event.type == pg.KEYUP:
                    if event.key == K_a or event.key == pg.K_LEFT: 
                        self.player.left_down = False 

                    if event.key == K_d or event.key == pg.K_RIGHT: 
                        self.player.right_down = False

            #background color
            self.screen.fill((200,200,255))

            #update and show player
            self.player.update(self.ground[self.curr_level], self.crystals[self.curr_level])
            self.player.show(self.screen)
            
            #show gate
            self.gates[self.curr_level].show(self.screen)

            #show crystals
            for crystal in self.crystals[self.curr_level]: 
                crystal.show(self.screen)

            #show grounds
            for g in self.ground[self.curr_level]: 
                g.show(self.screen)

            if False: 
                for i in range(self.height // self.cell):  
                    pg.draw.line(self.screen, (255,0,0), (0, i * self.cell), (self.width, i * self.cell))
                        
                for j in range(self.width // self.cell): 
                    pg.draw.line(self.screen, (255,0,0), (j * self.cell, 0), (j * self.cell, self.height))

            pg.display.flip()


def main(): 
    app = Application('Mutation', 640, 480, 32)
    app.mainloop()

if __name__ == '__main__': 
    main()