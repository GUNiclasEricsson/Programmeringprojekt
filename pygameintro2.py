# Pygame introduction

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('First')
clock = pygame.time.Clock()

def display_score():
    current_time = pygame.time.get_ticks()
    score_surf = test_font.render(current_time, False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    print(current_time)

test_font = pygame.font.Font('fonts/RETRO_SPACE.ttf', 50)

sky_surf = pygame.image.load('images/sky.png').convert()
ground_surf = pygame.image.load('images/Ground.png').convert()

#score_surf = test_font.render('First', False, (64, 64, 64))
#score_rect = score_surf.get_rect(center = (400, 100))

snail_surf = pygame.image.load('images/snail1.gif').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('images/spr_greaser.png').convert_alpha()
player_rect = player_surf.get_rect(topleft = (80, 270))
player_gravity = 0

game_active = True



while True:
    for event in pygame.event.get():
    # draw all our elements, and updates everything
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity -= 17



    if game_active:

        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,300))
        #pygame.draw.rect(screen, "#c0e8ec", score_rect)
        #pygame.draw.rect(screen, "#c0e8ec", score_rect,10)
        #screen.blit(score_surf, score_rect)
        display_score()





        snail_rect.x -= 2
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surf, (snail_rect))
        player_rect.left += 1
        screen.blit(player_surf, player_rect)

        #Player
        player_gravity += 0.3
        player_rect.y += player_gravity
        #print(player_gravity)
        #print(player_rect.y)

        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        if player_rect.colliderect(snail_rect):
            game_active = False


    else:
        screen.fill("Yellow")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_active = True
                snail_rect.left = 800
                player_rect.left = 80



    pygame.display.update()
    clock.tick(60)




#------------------------------------------------------------------------------------------------------------------------------------------------------------

    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #    print("jump")
    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.colliderect(snail_rect):
    #    print("collision")
    #if player_rect.collidepoint(mouse_pos):
      #  print(pygame.mouse.get_pressed())
          #if player_rect.collidepoint (ground_surf.y):
    #    player_gravity == 0

        #pygame.draw.ellipse(screen, "Brown",pygame.Rect(50, 200, 100, 100))
    #pygame.draw.line(screen, "Blue", (0, 0), (pygame.mouse.get_pos()), 10)
    #def apply_gravity (self):
     #   player_gravity.y += self.gravity
      #  self.player_rect.y += self.gravity
       # if event.type == pygame.MOUSEMOTION:
          #  if player_rect.collidepoint(event.pos):
              #  print("collision")
