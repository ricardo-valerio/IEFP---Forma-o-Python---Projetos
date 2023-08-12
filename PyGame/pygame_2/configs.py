import pygame
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 300


COLOR_LIST = ["green", "pink", "orange", "cyan", "indigo"]


def font_roboto(font_size=50):
	font_roboto = pygame.font.Font("fonts/Roboto-Regular.ttf", size=font_size)
	return font_roboto

def background_image(path="imgs/bg.png"):
	background_image = pygame.image.load(path)
	return background_image

def character(path="imgs/zombies/z1.png", x_flipped=False, y_flipped=False, xy_flipped=False):
	character = pygame.image.load(path)
	if x_flipped:
		return pygame.transform.flip(character, True, False)
	if y_flipped:
		return pygame.transform.flip(character, False, True)
	if xy_flipped:
		return pygame.transform.flip(character, True, True)
	return character
