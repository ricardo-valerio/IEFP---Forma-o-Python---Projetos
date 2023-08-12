from configs import *
import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Super Mario")


# def coordenates(x, y):
# 	return (x, screen_height )

clock = pygame.time.Clock()

running = True
while running:

	dt = clock.tick(60) # 60 FPS

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# screen.fill((123,23,23)) # rgb
	# screen.fill("yellow") # string
	screen.fill("#ad5199") # hexadecimal

	text = font_roboto.render("Olá Ricardo!", True, "green", "brown")
	screen.blit(text, (10, 250))

	# w, h = pygame.display.get_surface().get_size()
	print(pygame.display.get_surface().get_size())

	# desenhar frame
	pygame.display.update()

pygame.quit()
