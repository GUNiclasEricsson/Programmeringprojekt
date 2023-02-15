import pygame, sys
from settings import * 
from level import Level


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
icon = pygame.image.load("emoji_man.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Emoji-Man")
clock = pygame.time.Clock()


level = Level()


while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(BG_COLOR)
    level.run()

    # drawing logic 
    pygame.display.update()
    clock.tick(60)
