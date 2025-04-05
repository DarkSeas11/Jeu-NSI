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
x_pers=0
y_pers=y_ecran-156
pers=pygame.image.load('character.png')
rect_pers=pygame.Rect(x_pers,y_pers,118,118)
dir=1

#jump
speed=0
gravity=2
jump=False

# Camera offset
camera_x = 0

#création sol
x_sol=0
y_sol=y_ecran-48
sol=pygame.image.load('sol mario.png')
liste_x=[]
x_liste=0
for f in range(250):
    liste_x.append(x_liste)
    x_liste+=48
    

#Création Tubes
tube=pygame.image.load('pipe 3px.png')
x_tube=1440
y_tube=y_ecran-144
rect_tube1=pygame.Rect(x_tube,y_tube,144,101)

# Niveau 1
def niveau1(camera_x):
    pass

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
        print(rect_pers.right)
        dir=1
        #Collisions
        if rect_pers.right>=543 and rect_pers.bottom>y_sol-48:
            rect_pers.right+=0
            camera_x+=0
        elif rect_pers.right>=543 and rect_pers.bottom<=y_sol-48:
            y_pers=y_sol-48
        else:
            rect_pers.right+=3
            camera_x += 3
        y_pers=y_sol
            
    if keys[pygame.K_LEFT]:
        dir=-1
        
        if rect_pers.left<=250:
            rect_pers.right+=0
            camera_x -= 3
        else:
            rect_pers.right-=3
            camera_x -= 3
            
    if keys[pygame.K_SPACE] and jump==False:
        speed-=20
        son.play()
        
    #dessins
    if dir==1:
        screen.blit(pers,rect_pers) #dessin personnage
    elif dir==-1:
        screen.blit(pygame.transform.flip(pers,True,False),rect_pers)
    
    screen.blit(tube,rect_tube1)
    
        #niveau 1
    for i in range(len(liste_x)):
        screen.blit(sol, (liste_x[i]-camera_x, y_sol))
        screen.blit(sol, (liste_x[i]+960-camera_x, y_sol-48))
        screen.blit(sol, (liste_x[i]+1200-camera_x, y_sol-96))
    
    #mouvements
    rect_pers.bottom+=speed
    if rect_pers.bottom>=y_sol:
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
