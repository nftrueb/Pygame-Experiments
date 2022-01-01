import pygame as pg

def main():
    pg.init()
    size = (400,400)
    screen = pg.display.set_mode(size) 
    running = True

    colors = [(255,0,0),(100,100,0),(0,255,0),(0,100,100),(0,0,255),(100,0,100)]
    curr_idx = 0 

    while running: 
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                running = False
            elif event.type == pg.KEYDOWN: 
                if event.key == pg.K_ESCAPE: 
                    running = False
            elif event.type == pg.MOUSEWHEEL: 
                print(event)
                if event.y == -1: 
                    curr_idx = (curr_idx + 1) % len(colors)
                if event.y == 1: 
                    curr_idx = (curr_idx - 1) % len(colors)
        
        screen.fill(colors[curr_idx])
        pg.display.flip()

if __name__ == '__main__': 
    main()