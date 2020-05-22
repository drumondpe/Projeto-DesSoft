
####PRECISAMOS FAZER:
#Mudar de tela
#Fazer o mapa
#Movimentação do Pacman
#Movimentação inteligente dos mobs
#pontinhos brancos 
#vidas
#pontuação
#construindo o mapa

import pygame
import random

pygame.init()
pygame.mixer.init()


############ CONFIGURAÇÕES ##########
#config da tela
LARGURA = 500
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Joguinho do come-come')

jogo = True

#config de cores
preto = (0, 0, 0) 
branco = (255, 255, 255)
rosa = (255, 0, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)


#config de fontes 
fonte_texto_inicial = pygame.font.SysFont('Futura ZBlk BT', 50) 
fonte_texto_nomes = pygame.font.SysFont('Futura ZBlk BT', 30)

#textos que aparecem na primeira tela
titulo_do_jogo = fonte_texto_inicial.render('Jogo do Come-Come', True, (200, 205, 70))
botao_de_inicio1 = fonte_texto_inicial.render('"Pressione Barra de Espaço', True, (255, 40, 255))
botao_de_inicio2 = fonte_texto_inicial.render('para começar"', True, (255, 40, 255))
nome_dos_criadores1 = fonte_texto_nomes.render('Keiya Nishio', True, (200, 90, 210))
nome_dos_criadores2 = fonte_texto_nomes.render('Jerônimo Afrange', True, (200, 90, 210))
nome_dos_criadores3 = fonte_texto_nomes.render('Pedro Drumond', True, (200, 90, 210))

#posicionamento dos textos que aparecem na primeira tela
tela.fill(preto)
tela.blit(titulo_do_jogo, (90, 90))
tela.blit(botao_de_inicio1, (25, 270))
tela.blit(botao_de_inicio2, (135, 300))
tela.blit(nome_dos_criadores1, (180, 490))
tela.blit(nome_dos_criadores2, (180, 520))
tela.blit(nome_dos_criadores3, (180, 550))

#fundo = pygame.image.load('assests/img/map-pacman.png').convert()

#decide se o jogo fecha ou passa para a próxima tela
while jogo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False
        #if event.type == SPACE


    pygame.display.update()
pygame.quit()