import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([700, 700])

pontos = [
	(0, 0),
	(700, 0),
	(700, 700),
	(0, 700),
	(0, 50),
	(50, 50),
	(50, 650),
	(650, 650),
	(650, 50),
	(0, 50)
]

pygame.draw.polygon(screen, (255, 255, 255), pontos)

while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()

	pygame.display.flip()