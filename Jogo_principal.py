"""
Created on Fri May 15 19:26:29 2020

@author: Pedro Drumond
"""
import pygame
pygame.init()
jogo = True

#config da tela
LARGURA = 500
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Joguinho do Come-Come')
mapa = pygame.image.load('map-pacman.png').convert_alpha()

#tela.fill(0, 0, 0)
#tela.blit(mapa, (0, 0))

relogio = pygame.time.Clock()
FPS = 60


####################### CONFIG DAS IMAGENS ####################################

#configurações dos mobs - imagens (https://www.pngwing.com/pt/free-png-nyddf)
LARGURA_FANTASMA = 30
ALTURA_FANTASMA = 18
LARGURA_PACMAN = 30
ALTURA_PACMAN = 18

#imagens dos mobs
fantasma_verde_img = pygame.image.load('fantasma-verde.png').convert_alpha()
fantasma_rosa_img = pygame.image.load('fantasma-rosa.png').convert_alpha()
fantasma_vermelho_img = pygame.image.load('fantasma-vermelho.png').convert_alpha()
fantasma_tiltado_img = pygame.image.load('fantasma-tiltado.png').convert_alpha()
pacman_img = pygame.image.load('pacman.png').convert_alpha()

#imprime os fantasmas na tela
fantasma_verde = pygame.transform.scale(fantasma_verde_img, (LARGURA_FANTASMA, ALTURA_FANTASMA))
fantasma_rosa = pygame.transform.scale(fantasma_rosa_img, (LARGURA_FANTASMA, ALTURA_FANTASMA))
fantasma_vermelho = pygame.transform.scale(fantasma_vermelho_img, (LARGURA_FANTASMA, ALTURA_FANTASMA))
fantasma_tiltado = pygame.transform.scale(fantasma_tiltado_img, (LARGURA_FANTASMA, ALTURA_FANTASMA))
pacman = pygame.transform.scale(pacman_img, (LARGURA_PACMAN, ALTURA_PACMAN))




########################## CLASSE PRINCIPAL ###################################

class Fantasma(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img


########################## LOOP PRINCIPAL #####################################

while jogo:
    relogio.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False

    tela.fill((0, 0, 0))
    tela.blit(mapa, (0, 0))
    tela.blit(fantasma_verde, (0, 0))
    tela.blit(fantasma_vermelho, (20, 20))
    tela.blit(fantasma_rosa, (40, 40))
    tela.blit(pacman, (60, 60))
    tela.blit(fantasma_tiltado, (80, 80))



    pygame.display.update()

pygame.quit()