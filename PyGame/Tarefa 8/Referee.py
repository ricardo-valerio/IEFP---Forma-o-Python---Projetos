from configs import *

class Referee:

	SCORE_TEAM_ON_LEFT_SIDE = 0
	SCORE_TEAM_ON_RIGHT_SIDE = 0

	whistler = pygame.mixer.Sound('sounds/referee-whistle.ogg')

	def whistle():
		Referee.whistler.play()

	def write_text_with_font_roboto(text, text_color, bg_color=None, font_size=22, coords=(30, 30)):
	    font_roboto = pygame.font.Font("fonts/Roboto-Regular.ttf", size=font_size)
	    text_to_blit = font_roboto.render(text, True, text_color, bg_color)
	    screen.blit(text_to_blit, coords)

	def draw_score():
		# SCORE_TEAM_ON_LEFT_SIDE --------------------------------------------------------------------
	    Referee.write_text_with_font_roboto(
	    	text=str(Referee.SCORE_TEAM_ON_LEFT_SIDE),
	    	text_color="white",
	    	coords=(
	    		Screen.CENTER_X_OF_SOCCER_FIELD - (27 if Referee.SCORE_TEAM_ON_LEFT_SIDE < 10 else 33)	,
	    		Screen.HORIZONTAL_TOP_SOCCER_FIELD_LIMIT - World.GOALS_SCORE_BOARD.get_height()/2 - 6
	    	)
	    )
	    # SCORE_TEAM_ON_RIGHT_SIDE -------------------------------------------------------------------
	    Referee.write_text_with_font_roboto(
	    	text=str(Referee.SCORE_TEAM_ON_RIGHT_SIDE),
	    	text_color="white",
	    	coords=(
	    		Screen.CENTER_X_OF_SOCCER_FIELD + (15 if Referee.SCORE_TEAM_ON_RIGHT_SIDE < 10 else 9),
	    		Screen.HORIZONTAL_TOP_SOCCER_FIELD_LIMIT - World.GOALS_SCORE_BOARD.get_height()/2 - 6
	    	)
	    )

