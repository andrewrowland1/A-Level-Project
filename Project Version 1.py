import pygame
import random
import math
# -- Global constants
map = [[1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,1],
       [1,1,0,0,1,1,1,1,1,0,1],
       [1,0,0,0,0,0,0,1,0,0,1],
       [1,0,0,0,0,0,0,1,0,0,1],
       [1,0,0,1,1,1,0,1,0,0,1],
       [1,0,0,1,1,1,0,1,0,0,1],
       [1,0,0,1,1,1,0,1,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1]]

## -- Define the class title which is a sprite
class Tile(pygame.sprite.Sprite):
    # Define the constructor
    def __init__(self,color,width,height,x_ref,y_ref):
        # Call the sprite constructor
        super().__init__()
        #Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
# End Class


# -- colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)


# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode((size), pygame.FULLSCREEN)

# -- Title of new window/screen
pygame.display.set_caption("Escape")

# -- Exit game flag set to false
done = False

# --Manages how fast screen refreshes
clock = pygame.time.Clock()

# Create a list of all sprites
all_sprites_list = pygame.sprite.Group()

# Create a list of tiles for the walls and the player
wall_list = pygame.sprite.Group()

# Create walls on the screen (each tile is 20x20 so alter cords)
for y in range(11):
    for x in range(12):
        if map[x][y] == 1:
            my_wall = Tile(BLUE,20,20,x*20,y*20)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)


# -- Game Loop
while not done:
    # -- User input and controls
    

    # -- Game logic goes after this comment
    
    
    
    
    
    all_sprites_list.update()
    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    all_sprites_list.draw(screen)
    

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # -- The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
