'''
Módulo de configurações do jogo

Autores: Jerônimo Afrange, Keiya Nishio e Pedro Drumond
'''

import pygame

class Config():

	def __init__(self):

		self.titulo = 'Joguinho do Come-Come'
		self.largura_tela = 560
		self.altura_tela = 620
		self.FPS = 60

		self.velocidade = 5	# pixels/ciclo

		self.cores = Cores()
		self.textos = Textos()


class Cores():

	def __init__(self):

		self.titulo = (200, 205, 70)
		self.fundo = (0, 0, 0)
		self.nomes = (200, 90, 210)

		self.preto = (0, 0, 0)


class Textos():

	def __init__(self):

		self.fonte = 'Futura ZBlk BT'
		self.tamanho_grande = 50
		self.tamanho_pequeno = 30
