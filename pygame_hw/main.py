import pygame, sys 

size = width, height = 1000,800 

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Hello World')
player = pygame.Rect(100,100,50,50)

while 1: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
            sys.exit()
        # elif event.type == pygame.KEYDOWN: 
        #     print(event)
        #     if event.key == pygame.K_LEFT: 
        #         velx -= 1
        #     elif event.key == pygame.K_RIGHT: 
        #         velx += 1
        #     elif event.key == pygame.K_DOWN: 
        #         vely += 1 
        #     elif event.key == pygame.K_UP: 
        #         vely -= 1

    velx, vely = 0,0
    mx, my = pygame.mouse.get_pos()
    if player.centerx < mx: 
        velx += 1 
    elif player.centerx > mx: 
        velx -= 1 
    if player.centery < my: 
        vely += 1 
    elif player.centery > my: 
        vely -= 1 
    player = player.move(velx,vely)

    player_color = 255,255,255
    BG = 150,0,100
    screen.fill(BG)
    screen.fill(player_color, player)
    pygame.display.flip()

