from configs import *

class Ranking():
    positions = dict()
    has_been_shown = False

    @classmethod
    def rank(cls, player_race_number, player_race_time):
        # save 2 decimal places but wihtout rounding them
        cls.positions[f"Player {player_race_number}"] = str(player_race_time)[:5]

    @classmethod
    def show_rank(cls, players):
        # print("Ranking:", cls.positions)
        World.draw_ranking_board()
        play_sound_effect("sounds/ranking.mp3")

        # 1st Place -------------------------------------------------------------
        player_1st_place = players[list(cls.positions.keys())[0]]
        player_1st_place_time = cls.positions[list(cls.positions.keys())[0]]
        player_1st_place.scale_img(factor=3)
        player_1st_place.draw(surface=screen, coords=[650, 280])
        player_1st_place.scale_img(factor=1/3)

        write_text_with_font_roboto(
            text=f"time: {player_1st_place_time}",
            text_color="yellow",
            coords=(630, 645)
        )

        # 2nd Place -------------------------------------------------------------
        player_2nd_place = players[list(cls.positions.keys())[1]]
        player_2n_place_time = cls.positions[list(cls.positions.keys())[1]]
        player_2nd_place.scale_img(factor=2)
        player_2nd_place.draw(surface=screen, coords=[395, 340])
        player_2nd_place.scale_img(factor=1/2)


        write_text_with_font_roboto(
            text=f"time: {player_2n_place_time}",
            text_color="yellow",
            coords=(360, 600)
        )

        # 3rd Place -------------------------------------------------------------
        player_3rd_place = players[list(cls.positions.keys())[2]]
        player_3rd_place_time = cls.positions[list(cls.positions.keys())[2]]
        player_3rd_place.scale_img(factor=2)
        player_3rd_place.draw(surface=screen, coords=[910, 340])
        player_3rd_place.scale_img(factor=1/2)

        write_text_with_font_roboto(
            text=f"time: {player_3rd_place_time}",
            text_color="yellow",
            coords=(895, 600)
        )

        ###################################################################
        # Ensure the time on the board is the same of the last player
        ###################################################################
        World.draw_time_counter_board()
        write_text_with_font_roboto(
            text=player_3rd_place_time.replace(".", ":"),
            font_size=25,
            text_color="black",
            coords=(1255, 382)
        )


        cls.has_been_shown = True
