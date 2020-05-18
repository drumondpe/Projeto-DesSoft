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
tela.blit(mapa, (0, 0))

relogio = pygame.time.Clock()
FPS = 60


####################### CONFIG DAS IMAGENS ####################################

#configurações dos mobs - imagens (https://www.pngwing.com/pt/free-png-nyddf)
LARGURA_FANTASMA = 30
ALTURA_FANTASMA = 18

#imagens dos mobs
fantasma_verde_img = pygame.image.load('fantasma-verde.png').convert_alpha()
fantasma_rosa_img = pygame.image.load('fantasma-rosa.png').convert_alpha()
fantasma_vermelho_img = pygame.image.load('fantasma-vermelho.png').convert_alpha()
fantasma_tiltado_img = pygame.image.load('fantasma-tiltado.png').convert_alpha()

#imprime os fantasmas na tela
fantasma_verde = pygame.transform.scale(fantasma_verde_img, (LARGURA_FANTASMA, ALTURA_FANTASMA))
fantasma_rosa = pygame.transform.scale(fantasma_rosa_img, (LARGURA_FANTASMA, ALTURA_FANTASMA))
fantasma_vermelho = pygame.transform.scale(fantasma_vermelho_img, (LARGURA_FANTASMA, ALTURA_FANTASMA))
fantasma_tiltado = pygame.transform.scale(fantasma_tiltado_img, (LARGURA_FANTASMA, ALTURA_FANTASMA))


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



    pygame.display.update()



pygame.quit()