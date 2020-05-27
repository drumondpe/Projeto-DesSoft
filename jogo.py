''' 
Módulo principal do jogo

Autores: Jerônimo Afrange, Keiya Nishio e Pedro Drumond
'''

####PRECISAMOS FAZER:

# Mapa
# Movimentação inteligente (fantasmas)
# Colisões -------> Vidas
# Pontos brancos
# Pontuação
# Mudança de tela
# Pontuação na segunda tela

###ITERAÇÕES:
# Powerups
# Músicas


import pygame
import random

import funcoes as f

from config import Config
from pacman import Pacman

# obtem configurações
CONFIG = Config()
TEXTOS = CONFIG.textos
CORES = CONFIG.cores

# roda o jogo
def rodar():

	############ INICIALIZAÇÃO ##########
	pygame.init()
	pygame.mixer.init()

	TELA = pygame.display.set_mode((CONFIG.largura_tela, CONFIG.altura_tela))
	CLOCK = pygame.time.Clock()

	pygame.display.set_caption(CONFIG.titulo)

	# inicializacao de imagens
	MAPA = pygame.image.load('imagens/mapa.png').convert_alpha()

	# bandeiras do programa
	RODANDO = True
	TELA_INICIAL = True
	GAME_OVER = False

	# incializacao de entidades e módulos
	PACMAN = Pacman(TELA, CONFIG)
	f.init(CONFIG, TELA, PACMAN)

	# apresenta a tela inicial
	f.apresentar_tela_inicial()

	# loop principal
	while RODANDO:

		CLOCK.tick(CONFIG.FPS)

		# atualiza bandeiras de jogo
		TELA_INICIAL, RODANDO = f.checar_eventos(TELA_INICIAL, GAME_OVER, RODANDO)


		# loop do jogo
		if not GAME_OVER and not TELA_INICIAL:

			TELA.fill(CORES.fundo)
			TELA.blit(MAPA, (0, 0))

			PACMAN.update()	# atualiza a posição do pacman

			TELA.blit(PACMAN.image, PACMAN.rect)

		# loop de fim de jogo
		elif GAME_OVER: pass


		pygame.display.flip()



rodar()



