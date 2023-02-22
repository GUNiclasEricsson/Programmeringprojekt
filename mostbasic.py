# https://realpython.com/pygame-a-primer/ -----------------------------------------------

# importing the pygame library/package 
import pygame 
# initialize the library/modules
pygame.init()

# creating the window/screen that the graphics are drawn on, given a tuple as an argument 
# this is from the Surface-class, and is returning a Surface which we pass into other functions
# as the .draw.circle() beneath
screen = pygame.display.set_mode((500, 500))


# define a variable that is True
running = True
# creating a while loop that is running until the user quits the game
while running: 

    # checks the events/inputs using a for-loop that goes through each event in the pygame.event
    for event in pygame.event.get():
        # an if statement for the above for-loop that checks for the the event of clicking the "x-button"
        if event.type == pygame.QUIT:
            running = False


    # fills the screen/background with a color, given a tuple with RGB values as an argument
    screen.fill((122, 125, 100))

    # draws a circle, to the display/window, with the color as an RGB tuple, 
    # pixel coordinates as position in a tuple, the radius of the circle  
    pygame.draw.circle(screen, (0, 200, 0), (250, 250), 100)

    # "flips" the display, refreshing the screen/window with the above drawn graphics 
    # on the Surface in the screen-variable
    pygame.display.flip()

# makes sure the program is shutdown after exiting the main while-loop
pygame.quit()






















