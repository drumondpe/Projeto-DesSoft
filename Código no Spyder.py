# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import pygame
import random

pygame.init()
pygame.mixer.init()


############ CONFIGURAÇÕES ##########
LARGURA = 600
ALTURA = 700 #config da tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Joguinho do come-come')
FPS = 60

preto = (0, 0, 0) #config de cores
jogo=True

#config de fontes
fundo = pygame.image.load('assests/img/map-pacman.png').convert()

while jogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo=False
    tela.fill((0, 0, 0))
    tela.blit(fundo, (0, 0))
    pygame.display.update()
pygame.quit()

    
    
############ CLASSE ###############


            

                
########## Outras funções ############




###### Funções da primeira tela ######
   


###### Funções da tela de jogo #######


        
        
        
        
        
        
        