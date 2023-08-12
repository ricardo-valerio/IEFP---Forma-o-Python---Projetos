import pygame
from pygame.locals import *
from HeroKid import HeroKid
from Spaceship import Spaceship
from AlienDrLime import AlienDrLime
from Obstacles import *
from LifeBar import LifeBar
from Star import Star
from Planet import Planet
from Diamond import Diamond
from PointBoosterCollectable import PointBoosterCollectable
import random

pygame.init()
pygame.mixer.pre_init()
pygame.mixer.init()


class Window:
    WIDTH = 1400
    HEIGHT = 780
    TITLE = "Outer Space"
    ICON = pygame.image.load('imgs/star.ico')
    LOADING_IMAGE = pygame.image.load('imgs/splash.png')


screen = pygame.display.set_mode([Window.WIDTH, Window.HEIGHT])
pygame.display.set_icon(Window.ICON)
pygame.display.set_caption(Window.TITLE)

# draw splash image -------------------------------------
screen.blit(Window.LOADING_IMAGE, [0, 0])
pygame.display.update()
# -------------------------------------------------------


class Skins:
    HERO_KID = pygame.image.load('imgs/main_character.png').convert_alpha()
    HERO_KID_GRAY = pygame.image.load('imgs/main_character_gray.png').convert_alpha()
    SPACESHIP = pygame.image.load('imgs/spaceship.png').convert_alpha()
    SPACESHIP_GRAY = pygame.image.load('imgs/spaceship_gray.png').convert_alpha()
    STAR = pygame.image.load('imgs/star.png').convert_alpha()
    POINT_BOOSTER_COLLECTABLE = pygame.image.load('imgs/python_logo.png').convert_alpha()
    LIFE_BAR = [
        pygame.image.load('imgs/life_bar/lifebar_1.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/lifebar_2.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/lifebar_3.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/lifebar_4.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/lifebar_5.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/lifebar_6.png').convert_alpha(),
    ]
    DR_LIME_LIFE_BAR = [
        pygame.image.load('imgs/life_bar/dr_lime_life_bar_1.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/dr_lime_life_bar_2.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/dr_lime_life_bar_3.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/dr_lime_life_bar_4.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/dr_lime_life_bar_5.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/dr_lime_life_bar_6.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/dr_lime_life_bar_7.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/dr_lime_life_bar_8.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/dr_lime_life_bar_9.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/dr_lime_life_bar_10.png').convert_alpha(),
        pygame.image.load('imgs/life_bar/dr_lime_life_bar_11.png').convert_alpha(),
    ]
    LASER_BEAMS = [
        pygame.image.load('imgs/laser_beams/beam0.png').convert_alpha(),
        pygame.image.load('imgs/laser_beams/beam1.png').convert_alpha(),
        pygame.image.load('imgs/laser_beams/beam2.png').convert_alpha(),
        pygame.image.load('imgs/laser_beams/beam3.png').convert_alpha(),
        pygame.image.load('imgs/laser_beams/beam4.png').convert_alpha(),
        pygame.image.load('imgs/laser_beams/beam5.png').convert_alpha(),
        pygame.image.load('imgs/laser_beams/beam6.png').convert_alpha(),
    ]
    ALIEN_DR_LIME = pygame.image.load('imgs/main_enemy.png').convert_alpha()
    ALIEN_DR_LIME_GRAY = pygame.image.load('imgs/main_enemy_gray.png').convert_alpha()
    ALIEN_DR_LIME_SPEACH = pygame.image.load('imgs/dr_lime_speach.png').convert_alpha()

    OBSTACLES = {
        "ASTEROIDS": [
            pygame.image.load('imgs/obstacles/asteroids/asteroid1.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/asteroids/asteroid2.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/asteroids/asteroid3.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/asteroids/asteroid4.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/asteroids/asteroid5.png').convert_alpha(),
        ],
        "PLANET_EARTH_COLLISION_ASTEROIDS": [
            pygame.image.load('imgs/obstacles/planet_earth_collision_asteroids/asteroid1.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/planet_earth_collision_asteroids/asteroid2.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/planet_earth_collision_asteroids/asteroid3.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/planet_earth_collision_asteroids/asteroid4.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/planet_earth_collision_asteroids/asteroid5.png').convert_alpha(),
        ],
        "HUMAN_SPACE_JUNK": [
            pygame.image.load('imgs/obstacles/human_junk/junk1.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk2.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk3.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk4.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk5.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk6.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk7.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk8.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk9.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk10.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk11.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk12.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk13.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk14.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk15.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk16.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk17.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk18.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk19.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk20.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk21.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk22.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk23.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk24.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk25.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk26.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk27.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk28.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk29.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/human_junk/junk30.png').convert_alpha(),
        ],
        "SATELLITES": [
            pygame.image.load('imgs/obstacles/satellites/satellite1.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/satellites/satellite2.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/satellites/satellite3.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/satellites/satellite4.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/satellites/satellite5.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/satellites/satellite6.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/satellites/satellite7.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/satellites/satellite8.png').convert_alpha(),
        ],
        "ALIEN_SPACESHIPS": [
            pygame.image.load('imgs/obstacles/alien_spaceships/spaceship1.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/alien_spaceships/spaceship2.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/alien_spaceships/spaceship3.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/alien_spaceships/spaceship4.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/alien_spaceships/spaceship5.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/alien_spaceships/spaceship6.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/alien_spaceships/spaceship7.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/alien_spaceships/spaceship8.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/alien_spaceships/spaceship9.png').convert_alpha(),
        ],
        "ALIEN_MARBLES": [
            pygame.image.load('imgs/obstacles/marbles/marble1.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/marbles/marble2.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/marbles/marble3.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/marbles/marble4.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/marbles/marble5.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/marbles/marble6.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/marbles/marble7.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/marbles/marble8.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/marbles/marble9.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/marbles/marble10.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/marbles/marble11.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/marbles/marble12.png').convert_alpha(),
        ],
        "ALIEN_MONSTERS": [
            pygame.image.load('imgs/obstacles/monsters/monster1.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster2.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster3.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster4.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster5.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster6.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster7.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster8.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster9.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster17.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster18.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster19.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster20.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster21.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster22.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster23.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster24.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster25.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster26.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster27.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster28.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster29.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster30.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster31.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster32.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster33.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster34.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster35.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster36.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster37.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster38.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster39.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster40.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster41.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster10.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster11.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster12.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster13.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster14.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster15.png').convert_alpha(),
            pygame.image.load('imgs/obstacles/monsters/monster16.png').convert_alpha(),
        ]

    }

    EXPLOSIONS = [
        pygame.image.load('imgs/explosions/explosion1.png').convert_alpha(),
        pygame.image.load('imgs/explosions/explosion2.png').convert_alpha(),
        pygame.image.load('imgs/explosions/explosion3.png').convert_alpha(),
        pygame.image.load('imgs/explosions/explosion4.png').convert_alpha(),
    ]

    DIAMONDS = [
        pygame.image.load('imgs/diamonds/diamond_1.png').convert_alpha(),
        pygame.image.load('imgs/diamonds/diamond_2.png').convert_alpha(),
        pygame.image.load('imgs/diamonds/diamond_3.png').convert_alpha(),
        pygame.image.load('imgs/diamonds/diamond_4.png').convert_alpha(),
        pygame.image.load('imgs/diamonds/diamond_5.png').convert_alpha(),
        pygame.image.load('imgs/diamonds/diamond_6.png').convert_alpha(),
    ]

    COLLECTED_DIAMONDS = [
        pygame.image.load('imgs/diamonds/0_diamonds_colored.png').convert_alpha(),
        pygame.image.load('imgs/diamonds/1_diamond_colored.png').convert_alpha(),
        pygame.image.load('imgs/diamonds/2_diamonds_colored.png').convert_alpha(),
        pygame.image.load('imgs/diamonds/3_diamonds_colored.png').convert_alpha(),
        pygame.image.load('imgs/diamonds/4_diamonds_colored.png').convert_alpha(),
        pygame.image.load('imgs/diamonds/5_diamonds_colored.png').convert_alpha(),
        pygame.image.load('imgs/diamonds/6_diamonds_colored.png').convert_alpha(),
    ]

    PLANETS = [
        pygame.image.load('imgs/planets/planet_1.png').convert_alpha(),
        pygame.image.load('imgs/planets/planet_2.png').convert_alpha(),
        pygame.image.load('imgs/planets/planet_3.png').convert_alpha(),
        pygame.image.load('imgs/planets/planet_4.png').convert_alpha(),
        pygame.image.load('imgs/planets/planet_5.png').convert_alpha(),
        pygame.image.load('imgs/planets/planet_6.png').convert_alpha(),
        pygame.image.load('imgs/planets/planet-earth.png').convert_alpha(),
    ]

    SCORE_BOARD_TABLE = pygame.image.load('imgs/score_board_image_with_table.png')

