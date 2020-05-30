'''
Módulo principal do jogo
'''

import os
import sys
import pygame

import game_functions as gf

from settings import Settings
from pacman import Pacman
from map import Map

def run():
	''' inicia o programa '''

	DIR = os.path.dirname(__file__)

	# bandeira principal e estado de jogo
	RUNNING = True
	GAME_STATE = 0

	# importa as configurações
	SETTINGS = Settings()
	COLORS = SETTINGS.colors
	TEXTS = SETTINGS.texts

	# inicializa o pygame, abre a janela de jogo e inicializa o clock
	pygame.init()
	SCREEN = pygame.display.set_mode((SETTINGS.screen_width, SETTINGS.screen_height))
	pygame.display.set_caption(SETTINGS.caption)
	CLOCK = pygame.time.Clock()

	# carregas as imagens
	IMAGES = gf.load_images(DIR)

	# renderiza o menu principal
	MENU_TEXTS = gf.render_menu(TEXTS, COLORS)

	# loop geral
	while RUNNING:

		# --- --- loop do menu principal --- --- --- --- ---
		while GAME_STATE == 0:

			CLOCK.tick(SETTINGS.fps)

			# esvazia a tela
			SCREEN.fill(COLORS.bg)

			# desenha o menu principal, verifica entradas e atualiza o estado de jogo de acordo
			gf.draw_menu(SETTINGS, SCREEN, MENU_TEXTS)
			GAME_STATE = gf.check_events(GAME_STATE)

			# atualiza a tela
			pygame.display.flip()



		# --- --- trecho pré loop do jogo --- --- --- --- ---
		if GAME_STATE == 1:
			# renderiza o mapa
			MAP = Map(DIR, SETTINGS, IMAGES['tiles'], map_id = 1)
			PACMAN = Pacman(SETTINGS, IMAGES['pacman'])


		# --- --- loop de jogo --- --- --- --- --- --- --- ---
		while GAME_STATE == 1:

			CLOCK.tick(SETTINGS.fps)

			# esvazia a tela
			SCREEN.fill(COLORS.bg)

			# atualiza a posição dos sprites móveis
			PACMAN.update(MAP)

			# desenha os sprites, verifica entradas e atualiza o estado de jogo de acordo
			MAP.draw(SCREEN)
			PACMAN.draw(SCREEN)
			GAME_STATE = gf.check_events(GAME_STATE, PACMAN)

			pygame.display.flip()



		# --- --- loop da tela game over --- --- --- --- --- ---
		while GAME_STATE == 2: pass



		# --- --- loop da tela de vitoria --- --- --- --- --- ---
		while GAME_STATE == 3: pass


run()




	