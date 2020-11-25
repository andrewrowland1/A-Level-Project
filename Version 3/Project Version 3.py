import pygame
import random

font_name = pygame.font.match_font('calibri')

highestscorefile = open("HighestScore.txt","r")
highestscore = (highestscorefile.read())
highestscorefile.close()

# -- Global constants
map1 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
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

map2 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
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
        if self.rect.x > 1000 or self.rect.x < 0 or self.rect.y > 1000 or self.rect.y < 0:
            pygame.sprite.Sprite.kill(self)
            user.zombies_killed += 1
        
    #End procedure
    
#End Class
class BossZombie(Zombie):
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
        #Next hit
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
        #Endif
        if self.rect.x > 1000 or self.rect.x < 0:
            pygame.sprite.Sprite.kill(self)
        #End if
        if self.rect.y > 1000 or self.rect.y < 0:
            pygame.sprite.Sprite.kill(self)
        #End if
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
def draw_text(surf,text,size,x_val,y_val, colour):
        font = pygame.font.Font(font_name, size)
        text = font.render(text, True, colour)
        text_rect = text.get_rect()
        text_rect.midtop = (x_val, y_val)
        surf.blit(text, text_rect)
#End procedure

def spawn_health_pu():
    counter = 0
    while counter != 5:
        random_x = random.randint(1,49)
        random_y = random.randint(1,49)
            
        if map1[random_y][random_x] == 0:
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

        if map1[random_y][random_x] == 0:
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
                    game_choice()
                #End if
                if event.key == pygame.K_RETURN:
                    done = True
                    help_screen()
                #End if
            #End if
        #Next event
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, (0,475,size[0],100))
        pygame.draw.rect(screen, GREEN, (0,675,size[0],100))
        draw_text(screen, str("ESCAPE"),300,500,50, RED)
        draw_text(screen, str("Press the spacebar to play"),50,500,500, WHITE)
        draw_text(screen, str("Press the return key to view how the controls"),50,500,700, WHITE)
        pygame.display.update()
    #End while
#End procedure

def game_choice():
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
                if event.key == pygame.K_LEFT:
                    done = True 
                    endless_game_loop()
                #End if
                if event.key == pygame.K_RIGHT:
                    done = True
                    campaign_game_loop()
                #End if
                if event.key == pygame.K_RETURN:
                    done = True
                    menu_screen()
                #End if
            #End if
        #Next event
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, (0,475,size[0],100))
        pygame.draw.rect(screen, GREEN, (0,675,size[0],100))
        pygame.draw.rect(screen, GREEN, (0,875,size[0],100))
        draw_text(screen, str("ESCAPE"),300,500,50, RED)
        draw_text(screen, str("Press the left arrow key to play an endless game"),50,500,500, WHITE)
        draw_text(screen, str("Press the right arrow key to play a campaign game"),50,500,700, WHITE)
        draw_text(screen, str("Press the return key to return to the main menu"),50,500,900, WHITE)
        pygame.display.update()
    #End while
                    
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
            
                if event.key == pygame.K_RETURN:
                    done = True
                    menu_screen()
                #End if
            #End if
        #Next event

        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, (0,425,size[0],300))
        pygame.draw.rect(screen, GREEN, (0,875,size[0],100))
        draw_text(screen, str("ESCAPE"),300,500,50, RED)
        draw_text(screen, str("To move, use the arrow keys"),50,500,450, WHITE)
        draw_text(screen, str("To shoot, press the space bar"),50,500,500, WHITE)
        draw_text(screen, str("The gun will shoot in the"),50,500,550, WHITE)
        draw_text(screen, str("direction of your last movement"),50,500,600, WHITE)
        draw_text(screen, str("To quit the game, press the escape key"),50,500,650, WHITE)
        draw_text(screen, str("Press the return key to return to the main menu"),50,500,900, WHITE)
        pygame.display.update()
    #End while
#End procedure
def well_done_screen():
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
                if event.key == pygame.K_RETURN:
                    done = True
                    menu_screen()
                #End if
                if event.key == pygame.K_DOWN:
                    done = True
                    boss_level()
                #End if
            #End if
        #Next event
        screen.fill(BLACK)
        draw_text(screen, str("ESCAPE"),300,500,50, RED)
        draw_text(screen, str("Congratulations!"),150,500,500, BLUE)
        draw_text(screen, str("You have escaped"),100,500,700, BLUE)
        draw_text(screen, str("Press the return key to return to the main menu"),50,500,900, BLUE)
        pygame.display.update()
    #End while
#End procedure

def pre_boss_screen():
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
                if event.key == pygame.K_RETURN:
                    done = True
                    boss_level()
                #End if
            #End if
        #Next event
        screen.fill(BLACK)
        draw_text(screen, str("ESCAPE"),300,500,50, RED)
        draw_text(screen, str("BOSS LEVEL!!"),150,500,500, BLUE)
        draw_text(screen, str("Press the return key to start"),50,500,900, BLUE)
        pygame.display.update()
    #End while
#End procedure

def death_screen():
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
                if event.key == pygame.K_RETURN:
                    done = True
                    menu_screen()
                #End if
            #End if
        #Next event
        screen.fill(BLACK)
        draw_text(screen, str("ESCAPE"),300,500,50, RED)
        draw_text(screen, str("YOU ARE DEAD"),150,500,500, BLUE)
        draw_text(screen, str("Press the return key to return to the main menu"),50,500,900, BLUE)
        pygame.display.update()
    #End while
#End procedure
        
            
        
