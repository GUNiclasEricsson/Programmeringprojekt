# Pygame introduction

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('First')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/RETRO_SPACE.ttf', 50)

sky_surf = pygame.image.load('Sky.png').convert()
ground_surf = pygame.image.load('Ground.png').convert()

score_surf = test_font.render('First', False, 'Black')
score_rect = score_surf.get_rect(center = (400, 100))

snail_surf = pygame.image.load('images/snail1.gif').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('images/player/spr_greaser.png').convert_alpha()
player_rect = player_surf.get_rect(topleft = (80, 270))



while True:
    for event in pygame.event.get():
    # draw all our elements, and updates everything
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

       # if event.type == pygame.MOUSEMOTION:
          #  if player_rect.collidepoint(event.pos):
              #  print("collision")


            #Use the event loop to checck if the mouse is collidiong with the player rectangle

    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(0,300))
    pygame.draw.rect(screen, "Pink", score_rect)
    pygame.draw.rect(screen, "Pink", score_rect,10)
    pygame.draw.line(screen, "Blue", (0, 0), (800, 400), 10)
    #pygame.draw.line(screen, "Blue", (60, 80), (130, 100), 10)
    screen.blit(score_surf, score_rect)


    #Draw a line from the topleft to the bottom right

    snail_rect.x -= 2
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, (snail_rect))
    player_rect.left += 1
    screen.blit(player_surf, (player_rect))

    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.colliderect(snail_rect):
    #    print("collision")
    #if player_rect.collidepoint(mouse_pos):
      #  print(pygame.mouse.get_pressed())


    pygame.display.update()
    clock.tick(60)
