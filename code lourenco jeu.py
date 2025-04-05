import pygame
from utils_jeu import *
import time

#initiation
pygame.init()
pygame.mixer.init()

#ecran
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MY GAME")
fond_ecran=pygame.image.load('Mario fond.png')

# gestion de la vitesse de rafraichissement de l´écran
clock = pygame.time.Clock()

#ajouter un son de saut
son = pygame.mixer.Sound("sonsaut.wav")

#son de fond
sondefond=pygame.mixer.music.load("sondefond.mp3")
pygame.mixer.music.play()

#création personnage
x_pers=x_ecran/2
y_pers=y_ecran-160
pers=pygame.image.load('character.png')
rect_pers=pygame.Rect(x_pers,y_pers,118,118)
dir=1

#jump
speed=0
gravity=2
jump=False

#création sol
x_sol=0
y_sol=y_ecran-50
sol=pygame.image.load('sol mario.png')
liste_x=[]
x_liste=0
y_liste=y_sol
x=0
avance=0
for f in range(250):
    liste_x.append(x_liste)
    x_liste+=50

# Camera offset
camera_x = 0

# Niveau 1
def niveau1(camera_x):
    for i in range(len(liste_x)):
        screen.blit(sol, (liste_x[i] - camera_x, y_sol))
        screen.blit(sol, (liste_x[i]+1000 - camera_x, y_sol-50))
        screen.blit(sol, (liste_x[i]+2000 - camera_x, y_sol-100))

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
        dir=1
        if rect_pers.right>=x_ecran-250:
            rect_pers.right+=0
            camera_x += 5
        else:
            rect_pers.right+=3
            camera_x += 5
            
    if keys[pygame.K_LEFT]:
        dir=-1
        if rect_pers.left<=250:
            rect_pers.right+=0
            camera_x -= 5
        else:
            rect_pers.right-=3
            camera_x -= 5
            
    if keys[pygame.K_SPACE] and jump==False:
        speed-=20
        son.play()
        
    #dessins
    if dir==1:
        screen.blit(pers,rect_pers) #dessin personnage
    elif dir==-1:
        screen.blit(pygame.transform.flip(pers,True,False),rect_pers)
    
        #niveau 1
    niveau1(camera_x)
    
    #mouvements
    rect_pers.bottom+=speed
    if rect_pers.bottom>=y_ecran-50:
        speed=0
        jump=False
    else:
        jump=True
        speed+=gravity
        time.sleep(0.005)
    
    # mise à jour de l´écran
    pygame.display.update()
    clock.tick(60)
    
# On sort de la boucle et on quitte
pygame.quit()