class GameState:
    FIRST_TIME_RUNNING   = 0
    PRESENTING_STORY     = 1
    PAUSED               = 2
    OVER                 = 3
    RUNNING              = 4
    LEVEL_COMPLETE       = 5
    YOU_WIN              = 6
    THE_END              = 7



class Game:
    STATE = GameState.FIRST_TIME_RUNNING
    CURRENT_LEVEL = 14
    LIFE_BAR = LifeBar(x=15, y=10, skin=Skins.LIFE_BAR[0], number_of_lives=5)
    DR_LIME_LIFE_BAR = LifeBar(x=1000, y=10, skin=Skins.DR_LIME_LIFE_BAR[0], number_of_lives=10)
    STAR = Star(x=1405, y=785, skin=Skins.STAR)
    GAME_OVER_IMAGE = pygame.image.load('imgs/game_over.png')
    GAME_PAUSED_IMAGE = pygame.image.load('imgs/paused.png')
    GAME_WAS_PAUSED = False
    BACKGROUND_SOUND_IS_PLAYING = False
    SOUND_EFFECT_IS_PLAYING = False

    GAME_POINTS = 900
    START_LEVEL_POINTS = 900

    class Points:
        PLANET_EARTH_COLLISION_ASTEROIDS = 4
        HUMAN_SPACE_JUNK = 3
        ALIEN_SPACESHIPS = 2
        ALIEN_MARBLES = 1
        POINT_BOOSTER_COLLECTABLE = 5

        class Counter:
            PLANET_EARTH_COLLISION_ASTEROIDS = 0
            HUMAN_SPACE_JUNK = 0
            ALIEN_SPACESHIPS = 0
            ALIEN_MARBLES = 0
            POINT_BOOSTER_COLLECTABLE = 0

    def draw_background():
        screen.blit(GAME_LEVELS[Game.CURRENT_LEVEL]["background"], [0, 0])

    def draw_presenting_story_image():
        screen.blit(GAME_LEVELS[Game.CURRENT_LEVEL]["presenting_story"], [0, 0])
        pygame.display.update()

    def draw_life_bar():
        screen.blit(Game.LIFE_BAR.get_skin(), Game.LIFE_BAR.get_position())

    def draw_dr_lime_life_bar():
        screen.blit(Game.DR_LIME_LIFE_BAR.get_skin(), Game.DR_LIME_LIFE_BAR.get_position())

    def draw_dr_lime_speach():
        screen.blit(Skins.ALIEN_DR_LIME_SPEACH, [490, 470])

    def draw_star_if_life_is_low():
        if "alien_dr_lime" not in GAME_LEVELS[Game.CURRENT_LEVEL] and Game.LIFE_BAR.get_current_number_of_lives() < 2:
            if not Game.STAR.y_is_set:
                Game.STAR.set_y_according_to_current_level()

            Game.STAR.move_left()
            Game.STAR.draw()


    def draw_paused_game_image():
        if not Game.GAME_WAS_PAUSED:
            Game.GAME_WAS_PAUSED = True
            screen.blit(Game.GAME_PAUSED_IMAGE, [0, 0])

    def draw_gameover_image():
        screen.blit(Game.GAME_OVER_IMAGE, [0, 0])

    def draw_level_completed_image():
        screen.blit(GAME_LEVELS[Game.CURRENT_LEVEL]["level_complete_image"], [0, 0])
        pygame.display.update()

    def draw_you_made_it_to_the_top_10():
        screen.blit(GAME_LEVELS[Game.CURRENT_LEVEL]["you_did_make_it_to_the_top_10_image"], [0, 0])

    def draw_you_didnt_make_it_to_the_top_10():
        screen.blit(GAME_LEVELS[Game.CURRENT_LEVEL]["you_didnt_make_it_to_the_top_10_image"], [0, 0])

    def draw_score_board_background_with_table():
        screen.blit(Skins.SCORE_BOARD_TABLE, [0, 0])

    def draw_the_end_image():
        screen.blit(GAME_LEVELS[Game.CURRENT_LEVEL]["the_end_image"], [0, 0])
        pygame.display.update()

    def draw_you_win_image():
        screen.blit(GAME_LEVELS[Game.CURRENT_LEVEL]["you_win_image"], [0, 0])
        pygame.display.update()

    def play_level_background_sound(volume=None):
        sound_path = GAME_LEVELS[Game.CURRENT_LEVEL]["level_sound"]
        # background_sound = pygame.mixer.Sound(sound_path)
        # background_sound.play(loops=-1)
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play(loops=-1)

        if volume:
            pygame.mixer.music.set_volume(volume)
            # background_sound.set_volume(volume)


    def play_sound_effect(sound_effect_path, channel_number=0):
        pygame.mixer.Channel(channel_number).play(pygame.mixer.Sound(sound_effect_path))


    def write_text_with_font_valorax(text, text_color="white", bg_color=None, font_size=27, coords=(30, 30)):
        font_roboto = pygame.font.Font("fonts/Valorax.otf", size=font_size)
        text_to_blit = font_roboto.render(text, True, text_color, bg_color)
        screen.blit(text_to_blit, coords)

    def draw_level_X_of_6():
        if 0 < Game.CURRENT_LEVEL < 13:
            screen.blit(GAME_LEVELS[Game.CURRENT_LEVEL]["collected_diamonds"], [configs.Window.WIDTH - 215, 15])
        elif Game.CURRENT_LEVEL == 13:
            screen.blit(GAME_LEVELS[Game.CURRENT_LEVEL]["collected_diamonds"], [configs.Window.WIDTH/2 - 100, 15])


    def draw_game_points():
        match Game.CURRENT_LEVEL:
            case 3 | 5 | 7 | 9 | 11 | 13:
                configs.Game.write_text_with_font_valorax(
                    text=f"POINTS: {Game.GAME_POINTS}",
                    coords=(configs.Window.WIDTH/6, 15)
                )



