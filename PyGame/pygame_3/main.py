from configs import *
import pygame
from pygame.locals import *
import os

import random

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Super Zombies")


clock = pygame.time.Clock()

delta = 30

running = True
while running:

	dt = clock.tick(60) # 60 FPS

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	# green rectangle -------------------------------------------------------
	pygame.draw.rect(
		surface=screen,
		color="green",
		rect=[20 + delta, 20 + delta, 40, 80], # [x, y, width, height]
		width=0
	)

	# red rectangle -------------------------------------------------------
	pygame.draw.rect(
		surface=screen,
		color="red",
		rect=[60 + delta, 20 + delta, 70, 80],
		width=0
	)

	# yellow circle -------------------------------------------------------
	pygame.draw.circle(
		surface=screen,
		color="yellow",
		center=(60 + delta, 60 + delta),
		radius=20,
		width=0
	)


	pygame.draw.line(surface=screen, color="indigo", start_pos=(90,90), end_pos=(200, 200), width=3)

	pygame.draw.lines(
		surface=screen,
		color="lightgreen",
		closed=True,
		points=[(300, 100), (88, 290)],
		width=2
	)

	pygame.draw.aaline(surface=screen, color="cyan", start_pos=(10,200), end_pos=(200, 10))

	pygame.draw.aalines(
		surface=screen,
		color="orange",
		closed=True,
		points=[(30,70), (200, 15), (14,200)]
	)



	# desenhar frame
	pygame.display.update()

pygame.quit()
