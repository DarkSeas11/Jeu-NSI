import pygame
import random as rdm
from utils import *
import time


pygame.init()

# initialisation de l´écran avec sa taille et le titre
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MY GAME")

# gestion de la vitesse de rafraichissement de l´écran
clock = pygame.time.Clock()

#desssin du sol
ground_height = 50

# dessiner un rectangle:
largeur, hauteur = 30, 30
rectangle = pygame.Rect(30, 30, largeur, hauteur)
pygame.draw.rect(screen,BROWN,rectangle)
        
# dessiner un cercle: pygame.draw.circle(screen,couleur, [x, y], rayon)

# ajouter du texte:
    #font1 = pygame.font.SysFont(None, 72)
    #txt1 = font1.render('NSI FOR EVER', True, GREY)

# ajouter un nuage:
    nuage = pygame.image.load('nuage pixel projet python .png')
    rect_nuage = nuage.get_rect()

# Dessiner texte ou image dans la boucle du jeu:
    # texte: screen.blit(txt1,(x,y))
    # image: screen.blit(vaisseau,rect_vaisseau)




run = True
# -------- Boucle principale du jeu -----------
while run:
    # fond d´écran
    screen.fill(SKYBLUE)
    
    # --- Gestion des évènements
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("clic souris")
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pass
    

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


    #Mouvements

    



    # 60 mises à jour par seconde
    clock.tick(60)
    # mise à jour de l´écran
    pygame.display.update()

# On sort de la boucle et on quitte
pygame.quit()
 

