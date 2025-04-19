import pygame
from jeu import *
import time

#initiation
pygame.init()

#vitesse de rafraîchissement de la page 
clock = pygame.time.Clock()

#ecran
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MY GAME")

# Boutons
bouton_joueur_lourenco = pygame.image.load('JOUEURLOURENCO.png')
bouton_joueur_clemence = pygame.image.load('JOUEURCLEMENCE.png')
bouton_sortie = pygame.image.load('SORTIE.png')

# Positions des boutons
bouton_joueur_lourenco_rect = bouton_joueur_lourenco.get_rect(topleft=(225, 50))
bouton_joueur_clemence_rect = bouton_joueur_clemence.get_rect(topleft=(225, 200))
bouton_sortie_rect = bouton_sortie.get_rect(topleft=(200, 425))

#boucle jeu
run = True
while run:
    
    #fond decran
    screen.fill(SKYBLUE)
    
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifie si un bouton a été cliqué
            if bouton_joueur_lourenco_rect.collidepoint(event.pos):
                lourenco()
            elif bouton_joueur_clemence_rect.collidepoint(event.pos):
                clemence()
            #si le bouton sortie est préssé alors quitter le jeu
            elif bouton_sortie_rect.collidepoint(event.pos):
                run = False 
    
    screen.blit(bouton_joueur_lourenco,bouton_joueur_lourenco_rect)
    screen.blit(bouton_joueur_clemence,bouton_joueur_clemence_rect)
    screen.blit(bouton_sortie,bouton_sortie_rect)
    
    
    # 60 mises à jour par seconde
    clock.tick(60)
    # mise à jour de l´écran
    pygame.display.update()



pygame.quit()
