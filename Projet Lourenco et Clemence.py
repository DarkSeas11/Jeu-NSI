import pygame
import random as rdm
from utils import *
from time import time

pygame.init()
pygame.mixer.init()

# initialisation de l´écran avec sa taille et le titre
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("MY GAME")

# gestion de la vitesse de rafraichissement de l´écran
clock = pygame.time.Clock()

#debut du temps
debut = time()

# ajouter un son de fond
sondefond=pygame.mixer.music.load('sondefond.mp3')
print(sondefond)

# Jouer la musique
pygame.mixer.music.play()

# Ajouter un son de saut
son = pygame.mixer.Sound("sonsaut.wav")
print(son)

#desssin du sol
ground_height = 50

# dessiner un rectangle:

#largeur, hauteur = 30, 30
#rectangle = pygame.Rect(30, 30, largeur, hauteur)
#pygame.draw.rect(screen,BROWN,rectangle)
        
# dessiner un cercle: pygame.draw.circle(screen,couleur, [x, y], rayon)

# ajouter du texte:
    #font1 = pygame.font.SysFont(None, 72)
    #txt1 = font1.render('NSI FOR EVER', True, GREY)

# ajouter un nuage:
nuage = pygame.image.load('nuage.png')
rect_nuage = nuage.get_rect()
rect_nuage.top = 600
rect_nuage.left = 100

#ajouter un son de saut
son = pygame.mixer.Sound("sonsaut.wav")


# Dessiner texte ou image dans la boucle du jeu:
    # texte: screen.blit(txt1,(x,y))




run = True
# -------- Boucle principale du jeu -----------
while run:
    # fond d´écran
    screen.fill(SKYBLUE)
    
    # Gestion des évènements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Si la touche espace est presse 
                son.play()
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pass
        
    if keys[pygame.K_DOWN]:
        pass
      
    if keys[pygame.K_RIGHT]:
        pass
       
    if keys[pygame.K_LEFT]:
       pass
    
    duree = time() - debut
    if duree > 180:
        pygame.mixer.music.stop()
        pygame.quit()
        run = False



    
    # Dessins
    #pygame.draw.rect(screen, BROWN, rectangle)
    screen.blit(nuage, rect_nuage)

    #Mouvements

    



    # 60 mises à jour par seconde
    clock.tick(60)
    # mise à jour de l´écran
    pygame.display.update()
    

# arret de la musique et on quitte
pygame.mixer.music.stop()
pygame.quit() 
