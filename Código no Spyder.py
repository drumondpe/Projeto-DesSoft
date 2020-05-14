# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import pygame
import sys
import random

pygame.init()
posicao = pygame.math.Vector2

########################## CONFIG #############################################
LARGURA, ALTURA = 600, 700 #config da tela
FPS = 60
        #config de cores
preto = (0, 0, 0)
vermelho = (210, 20, 20)
        
        #config de fontes 
tamanho_texto_inicial = 18
fonte_inicial = 'Futura ZBlk BT'
        #config de jogador

        #config dos mobs
     
#################### CLASSE PRINCIPAL #########################################
class Jogo:
    def __init__(self): 
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        self.tempo = pygame.time.Clock()
        self.rodando = True
        self.estado = 'tela inicial'
        
        self.carrega()
        
    def rodar(self):
        while self.rodando:
            if self.estado == 'tela inicial':
                self.comeco_eventos()
                self.comeco_update()
                self.comeco_desenho()
            
            elif self.estado == 'jogando':
                self.jogando_eventos()
                self.jogando_update()
                self.jogando_desenho()
            
            else:
                self.rodando = False
            self.tempo.verifica(FPS)
        pygame.quit()
        sys.exit()

################## FUNÇÕES AUXILIARES #########################################
    def desenho_texto (self, textos, tela, posicao, tamanho, cor, nome_fonte, centraliza = False):
        
        fonte = pygame.font.SysFont(nome_fonte, tamanho)
        texto = fonte.render(textos, False, cor)
        tamanho_texto = texto.get_size()
        tela.blit(texto, posicao)
        if centraliza:
            posicao[0] = posicao[0] - tamanho_texto[0]/2
            posicao[1] = posicao[1] - tamanho_texto[1]/2
            
    def carrega(self):
        self.mapa = pygame.image.load('mapa_pacman.JFIF')
        self.mapa = pygame.transform.scale(self.mapa, (LARGURA, ALTURA))


################## FUNÇÕES PARA COMEÇAR #######################################
    def comeco_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
            if evento.type == pygame.KEYDOWN and evento.pressionado == K_SPACE:
                self.estado = 'jogando'
                
    def comeco_update(self):
        pass
    
    def comeco_desenho(self):
        self.tela.fill(preto)
        #textos comuns em jogos
        self.desenho_texto('PRESSIONE BARRA DE ESPAÇO', self.tela, [LARGURA/2, ALTURA/2-30], tamanho_texto_inicial, (85, 205, 80), fonte_inicial, centraliza = True)
        self.desenho_texto('SOMENTE PARA UM JOGADOR', self.tela, [LARGURA/2, ALTURA/2+30], tamanho_texto_inicial, (75, 45, 220), fonte_inicial, centraliza = True)
        self.desenho_texto('MAIOR PONTUAÇÃO', self.tela, [5,5], tamanho_texto_inicial, (220, 220, 235), fonte_inicial)
        
        #o nome dos desenvolvedores :D
        self.desenho_texto('FEITO POR:', self.tela, [LARGURA/2, ALTURA/2+70], tamanho_texto_inicial, (50, 130, 150), fonte_inicial, centraliza = True)
        self.desenho_texto('Jeronimo Afrange', self.tela, [LARGURA/2, ALTURA/2+90], tamanho_texto_inicial, (50, 130, 150), fonte_inicial, centraliza = True)
        self.desenho_texto('Keiya Nishio', self.tela, [LARGURA/2, ALTURA/2+100], tamanho_texto_inicial, (50, 130, 150), fonte_inicial, centraliza = True)
        self.desenho_texto('Pedro Drumond', self.tela, [LARGURA/2, ALTURA/2+110], tamanho_texto_inicial, (50, 130, 150), fonte_inicial, centraliza = True)
        
        pygame.display.update()

################## FUNÇÕES PARA JOGAR #########################################
    def jogando_eventos(self):
        for evento in pygame.event.get():
            if evento.digitado == pygame.QUIT:
                self.rodando = False
                
    def jogando_update(self):
        pass
    
    def jogando_desenho(self):
        self.tela.blit(self.mapa, (0,0)) #encher 
        pygame.display.update()
        
#################### RODA O JOGO ##############################################

programa = Jogo()
programa.rodar()
    
    
    
        
                
        
        
        
        
        
        
        
        