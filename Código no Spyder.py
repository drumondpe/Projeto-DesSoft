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
LARGURA = 500
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Joguinho do come-come')

jogo = True

#config de cores
preto = (0, 0, 0) 


#config de fontes
fonte_texto_inicial = pygame.font.SysFont('Futura ZBlk BT', 50)
fonte_texto_nomes = pygame.font.SysFont('Futura ZBlk BT', 30)
titulo_do_jogo = fonte_texto_inicial.render('Jogo do Come-Come', True, (200, 205, 70))
botao_de_inicio1 = fonte_texto_inicial.render('Pressione Barra de Espaço', True, (255, 40, 255))
botao_de_inicio2 = fonte_texto_inicial.render('para começar', True, (255, 40, 255))
nome_dos_criadores1 = fonte_texto_nomes.render('Keiya Nishio', True, (200, 90, 210))
nome_dos_criadores2 = fonte_texto_nomes.render('Jerônimo Afrange', True, (200, 90, 210))
nome_dos_criadores3 = fonte_texto_nomes.render('Pedro Drumond', True, (200, 90, 210))


#fundo = pygame.image.load('assests/img/map-pacman.png').convert()

while jogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False
    
    tela.fill(preto)
    tela.blit(titulo_do_jogo, (90, 200))
    tela.blit(botao_de_inicio1, (30, 270))
    tela.blit(botao_de_inicio2, (140, 300))
    tela.blit(nome_dos_criadores1, (180, 490))
    tela.blit(nome_dos_criadores2, (180, 520))
    tela.blit(nome_dos_criadores3, (180, 550))



    pygame.display.update()
pygame.quit()

    
    
############ CLASSE ###############


            

                
########## Outras funções ############




###### Funções da primeira tela ######
   


###### Funções da tela de jogo #######

        
        
        
        
        
        
        