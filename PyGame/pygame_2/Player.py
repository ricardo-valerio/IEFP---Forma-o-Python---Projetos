import pygame

class Player():
	def __init__(self, x, y):
		self.__x = x
		self.__y = y
		self.__img = pygame.image.load("imgs/z1.png")

	def get_coordinates(self):
		return (self.__x, self.__y)

	def get_img(self):
		return self.__img

	def move_right(self, pixels=1):
		self.__x += pixels

	def move_left(self, pixels=1):
		self.__x -= pixels

	def draw_me(self, surface):
		surface.blit()
