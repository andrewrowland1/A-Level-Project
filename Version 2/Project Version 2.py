import pygame
import random
import math
font_name = pygame.font.match_font('calibri')

from classes import *




# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (1000,1000)
screen = pygame.display.set_mode((size))

# -- Title of new window/screen
pygame.display.set_caption("Escape")

# -- Exit game flag set to false
done = False

# --Manages how fast screen refreshes
clock = pygame.time.Clock()

#Spawns walls and zombies
spawn_walls()

#Spawns powerups
spawn_bullet_pu()
spawn_health_pu()

# Create player on the screen
spawn_player()

#Main game loop
game_loop()
