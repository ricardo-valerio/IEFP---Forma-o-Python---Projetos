import pygame
pygame.init()

screen_width = 600
screen_height = 300

def font_roboto(font_size=50):
	font_roboto = pygame.font.Font("fonts/Roboto-Regular.ttf", size=font_size)
	return font_roboto
