import pygame
from utils_jeu import *

#ecran
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MY GAME")
fond_ecran=pygame.image.load('mario back.jpg')

#création personnage
x_pers=x_ecran/2-45
y_pers=0
pers=pygame.image.load('character.png')
rect_pers=pygame.Rect(x_pers,y_pers,118,118)

#jump
speed=0
gravity=1
jump=False

#création sol
x_sol=0
y_sol=y_ecran-50
sol=pygame.image.load('sol mario.png')
liste_x=[]
x_liste=0
y_liste=y_sol
x=0
for f in range(20):
    liste_x.append(x_liste)
    x_liste+=50

#boucle jeu
run = True
while run:
    #fond ecran
    screen.blit(fond_ecran,(0,0))
    #event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and jump==False:
                speed-=1
    #keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_RIGHT]:
        rect_pers.left+=2
    if keys[pygame.K_LEFT]:
        rect_pers.left-=2
    if keys[pygame.K_SPACE] and jump==False:
        speed-=20
        
    #dessins
    screen.blit(pers,rect_pers) #dessin personnage
    
    for i in range(20): #dessins carreaux sol
        screen.blit(sol,(liste_x[i],y_sol))
        if rect_pers.left==x_ecran-218:
            liste_x.pop[0]
            for f in range(20):
                liste_x[f]-=50
            x+=1
            print(x)
            rect_pers.left=0
        elif x==40:
            y_liste-=50
            screen.blit(sol,(liste_x[i],y_liste))
        
    
                        
    #mouvements
    rect_pers.bottom+=speed
    if rect_pers.bottom>=y_ecran-50:
        speed=0
        jump=False
    else:
        jump=True
        speed+=gravity*1.2
    
    # mise à jour de l´écran
    pygame.display.update()

# On sort de la boucle et on quitte
pygame.quit()


