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

# pour tomber au début
y_pers=0

#booleen pour obstacle
level=0
pers=pygame.image.load('character.png')
#rectangle défini différemment
rect_pers=pers.get_rect()
dir=1

#jump
speed=0
gravity=0.5
jump=False

# Camera offset
camera_x = 0

#création sol
x_sol=0
y_sol=y_ecran-48

#pour les jump:
niveau=y_sol
sol=pygame.image.load('sol mario.png')

# rectangles dans une liste
offset=0
liste=[]
for i in range(249):
    liste.append(sol.get_rect())

for caisse in liste:
    caisse.left+=offset
    caisse.top=y_sol
    offset+=48

offset2=0
liste2=[]
for i in range(249):
    liste2.append(sol.get_rect())
    
for caisse in liste2:
    caisse.left+=offset2
    caisse.top=y_sol-48
    offset2+=48

offset3=0
liste3=[]
for i in range(249):
    liste3.append(sol.get_rect())

for caisse in liste3:
    caisse.left+=offset3
    caisse.top=y_sol-96
    offset3+=48
    
liste_x=[]
x_liste=0
for f in range(249):
    liste_x.append(x_liste)
    x_liste+=48
    

#Création Tubes
'''tube=pygame.image.load('pipe 3px.png')
x_tube=1440
y_tube=y_ecran-144
rect_tube1=pygame.Rect(x_tube,y_tube,144,101)'''

# GAME OVER
font1 = pygame.font.SysFont(None, 200)
txt1 = font1.render('GAME OVER', True, (255,0,0),(0,0,0))

#boucle jeu
run = True
while run:
    #fond ecran
    screen.blit(fond_ecran,(0,0))
    #print(rect_pers)
    #event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and jump==False:
                speed-=10
                son.play()
    #keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
        
    if keys[pygame.K_RIGHT]:
        dir=1
        if rect_pers.right>=x_ecran-240:
            rect_pers.right+=0
            camera_x+=5
        else:
            rect_pers.right+=3
            camera_x += 5
        
    if keys[pygame.K_LEFT]:
        dir=-1
        if rect_pers.left<=240:
            rect_pers.right-=0
            camera_x -= 5
        else:
            rect_pers.right-=3
            camera_x-=5
            
    #dessins
    if dir==1:
        screen.blit(pers,rect_pers) #dessin personnage
    elif dir==-1:
        screen.blit(pygame.transform.flip(pers,True,False),rect_pers)
    
    #screen.blit(tube,rect_tube1)
    
    #niveau 1
    '''for i in range(len(liste_x)):
        screen.blit(sol, (liste_x[i]-camera_x, y_sol))
        screen.blit(sol, (liste_x[i]+960-camera_x, y_sol-48))
        screen.blit(sol, (liste_x[i]+1200-camera_x, y_sol-96))'''
    
    # on gére ici les interaction du joueur avec le sol
    
    # premier niveau
    for caisse in liste:
        if caisse.left<=liste[19].left:
            screen.blit(sol,(caisse.left-camera_x,y_sol))
            

    # deuxième niveau
    for caisse2 in liste2:
        if caisse2.left>=liste2[14].left and caisse2.left<=liste2[19].left:
            screen.blit(sol,(caisse2.left-camera_x,y_sol-48))
            if rect_pers.right>liste2[14].left-camera_x and jump==False and level==0:
                camera_x-=3
                rect_pers.right=liste2[14].left-camera_x
            elif rect_pers.right>liste2[14].left-camera_x and jump:
                level=1
            elif rect_pers.right<liste2[14].left-camera_x :
                level=0
        elif caisse2.left>=liste2[24].left and caisse2.left<=liste2[32].left:
            screen.blit(sol,(caisse2.left-camera_x,y_sol-48))
            if rect_pers.left>liste2[24].right-camera_x and jump==False and level==0:
                camera_x-=3
                rect_pers.left=liste2[24].right-camera_x
            elif rect_pers.left>liste2[25].right-camera_x:
                level=1
            elif rect_pers.left>liste2[32].right-camera_x :
                level=0  

            
    # troisième niveau
    for caisse3 in liste3:
        if caisse3.left>=liste3[17].left and caisse3.left<=liste3[19].left:
            screen.blit(sol,(caisse3.left-camera_x,y_sol-96))
            if rect_pers.right>liste3[17].left-camera_x and jump==False and level==1:
                camera_x-=3
                rect_pers.right=liste3[17].left-camera_x
            elif rect_pers.right>liste3[17].left-camera_x and rect_pers.left<=liste3[19].right-camera_x and jump:
                level=2
            elif rect_pers.right<liste3[17].left-camera_x and rect_pers.right>liste2[14].left-camera_x:
                level=1
            elif rect_pers.left>liste3[19].right-camera_x and rect_pers.right<=liste3[23].left-camera_x:
                level=-3
        elif caisse3.left>=liste3[24].left and caisse3.left<=liste3[25].left:
            screen.blit(sol,(caisse3.left-camera_x,y_sol-96))
            if rect_pers.left>=liste3[24].right-camera_x and jump==False and level==2:
                camera_x-=3
                rect_pers.left=liste3[24].right-camera_x
            elif rect_pers.left>=liste3[24].right-camera_x and rect_pers.left<=liste3[25].right-camera_x:
                level=2
            elif rect_pers.left>liste3[25].right-camera_x:
                level=1
            
    #print(level)
    
    # détermine le niveau de heuteur
    niveau=y_sol-48*level
    rect_pers.bottom+=speed
    if rect_pers.bottom>=niveau:
        speed=0
        jump=False
        rect_pers.bottom=niveau
    elif level==-3 and rect_pers.top>y_sol:
        screen.blit(txt1,(x_ecran/6+20,y_ecran/2-30))
        time.sleep(5)
        run=False
    else:
        jump=True
        speed+=gravity
        #time.sleep(0.005)
    
    # mise à jour de l´écran
    pygame.display.update()
    clock.tick(60)
    
# On sort de la boucle et on quitte
pygame.quit()

