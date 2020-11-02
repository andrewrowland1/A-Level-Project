import pygame
import random
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
        self.zombie_old_x = x_zombie
        self.zombie_old_y = y_zombie
        self.speed_y = 1
        self.speed_x = 1
        
    #End procedure
#End Class
class FollowerZombie(Zombie):
    def update(self):
        if user.rect.x > self.rect.x:
            self.rect.x = self.rect.x + self.speed_x
        if user.rect.x < self.rect.x:
            self.rect.x = self.rect.x - self.speed_x
        if user.rect.y > self.rect.y:
            self.rect.y = self.rect.y + self.speed_y
        if user.rect.y < self.rect.y:
            self.rect.y = self.rect.y - self.speed_y
        #if zombie collides with the wall, they will go back to their previous x and y value
        
        for x in pygame.sprite.spritecollide(self, wall_list, False):
            self.rect.x = self.zombie_old_x
            self.rect.y = self.zombie_old_y
            
            
        self.zombie_old_x = self.rect.x
        self.zombie_old_y = self.rect.y
    #End procedure
    def zombie_set_speed_x(self, val):
        self.speed_x = val
    # End procedure
    def zombie_set_speed_y(self, val):
        self.speed_y = val
    # End procedure
#End class
    
class RandZombie(Zombie):
    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        diff_speed_list = [-1,1]
        randhit = pygame.sprite.spritecollide(self, wall_list, False)
        for hit in randhit:
            
            self.speed_x *= random.choice(diff_speed_list)
            self.speed_y *= random.choice(diff_speed_list)
    #End Procedure
#End class
            
        
            
    
    
            
    
class BounceZombie(Zombie):
    
    def update(self):
        
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        
        bouncehit = pygame.sprite.spritecollide(self, wall_list, False)
        if len(bouncehit) > 0:
            self.speed_x *= -1
            self.speed_y *= -1
                
        
        
    #End procedure
    def zombie_set_speed_x(self, val):
        self.speed_x = val
    # End procedure
    def zombie_set_speed_y(self, val):
        self.speed_y = val
    # End procedure
    
        
#End Class
    

