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

'''#son de fond
sondefond=pygame.mixer.music.load("sondefond.mp3")
pygame.mixer.music.play()''' 

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

# rectangles dans une liste pour les differents etages
offset=0
liste=[]
for i in range(248):
    liste.append(sol.get_rect())

for caisse in liste:
    caisse.left+=offset
    caisse.top=y_sol
    offset+=48

offset2=0
liste2=[]
for i in range(248):
    liste2.append(sol.get_rect())
    
for caisse in liste2:
    caisse.left+=offset2
    caisse.top=y_sol-48
    offset2+=48

offset3=0
liste3=[]
for i in range(248):
    liste3.append(sol.get_rect())

for caisse in liste3:
    caisse.left+=offset3
    caisse.top=y_sol-48*2
    offset3+=48
    
offset4=0
liste4=[]
for i in range(248):
    liste4.append(sol.get_rect())

for caisse in liste4:
    caisse.left+=offset4
    caisse.top=y_sol-48*3
    offset4+=48

offset5=0
liste5=[]
for i in range(248):
    liste5.append(sol.get_rect())

for caisse in liste5:
    caisse.left+=offset5
    caisse.top=y_sol-48*4
    offset5+=48

offset6=0
liste6=[]
for i in range(248):
    liste6.append(sol.get_rect())

for caisse in liste6:
    caisse.left+=offset6
    caisse.top=y_sol-48*5
    offset6+=48

offset7=0
liste7=[]
for i in range(248):
    liste7.append(sol.get_rect())

for caisse in liste7:
    caisse.left+=offset7
    caisse.top=y_sol-48*6
    offset7+=48

offset8=0
liste8=[]
for i in range(248):
    liste8.append(sol.get_rect())

for caisse in liste8:
    caisse.left+=offset8
    caisse.top=y_sol-48*7
    offset8+=48

# GAME OVER
font1 = pygame.font.SysFont(None, 200)
txt1 = font1.render('GAME OVER', True, (255,0,0),None)

