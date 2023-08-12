import pygame
from pygame.locals import *

pygame.init()

class Window:
    WIDTH = 626
    HEIGHT = 470
    TITLE = "Looney Tunes"
    ICON = pygame.image.load('imgs/rabbit.png')

screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])


class World:
    BACKGROUND = pygame.image.load('imgs/fundo.png')

    def draw_background():
        screen.blit(World.BACKGROUND, [0, 0])


pygame.display.set_icon(Window.ICON)

clock = pygame.time.Clock()




pygame.mixer.init()

background_sound = pygame.mixer.Sound("sounds/nature.ogg")

background_sound.play(loops=-1)
background_sound.set_volume(0.2)

def play_sound_effect(sound_effect_path):
    pygame.mixer.music.load(sound_effect_path)
    pygame.mixer.music.play()

