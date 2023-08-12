import pygame
pygame.init()

pygame.display.set_caption("Tarefa 8")


class World:
    SOCCER_FIELD      = pygame.image.load('imgs/soccer-field.png')
    GOAL_WALLPAPER    = pygame.image.load('imgs/goal-poster.png')
    SOCCER_BALL       = pygame.image.load('imgs/soccer-ball.png')
    GOALS_SCORE_BOARD = pygame.image.load('imgs/score-board.png')

    def draw_soccer_field_and_score_board():
        screen.blit(World.SOCCER_FIELD, (0, 0))
        World.draw_goals_score_board()


    def draw_goal_wallpaper():
        screen.blit(
            World.GOAL_WALLPAPER,
            [
                Screen.CENTER_X_OF_SOCCER_FIELD - Screen.CENTER_X_OF_GOAL_WALLPAPER,
                Screen.CENTER_Y_OF_SOCCER_FIELD - Screen.CENTER_Y_OF_GOAL_WALLPAPER
            ]
        )
        pygame.display.update()


    def draw_goals_score_board():
        screen.blit(
            World.GOALS_SCORE_BOARD,
            (
                Screen.CENTER_X_OF_SOCCER_FIELD - Screen.CENTER_X_OF_GOALS_SCORE_BOARD,
                Screen.HORIZONTAL_TOP_SOCCER_FIELD_LIMIT - World.GOALS_SCORE_BOARD.get_height() - 3
            )
        )


class Screen:
    # SOCCER FIELD: DIMENSIONS AND CENTER COORDS ----------------------------------------------------
    WIDTH  = World.SOCCER_FIELD.get_width()
    HEIGHT = World.SOCCER_FIELD.get_height()

    CENTER_COORDS_OF_SOCCER_FIELD = World.SOCCER_FIELD.get_rect().center # tuple with coordinates
    CENTER_X_OF_SOCCER_FIELD      = CENTER_COORDS_OF_SOCCER_FIELD[0]
    CENTER_Y_OF_SOCCER_FIELD      = CENTER_COORDS_OF_SOCCER_FIELD[1]

    # SOCCER FIELD: LIMITS --------------------------------------------------------------------------
    VERTICAL_RIGHT_SOCCER_FIELD_LIMIT    = 1133 # x  = 1133
    VERTICAL_LEFT_SOCCER_FIELD_LIMIT     = 68   # x  = 68
    HORIZONTAL_TOP_SOCCER_FIELD_LIMIT    = 70   # y  = 70
    HORIZONTAL_BOTTOM_SOCCER_FIELD_LIMIT = 731  # y  = 731

    # BALL ------------------------------------------------------------------------------------------
    CENTER_COORDS_OF_SOCCER_BALL = World.SOCCER_BALL.get_rect().center # tuple with coordinates
    CENTER_X_OF_SOCCER_BALL      = CENTER_COORDS_OF_SOCCER_BALL[0]
    CENTER_Y_OF_SOCCER_BALL      = CENTER_COORDS_OF_SOCCER_BALL[1]

    print(CENTER_COORDS_OF_SOCCER_BALL, CENTER_X_OF_SOCCER_BALL, CENTER_Y_OF_SOCCER_BALL)

    # GOALS SCORE BOARD -----------------------------------------------------------------------------
    CENTER_COORDS_OF_GOALS_SCORE_BOARD = World.GOALS_SCORE_BOARD.get_rect().center
    CENTER_X_OF_GOALS_SCORE_BOARD      = CENTER_COORDS_OF_GOALS_SCORE_BOARD[0]
    CENTER_Y_OF_GOALS_SCORE_BOARD      = CENTER_COORDS_OF_GOALS_SCORE_BOARD[1]

    # GOAL NET --------------------------------------------------------------------------------------
    GOAL_NET_TOP_LIMIT    = 336   # y = 336
    GOAL_NET_BOTTOM_LIMIT = 464   # y = 464

    # GOAL NET LINE CORRECTION WHEN CROSSED  --------------------------------------------------------
    GOAL_LINE_CROSSING_MARGIN_RIGHT_SIDE = 5
    GOAL_LINE_CROSSING_MARGIN_LEFT_SIDE  = 7

    # GOAL POSTER -----------------------------------------------------------------------------------
    CENTER_COORDS_OF_GOAL_WALLPAPER = World.GOAL_WALLPAPER.get_rect().center # tuple with coordinates
    CENTER_X_OF_GOAL_WALLPAPER      = CENTER_COORDS_OF_GOAL_WALLPAPER[0]
    CENTER_Y_OF_GOAL_WALLPAPER      = CENTER_COORDS_OF_GOAL_WALLPAPER[1]


screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))



# AUDIO ------------------------------------------------------
pygame.mixer.init()
background_sound = pygame.mixer.Sound('sounds/som.ogg')
background_sound.play(loops=-1)
background_sound.set_volume(0.3)

goal_sound = pygame.mixer.Sound('sounds/goal.ogg')
goal_sound.set_volume(0.7)

