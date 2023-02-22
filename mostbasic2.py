# https://realpython.com/pygame-a-primer/ -----------------------------------------------

# importing the pygame library/package
import pygame

# importing constants for easier/quicker access to inputs
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# defining constants to use as screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



# initialize the library/modules
pygame.init()

# creating the window/screen that the graphics are drawn on, given a tuple as an argument
# this is from the Surface-class, and is returning a Surface which we pass into other functions
# such as the .draw.circle() beneath
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# fills the screen/background with a color, given a tuple with RGB values as an argument
screen.fill("red")


# creates an instance/object of the Surface-class,
# given the dimensions as an argument in a tuple
surf = pygame.Surface((150, 50))

# fills the above instance surface with
# an argument of a tuple with the RGB of black
surf.fill((0, 0, 0))
# gets the underlying Rect from the above instance of a surface in surf-variable
# in a new variable named "rect"
rect = surf.get_rect()


# define a variable that is True
running = True
# creating a while loop that is running until the user quits the game
while running:

    # checks the events/inputs using a for-loop that goes through
    # each event in the pygame.event queue
    for event in pygame.event.get():
        # if the event from the event get above is a key pressed down
        if event.type == KEYDOWN:
            # checks to see if the key pressed was the ESCape key
            if event.key == K_ESCAPE:
                # sets the main while-loop dependent variable to False
                running = False



        # an if statement for the above for-loop that checks for the the event of clicking the "x-button"
        elif event.type == pygame.QUIT:
            running = False

    # blit the surf to the screen
    # blit = Block Transfer --> it transfers one surface to another
    # from the "surf" surface to the "screen" surface
    # argument is taken for the surface to be transfered and
    # a tuple with the position
    screen.blit(surf, (250, SCREEN_HEIGHT / 2))


    # "flips" the display, refreshing the screen/window with the above drawn graphics
    # on the Surface in the screen-variable


    # draws a circle, to the display/window, with the color as an RGB tuple,
    # pixel coordinates as position in a tuple, the radius of the circle
    pygame.draw.circle(screen, (0, 200, 0), (250, 250), 100)

    pygame.display.flip()


# stope the initializing and makes sure the program is shutdown
# after exiting the main while-loop
pygame.quit()






















