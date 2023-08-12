from configs import *
from KeyboardKeysManager import *
import pygame_gui
import sys
import sqlite3


MANAGER = pygame_gui.UIManager((Window.WIDTH, Window.HEIGHT))

TEXT_INPUT = pygame_gui.elements.UITextEntryLine(
                relative_rect=pygame.Rect((835, 385), (400, 50)),
                manager=MANAGER,
                object_id="#insert_name_for_score_board"
             )

def insert_user_and_score_into_database_then_show_scoreboard(user_name):

    if user_name.strip() == "" or user_name == None:
        Game.STATE = GameState.THE_END
        main_game_loop()

    did_insert_into_db = False
    did_select_into_db = False

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                cursor.close()
                connection.close()


        connection = sqlite3.connect('score_board.db')
        cursor = connection.cursor()

        if not did_insert_into_db:
            insert_query = 'INSERT INTO score_board (name, points, datetime) VALUES (?, ?, datetime("now"))'
            cursor.execute(insert_query, (user_name, Game.GAME_POINTS))
            connection.commit()
            did_insert_into_db = True

        if not did_select_into_db:
            Game.draw_score_board_background_with_table()
            select_query = 'SELECT * FROM score_board ORDER BY points DESC, datetime DESC LIMIT 10'
            cursor.execute(select_query)

            rows = cursor.fetchall()
            max_name_length = max(len(row[0]) for row in rows)
            max_points_length = max(len(str(row[1])) for row in rows)

            for i, row in enumerate(rows, start=1):
                print(f"{i:>2}º - {row[0]:>{max_name_length}} | {row[1]:>{max_points_length}} | {row[2]}")

                # Name column
                new_text = pygame.font.SysFont("bahnschrift", 25).render(f"{row[0]:<{max_name_length}}", True, "black")
                screen.blit(new_text, (420, 142 + 50 * i))

                # Points column
                new_text = pygame.font.SysFont("bahnschrift", 25).render(f"{row[1]:<{max_points_length}}", True, "black")
                screen.blit(new_text, (700, 142 + 50 * i))

                # Datetime column
                new_text = pygame.font.SysFont("bahnschrift", 25).render(f"{row[2]}", True, "black")
                screen.blit(new_text, (940, 142 + 50 * i))

            did_select_into_db = True

        pygame.display.update()
        pygame.time.wait(8000)

        Game.STATE = GameState.THE_END
        main_game_loop()


