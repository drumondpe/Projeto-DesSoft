'''
Módulo para as funções do jogo

Autores: Jerônimo Afrange, Keiya Nishio e Pedro Drumond
'''

import pygame

CONFIG = None
CORES = None
TEXTOS = None
TELA = None
PACMAN = None

def init(config, tela, pacman):
	''' incializa as variáveis do módulo de funções '''

	global CONFIG, TELA, TEXTOS, CORES, PACMAN

	CONFIG = config
	TELA = tela
	PACMAN = pacman

	TEXTOS = CONFIG.textos
	CORES = CONFIG.cores



def apresentar_tela_inicial():
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
	TELA.fill(CORES.fundo)
	TELA.blit(titulo_do_jogo, (CONFIG.largura_tela//2 - titulo_do_jogo.get_width() // 2, 90))
	TELA.blit(botao_de_inicio1, (CONFIG.largura_tela//2 - botao_de_inicio1.get_width() // 2, 270))
	TELA.blit(botao_de_inicio2, (CONFIG.largura_tela//2 - botao_de_inicio2.get_width() // 2, 310))
	TELA.blit(nome_dos_criadores1, (CONFIG.largura_tela//2 - nome_dos_criadores1.get_width() // 2, 490))
	TELA.blit(nome_dos_criadores2, (CONFIG.largura_tela//2 - nome_dos_criadores2.get_width() // 2, 520))
	TELA.blit(nome_dos_criadores3, (CONFIG.largura_tela//2 - nome_dos_criadores3.get_width() // 2, 550))


def checar_eventos(tela_inicial, game_over, rodando):
	''' avalia entradas e retorna bandeiras de estado de jogo '''

	# verifica inputs do usuário
	for event in pygame.event.get():

		# verifica, antes de tudo, se o usuário quer sair
		if event.type == pygame.QUIT:
			rodando = False
			break

		# se estiver na tela inicial, verificar as seguintes
		if tela_inicial:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					tela_inicial = False
					break

		# se estiver em jogo, verificar as seguintes
		elif not game_over:
			
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					PACMAN.velocidade_y = PACMAN.velocidade

				elif event.key == pygame.K_UP or event.key == pygame.K_w:
					PACMAN.velocidade_y = -1 * PACMAN.velocidade

				elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
					PACMAN.velocidade_x = -1 * PACMAN.velocidade

				elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					PACMAN.velocidade_x = PACMAN.velocidade

			if event.type == pygame.KEYUP:

				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					PACMAN.velocidade_y = 0

				elif event.key == pygame.K_UP or event.key == pygame.K_w:
					PACMAN.velocidade_y = 0

				elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
					PACMAN.velocidade_x = 0

				elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					PACMAN.velocidade_x = 0

	return tela_inicial, rodando


