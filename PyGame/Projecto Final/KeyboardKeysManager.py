from configs import *

def odd_levels_keys(key):
    spaceship = GAME_LEVELS[Game.CURRENT_LEVEL]["main_character"]

    if key[pygame.K_w] or key[pygame.K_UP]:
        spaceship.move_up()
    if key[pygame.K_s] or key[pygame.K_DOWN]:
        spaceship.move_down()
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        spaceship.move_left()
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        spaceship.move_right()

    match Game.CURRENT_LEVEL:
        case 3 | 5 | 7 | 9 | 11 | 13:
            if key[pygame.K_SPACE]:
                spaceship.shoot_laser_beam()

    paused_keys(key)


def even_levels_keys(key):
    hero_kid = GAME_LEVELS[Game.CURRENT_LEVEL]["main_character"]

    if key[pygame.K_a] or key[pygame.K_LEFT]:
        hero_kid.move_left()
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        hero_kid.move_right()
    if key[pygame.K_UP] or key[pygame.K_SPACE]:
        hero_kid.jump()

    paused_keys(key)


def press_space_to_start_game(key):
    if key[pygame.K_SPACE]:
        Game.STATE = GameState.LEVEL_COMPLETE

def presenting_story_keys(key):
    if key[pygame.K_RETURN]:
        Game.STATE = GameState.RUNNING

def paused_keys(key):
    if Game.STATE != GameState.PAUSED:
        if key[pygame.K_p]:
            Game.STATE = GameState.PAUSED

    if key[pygame.K_SPACE]:
        Game.GAME_WAS_PAUSED = False

        if Game.SOUND_EFFECT_IS_PLAYING:
            Game.play_sound_effect('sounds/unpause.mp3')
            Game.SOUND_EFFECT_IS_PLAYING = False

        # unpause background music
        pygame.mixer.music.unpause()

        Game.STATE = GameState.RUNNING
    elif key[pygame.K_q]:
        pygame.quit()


def game_over_keys(key):
    if key[pygame.K_r]:

        Game.SOUND_EFFECT_IS_PLAYING = False

        Game.LIFE_BAR.reset_lives()
        Game.DR_LIME_LIFE_BAR.reset_dr_lime_lives()
        Game.STAR.reset_position()

        current_level = GAME_LEVELS[Game.CURRENT_LEVEL]

        # either a space travelling level or a ground planet level
        if "obstacles" in current_level:
            for obstacle in current_level["obstacles"]:
                obstacle.reset_skin_and_position()
                obstacle.rounds_counter = 0

        # a space travelling level
        if "point_booster_collectable_objects" in current_level:
            for pbo in current_level["point_booster_collectable_objects"]:
                pbo.reset_position()

        if "alien_dr_lime" in current_level:
            dr_lime = current_level["alien_dr_lime"]
            dr_lime.clear_marbles_list()
            dr_lime.reset_position()
            dr_lime.show()

        # A ground planet level
        if "diamond" in current_level:
            hero_kid = current_level["main_character"]
            hero_kid.set_position(
                x=130,
                y=current_level["ground_y"] - hero_kid.get_skin().get_height()
            )
        else:
        # a space travelling level
            spaceship = current_level["main_character"]
            spaceship.set_position(x=30, y=Window.HEIGHT/2 )

        Obstacles.reset_rounds_counter()

        Game.GAME_POINTS = Game.START_LEVEL_POINTS

        Game.STATE = GameState.RUNNING

    elif key[pygame.K_q]:
        pygame.quit()

