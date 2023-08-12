from Elements import Elements
import configs
import random

class PointBoosterCollectable(Elements):
	def __init__(self, offset):
		skin = configs.Skins.POINT_BOOSTER_COLLECTABLE
		x=configs.Window.WIDTH + offset
		y=random.randint(5, configs.Window.HEIGHT - skin.get_height())

		super().__init__(x, y, skin)


	def move_left(self):
		if self.less_than_number_of_rounds_to_play():
			self._x -= random.randint(4, 7)
			if self._x < -self._skin.get_width():
				self.reset_position()

		elif configs.Obstacles.ROUNDS_COUNTER == configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]['number_of_rounds']:
			if -self._skin.get_width() < self._x < configs.Window.WIDTH:
				self._x -= 5
			else:
				self.reset_position()


	def less_than_number_of_rounds_to_play(self):
		current_level = configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]
		NUMBER_OF_ROUNDS = current_level["number_of_rounds"]
		return configs.Obstacles.ROUNDS_COUNTER < NUMBER_OF_ROUNDS


	def reset_position(self):
		self.set_position(
			x=configs.Window.WIDTH + random.randint(5, 700),
			y=random.randint(5, configs.Window.HEIGHT - self._skin.get_height())
		)

	def add_boost_points(self):
		configs.Game.GAME_POINTS += configs.Game.Points.POINT_BOOSTER_COLLECTABLE
		self.reset_position()
		configs.Game.Points.Counter.POINT_BOOSTER_COLLECTABLE += 1

		print(
			f"CURRENT_LEVEL: {configs.Game.CURRENT_LEVEL}\n"
			f"GAME_POINTS: {configs.Game.GAME_POINTS}\n"
			f"PLANET_EARTH_COLLISION_ASTEROIDS({configs.Game.Points.PLANET_EARTH_COLLISION_ASTEROIDS}): {configs.Game.Points.Counter.PLANET_EARTH_COLLISION_ASTEROIDS}\n"
			f"HUMAN_SPACE_JUNK({configs.Game.Points.HUMAN_SPACE_JUNK}): {configs.Game.Points.Counter.HUMAN_SPACE_JUNK}\n"
			f"ALIEN_SPACESHIPS({configs.Game.Points.ALIEN_SPACESHIPS}): {configs.Game.Points.Counter.ALIEN_SPACESHIPS}\n"
			f"ALIEN_MARBLES({configs.Game.Points.ALIEN_MARBLES}): {configs.Game.Points.Counter.ALIEN_MARBLES}\n"
			f"POINT_BOOSTER_COLLECTABLE({configs.Game.Points.POINT_BOOSTER_COLLECTABLE}): {configs.Game.Points.Counter.POINT_BOOSTER_COLLECTABLE}\n"
			"----------------------------------------\n"
		)