def main_game_loop():
    did_select_into_db = False

    running = True
    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if Game.CURRENT_LEVEL == 14:

                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == '#insert_name_for_score_board'):
                    if len(event.text) > 16:
                        insert_user_and_score_into_database_then_show_scoreboard(f"{event.text[0:16]}.")
                    else:
                        insert_user_and_score_into_database_then_show_scoreboard(event.text)

                MANAGER.process_events(event)


        key = pygame.key.get_pressed()

        current_level = GAME_LEVELS[Game.CURRENT_LEVEL]

        match Game.STATE:

            case GameState.FIRST_TIME_RUNNING:

                if Game.CURRENT_LEVEL == 0:
                    Game.draw_background()
                    press_space_to_start_game(key)
                elif Game.CURRENT_LEVEL == 14:
                        Game.STATE = GameState.YOU_WIN
                else:
                    Game.STATE = GameState.RUNNING

            case GameState.PRESENTING_STORY:
                Game.draw_presenting_story_image()
                presenting_story_keys(key)

            case GameState.PAUSED:
                pygame.mixer.music.pause()
                Game.draw_paused_game_image()

                if not Game.SOUND_EFFECT_IS_PLAYING:
                    Game.play_sound_effect('sounds/pause.mp3')
                    Game.SOUND_EFFECT_IS_PLAYING = True
                else:
                    paused_keys(key)

            case GameState.OVER:
                if Game.BACKGROUND_SOUND_IS_PLAYING:
                    pygame.mixer.music.stop()
                    Game.BACKGROUND_SOUND_IS_PLAYING = False
                    Game.play_sound_effect("sounds/game-over.mp3")

                Game.draw_gameover_image()
                game_over_keys(key)

            case GameState.YOU_WIN:

                connection = sqlite3.connect('score_board.db')
                cursor = connection.cursor()
                select_query = 'SELECT points FROM score_board ORDER BY points DESC LIMIT 1 OFFSET 9'
                cursor.execute(select_query)
                result = cursor.fetchone()
                tenth_highest_score = result[0] if result else None
                cursor.close()
                connection.close()

                if tenth_highest_score == None or (Game.GAME_POINTS >= tenth_highest_score):
                    Game.draw_you_made_it_to_the_top_10()
                    MANAGER.update(dt/1000)
                    MANAGER.draw_ui(screen)
                else:
                    Game.draw_you_didnt_make_it_to_the_top_10()
                    pygame.display.update()
                    pygame.time.wait(7000)

                    # show scoreboard
                    if not did_select_into_db:
                        connection = sqlite3.connect('score_board.db')
                        cursor = connection.cursor()
                        Game.draw_score_board_background_with_table()
                        select_query = 'SELECT * FROM score_board ORDER BY points DESC, datetime DESC LIMIT 10'
                        cursor.execute(select_query)

                        rows = cursor.fetchall()
                        max_name_length = max(len(row[0]) for row in rows)
                        max_points_length = max(len(str(row[1])) for row in rows)

                        for i, row in enumerate(rows, start=1):
                            print(f"{i:>2}º - {row[0]:>{max_name_length}} | {row[1]:>{max_points_length}} | {row[2]}")

                            # Name column
                            new_text = pygame.font.SysFont("bahnschrift", 25).render(f"{row[0]:<{max_name_length}}", True, "black")
                            screen.blit(new_text, (420, 142 + 50 * i))

                            # Points column
                            new_text = pygame.font.SysFont("bahnschrift", 25).render(f"{row[1]:<{max_points_length}}", True, "black")
                            screen.blit(new_text, (700, 142 + 50 * i))

                            # Datetime column
                            new_text = pygame.font.SysFont("bahnschrift", 25).render(f"{row[2]}", True, "black")
                            screen.blit(new_text, (940, 142 + 50 * i))

                        did_select_into_db = True

                    pygame.display.update()
                    pygame.time.wait(7000)

                    Game.STATE = GameState.THE_END

            case GameState.THE_END:
                Game.draw_the_end_image()

            case GameState.RUNNING:
                # Keys Management -----------------------
                match Game.CURRENT_LEVEL:
                    case 1 | 3 | 5 | 7 | 9 | 11 | 13:
                        odd_levels_keys(key)
                    case 2 | 4 | 6 | 8 | 10 | 12:
                        even_levels_keys(key)
                # -----------------------------------------

                if "level_sound" in current_level:
                    if not Game.BACKGROUND_SOUND_IS_PLAYING:
                        Game.play_level_background_sound()
                        Game.BACKGROUND_SOUND_IS_PLAYING = True

                Game.draw_background()
                Game.draw_life_bar()
                if "alien_dr_lime" in current_level and Obstacles.ROUNDS_COUNTER == current_level["number_of_rounds"]:
                    Game.draw_dr_lime_life_bar()
                Game.draw_level_X_of_6()
                Game.draw_game_points()

                current_level["main_character"].draw()

                if isinstance(current_level["main_character"], HeroKid):
                    current_level["main_character"].update_jump()

                if "obstacles" in current_level:
                    for obstacle in current_level["obstacles"]:
                        obstacle.draw()
                        obstacle.move_left()

                        if obstacle.collides_with(current_level["main_character"]):
                            current_level["main_character"].has_been_hit()

                        if isinstance(obstacle, PlanetEarthCollisionAsteroid):
                            current_level["main_character"].draw_and_move_laser_beams_if_shooted(against_who=obstacle)
                        elif isinstance(obstacle, HumanJunk):
                            current_level["main_character"].draw_and_move_laser_beams_if_shooted(against_who=obstacle)


                if "point_booster_collectable_objects" in current_level:
                    for pbo in current_level["point_booster_collectable_objects"]:
                        pbo.draw()
                        pbo.move_left()

                        if pbo.collides_with(current_level["main_character"]):
                            Game.play_sound_effect('sounds/collect-point-boost.mp3')
                            pbo.add_boost_points()


                if "alien_dr_lime" in current_level and \
                   Obstacles.ROUNDS_COUNTER == current_level['number_of_rounds']:
                    current_level["alien_dr_lime"].move_vertically_in_a_random_fashion_and_shoot_marbles()
                    current_level["main_character"].draw_and_move_laser_beams_if_shooted(against_who=current_level["alien_dr_lime"])


                if "planet" in current_level:
                    # spaceship is the main character
                    if current_level["main_character"].collides_with(current_level["planet"]) \
                    and Obstacles.ROUNDS_COUNTER == current_level["number_of_rounds"]:
                        current_level["main_character"].clear_laser_beams_list()
                        Game.play_sound_effect('sounds/collect-crystal.mp3')
                        Game.STATE = GameState.LEVEL_COMPLETE

                elif "diamond" in current_level:
                    # hero_kid is the main character
                    if current_level["main_character"].collides_with(current_level["diamond"]):
                        Game.play_sound_effect('sounds/collect-crystal.mp3')
                        Game.STATE = GameState.LEVEL_COMPLETE


                Game.draw_star_if_life_is_low()

                if current_level["main_character"].collides_with(Game.STAR):
                    Game.play_sound_effect("sounds/star-picking.mp3")
                    Game.LIFE_BAR.reset_lives()
                    Game.STAR.reset_position()

            case GameState.LEVEL_COMPLETE:

                Obstacles.reset_rounds_counter()
                Game.STAR.reset_position()

                Game.BACKGROUND_SOUND_IS_PLAYING = False
                pygame.mixer.music.stop()


                if "level_complete_image" in current_level:
                    Game.play_sound_effect('sounds/level-completed.mp3')
                    Game.draw_level_completed_image()
                    pygame.time.wait(5000)

                    # show the "YOU WIN" image
                    if Game.CURRENT_LEVEL == 12:
                        # if "you_win_image" in current_level:
                        Game.draw_you_win_image()
                        pygame.time.wait(5000)

                Game.CURRENT_LEVEL += 1

                if Game.CURRENT_LEVEL == 14: # REAL YOU_WIN_LEVEL
                    Game.STATE = GameState.YOU_WIN
                else:
                    Game.LIFE_BAR.reset_lives()
                    Game.START_LEVEL_POINTS = Game.GAME_POINTS
                    print("START_LEVEL_POINTS:", Game.START_LEVEL_POINTS)
                    Game.STATE = GameState.PRESENTING_STORY

        pygame.display.update()

    pygame.quit()
    sys.exit()


main_game_loop()
