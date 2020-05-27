''' 
Módulo da classe Barreira do jogo
Descreve as paredes do mapa

Autores: Jerônimo Afrange, Keiya Nishio e Pedro Drumond
'''

import pygame

class Barreira():
	''' Descreve as paredes invisíveis da arena '''

	def __init__(self, config, tela, pontos):
		''' incializa e desenha uma nova barreira '''
		
		self.config = config.poligonos
		self.pontos = pontos
		self.tela = tela


	def desenhar(self):
		''' desenha o rect da barreira na tela '''

		pygame.draw.polygon(self.tela, self.config.cor, self.pontos)




