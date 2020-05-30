'''
Módulo das funções de jogo
'''

import os
import sys
import pygame


def render_menu(text_settings, color_settings):
	''' Renderiza a tela do menu inicial '''

	txt, clr = text_settings, color_settings
	return_value = dict()

	# config de fontes 
	large_font = pygame.font.SysFont(txt.font, txt.large_fontsize) 
	small_font = pygame.font.SysFont(txt.font, txt.small_fontsize)

	# textos que aparecem na primeira tela
	return_value['title'] = large_font.render(txt.title, True, clr.title)
	return_value['button_1'] = large_font.render('Pressione Barra de Espaço', True, clr.menu_button)
	return_value['button_2'] = large_font.render('para começar', True, clr.menu_button)
	return_value['name_1'] = small_font.render('Keiya Nishio', True, clr.names)
	return_value['name_2'] = small_font.render('Jerônimo Afrange', True, clr.names)
	return_value['name_3'] = small_font.render('Pedro Drumond', True, clr.names)

	return return_value


def draw_menu(settings, screen, rendered_text):
	''' desenha o menu na tela '''

	sts, clr, scr, rtx = settings, settings.colors, screen, rendered_text

	# desenha os textos
	scr.blit(rtx['title'], (sts.screen_width//2 - rtx['title'].get_width() // 2, 90))
	scr.blit(rtx['button_1'], (sts.screen_width//2 - rtx['button_1'].get_width() // 2, 270))
	scr.blit(rtx['button_2'], (sts.screen_width//2 - rtx['button_2'].get_width() // 2, 310))
	scr.blit(rtx['name_1'], (sts.screen_width//2 - rtx['name_1'].get_width() // 2, 490))
	scr.blit(rtx['name_2'], (sts.screen_width//2 - rtx['name_2'].get_width() // 2, 520))
	scr.blit(rtx['name_3'], (sts.screen_width//2 - rtx['name_3'].get_width() // 2, 550))


def check_events(game_state, pacman=None):
	''' checks events according to game state '''

	# verifica as entradas nos diferentes estados de jogo
	if game_state == 0: return check_menu_event()
	elif game_state == 1: return check_game_event(pacman)
	elif game_state == 2: return check_over_event()
	elif game_state == 3: return check_vict_event()

	return game_state


def check_menu_event():
	''' verifica eventos quando na tela incial de jogo '''

	for event in pygame.event.get():

		if event.type == pygame.QUIT: sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE: return 1

	else: return 0


def check_game_event(pacman):
	''' verifica eventos quando em jogo '''

	for event in pygame.event.get():

		if event.type == pygame.QUIT: sys.exit()

		elif event.type == pygame.KEYDOWN:

			if event.key == pygame.K_UP or event.key == pygame.K_w:
				pacman.moving_up = True

			if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				pacman.moving_down = True

			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				pacman.moving_left = True

			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				pacman.moving_right = True


		elif event.type == pygame.KEYUP:

			if event.key == pygame.K_UP or event.key == pygame.K_w:
				pacman.moving_up = False

			if event.key == pygame.K_DOWN or event.key == pygame.K_s:
				pacman.moving_down = False

			if event.key == pygame.K_LEFT or event.key == pygame.K_a:
				pacman.moving_left = False

			if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
				pacman.moving_right = False

	return 1


def check_over_event():
	''' verifica eventos na tela de game over '''

	return 2


def check_vict_event():
	''' verifica eventos na tela de vitoria '''

	return 3


def load_images(game_dir):
	''' loads the game images '''

	images = dict()
	img_dir = os.path.join(game_dir, 'images')

	images['tiles'] = [ 
		pygame.image.load(os.path.join(img_dir, 'black_tile.png')).convert(),
		pygame.image.load(os.path.join(img_dir, 'purple_tile.png')).convert()
	]

	images['pacman'] = pygame.image.load(os.path.join(img_dir, 'pacman.png')).convert_alpha()

	return images





