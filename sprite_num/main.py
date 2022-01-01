import pygame as pg 
from spritesheet import Spritesheet

def main(): 
    size = width,height = 640,480 
    screen = pg.display.set_mode(size)
    running = True 

    sprite_sheet = Spritesheet('./numbers.png', 2)
    temp,_,_ = sprite_sheet.load_sprite_name('Sprite-0003 5.')
    numbers = [sprite_sheet.get_sprite(8*i,0,8,16) for i in range(10)]
    score = 400
    startx = width * .05 
    starty = height * .05

    timer_event = pg.USEREVENT + 1
    pg.time.set_timer(timer_event, 1000)

    while running: 
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                running = False 
            elif event.type == timer_event: 
                score -= 1
            elif event.type == pg.KEYDOWN: 
                if event.key == pg.K_ESCAPE: 
                    running = False 
                if ord(event.unicode) >= 48 and ord(event.unicode) <= 57: 
                    score *= 10
                    score += int(event.unicode)

        screen.fill((255,255,255))

        #print number sprites for score
        for i in range(len(str(score))): 
            sprite = numbers[int(str(score)[i])]
            screen.blit(sprite[0],(startx+(sprite[1]+2)*i, starty))

        screen.blit(temp, (200,200))

        pg.display.flip()


if __name__ == '__main__': 
    main()