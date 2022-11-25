'''
Módulo do mapa do jogo
'''

import os

from tile import Tile
from pygame.sprite import Group


class Map():
	''' Um conjunto de tiles '''

	def __init__(self, game_dir, settings, images, map_id):
		''' renderiza um novo mapa '''

		# converte o arquvio csv da distribuicao de tiles no mapa e cria os tiles
		self.matrix = Map.convert_map_file(game_dir, map_id)
		self.tiles = Map.build(settings, self.matrix, images)


	def draw(self, screen):
		''' desenha o mapa na tela '''

		self.tiles.draw(screen)


	@staticmethod
	def convert_map_file(game_dir, map_id):
		'''determina a matriz do mapa a partir do arquivo csv'''

		matrix = list()

		with open(os.path.join(game_dir, 'maps/map' + str(map_id) + '.csv')) as map_file:

			for line in map_file:

				split_line_str = line.split(',')
				split_line_int = list()

				for value in split_line_str:
					split_line_int.append(int(value))

				matrix.append(split_line_int)

		return matrix


	@staticmethod
	def build(settings, matrix, images):
		''' cria os tiles a partir da matriz do mapa '''

		tiles = Group()
		position = [0, 0]

		for line in matrix:

			for specific_id in line:
				tiles.add(Tile(position, images[specific_id]))
				position[0] += settings.tile_size

			position[0] = 0
			position[1] += settings.tile_size

		return tiles




