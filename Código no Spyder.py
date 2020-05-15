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
#config da tela
LARGURA = 600
ALTURA = 700
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Joguinho do come-come')

<<<<<<< HEAD
jogo = True

#config de cores
preto = (0, 0, 0) 


#config de fontes
fonte_texto_inicial = pygame.font.SysFont('Futura ZBlk BT', 60)
titulo_do_jogo = fonte_texto_inicial.render('Jogo do Come-Come', True, (200, 205, 70))
botao_de_inicio = fonte_texto_inicial.render('Pressione Barra de Espaço para começar', True, (255, 40, 255))
nome_dos_criadores1 = fonte_texto_inicial.render('Keiya Nishio', True, (200, 90, 210))
nome_dos_criadores2 = fonte_texto_inicial.render('Jerônimo Afrange', True, (200, 90, 210))
nome_dos_criadores3 = fonte_texto_inicial.render('Pedro Drumond', True, (200, 90, 210))




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


        
        
        
        
        
        
        