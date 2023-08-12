import pygame
pygame.init()

class Window:
    WIDTH = 626
    HEIGHT = 470
    TITLE = "Looney Tunes"
    ICON = pygame.image.load("imgs/icon.png")

class World:
    BACKGROUND = pygame.image.load("imgs/fundo.png")

class Skins:
    BUGS_BUNNY = pygame.image.load("imgs/coelho.png")
    ELMER = pygame.image.load("imgs/cacador.png")

#class Font:
    #ROBOTO50 = pygame.font.Font('fonts/Roboto-Regular.ttf', 50)