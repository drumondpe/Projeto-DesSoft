'''
Módulo do jogador
'''

import pygame

from pygame.sprite import Sprite, spritecollide


class Pacman(Sprite):
	''' descreve o boneco do jogador '''

	def __init__(self, settings, image):
		''' cria o objeto do jogador '''

		# inicializa a instância da classe Sprite
		Sprite.__init__(self)

		# amarra a imagem ao objeto e define o Sprite.rect do tile
		self.image = image
		self.rect = image.get_rect()

		# posiciona o boneco
		self.rect.x = settings.screen_width // 2
		self.rect.y = settings.screen_height - 2 * settings.tile_size

		# bandeiras de movimento
		self.moving_up = False
		self.moving_down = False
		self.moving_left = False
		self.moving_right = False

		# float da posição
		self.pos = [float(self.rect.x), float(self.rect.y)]

		# propriedade de velocidade
		self.speed = settings.pacman_speed


	def draw(self, screen):
		''' desenha o pacman na tela '''

		screen.blit(self.image, self.rect)


	def update(self, map):
		''' atualiza a posição do pacman com base nas suas bandeiras de movimento '''

		if self.moving_up: self.pos[1] -= self.speed
		if self.moving_down: self.pos[1] += self.speed
		if self.moving_left: self.pos[0] -= self.speed
		if self.moving_right: self.pos[0] += self.speed

		collisions = spritecollide(self, map.tiles[1], False)

		for collision in collisions:

			if self.moving_up and not self.moving_down:
				self.pos[1] = collision.rect.bottom

			if self.moving_down and not self.moving_up:
				self.pos[1] = collision.rect.top

			if self.moving_right and not self.moving_left:
				self.pos[0] = collision.rect.left

			if self.moving_left and not self.moving_right:
				self.pos[0] = collision.rect.right

		self.rect.x = round(self.pos[0])
		self.rect.y = round(self.pos[1])



