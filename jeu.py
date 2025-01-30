import pygame
from utils_jeu import *

#ecran
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MY GAME")
fond_ecran=pygame.image.load('mario back.jpg')

#création personnage
pers=pygame.image.load('character.png')
rect_pers=pygame.Rect(x_ecran/2-45,y_ecran-100,118,118)

#boucle jeu
run = True
while run:
    #fond ecran
    screen.blit(fond_ecran,(-50,0))
    #event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_RIGHT]:
        rect_pers.left+=1
    if keys[pygame.K_LEFT]:
        rect_pers.left-=1
    if keys[pygame.K_SPACE]:
        rect_pers.bottom-=3
        for i in range(3):
            rect_pers.bottom+=1
        
    #dessins
    screen.blit(pers,rect_pers)    
        
    # mise à jour de l´écran
    pygame.display.update()

# On sort de la boucle et on quitte
pygame.quit()

