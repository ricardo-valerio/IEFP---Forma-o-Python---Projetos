from configs import *
import pygame
from pygame.locals import *
import os

import random

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Super Zombies")


clock = pygame.time.Clock()

x_player = 0
running = True
while running:

	dt = clock.tick(60) # 60 FPS

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False



	screen.blit(background_image(), [0, 0])
	# screen.blit( pygame.transform.flip(characther("imgs/zombies/z1.png"), True, False) , [30, 190])
	screen.blit(character("imgs/zombies/z1.png", x_flipped=True), [30 + x_player, 190])
	screen.blit(character("imgs/zombies/z2.png"), [250, 190])
	screen.blit(character("imgs/zombies/z3.png"), [450, 190])

	x_player += 1


	# desenhar frame
	pygame.display.update()

pygame.quit()
