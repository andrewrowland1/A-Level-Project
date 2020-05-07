import pygame
import random
import math

done = False
size = (1000,1000)
# -- colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
GREEN = (0,255,0)

#A list of all sprites
all_sprites_list = pygame.sprite.Group()

# Create a list of tiles for the walls and the player
wall_list = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
bullet_pu_list = pygame.sprite.Group()
zombie_list = pygame.sprite.Group()
health_pu_list = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
    # Define the constructor
    def __init__(self,color,width,height,x_ref,y_ref):

        # Call the sprite constructor
        super().__init__()

        #Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.image = pygame.image.load("brick_wall.png").convert()
        self.rect = self.image.get_rect()

        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    # End procedure
# End Class

#Create enemy class
class Zombie(pygame.sprite.Sprite):
    #Define the constructor
    def __init__(self,color,width,height,x_zombie,y_zombie):
        # Call the sprite constructor
        super().__init__()

        #Create a sprite and fill it with a colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        #Position of player attributes
        self.rect.x = x_zombie
        self.rect.y = y_zombie
    #End procedure
#End Class


class Player(pygame.sprite.Sprite):

    #Constructor
    def __init__(self, color, width, height):
        self.speed_x = 0
        self.speed_y = 0
        self.bullet_count = 10
        self.lives_count = 5
        self.zombies_killed = 0

        # Call the sprite constructor
        super().__init__()

        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        # Set position of sprite
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
    # End procedure

    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= size[0]:

            self.rect.x = size[0] - 10
    # End procedure

    def player_set_speed_x(self, val):
        self.speed_x = val
    # End procedure

    def player_set_speed_y(self,val):
        self.speed_y = val
    #End procedure
    def shoot_up(self):
        my_bullet = Bullet(self.rect.x,self.rect.y,0,-1)
        bullet_group.add(my_bullet)
        self.bullet_count += -1
        all_sprites_list.add(my_bullet)
        #If player is facing up, the bullet shoots up
    def shoot_down(self):
        my_bullet = Bullet(self.rect.x,self.rect.y,0,1)
        bullet_group.add(my_bullet)
        self.bullet_count += -1
        all_sprites_list.add(my_bullet)
        #If player is facing down, then bullet shoots down
    def shoot_right(self):
        my_bullet = Bullet(self.rect.x,self.rect.y,1,0)
        bullet_group.add(my_bullet)
        self.bullet_count += -1
        all_sprites_list.add(my_bullet)
        #If player is facing right, the bullet will shoot right
    def shoot_left(self):
        my_bullet = Bullet(self.rect.x,self.rect.y,-1,0)
        bullet_group.add(my_bullet)
        self.bullet_count +=-1
        all_sprites_list.add(my_bullet)
        #If player if facing left, the bullet will shoot left
#End Class

class Bullet(pygame.sprite.Sprite):

    #Constructor
    def __init__(self,x,y,speed_x,speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([10,10])
        self.image.fill((255,0,0))
        # Set position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    # End Procedure

    def update(self):
        self.rect.y = self.rect.y + self.speed_y
        self.rect.x = self.rect.x + self.speed_x
    # End Procedure
# End Class

class Bullet_pu(pygame.sprite.Sprite):

    def __init__(self,color,width,height,x_ref,y_ref):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        
class Health_pu(pygame.sprite.Sprite):

    def __init__(self,color,width,height,x_ref,y_ref):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #End procedure
#End class