''' 
Módulo das classes do jogo

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


    def checar_evento(self, event):
    	''' faz a análise das entradas relativas aos movimentos do pacman '''

    	if event.type == pygame.KEYDOWN:

    		if event.key == pygame.K_DOWN or event.key == pygame.K_s:
    			self.velocidade_y = self.velocidade

    		elif event.key == pygame.K_UP or event.key == pygame.K_w:
    			self.velocidade_y = -1 * self.velocidade

    		elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
    			self.velocidade_x = -1 * self.velocidade

    		elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
    			self.velocidade_x = self.velocidade

    	if event.type == pygame.KEYUP:

    		if event.key == pygame.K_DOWN or event.key == pygame.K_s:
    			self.velocidade_y = 0

    		elif event.key == pygame.K_UP or event.key == pygame.K_w:
    			self.velocidade_y = 0

    		elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
    			self.velocidade_x = 0

    		elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
    			self.velocidade_x = 0


    
class Fantasma(pygame.sprite.Sprite):
	''' Classe que define o sprite dos fantasmas '''
	pass

class Fruta(pygame.sprite.Sprite):
	''' Classe que define o sprite das frutas '''
	pass

class Ponto(pygame.sprite.Sprite):
	''' Classe que define o sprite dos pontos '''
	pass



