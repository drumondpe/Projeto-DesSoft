'''
Módulo de configurações do jogo

Autores: Jerônimo Afrange, Keiya Nishio e Pedro Drumond
'''

import pygame

class Config():

	def __init__(self):

		self.titulo = 'Joguinho do Come-Come'
		self.pontuacao = 'Pontuação atual: XXX'
	#	self.pontuacao_record = 'Pontuação record: XXX'
		self.largura_tela = 560
		self.altura_tela = 620
		self.FPS = 60

		self.velocidade = 5	# pixels/ciclo

		self.cores = Cores()
		self.textos = Textos()
		self.poligonos = Poligonos(self.altura_tela, self.largura_tela)


class Cores():

	def __init__(self):

		self.titulo = (200, 205, 70)
		self.fundo = (0, 0, 0)
		self.nomes = (200, 90, 210)
	#	self.pontuacao = (250, 250, 250)
	#	self.pontuacao_record = (250, 250, 250)




class Textos():

	def __init__(self):

		self.fonte = 'Futura ZBlk BT'
		self.tamanho_grande = 50
		self.tamanho_pequeno = 30
		self.tamanho_menor = 15


class Poligonos():
	''' dimensoes das barreiras da arena '''

	def __init__(self, altura_tela, largura_tela):

		self.cor = pygame.Color(255, 255, 255, 0)
		self.larguras = [16]
		
		self.barreiras = [

			(	# pontos do polígono da barreira externa
				(0, 0),
				(largura_tela, 0),
				(largura_tela, altura_tela),
				(0, altura_tela),
				(0, self.larguras[0]),
				(self.larguras[0], self.larguras[0]),
				(self.larguras[0], altura_tela - self.larguras[0]),
				(largura_tela - self.larguras[0], altura_tela - self.larguras[0]),
				(largura_tela - self.larguras[0], self.larguras[0]),
				(0, self.larguras[0])
			)
		]