def campaign_game_loop():
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
            user.zombies_killed += 1
            
        #If player runs out of lives, the game quits
        if user.lives_count < 1:
            done = True
            death_screen()
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
        
        if len(zombie_list) == 0:
            pre_boss_screen()
        
        all_sprites_list.update()
        # -- Screen background is BLACK
        screen.fill(BLACK)
    
        # -- Draw here
        all_sprites_list.draw(screen)
        
        draw_text(screen, str("Bullets: %d" % user.bullet_count),20,40,40, WHITE)
        draw_text(screen, str("Zombies Killed: %d" % user.zombies_killed),20,70,60, WHITE)
        draw_text(screen, str("Lives: %d" % user.lives_count),20,40,80, WHITE)
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # -- The clock ticks over
        clock.tick(60)
    #End While - End of game loop
    pygame.quit()
#End procedure

def boss_level():
    for x in wall_list:
        x.kill()
    
    # Create walls on the screen (each tile is 20x20 so alter cords)
    # Create player on the screen
    
    boss = BossZombie(BLUE,100,100,200,200)
    all_sprites_list.add(boss)
    zombie_list.add(boss)
    boss_lives = 10
    for y in range(50):
        for x in range(50):
            #Creates the walls on the map
            if map2[x][y] == 1:
                my_wall = Tile(BLUE,20,20,x*20,y*20)
                all_sprites_list.add(my_wall)
                #End if
        #next x
    #next y
    
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
            user.zombies_killed += 1
            
        #If player runs out of lives, the game quits
        if user.lives_count < 1:
            done = True
            death_screen()
        #Endif
        
        #If bullet collides with wall, bullet is deleted
        pygame.sprite.groupcollide(wall_list, bullet_group, False, True)
    
        bullet_hits = pygame.sprite.groupcollide(zombie_list, bullet_group, False, True)
        
        for shot in bullet_hits:
            boss_lives += -1
        #Next shot
        if boss_lives < 1:
            well_done_screen()

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
        
        draw_text(screen, str("Bullets: %d" % user.bullet_count),20,40,40, WHITE)
        draw_text(screen, str("Zombies Killed: %d" % user.zombies_killed),20,70,60, WHITE)
        draw_text(screen, str("Lives: %d" % user.lives_count),20,40,80, WHITE)
 
        # -- flip display to reveal new position of objects
        pygame.display.flip()
    
        # -- The clock ticks over
        clock.tick(60)
    #End While - End of game loop
    pygame.quit()
#End procedure
    
def endless_game_loop():
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    global countrand
                    #Spawns zombies in random locations on the map. Cannot spawn on walls
                    rand_zombrand_x = random.randint(1,49)
                    rand_zombrand_y = random.randint(1,49)
                    if map2[rand_zombrand_x][rand_zombrand_y] == 0:
                        #Spawns zombies that bounce off of walls in a random directly and adds them to the necessary sprite list
                        zombierand = RandZombie(YELLOW,20,20,rand_zombrand_x*20,rand_zombrand_y*20)
                        all_sprites_list.add(zombierand)
                        zombie_list.add(zombierand)
                        countrand += 1
                    #End if
                if event.key == pygame.K_p:
                    spawn_bullet_pu()
                    spawn_health_pu()
                #End if
            #End if
        #Next event
    
        # -- Game logic goes after this comment
        #If player collides with a zombie, their number of lives decreases by 1
        user_hit_group = pygame.sprite.spritecollide(user, zombie_list, True)
        for hit in user_hit_group:
            user.lives_count += -1
            user.zombies_killed += -1
        #If player runs out of lives, the game quits
        if user.lives_count < 1:
            done = True
            death_screen()
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
        global highestscore
        if user.zombies_killed > int(highestscore):
            highestscore = user.zombies_killed
            highestscorefile = open("HighestScore.txt","w")
            highestscorefile.write(str(highestscore))
            highestscorefile.close()
            
        all_sprites_list.update()
        # -- Screen background is BLACK
        screen.fill(BLACK)
    
        # -- Draw here
        all_sprites_list.draw(screen)
        
        draw_text(screen, str("Highest score: %d" % int(highestscore)),20,70,100,WHITE)
        draw_text(screen, str("Bullets: %d" % user.bullet_count),20,40,40, WHITE)
        draw_text(screen, str("Zombies Killed: %d" % user.zombies_killed),20,70,60, WHITE)
        draw_text(screen, str("Lives: %d" % user.lives_count),20,30,80, WHITE)
    
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
#, pygame.FULLSCREEN

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
        if map1[x][y] == 1:
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
    if map1[rand_bouncezomb_x][rand_bouncezomb_y] == 0:
        #Spawns zombies that bounce off of walls and adds them to the necessary sprite list
        bouncer = BounceZombie(BLUE,20,20,rand_bouncezomb_x*20,rand_bouncezomb_y*20)
        all_sprites_list.add(bouncer)
        zombie_list.add(bouncer)
        countbounce += 1
#End while
while countfollow != 5:
    rand_zombfollow_x = random.randint(1,49)
    rand_zombfollow_y = random.randint(1,49)
    if map1[rand_zombfollow_x][rand_zombfollow_y] == 0:
        #Spawns zombies that follow the player and adds them to the necessary sprite list
        zombiefollower = FollowerZombie(YELLOW,20,20,rand_zombfollow_x*20,rand_zombfollow_y*20)
        all_sprites_list.add(zombiefollower)
        zombie_list.add(zombiefollower)
        countfollow += 1
#End While
while countrand != 5:
    rand_zombrand_x = random.randint(1,49)
    rand_zombrand_y = random.randint(1,49)
    if map1[rand_zombrand_x][rand_zombrand_y] == 0:
        zombierand = RandZombie(YELLOW,20,20,rand_zombrand_x*20,rand_zombrand_y*20)
        all_sprites_list.add(zombierand)
        zombie_list.add(zombierand)
        countrand += 1
#End While

#Creates the game loop
menu_screen()