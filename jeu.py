import pygame
from utils_jeu import *

#ecran
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MY GAME")
fond_ecran=pygame.image.load('mario back.jpg')

#création personnage
x_pers=x_ecran/2-45
y_pers=y_ecran-148
pers=pygame.image.load('character.png')
rect_pers=pygame.Rect(x_ecran/2-45,y_ecran-148,118,118)

#jump
speed=1
gravity=1
jump=False

#création sol
x=0
x_sol=0
y_sol=y_ecran-48
sol=pygame.image.load('sol mario.png')
rect_sol=pygame.Rect(x_sol+x,y_sol,48,48)

#boucle jeu
run = True
while run:
    #fond ecran
    screen.blit(fond_ecran,(-50,0))
    #event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.key==pygame.K_SPACE and jump==False:#double jump tirar "jump==False"
                    speed-=20
    #keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_RIGHT]:
        rect_pers.left+=2
    if keys[pygame.K_LEFT]:
        rect_pers.left-=2
    if keys[pygame.K_SPACE]:
        rect_pers.bottom-=10
    elif rect_pers.bottom<=rect_sol.top-10:
        rect_pers.bottom=rect_sol.top    
    #dessins
    screen.blit(pers,rect_pers)
    
    screen.blit(sol,rect_sol)
    
    #mouvements
    y_pers+=speed
    if y_pers>=x_ecran-(rect_sol.top-48):
        speed=0
        jump=False
    else:
        jump=True
        speed+=gravity
    
    # mise à jour de l´écran
    pygame.display.update()

# On sort de la boucle et on quitte
pygame.quit()


