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

from config import Config
from classes import *


# obtem configurações
CONFIG = Config()
TEXTOS = CONFIG.textos
CORES = CONFIG.cores

############ INICIALIZAÇÃO ##########
pygame.init()
pygame.mixer.init()

TELA = pygame.display.set_mode((CONFIG.largura_tela, CONFIG.altura_tela))
CLOCK = pygame.time.Clock()

pygame.display.set_caption(CONFIG.titulo)

# inicializacao de imagens
MAPA = pygame.image.load('mapa.png').convert_alpha()

# bandeiras do programa
RODANDO = True
TELA_INICIAL = True
GAME_OVER = False

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
TELA.fill(CORES.fundo)
TELA.blit(titulo_do_jogo, (CONFIG.largura_tela//2 - titulo_do_jogo.get_width() // 2, 90))
TELA.blit(botao_de_inicio1, (CONFIG.largura_tela//2 - botao_de_inicio1.get_width() // 2, 270))
TELA.blit(botao_de_inicio2, (CONFIG.largura_tela//2 - botao_de_inicio2.get_width() // 2, 310))
TELA.blit(nome_dos_criadores1, (CONFIG.largura_tela//2 - nome_dos_criadores1.get_width() // 2, 490))
TELA.blit(nome_dos_criadores2, (CONFIG.largura_tela//2 - nome_dos_criadores2.get_width() // 2, 520))
TELA.blit(nome_dos_criadores3, (CONFIG.largura_tela//2 - nome_dos_criadores3.get_width() // 2, 550))

# fundo = pygame.image.load('assests/img/map-pacman.png').convert()

# decide se o jogo fecha ou passa para a próxima tela
while RODANDO:

	CLOCK.tick(CONFIG.FPS)

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			RODANDO = False
			break

		if TELA_INICIAL:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					TELA_INICIAL = False
					break

		elif not GAME_OVER: pass


	# parte do loop que é o jogo mesmo
	if not GAME_OVER and not TELA_INICIAL:

		TELA.fill(CORES.fundo)
		TELA.blit(MAPA, (0, 0))


	elif GAME_OVER: pass




	pygame.display.flip()
