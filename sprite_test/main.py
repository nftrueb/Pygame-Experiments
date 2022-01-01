import pygame
from spritesheet import Spritesheet

################################# LOAD UP A BASIC WINDOW #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 480, 270
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
###########################################################################################

sprite_sheet = Spritesheet('../mutation/assets/numbers.png')
number = sprite_sheet.get_sprite(8*4,0,8,16)
number2 = pygame.transform.scale(number, (8*3,16*3))
# my_spritesheet = Spritesheet('trainer_sheet_two.png')
# trainer = [my_spritesheet.parse_sprite('trainer1.png'), my_spritesheet.parse_sprite('trainer2.png'),my_spritesheet.parse_sprite('trainer3.png'),
#            my_spritesheet.parse_sprite('trainer4.png'),my_spritesheet.parse_sprite('trainer5.png')]
# f_trainer = [my_spritesheet.parse_sprite('f_trainer1.png'), my_spritesheet.parse_sprite('f_trainer2.png'),my_spritesheet.parse_sprite('f_trainer3.png'),
#            my_spritesheet.parse_sprite('f_trainer4.png'),my_spritesheet.parse_sprite('f_trainer5.png')]
# index = 0

while running:
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
            ############### UPDATE SPRITE IF SPACE IS PRESSED #################################
            # if event.key == pygame.K_SPACE:
            #     index = (index + 1) % len(trainer)


    ################################# UPDATE WINDOW AND DISPLAY #################################
    canvas.fill((255,255,255))
    canvas.blit(number, (0,0))
    canvas.blit(number2, (0,20))
    # canvas.blit(trainer[index], (0, DISPLAY_H - 128))
    # canvas.blit(f_trainer[index], (128, DISPLAY_H - 128))
    window.blit(canvas, (0,0))
    pygame.display.update()