class Player(pygame.sprite.Sprite):

    #Constructor
    def __init__(self, color, width, height):
        self.speed_x = 0
        self.speed_y = 0
        self.bullet_count = 10
        self.lives_count = 1
        self.zombies_killed = 0

        # Call the sprite constructor
        super().__init__()

        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        # Set position of sprite
        self.rect = self.image.get_rect()
        self.rect.centerx = size[0] / 2
        self.rect.bottom = size[1] / 2
        #Declares the Players previous x and y values
        self.old_x = self.rect.x
        self.old_y = self.rect.y
    # End procedure

    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        
        #If player collides with the wall,they go back to their previous x and y value
        player_hit_list = pygame.sprite.spritecollide(user, wall_list, False)
        for x in player_hit_list:
    
            self.player_set_speed_y(0)
            self.player_set_speed_x(0)
            self.rect.x = self.old_x
            self.rect.y = self.old_y
            
        #Updates the players old x and y values with its current x and y values
        self.old_x = self.rect.x
        self.old_y = self.rect.y
        
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
    def __init__(self,colour,x,y,speed_x,speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([10,10])
        self.image.fill(colour)
        # Set position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    # End Procedure

    def update(self):
        self.rect.y = self.rect.y + self.speed_y
        self.rect.x = self.rect.x + self.speed_x
        if self.rect.x > 1000:
            self.kill()
        if self.rect.y > 1000:
            self.kill()
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
    #End procedure
#End class
        
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

#Function that draws text on screen
def draw_text(surf,text,size,x_val,y_val):
        font = pygame.font.Font(font_name, size)
        text = font.render(text, True, WHITE)
        text_rect = text.get_rect()
        text_rect.midtop = (x_val, y_val)
        surf.blit(text, text_rect)
#End procedure

def spawn_health_pu():
    counter = 0
    while counter != 5:
        random_x = random.randint(1,49)
        random_y = random.randint(1,49)
            
        if map[random_y][random_x] == 0:
            pu_health = Health_pu(GREEN,20,20,random_x*20,random_y*20)
            health_pu_list.add(pu_health)
            all_sprites_list.add(pu_health)
            counter += 1
        #End if
    #Endwhile
#End procedure

def spawn_bullet_pu():
    counter = 0
    while counter != 5:
        random_x = random.randint(1,49)
        random_y = random.randint(1,49)

        if map[random_y][random_x] == 0:
            pu_bullet = Bullet_pu(WHITE,20,20,random_x*20,random_y*20)
            bullet_pu_list.add(pu_bullet)
            all_sprites_list.add(pu_bullet)
            counter += 1
        #End if
    #Endwhile
#End procedure

def shoot_up():
    my_bullet = Bullet(RED,user.rect.x,user.rect.y,0,-5)
    bullet_group.add(my_bullet)
    user.bullet_count += -1
    all_sprites_list.add(my_bullet)
    #If player is facing up, the bullet shoots up
#End procedure
    
def shoot_down():
    my_bullet = Bullet(RED,user.rect.x,user.rect.y,0,5)
    bullet_group.add(my_bullet)
    user.bullet_count += -1
    all_sprites_list.add(my_bullet)
    #If player is facing down, then bullet shoots down
#End procedure
    
def shoot_right():
    my_bullet = Bullet(RED,user.rect.x,user.rect.y,5,0)
    bullet_group.add(my_bullet)
    user.bullet_count += -1
    all_sprites_list.add(my_bullet)
    #If player is facing right, the bullet will shoot right
#End procedure
    
def shoot_left():
    my_bullet = Bullet(RED,user.rect.x,user.rect.y,-5,0)
    bullet_group.add(my_bullet)
    user.bullet_count +=-1
    all_sprites_list.add(my_bullet)
    #If player if facing left, the bullet will shoot left
#End procedure

def menu_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #End if
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    pygame.quit()
                #End if
            #End if
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True
                    game_loop()
                if event.key == pygame.K_RETURN:
                    done = True
                    help_screen()
        screen.fill(BLACK)
        draw_text(screen, str("Press the spacebar to play or press the return key to view how to play"),30,500,500)
        pygame.display.update()
def help_screen():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #End if
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    pygame.quit()
                #End if
            #End if
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
                    menu_screen()
        screen.fill(BLACK)
        draw_text(screen, str("To move, use the arrow keys"),30,500,200)
        draw_text(screen, str("To shoot, press the space bar"),30,500,400)
        draw_text(screen, str("The gun will shoot in the direction of your last movement"),30,500,450)
        draw_text(screen, str("To quit the game, press the escape key"),30,500,600)
        draw_text(screen, str("Press the return key to return to the main menu"),30,500,800)
        pygame.display.update()
    
def game_loop():
    done = False
    while not done:
    # -- User input and controls

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #End if
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                #End if
            #End if
            #Movement controls: right, left, up, down. When key is released, player stops moving
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    user.player_set_speed_x(-2)
                    facing = "left"
    
                elif event.key == pygame.K_RIGHT:
                    user.player_set_speed_x(2)
                    facing = "right"
                #End if
            #End if
    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    user.player_set_speed_x(0)
    
                elif event.key == pygame.K_LEFT:
                    user.player_set_speed_x(0)
                #End if
            #End if
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    user.player_set_speed_y(-2)
                    facing = "up"
    
                elif event.key == pygame.K_DOWN:
                    user.player_set_speed_y(2)
                    facing = "down"
                #End if
            #End if
    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    user.player_set_speed_y(0)
                #End if
    
                if event.key == pygame.K_DOWN:
                    user.player_set_speed_y(0)
                #End if
            #End if
    
            if event.type == pygame.KEYDOWN:
    
                if event.key == pygame.K_SPACE and user.bullet_count > 0 and facing == "left":
                    shoot_left()
    
                elif event.key == pygame.K_SPACE and user.bullet_count > 0 and facing == "right":
                    shoot_right()
    
                elif event.key == pygame.K_SPACE and user.bullet_count > 0 and facing == "up":
                    shoot_up()
    
                elif event.key == pygame.K_SPACE and user.bullet_count > 0 and facing == "down":
                    shoot_down()
                #End if
            #End if
        #Next event
    
        # -- Game logic goes after this comment
    
        #If player collides with a zombie, their number of lives decreases by 1
        user_hit_group = pygame.sprite.spritecollide(user, zombie_list, True)
        for hit in user_hit_group:
            user.lives_count += -1
        #Next hit
        #If player runs out of lives, the game quits
        if user.lives_count < 1:
            done = True
        #Endif
        
        #If bullet collides with wall, bullet is deleted
        pygame.sprite.groupcollide(wall_list, bullet_group, False, True)
    
    
        bullet_hits = pygame.sprite.groupcollide(zombie_list, bullet_group, True, True)
        for shot in bullet_hits:
            user.zombies_killed += 1
        #Next shot
            
    
        #If player collides with a powerup, the powerup gets deleted, and the player's number of bullets increases
        bulletpu_hit_list = pygame.sprite.spritecollide(user, bullet_pu_list, True,)
        
        for pu_bullet in bulletpu_hit_list:
            user.bullet_count += 10
            bullet_pu_list.remove(pu_bullet)
            all_sprites_list.remove(pu_bullet)
        #Next pu_bullet
            
        healthpu_hit_list = pygame.sprite.spritecollide(user, health_pu_list, True)
        for pu_health in healthpu_hit_list:
            user.lives_count += 1
            health_pu_list.remove(pu_health)
            all_sprites_list.remove(pu_health)
        #Next pu_health
    
        
        
        
    
    
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
#End procedure






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





#Spawns powerups
spawn_bullet_pu()
spawn_health_pu()




# Create player on the screen
user = Player(RED,18,18)
all_sprites_list.add(user)
facing = "right"

countfollow = 0
countbounce = 0
countrand = 0
# Create walls on the screen (each tile is 20x20 so alter cords)
for y in range(50):

    for x in range(50):
        #Creates the walls on the map
        if map[x][y] == 1:
            my_wall = Tile(BLUE,20,20,x*20,y*20)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)
        #End if
    #next x
