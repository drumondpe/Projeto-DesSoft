''' 
Módulo da classe Pacman do jogo

Autores: Jerônimo Afrange, Keiya Nishio e Pedro Drumond
'''

import pygame

class Pacman(pygame.sprite.Sprite):
    ''' Classe que define o sprite do jogador '''
    
    def __init__(self, tela, config):
    	''' cria uma nova instancia da classe Pacman '''

    	self.tela = tela
    	self.image = pygame.image.load('imagens/pacman.png')
    	self.rect = self.image.get_rect()
    	self.screen_rect = tela.get_rect()
    	self.rect.centerx = self.screen_rect.centerx
    	self.rect.bottom = self.screen_rect.bottom - 20

    	self.velocidade = config.velocidade
    	self.velocidade_x = 0
    	self.velocidade_y = 0


    def update(self):
    	''' atualiza a posição do pacman com base em sua velocidade '''

    	self.rect.centerx += self.velocidade_x
    	self.rect.centery += self.velocidade_y




