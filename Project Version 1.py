import pygame
import random
import math
font_name = pygame.font.match_font('calibri')

# -- Global constants
map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], ##
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], ##
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


## -- Define the class title which is a sprite
class Tile(pygame.sprite.Sprite):
    # Define the constructor
    def __init__(self,color,width,height,x_ref,y_ref):

        # Call the sprite constructor
        super().__init__()

        #Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.image = pygame.image.load("brick_wall.png")
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
#End Class

class Bullet(pygame.sprite.Sprite):

    #Constructor
    def __init__(self,color,width,height,speed_x,speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = user.rect.x + 9
        self.rect.y = user.rect.y + 9
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

#Function that draws text
def draw_text(surf,text,size,x_val,y_val):
        font = pygame.font.Font(font_name, size)
        text = font.render(text, True, WHITE)
        text_rect = text.get_rect()
        text_rect.midtop = (x_val, y_val)
        surf.blit(text, text_rect)
#End procedure

# -- colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (1000,1000)
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
bullet_group = pygame.sprite.Group()
bullet_pu_list = pygame.sprite.Group()
zombie_list = pygame.sprite.Group()

counter = 0
count = 0

# Create walls on the screen (each tile is 20x20 so alter cords)
for x in range(50):

    for y in range(50):

        #Creates the walls on the map
        if map[y][x] == 1:
            my_wall = Tile(BLUE,20,20,x*20,y*20)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)

        #Spawns powerups in random locations on the map
        while counter != 5:
            random_x = random.randint(1,49)
            random_y = random.randint(1,49)

            if map[random_y][random_x] == 0:
                pu_bullet = Bullet_pu(WHITE,20,20,random_x*20,random_y*20)
                bullet_pu_list.add(pu_bullet)
                all_sprites_list.add(pu_bullet)
                counter += 1

        #Spawns zombies in random locations on the map. Cannot spawn on walls
        while count != 20:
            rand_zomb_x = random.randint(1,49)
            rand_zomb_y = random.randint(1,49)

            if map [rand_zomb_y][rand_zomb_x] == 0:
                zombie = Zombie(YELLOW,20,20,rand_zomb_x*20,rand_zomb_y*20)
                all_sprites_list.add(zombie)
                zombie_list.add(zombie)
                count += 1








# Create player on the screen
user = Player(RED,18,18)
all_sprites_list.add(user)
facing = "right"

# -- Game Loop
while not done:
    # -- User input and controls

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        #Movement controls: right, left, up, down. When key is released, player stops moving
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                user.player_set_speed_x(-2)
                facing = "left"

            elif event.key == pygame.K_RIGHT:
                user.player_set_speed_x(2)
                facing = "right"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                user.player_set_speed_x(0)

            elif event.key == pygame.K_LEFT:
                user.player_set_speed_x(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                user.player_set_speed_y(-2)
                facing = "up"

            elif event.key == pygame.K_DOWN:
                user.player_set_speed_y(2)
                facing = "down"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                user.player_set_speed_y(0)

            if event.key == pygame.K_DOWN:
                user.player_set_speed_y(0)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and user.bullet_count > 0 and facing == "left":
                my_bullet = Bullet(RED,5,5,-5,0)
                bullet_group.add(my_bullet)
                user.bullet_count +=-1
                all_sprites_list.add(my_bullet)
                #If player if facing left, the bullet will shoot left

            elif event.key == pygame.K_SPACE and user.bullet_count > 0 and facing == "right":
                my_bullet = Bullet(RED,5,5,5,0)
                bullet_group.add(my_bullet)
                user.bullet_count += -1
                all_sprites_list.add(my_bullet)
                #If player is facing right, the bullet will shoot right

            elif event.key == pygame.K_SPACE and user.bullet_count > 0 and facing == "up":
                my_bullet = Bullet(RED,5,5,0,-5)
                bullet_group.add(my_bullet)
                user.bullet_count += -1
                all_sprites_list.add(my_bullet)
                #If player is facing up, the bullet shoots up

            elif event.key == pygame.K_SPACE and user.bullet_count > 0 and facing == "down":
                my_bullet = Bullet(RED,5,5,0,5)
                bullet_group.add(my_bullet)
                user.bullet_count += -1
                all_sprites_list.add(my_bullet)
                #If player is facing down, then bullet shoots down

        # -- Game logic goes after this comment

        #If plyaer collides with a zombie, their number of lives decreases by 1
        user_hit_group = pygame.sprite.spritecollide(user, zombie_list, True)
        for hit in user_hit_group:
            user.lives_count += -1
        #If player runs out of lives, the game quits
        if user.lives_count < 1:
            done = True


        #When a bullet collides with a zombie, the zombie is removed
        for bullet_shot in bullet_group:
            zombie_hit_list = pygame.sprite.spritecollide(bullet_shot, zombie_list, True)
            for bullet_shot in zombie_hit_list:
                bullet_group.remove(my_bullet)
                all_sprites_list.remove(my_bullet)
                user.zombies_killed += 1

    #If player collides with a powerup, the powerup gets deleted, and the player's number of bullets increases
    powerup_hit_list = pygame.sprite.spritecollide(user, bullet_pu_list, True)
    for pu_bullet in powerup_hit_list:
        user.bullet_count += 10
        bullet_pu_list.remove(pu_bullet)
        all_sprites_list.remove(pu_bullet)

    #If player collides with the wall,they go back to their previous x and y value
    player_hit_list = pygame.sprite.spritecollide(user, wall_list, False)
    for x in player_hit_list:

        user.player_set_speed_y(0)
        user.player_set_speed_x(0)
        user.rect.x = user_old_x
        user.rect.y = user_old_y

    user_old_x = user.rect.x
    user_old_y = user.rect.y


    all_sprites_list.update()
    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    all_sprites_list.draw(screen)
    draw_text(screen, str("Bullets: %d" % user.bullet_count),20,40,40)
    draw_text(screen, str("Zombies Killed: %d" % user.zombies_killed),20,70,60)
    draw_text(screen, str("Lives: %d" % user.lives_count),20,40,80)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # -- The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
