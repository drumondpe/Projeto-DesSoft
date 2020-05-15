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

#config de fontes
tamanho_texto_start = 18

fonte_texto_start = 'Futura XBlk BT'
    
    
############ CLASSE ###############

class Jogo:
    def __init__(self):
        self.tela = pygame.display.set_mode(LARGURA, ALTURA)
        pygame.display.set_caption('Joguinho do come-come')
        self.rodando = True

    def rodar(self):
        while self.rodando:
            if self.estado == 'tela de inicio'
            

                
########## Outras funções ############




###### Funções da primeira tela ######
    def comeco_eventos(self):
        for evento in pygame.event.get():
            if evento.digitado == pygame.QUIT:
                self.rodando = False



###### Funções da tela de jogo #######


        
        
        
        
        
        
        