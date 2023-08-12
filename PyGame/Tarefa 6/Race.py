from configs import *

class Race():
	STARTING_TIME = None
	FINISH_LINE_HAS_BEEN_CROSSED = False
	PHOTOGRAPHER_LINE_HAS_BEEN_CROSSED = False

	@classmethod
	def start(cls):
		cls.STARTING_TIME = time.time()

	@classmethod
	def draw_time_zero_onto_the_board(cls):
		write_text_with_font_roboto(
		    text="00:00",
		    font_size=25,
		    text_color="black",
		    coords=(1255, 382)
		)

	@classmethod
	def draw_elapsed_time_onto_the_board(cls):
		elapsed_seconds, elapsed_hundreds_of_a_second = str(time.time() - cls.STARTING_TIME).split(".")
		elapsed_time = f"{elapsed_seconds.zfill(2)}:{elapsed_hundreds_of_a_second[:2]}"
		# print(elapsed_time)

		write_text_with_font_roboto(
			text=elapsed_time,
			font_size=25,
			text_color="black",
			coords=(1255, 382)
		)

	@classmethod
	def finish_line_was_crossed(cls):
		cls.FINISH_LINE_HAS_BEEN_CROSSED = True

	@classmethod
	def photographer_line_was_crossed(cls):
		cls.PHOTOGRAPHER_LINE_HAS_BEEN_CROSSED = True