#next y
                
    #Spawns zombies in random locations on the map. Cannot spawn on walls
while countbounce != 5:
    rand_bouncezomb_x = random.randint(1,49)
    rand_bouncezomb_y = random.randint(1,49)
    if map[rand_bouncezomb_x][rand_bouncezomb_y] == 0:
        #Spawns zombies that bounce off of walls and adds them to the necessary sprite list
        bouncer = BounceZombie(BLUE,20,20,rand_bouncezomb_x*20,rand_bouncezomb_y*20)
        all_sprites_list.add(bouncer)
        zombie_list.add(bouncer)
        countbounce += 1
#End while
        
    
while countfollow != 5:
    rand_zombfollow_x = random.randint(1,49)
    rand_zombfollow_y = random.randint(1,49)
    if map[rand_zombfollow_x][rand_zombfollow_y] == 0:
        #Spawns zombies that follow the player and adds them to the necessary sprite list
        zombiefollower = FollowerZombie(YELLOW,20,20,rand_zombfollow_x*20,rand_zombfollow_y*20)
        all_sprites_list.add(zombiefollower)
        zombie_list.add(zombiefollower)
        countfollow += 1
#End While

while countrand != 5:
    rand_zombrand_x = random.randint(1,49)
    rand_zombrand_y = random.randint(1,49)
    if map[rand_zombrand_x][rand_zombrand_y] == 0:
        zombierand = RandZombie(YELLOW,20,20,rand_zombrand_x*20,rand_zombrand_y*20)
        all_sprites_list.add(zombierand)
        zombie_list.add(zombierand)
        countrand += 1
#End While
    
                

#Creates the game loop
menu_screen()
