"""
Created on Fri May 15 19:26:29 2020

@authors: Pedro Drumond, Keiya Nishio, Jerônimo Afrange
"""

#poderes (iteração)

import pygame
pygame.init()
jogo = True

#config da tela
LARGURA = 500
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Joguinho do Come-Come')
mapa = pygame.image.load('mapa_pacman.png').convert_alpha()

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

class Pacman(pygame.sprite.Sprite):
    #construção do pacman
    def _init_(self, imagem, todos_personagens, todas_frutas, frutas_img):
        pygame.sprite.Sprite._init_(self)

        self.image_pacman = imagem
        self.posicao = self.image.get_rect()
        self.posicao.centerx = WIDTH / 2
        self.posicao.inferior = HEIGHT - 10
        self.velocidade.x = 0
        self.velocidade.y = 0
        self.todos_personagens = todos_personagens
        self.todas_frutas = todas_frutas
        self.frutas_img = frutas_img

     def Movimento(self):
        #atualiza a posição do pacman
        self.posicao.x += self.velocidade.x
        self.posicao.y += self.velocidade.y
        
        #mantem dentro do mapa
        if self.posicao.direita > LARGURA:
            self.posicao.direita = LARGURA
        if self.posicao.esquerda < 0:
            self.posicao.esquerda = 0
        
    def Bolado(self):
        #deixa o pacman bolado para comer os fantasmas
        pass
    
class Fantasma(pygame.sprite.Sprite):
    def _init_(self, imagem):
        pygame.sprite.Sprite._init_(self)
        
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        #precisamos fazer a movimentação inteligente
        
        #self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
        #self.rect.y = random.randint(-100, -METEOR_HEIGHT)
        #self.speedx = random.randint(-3, 3)
        #self.speedy = random.randint(2, 9)
        
        
        ################ TESTE #############
        #self.image_fantasma_verde = pygame.image.load('fantasma-verde.png').convert_alpha() #imprime a imagem dos fantasmas na tela
        #self.image_fantasma_verde = pygame.transform.scale(self.image_fantasma_verde, (LARGURA_FANTASMA, ALTURA_FANTASMA))
        
        #self.image_fantasma_rosa = pygame.image.load('fantasma-rosa.png').convert_alpha()
        #self.image_fantasma_rosa = pygame.transform.scale(self.image_fantasma_rosa, (LARGURA_FANTASMA, ALTURA_FANTASMA))
        
        #self.image_fantasma_vermelho = pygame.image.load('fantasma-vermelho.png').convert_alpha()
        #self.image_fantasma_vermelho = pygame.transform.scale(self.image_fantasma_vermelho, (LARGURA_FANTASMA, ALTURA_FANTASMA))

    def Update(self):
        #fazer a movimentação inteligente do fantasma
        #fantasma não pode atravessar a parede
        pass


#Criando o grupo dos personagens
todos_personagens = pygame.sprite.Group()
todos_fantasmas = pygame.sprite.Group()

fantasma_verde = Fantasma(fantasma_verde_img)
fantasma_rosa = Fantasma(fantasma_rosa_img)
fantasma_vermelho = Fantasma(fantasma_vermelho_img)
todos_personagens.add(fantasma_verde, fantasma_rosa, fantasma_vermelho)
todos_fantasmas.add(fantasma_verde, fantasma_rosa, fantasma_vermelho)

player = Pacman(pacman_img)
todos_personagens.add(player)




jogo = True
########################## LOOP PRINCIPAL #####################################

while jogo:
    relogio.tick(FPS)

    # Reaiza os eventos
    for tecla in pygame.event.get():
        # Verifica as consequências
        if tecla.evento == pygame.QUIT:
            jogo = False
            
        # Verifica se apertou alguma tecla.
        if tecla.evento == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if tecla.evento == pygame.K_LEFT: #or pygame.K_A:
                player.velocidadex -= 4
            if tecla.evento == pygame.K_RIGHT: #or pygame.K_D:
                player.velocidadex += 4
            if tecla.evento == pygame.K_UP: #or pygame.K_W
                player.velocidadey -= 4
            if tecla.evento == pygame.K_DOWN: #or pygame.K_S
                player.velocidadey += 4
        # Verifica se soltou alguma tecla.
        if tecla.evento == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if tecla.evento == pygame.K_LEFT: #or pygame.K_A:
                player.velocidadex += 4
            if tecla.evento == pygame.K_RIGHT: #or pygame.K_D:
                player.velocidadex -= 4
            if tecla.evento == pygame.K_UP: #or pygame.K_W
                player.velocidadey += 4
            if tecla.evento == pygame.K_DOWN: #or pygame.K_S
                player.velocidadey -= 4
#####Atualiza o estado do jogo
    #Atualiza a posição dos fantasmas
    todos_personagens.update()

    #verifica se houve colisão entre o pacman e os fantasmas
    colisao = pygame.sprite.spritecollide(player, todos_fantasmas, True)

    tela.fill((0, 0, 0)) #preenche com a cor preta
    #tela.blit(mapa, (0, 0)) #desenha o mapa
    
    #desenho dos fantasmas
    todos_personagens.draw(tela)
    
    #tela.blit(fantasma_verde, (0, 0))
    #tela.blit(fantasma_vermelho, (20, 20))
    #tela.blit(fantasma_rosa, (40, 40))
    #tela.blit(pacman, (60, 60))
    #tela.blit(fantasma_tiltado, (80, 80))



    pygame.display.update() #mostra novo frame para o jogador

pygame.quit() #fecha o jogo

