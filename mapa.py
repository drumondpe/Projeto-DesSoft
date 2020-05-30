'''
Módulo de composição de mapas

Autores: Jerônimo Afrange, Keiya Nishio e Pedro Drumond
'''

import pygame
from pygame.sprite import Sprite, Group

from tile import Tile

class Mapa():
	''' Descreve um mapa '''

	def __init__(self, config, tela, imagens, map_id):
		''' cria um novo mapa com base nas configuracoes '''

		self.config = config
		self.tela = tela
		self.id = id_mapa

		bitmap = config.bitmap[id_mapa]
		self.tiles = Group()

		posicao = [0, 0]

		for linha in bitmap:
			for bit in linha:
				print(imagens[bit])
				self.tiles.add(Tile(config, posicao, imagens[bit], bit))
				posicao[0] += config.tamanho_tile
			posicao[0] = 0
			posicao[1] += config.tamanho_tile







