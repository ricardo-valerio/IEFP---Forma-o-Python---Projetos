from configs import *
import pygame
from pygame.locals import *

import random

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Super Mario")


# def coordenates(x, y):
# 	return (x, screen_height )

# def draw_rectangle(surface=screen, color="black", rect=(20 + x, 30, 70, 50 ), width)

clock = pygame.time.Clock()
x = 0
color="green"
color_list = ["green", "pink", "orange", "cyan", "indigo"]

running = True
while running:

	dt = clock.tick(120) # 60 FPS

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	if x >= screen_width:
		x = -130
		color = random.choice(color_list)
	else:
		x += 1

	text = font_roboto(font_size=15).render("Olá Ricardo!", True, "green", "brown")
	screen.blit(text, (10, 250))
														# (x , y)(width, height)
	pygame.draw.rect(surface=screen, color=color, rect=((20 + x, 30), (70, 50)), width=0 )
	pygame.draw.rect(surface=screen, color="gray", rect=(80 + x, 50, 50, 30), width=0)
	pygame.draw.rect(surface=screen, color="black", rect=(80 + x, 35, 50, 10), width=0)
	pygame.draw.circle(surface=screen, color="black", center=(45 + x, 85), radius=15)
	pygame.draw.circle(surface=screen, color="black", center=(105 + x, 85), radius=15)

	# desenhar frame
	pygame.display.update()

pygame.quit()
