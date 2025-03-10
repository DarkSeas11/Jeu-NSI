import pygame
import random as rdm
from utils import *
import time

pygame.init()

# initialisation de l´écran avec sa taille et le titre
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("MY GAME")

# gestion de la vitesse de rafraichissement de l´écran
clock = pygame.time.Clock()

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
    
    #son du saut lorsque espace est cliqué
    if jump == True:
        son.play()
        pass
    
    # Gestion des évènements
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pass
        
    if keys[pygame.K_DOWN]:
        pass
      
    if keys[pygame.K_RIGHT]:
        pass
       
    if keys[pygame.K_LEFT]:
       pass



    
    # Dessins
    #pygame.draw.rect(screen, BROWN, rectangle)
    screen.blit(nuage, rect_nuage)

    #Mouvements

    



    # 60 mises à jour par seconde
    clock.tick(60)
    # mise à jour de l´écran
    pygame.display.update()

# On sort de la boucle et on quitte
pygame.quit()
