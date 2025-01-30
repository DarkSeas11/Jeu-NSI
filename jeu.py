import pygame
from utils_jeu import *

#ecran
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MY GAME")
fond_ecran=pygame.image.load('mario back.jpg')

#boucle jeu
run = True
while run:
    #fond ecran
    screen.blit(fond_ecran,(0,0))
    #keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False