clock = pygame.time.Clock()


# AUDIO ------------------------------------------------------
# pygame.mixer.init()
# background_sound = pygame.mixer.Sound('sounds/nature.ogg')
# background_sound.play(loops=-1)

# balloon_pop = pygame.mixer.Sound('sounds/balloon-pop.ogg')
# balloon_pop.set_volume(0.5)

# arrow_shoot = pygame.mixer.Sound('sounds/arrow-shoot.ogg')
# arrow_shoot.set_volume(0.5)

# e_oh = pygame.mixer.Sound('sounds/e-oh.ogg')
# e_oh.set_volume(0.5)

# level_complete = pygame.mixer.Sound('sounds/level-complete.ogg')
# level_complete.set_volume(0.5)

# you_win = pygame.mixer.Sound('sounds/you-win.ogg')
# you_win.set_volume(0.5)



GAME_LEVELS = {
    0: {
        "background": pygame.image.load('imgs/press_start.png'),
        "level_sound": "sounds/levels/intro-story.mp3",
    },
    1: {
        "presenting_story": pygame.image.load('imgs/story/voyage-1.png'),
        "background": pygame.image.load('imgs/backgrounds/bg1.jpg'),
        "level_sound": "sounds/levels/level-1.mp3",
        "main_character": Spaceship(
                            x=30,
                            y=Window.HEIGHT/2,
                            skin=Skins.SPACESHIP,
                            gray_skin=Skins.SPACESHIP_GRAY
                          ),
        "obstacles": [
            Asteroid(offset=5),
            Asteroid(offset=150),
            Asteroid(offset=250),
            Asteroid(offset=350),
            Asteroid(offset=650),
        ],
        "number_of_rounds": 5,
        "planet": Planet(skin_index=0),
        "collected_diamonds": Skins.COLLECTED_DIAMONDS[0],
    },
    2: {
        "presenting_story": pygame.image.load('imgs/story/arrived-at-planet-1.png'),
        "background": pygame.image.load('imgs/backgrounds/bgd1.jpg'),
        "level_sound": "sounds/levels/planet-levels.mp3",
        "ground_y": 700,
        "main_character": HeroKid(
                            x=130,
                            y=700 - Skins.HERO_KID.get_height(),
                            skin=Skins.HERO_KID,
                            gray_skin=Skins.HERO_KID_GRAY
                          ),
        "obstacles": [
            AlienMonster(ground_y=700, offset=5, skin_lower_limit=0, skin_upper_limit=9),
            AlienMonster(ground_y=700, offset=700, skin_lower_limit=0, skin_upper_limit=9),
            AlienMonster(ground_y=700, offset=1400, skin_lower_limit=0, skin_upper_limit=9),
            AlienMonster(ground_y=700, offset=2100, skin_lower_limit=0, skin_upper_limit=9),
            AlienMonster(ground_y=700, offset=2800, skin_lower_limit=0, skin_upper_limit=9),
        ],
        "number_of_rounds": 3,
        "diamond": Diamond(skin_index=0),
        "collected_diamonds": Skins.COLLECTED_DIAMONDS[0],
        "level_complete_image": pygame.image.load('imgs/level_completed/level_completed_1.png'),
    },
    3: {
        "presenting_story": pygame.image.load('imgs/story/voyage-2.png'),
        "background": pygame.image.load('imgs/backgrounds/bg2.jpg'),
        "level_sound": "sounds/levels/level-1.mp3",
        "main_character": Spaceship(
                            x=30,
                            y=Window.HEIGHT/2,
                            skin=Skins.SPACESHIP,
                            gray_skin=Skins.SPACESHIP_GRAY
                          ),
        "obstacles": [
            Asteroid(offset=5),
            Asteroid(offset=150),
            Asteroid(offset=250),
            Asteroid(offset=350),
            Asteroid(offset=650),
            PlanetEarthCollisionAsteroid(offset=1000),
            PlanetEarthCollisionAsteroid(offset=1590),
        ],
        "number_of_rounds": 10,
        "planet": Planet(skin_index=1),
        "collected_diamonds": Skins.COLLECTED_DIAMONDS[1],
    },
    4: {
        "presenting_story": pygame.image.load('imgs/story/arrived-at-planet-2.png'),
        "background": pygame.image.load('imgs/backgrounds/bgd2.jpg'),
        "level_sound": "sounds/levels/planet-levels.mp3",
        "ground_y": 700,
        "main_character": HeroKid(
                            x=130,
                            y=700 - Skins.HERO_KID.get_height(),
                            skin=Skins.HERO_KID,
                            gray_skin=Skins.HERO_KID_GRAY
                          ),
        "obstacles": [
            AlienMonster(ground_y=700, offset=5, skin_lower_limit=9, skin_upper_limit=16),
            AlienMonster(ground_y=700, offset=700, skin_lower_limit=9, skin_upper_limit=16),
            AlienMonster(ground_y=700, offset=1400, skin_lower_limit=9, skin_upper_limit=16),
            AlienMonster(ground_y=700, offset=2100, skin_lower_limit=9, skin_upper_limit=16),
            AlienMonster(ground_y=700, offset=2800, skin_lower_limit=9, skin_upper_limit=16),
        ],
        "number_of_rounds": 3,
        "diamond": Diamond(skin_index=1),
        "collected_diamonds": Skins.COLLECTED_DIAMONDS[1],
        "level_complete_image": pygame.image.load('imgs/level_completed/level_completed_2.png'),
    },
    5: {
        "presenting_story": pygame.image.load('imgs/story/voyage-3.png'),
        "background": pygame.image.load('imgs/backgrounds/bg3.jpg'),
        "level_sound": "sounds/levels/level-1.mp3",
        "main_character": Spaceship(
                            x=30,
                            y=Window.HEIGHT/2,
                            skin=Skins.SPACESHIP,
                            gray_skin=Skins.SPACESHIP_GRAY
                          ),
        "obstacles": [
            Asteroid(offset=5),
            Asteroid(offset=150),
            Asteroid(offset=250),
            Asteroid(offset=350),
            Asteroid(offset=650),
            HumanJunk(offset=5),
            HumanJunk(offset=150),
            HumanJunk(offset=250),
            HumanJunk(offset=350),
            HumanJunk(offset=650),
            HumanJunk(offset=950),
        ],
        "number_of_rounds": 15,
        "planet": Planet(skin_index=2),
        "collected_diamonds": Skins.COLLECTED_DIAMONDS[2],
    },
    6: {
        "presenting_story": pygame.image.load('imgs/story/arrived-at-planet-3.png'),
        "background": pygame.image.load('imgs/backgrounds/bgd3.jpg'),
        "level_sound": "sounds/levels/planet-levels.mp3",
        "ground_y": 727,
        "main_character": HeroKid(
                            x=130,
                            y=727 - Skins.HERO_KID.get_height(),
                            skin=Skins.HERO_KID,
                            gray_skin=Skins.HERO_KID_GRAY
                          ),
        "obstacles": [
            AlienMonster(ground_y=727, offset=5, skin_lower_limit=17, skin_upper_limit=23),
            AlienMonster(ground_y=727, offset=700, skin_lower_limit=17, skin_upper_limit=23),
            AlienMonster(ground_y=727, offset=1400, skin_lower_limit=17, skin_upper_limit=23),
            AlienMonster(ground_y=727, offset=2100, skin_lower_limit=17, skin_upper_limit=23),
            AlienMonster(ground_y=727, offset=2800, skin_lower_limit=17, skin_upper_limit=23),
        ],
        "number_of_rounds": 3,
        "diamond": Diamond(skin_index=2),
        "collected_diamonds": Skins.COLLECTED_DIAMONDS[2],
        "level_complete_image": pygame.image.load('imgs/level_completed/level_completed_3.png'),
    },
    7: {
        "presenting_story": pygame.image.load('imgs/story/voyage-4.png'),
        "background": pygame.image.load('imgs/backgrounds/bg4.jpg'),
        "level_sound": "sounds/levels/level-1.mp3",
        "main_character": Spaceship(
                            x=30,
                            y=Window.HEIGHT/2,
                            skin=Skins.SPACESHIP,
                            gray_skin=Skins.SPACESHIP_GRAY
                          ),
        "obstacles": [
            Asteroid(offset=5),
            Asteroid(offset=150),
            Asteroid(offset=250),
            Asteroid(offset=350),
            Asteroid(offset=650),
            AlienSpaceship(offset=450),
            AlienSpaceship(offset=750),
            AlienSpaceship(offset=1050),
        ],
        "number_of_rounds": 15,
        "planet": Planet(skin_index=3),
        "collected_diamonds": Skins.COLLECTED_DIAMONDS[3],
    },
    8: {
        "presenting_story": pygame.image.load('imgs/story/arrived-at-planet-4.png'),
        "background": pygame.image.load('imgs/backgrounds/bgd4.jpg'),
        "level_sound": "sounds/levels/planet-levels.mp3",
        "ground_y": 740,
        "main_character": HeroKid(
                            x=130,
                            y=740 - Skins.HERO_KID.get_height(),
                            skin=Skins.HERO_KID,
                            gray_skin=Skins.HERO_KID_GRAY
                          ),
        "obstacles": [
            AlienMonster(ground_y=740, offset=5, skin_lower_limit=17, skin_upper_limit=30),
            AlienMonster(ground_y=740, offset=700, skin_lower_limit=17, skin_upper_limit=30),
            AlienMonster(ground_y=740, offset=1400, skin_lower_limit=17, skin_upper_limit=30),
            AlienMonster(ground_y=740, offset=2100, skin_lower_limit=17, skin_upper_limit=30),
            AlienMonster(ground_y=740, offset=2800, skin_lower_limit=17, skin_upper_limit=30),
        ],
        "number_of_rounds": 3,
        "diamond": Diamond(skin_index=3),
        "collected_diamonds": Skins.COLLECTED_DIAMONDS[3],
        "level_complete_image": pygame.image.load('imgs/level_completed/level_completed_4.png'),
    },
    9: {
        "presenting_story": pygame.image.load('imgs/story/voyage-5.png'),
        "background": pygame.image.load('imgs/backgrounds/bg5.jpg'),
        "level_sound": "sounds/levels/level-1.mp3",
        "main_character": Spaceship(
                            x=30,
                            y=Window.HEIGHT/2,
                            skin=Skins.SPACESHIP,
                            gray_skin=Skins.SPACESHIP_GRAY
                          ),
        "obstacles": [
            Asteroid(offset=5),
            Asteroid(offset=150),
            Asteroid(offset=250),
            Asteroid(offset=350),
            Asteroid(offset=650),
            AlienSpaceship(offset=450),
            AlienSpaceship(offset=450),
            PlanetEarthCollisionAsteroid(offset=1000),

        ],
        "number_of_rounds": 15,
        "planet": Planet(skin_index=4),
        "collected_diamonds": Skins.COLLECTED_DIAMONDS[4],
    },
    10: {
        "presenting_story": pygame.image.load('imgs/story/arrived-at-planet-5.png'),
        "background": pygame.image.load('imgs/backgrounds/bgd5.jpg'),
        "level_sound": "sounds/levels/planet-levels.mp3",
        "ground_y": 700,
        "main_character": HeroKid(
                            x=130,
                            y=700 - Skins.HERO_KID.get_height(),
                            skin=Skins.HERO_KID,
                            gray_skin=Skins.HERO_KID_GRAY
                          ),
        "obstacles": [
            AlienMonster(ground_y=700, offset=5, skin_lower_limit=33, skin_upper_limit=41),
            AlienMonster(ground_y=700, offset=700, skin_lower_limit=33, skin_upper_limit=41),
            AlienMonster(ground_y=700, offset=1400, skin_lower_limit=33, skin_upper_limit=41),
            AlienMonster(ground_y=700, offset=2100, skin_lower_limit=33, skin_upper_limit=41),
            AlienMonster(ground_y=700, offset=2800, skin_lower_limit=33, skin_upper_limit=41),
        ],
        "number_of_rounds": 3,
        "diamond": Diamond(skin_index=4),
        "collected_diamonds": Skins.COLLECTED_DIAMONDS[4],
        "level_complete_image": pygame.image.load('imgs/level_completed/level_completed_5.png'),
    },
    11: {
        "presenting_story": pygame.image.load('imgs/story/voyage-6.png'),
        "background": pygame.image.load('imgs/backgrounds/bg6.jpg'),
        "level_sound": "sounds/levels/level-1.mp3",
        "main_character": Spaceship(
                            x=30,
                            y=Window.HEIGHT/2,
                            skin=Skins.SPACESHIP,
                            gray_skin=Skins.SPACESHIP_GRAY
                          ),
        "obstacles": [
            Asteroid(offset=5),
            Asteroid(offset=150),
            Asteroid(offset=250),
            Asteroid(offset=350),
            Asteroid(offset=650),
            AlienSpaceship(offset=450),
            PlanetEarthCollisionAsteroid(offset=1000),
            HumanJunk(offset=850),
        ],
        "point_booster_collectable_objects": [
            PointBoosterCollectable(offset=250),
            PointBoosterCollectable(offset=650),
            PointBoosterCollectable(offset=1000),
        ],
        "number_of_rounds": 20,
        "planet": Planet(skin_index=5),
        "collected_diamonds": Skins.COLLECTED_DIAMONDS[5],
    },
    12: {
        "presenting_story": pygame.image.load('imgs/story/arrived-at-planet-6.png'),
        "background": pygame.image.load('imgs/backgrounds/bgd6.jpg'),
        "level_sound": "sounds/levels/planet-levels.mp3",
        "ground_y": 662,
        "main_character": HeroKid(
                            x=130,
                            y=662 - Skins.HERO_KID.get_height(),
                            skin=Skins.HERO_KID,
                            gray_skin=Skins.HERO_KID_GRAY
                          ),
        "obstacles": [
            AlienMonster(ground_y=662, offset=5, skin_lower_limit=0, skin_upper_limit=41),
            AlienMonster(ground_y=662, offset=1700, skin_lower_limit=0, skin_upper_limit=41),
            AlienMonster(ground_y=662, offset=2400, skin_lower_limit=0, skin_upper_limit=41),
            AlienMonster(ground_y=662, offset=3100, skin_lower_limit=0, skin_upper_limit=41),
            AlienMonster(ground_y=662, offset=4800, skin_lower_limit=0, skin_upper_limit=41),
        ],
        "number_of_rounds": 3,
        "diamond": Diamond(skin_index=5),
        "collected_diamonds": Skins.COLLECTED_DIAMONDS[5],
        "level_complete_image": pygame.image.load('imgs/level_completed/level_completed_6.png'),
        "you_win_image": pygame.image.load('imgs/you_win.png'),
    },
    13: {
        "presenting_story": pygame.image.load('imgs/story/voyage-7.png'),
        "background": pygame.image.load('imgs/backgrounds/bg6.jpg'),
        "level_sound": "sounds/levels/level-13.mp3",
        "main_character": Spaceship(
                            x=30,
                            y=Window.HEIGHT/2,
                            skin=Skins.SPACESHIP,
                            gray_skin=Skins.SPACESHIP_GRAY
                          ),
        "obstacles": [
            Asteroid(offset=5),
            Asteroid(offset=150),
            Asteroid(offset=250),
            Asteroid(offset=350),
            AlienSpaceship(offset=450),
            HumanJunk(offset=850),
            HumanJunk(offset=850),
        ],
        "point_booster_collectable_objects": [
            PointBoosterCollectable(offset=250),
        ],
        "alien_dr_lime": AlienDrLime(
                            x=Window.WIDTH + 5,
                            y=Window.HEIGHT/2,
                            skin=Skins.ALIEN_DR_LIME,
                            gray_skin=Skins.ALIEN_DR_LIME_GRAY
                          ),
        "number_of_rounds": 3,
        "collected_diamonds": Skins.COLLECTED_DIAMONDS[6],
        "planet": Planet(skin_index=6),
    },
    14: {
        "you_did_make_it_to_the_top_10_image": pygame.image.load('imgs/finished_and_did_make_it_to_top_10.png'),
        "you_didnt_make_it_to_the_top_10_image": pygame.image.load('imgs/finished_but_didnt_make_it_to_top_10.png'),
        "the_end_image": pygame.image.load('imgs/the_end.png'),
    },
}
