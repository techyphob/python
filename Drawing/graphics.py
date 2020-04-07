import pygame
import math

pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

WIDTH = 700
HEIGHT = 500
size = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False
count = 0 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYUP:
            if event.key == 113:
                done = True
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
     # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    x = 50
    pygame.draw.rect(screen, RED, [x, 55, 20, 25], 0)
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # Draw on the screen several lines from (0,10) to (100,110)
    # 5 pixels wide using a for loop
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5)
    for x_offset in range(30, 300, 30):
        pygame.draw.line(screen,BLACK,[x_offset,100],[x_offset-10,90],2)
        pygame.draw.line(screen,BLACK,[x_offset,90],[x_offset-10,100],2)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    count = count + 1
pygame.quit()




