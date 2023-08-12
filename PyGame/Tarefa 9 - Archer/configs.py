import pygame
pygame.init()

pygame.display.set_caption("Archer!")

class Screen:
    WIDTH = 1500
    HEIGHT = 833

screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))


class World:
    CURRENT_LEVEL = 1
    LEVEL_1_BACKGROUND = pygame.image.load(f'imgs/background-levels/level_1.png')
    LEVEL_2_BACKGROUND = pygame.image.load(f'imgs/background-levels/level_2.png')
    LEVEL_3_BACKGROUND = pygame.image.load(f'imgs/background-levels/level_3.png')
    LEVEL_COMPLETE_BANNER = pygame.image.load(f'imgs/level-complete.png')
    YOU_WIN_BANNER = pygame.image.load(f'imgs/you-win.png')

    def draw_background():
        match World.CURRENT_LEVEL:
            case 1:
                screen.blit(World.LEVEL_1_BACKGROUND, (0, 0))
            case 2:
                screen.blit(World.LEVEL_2_BACKGROUND, (0, 0))
            case 3:
                screen.blit(World.LEVEL_3_BACKGROUND, (0, 0))
            case _:
                screen.blit(World.LEVEL_1_BACKGROUND, (0, 0))


    def draw_level_complete_banner():
        screen.blit(
            World.LEVEL_COMPLETE_BANNER,
            (Screen.WIDTH / 2 - World.LEVEL_COMPLETE_BANNER.get_width() / 2, 0)
        )

    def draw_you_win_banner():
        screen.blit(
            World.YOU_WIN_BANNER,
            (Screen.WIDTH / 2 - World.YOU_WIN_BANNER.get_width() / 2, 0)
        )

clock = pygame.time.Clock()


# AUDIO ------------------------------------------------------
pygame.mixer.init()
background_sound = pygame.mixer.Sound('sounds/nature.ogg')
background_sound.play(loops=-1)

balloon_pop = pygame.mixer.Sound('sounds/balloon-pop.ogg')
balloon_pop.set_volume(0.5)

arrow_shoot = pygame.mixer.Sound('sounds/arrow-shoot.ogg')
arrow_shoot.set_volume(0.5)

e_oh = pygame.mixer.Sound('sounds/e-oh.ogg')
e_oh.set_volume(0.5)

level_complete = pygame.mixer.Sound('sounds/level-complete.ogg')
level_complete.set_volume(0.5)

you_win = pygame.mixer.Sound('sounds/you-win.ogg')
you_win.set_volume(0.5)