#obstacle


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
    
    # on gére ici les interaction du joueur avec le sol
    
    # premier niveau
    for caisse in liste:
        if caisse.left<=liste[19].left or (caisse.left>=liste[24].left and caisse.left<=liste[56].left) or caisse.left>=liste[63].left:
            screen.blit(sol,(caisse.left-camera_x,y_sol))
            

    # deuxième niveau
    for caisse2 in liste2:
        if caisse2.left>=liste2[14].left and caisse2.left<=liste2[19].left:
            screen.blit(sol,(caisse2.left-camera_x,y_sol-48))
            if rect_pers.right>liste2[14].left-camera_x and jump==False and level==0 and rect_pers.right<liste2[17].left-camera_x:
                camera_x-=0
                rect_pers.right=liste2[14].left-camera_x
                
            elif rect_pers.right>liste2[14].left-camera_x and jump and rect_pers.right<liste2[17].left-camera_x:
                level=1
            elif rect_pers.right<liste2[14].left-camera_x :
                level=0
        elif caisse2.left>=liste2[24].left and caisse2.left<=liste2[32].left:
            screen.blit(sol,(caisse2.left-camera_x,y_sol-48))
            if rect_pers.left>liste2[25].right-camera_x and rect_pers.right<=liste2[32].left-camera_x:
                level=1
            elif rect_pers.left>liste2[32].right-camera_x and rect_pers.right<liste2[40].right-camera_x:
                level=0
            elif rect_pers.left>liste2[31].right-camera_x and rect_pers.left<=liste2[32].right-camera_x and jump==False and level==0:
                rect_pers.left=liste2[32].right-camera_x
        elif caisse2.left>=liste2[40].left and caisse2.left<=liste2[56].left:
            screen.blit(sol,(caisse2.left-camera_x,y_sol-48))
            if rect_pers.right<liste2[41].left-camera_x and rect_pers.right>=liste2[40].left-camera_x and jump==False:
                rect_pers.right=liste2[40].left-camera_x
        elif (caisse2.left>=liste2[63].left and caisse2.left<=liste2[74].left) or (caisse2.left>=liste2[79].left):
            screen.blit(sol,(caisse2.left-camera_x,y_sol-48))
            if (rect_pers.left<=liste2[74].right-camera_x and rect_pers.left>liste2[70].right-camera_x) or rect_pers.right>=liste2[79].left-camera_x:
                level=1
            elif rect_pers.left>liste2[74].right-camera_x and rect_pers.right<liste2[79].left-camera_x:
                level=0
            elif rect_pers.left<=liste2[74].right-camera_x and level==0 and rect_pers.left>liste2[73].right-camera_x and jump==False:
                rect_pers.left=liste2[74].right-camera_x
            elif rect_pers.left>=liste2[79].right-camera_x and level==0 and rect_pers.left<liste2[80].right-camera_x and jump==False:
                rect_pers.right=liste2[79].left-camera_x
            
    # troisième niveau
    for caisse3 in liste3:
        if caisse3.left>=liste3[17].left and caisse3.left<=liste3[19].left:
            screen.blit(sol,(caisse3.left-camera_x,y_sol-96))
            if rect_pers.right>liste3[17].left-camera_x and jump==False and level==1 and rect_pers.right<=liste3[19].left-camera_x:
                rect_pers.right=liste3[17].left-camera_x
                
            elif rect_pers.right>liste3[17].left-camera_x and rect_pers.left<=liste3[19].right-camera_x and jump:
                level=2
            elif rect_pers.right<liste3[17].left-camera_x and rect_pers.right>liste3[14].left-camera_x:
                level=1
            elif rect_pers.left>liste3[19].right-camera_x and rect_pers.right<liste3[23].left-camera_x:
                level=-3
                if rect_pers.right>=liste3[23].left-camera_x and rect_pers.top<y_sol-48*2:
                    rect_pers.right=liste3[23].left-camera_x
        elif caisse3.left>=liste3[24].left and caisse3.left<=liste3[25].left:
            screen.blit(sol,(caisse3.left-camera_x,y_sol-96))
            if rect_pers.left>=liste3[24].left-camera_x and rect_pers.left<=liste3[25].right-camera_x and level==1 and jump==False:
                rect_pers.left=liste3[25].right-camera_x
            elif rect_pers.right>=liste3[24].left-camera_x and rect_pers.left<=liste3[25].right-camera_x:
                level=2
        elif caisse3.left>=liste3[42].left and caisse3.left<=liste3[56].left:
            screen.blit(sol,(caisse3.left-camera_x,y_sol-96))
            if rect_pers.right>=liste3[42].left-camera_x and jump==False and level==1 and rect_pers.right<liste3[43].left-camera_x:
                camera_x-=0
                rect_pers.right=liste3[42].left-camera_x
            elif rect_pers.right>=liste3[42].left-camera_x and jump and rect_pers.left<=liste3[56].right-camera_x:
                level=2
            elif rect_pers.right<liste3[42].left-camera_x and rect_pers.right>liste3[40].left-camera_x:
                level=1
        elif caisse3.left>=liste3[63].left and caisse3.left<=liste3[70].left:
            screen.blit(sol,(caisse3.left-camera_x,y_sol-96))
            if rect_pers.left<=liste3[70].right-camera_x and level==1 and rect_pers.right>liste3[69].left-camera_x and jump==False:
                rect_pers.left=liste3[70].right-camera_x
            elif rect_pers.left<liste3[70].right-camera_x and rect_pers.right>=liste3[63].left-camera_x:
                level=2
                
    #4e niveau
    for caisse4 in liste4:
        if caisse4.left>=liste4[44].left and caisse4.left<=liste4[56].left:
            screen.blit(sol,(caisse4.left-camera_x,y_sol-144))
            if rect_pers.right>liste4[44].left-camera_x and jump==False and level==2 and rect_pers.left<=liste4[56].right-camera_x:
                camera_x-=0
                rect_pers.right=liste4[44].left-camera_x
                
            elif rect_pers.right>liste4[44].left-camera_x and jump and rect_pers.left<=liste4[56].right-camera_x:
                level=3
            elif rect_pers.right<liste4[44].left-camera_x and rect_pers.right>liste4[42].left-camera_x:
                level=2
                
    #5e niveau
    for caisse5 in liste5:
        if caisse5.left>=liste5[46].left and caisse5.left<=liste5[56].left:
            screen.blit(sol,(caisse5.left-camera_x,y_sol-(48*4)))
            if rect_pers.right>liste5[46].left-camera_x and jump==False and level==3 and rect_pers.right<liste5[47].left-camera_x:
                camera_x-=0
                rect_pers.right=liste5[46].left-camera_x
                
            elif rect_pers.right>liste5[46].left-camera_x and jump and rect_pers.left<=liste5[56].right-camera_x:
                level=4
            elif rect_pers.right<liste5[46].left-camera_x and rect_pers.right>liste5[44].left-camera_x:
                level=3
                
    #6e niveau
    for caisse6 in liste6:
        if caisse6.left>=liste6[48].left and caisse6.left<=liste6[56].left:
            screen.blit(sol,(caisse6.left-camera_x,y_sol-(48*5)))
            if rect_pers.right>=liste6[48].left-camera_x and jump==False and level==4 and rect_pers.right<liste6[49].left-camera_x:
                camera_x-=0
                rect_pers.right=liste6[48].left-camera_x
                
            elif rect_pers.right>liste6[48].left-camera_x and jump and rect_pers.left<=liste6[56].right-camera_x:
                level=5
            elif rect_pers.right<liste6[48].left-camera_x and rect_pers.right>liste6[46].left-camera_x:
                level=4
            
    #7e niveau
    for caisse7 in liste7:
        if caisse7.left>=liste7[50].left and caisse7.left<=liste7[56].left:
            screen.blit(sol,(caisse7.left-camera_x,y_sol-(48*6)))
            if rect_pers.right>=liste7[50].left-camera_x and jump==False and level==5 and rect_pers.right<liste7[51].left-camera_x:
                camera_x-=0
                rect_pers.right=liste7[50].left-camera_x
                
            elif rect_pers.right>liste7[50].left-camera_x and jump and rect_pers.left<=liste7[56].right-camera_x:
                level=6
            elif rect_pers.right<liste7[50].left-camera_x and rect_pers.right>liste7[48].left-camera_x:
                level=5
                
    #8e niveau
    for caisse8 in liste8:
        if caisse8.left>=liste8[52].left and caisse8.left<=liste8[56].left:
            screen.blit(sol,(caisse8.left-camera_x,y_sol-(48*7)))
            if rect_pers.right>=liste8[52].left-camera_x and jump==False and level==6 and rect_pers.right<liste8[53].left-camera_x:
                camera_x-=0
                rect_pers.right=liste8[52].left-camera_x
                
            elif rect_pers.right>liste8[52].left-camera_x and jump and rect_pers.left<liste8[55].right-camera_x:
                level=7
            elif rect_pers.right<liste8[52].left-camera_x and rect_pers.right>liste8[50].left-camera_x:
                level=6
            elif rect_pers.left>liste8[56].left-camera_x and rect_pers.right<liste8[63].left-camera_x:
                level=-3
                if rect_pers.top<(y_sol-48*2) and rect_pers.right>=liste8[63].left-camera_x:
                    rect_pers.right=liste8[60].left-camera_x
                    level=-3
                elif rect_pers.bottom<(y_sol-48*7) and rect_pers.left<=liste8[56].left-camera_x:
                    rect_pers.left=liste8[56].left-camera_x
                    level=-3
    
    # détermine le niveau de heuteur
    niveau=y_sol-48*level
    rect_pers.bottom+=speed
    if rect_pers.bottom>=niveau:
        speed=0
        jump=False
        rect_pers.bottom=niveau
    elif level==-3 and rect_pers.top>y_sol:
        screen.blit(txt1,(x_ecran/6+20,y_ecran/2-30))
        time.sleep(1)
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


