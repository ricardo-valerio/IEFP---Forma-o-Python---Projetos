import pygame
from pygame.locals import *
import time
import random

pygame.mixer.pre_init()
pygame.mixer.init()
pygame.init()

pygame.display.set_caption("Zombie Race")

clock = pygame.time.Clock()

def play_sound_effect(sound_effect_path, second_channel=None):
    if second_channel:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(sound_effect_path))
    else:
        # pygame.mixer.music.load(sound_effect_path)
        # pygame.mixer.music.play()
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(sound_effect_path))


class Screen:
    WIDTH             = 1380
    HEIGHT            = 766
    FINISH_LINE_X     = 1235
    PHOTOGRAPHER_LINE = 760


screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))


class World:
    BACKGROUND         = pygame.image.load('imgs/track.png')
    RANKING_IMG        = pygame.image.load('imgs/ranking.png')
    PUBLIC_CHEARING    = pygame.image.load('imgs/public-cheering.png')
    FINISH_LINE        = pygame.image.load('imgs/finish-line.png')
    TIME_COUNTER_BOARD = pygame.image.load('imgs/time-counter-board.png')

    def draw_background():
        screen.blit(World.BACKGROUND, [0, 0])
        World.draw_public_chearing_img()
        World.draw_finish_line()
        World.draw_time_counter_board()

    def draw_ranking_board():
        screen.blit(World.RANKING_IMG, [200, 90])

    def draw_time_counter_board():
        screen.blit(World.TIME_COUNTER_BOARD, [1223, 346])

    def draw_finish_line():
        screen.blit(World.FINISH_LINE, [1223, 546])

    def draw_public_chearing_img():
        # 1st row
        for x in range(8):
            screen.blit( World.PUBLIC_CHEARING, [180+(128*x) + random.randint(1, 3), 190 + random.randint(1, 3)])
        # 2nd row
        for x in range(10):
            screen.blit(World.PUBLIC_CHEARING, [55+(128*x) + random.randint(1, 3), 290 + random.randint(1, 3)])


def write_text_with_font_roboto(text, text_color, bg_color=None, font_size=30, coords=(30, 30)):
    font_roboto = pygame.font.Font("fonts/Roboto-Regular.ttf", size=font_size)
    text_to_blit = font_roboto.render(text, True, text_color, bg_color)
    screen.blit(text_to_blit, coords)
