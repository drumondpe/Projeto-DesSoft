'''
Módulo de tiles do jogo
'''

import pygame

from pygame.sprite import Sprite, Group


class Tile(Sprite):
	''' Classe que representa um unico tile por instancia '''

	def __init__(self, position, image):
		''' cria um novo objeto da classe Tile '''

		# inicializa a instancia da classe Sprite
		Sprite.__init__(self)

		# amarra a imagem ao objeto e define o Sprite.rect do tile
		self.image = image
		self.rect = image.get_rect()

		# posiciona o tile
		self.rect.x = position[0]
		self.rect.y = position[1]
		





