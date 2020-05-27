''' 
Módulo principal do jogo

Autores: Jerônimo Afrange, Keiya Nishio e Pedro Drumond
'''

####PRECISAMOS FAZER:

## Mapa
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

from config import Config
from classes import *

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

	# incializacao de entidades
	PACMAN = Pacman(TELA, CONFIG)

	# apresenta a tela inicial
	apresentar_tela_inicial(TELA)

	# loop principal
	while RODANDO:

		CLOCK.tick(CONFIG.FPS)

		# verifica inputs do usuário
		for event in pygame.event.get():

			# verifica, antes de tudo, se o usuário quer sair
			if event.type == pygame.QUIT:
				RODANDO = False
				break

			# se estiver na tela inicial, verificar as seguintes
			if TELA_INICIAL:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						TELA_INICIAL = False
						break

			# se estiver em jogo, verificar as seguintes
			elif not GAME_OVER:

				PACMAN.checar_evento(event)	# checa todos inputs de movimento do pacman


		# loop do jogo
		if not GAME_OVER and not TELA_INICIAL:

			TELA.fill(CORES.fundo)
			TELA.blit(MAPA, (0, 0))

			PACMAN.update()	# atualiza a posição do pacman

			TELA.blit(PACMAN.image, PACMAN.rect)

		# loop de fim de jogo
		elif GAME_OVER: pass




		pygame.display.flip()




def apresentar_tela_inicial(tela):
	''' apresenta a tela inicial '''

	# config de fontes 
	fonte_texto_inicial = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_grande) 
	fonte_texto_nomes = pygame.font.SysFont(TEXTOS.fonte, TEXTOS.tamanho_pequeno)

	# textos que aparecem na primeira tela
	titulo_do_jogo = fonte_texto_inicial.render(CONFIG.titulo, True, CORES.titulo)
	botao_de_inicio1 = fonte_texto_inicial.render('Pressione Barra de Espaço', True, (255, 40, 255))
	botao_de_inicio2 = fonte_texto_inicial.render('para começar', True, (255, 40, 255))
	nome_dos_criadores1 = fonte_texto_nomes.render('Keiya Nishio', True, CORES.nomes)
	nome_dos_criadores2 = fonte_texto_nomes.render('Jerônimo Afrange', True, CORES.nomes)
	nome_dos_criadores3 = fonte_texto_nomes.render('Pedro Drumond', True, CORES.nomes)

	# posicionamento dos textos que aparecem na primeira tela
	tela.fill(CORES.fundo)
	tela.blit(titulo_do_jogo, (CONFIG.largura_tela//2 - titulo_do_jogo.get_width() // 2, 90))
	tela.blit(botao_de_inicio1, (CONFIG.largura_tela//2 - botao_de_inicio1.get_width() // 2, 270))
	tela.blit(botao_de_inicio2, (CONFIG.largura_tela//2 - botao_de_inicio2.get_width() // 2, 310))
	tela.blit(nome_dos_criadores1, (CONFIG.largura_tela//2 - nome_dos_criadores1.get_width() // 2, 490))
	tela.blit(nome_dos_criadores2, (CONFIG.largura_tela//2 - nome_dos_criadores2.get_width() // 2, 520))
	tela.blit(nome_dos_criadores3, (CONFIG.largura_tela//2 - nome_dos_criadores3.get_width() // 2, 550))

rodar()



