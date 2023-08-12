from Elements import Elements
import configs
import random
import pygame

class Obstacles(Elements):
	COUNTER_OF_OBSTACLES_CROSSING_THE_Y_AXIS = 0
	ROUNDS_COUNTER = 0

	def __init__(self, x, y, skin):
		super().__init__(x, y, skin)

	def reset_rounds_counter():
		Obstacles.ROUNDS_COUNTER = 0
		Obstacles.COUNTER_OF_OBSTACLES_CROSSING_THE_Y_AXIS = 0

	def draw_rounds():
		if configs.Game.CURRENT_LEVEL < 13:
			configs.Game.write_text_with_font_valorax(
				text=f"ROUNDS: {Obstacles.ROUNDS_COUNTER} of {configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]['number_of_rounds']}",
				coords=(configs.Window.WIDTH/2 - 150, 15)
			)


class AlienMonster(Obstacles):
	def __init__(self, ground_y, offset, skin_lower_limit=None, skin_upper_limit=None):

		self.available_skins = configs.Skins.OBSTACLES["ALIEN_MONSTERS"][skin_lower_limit:skin_upper_limit]

		skin = random.choice(self.available_skins)
		x = configs.Window.WIDTH + offset
		y = ground_y - skin.get_height()

		super().__init__(x, y, skin)

		self.offset = offset
		self.rounds_counter = 0
		self.ground = ground_y

	def move_left(self):
		if self.less_than_number_of_rounds_to_play():
			self._x -= 5
			if self._x < -self._skin.get_width():
				self.rounds_counter += 1
				Obstacles.COUNTER_OF_OBSTACLES_CROSSING_THE_Y_AXIS += 1
				self.reset_skin_and_position()

		elif Obstacles.ROUNDS_COUNTER == configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]['number_of_rounds']:
			diamond = configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]["diamond"]
			diamond.move_left()
			diamond.draw()

			self.reset_skin_and_position()

		if Obstacles.COUNTER_OF_OBSTACLES_CROSSING_THE_Y_AXIS == len(configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]['obstacles']):
			Obstacles.COUNTER_OF_OBSTACLES_CROSSING_THE_Y_AXIS = 0
			Obstacles.ROUNDS_COUNTER += 1

		Obstacles.draw_rounds()

	def reset_skin_and_position(self):
		self._skin = random.choice(self.available_skins)
		self.set_position(
			x=configs.Window.WIDTH + self._skin.get_width() + random.randint(self._skin.get_width() * 2, self._skin.get_height() * 6),
			y=self.ground - self._skin.get_height()
		)

	def less_than_number_of_rounds_to_play(self):
		current_level = configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]
		NUMBER_OF_ROUNDS = current_level["number_of_rounds"]
		return self.rounds_counter < NUMBER_OF_ROUNDS


class Asteroid(Obstacles):
	def __init__(self, offset):
		skin=random.choice(configs.Skins.OBSTACLES["ASTEROIDS"])
		x=configs.Window.WIDTH + offset
		y=random.randint(5, configs.Window.HEIGHT - skin.get_height())
		super().__init__(x, y, skin)
		self.rounds_counter = 0

	def move_left(self):
		if self.less_than_number_of_rounds_to_play():
			self._x -= random.randint(5, 7)
			if self._x < -self._skin.get_width():
				self.rounds_counter += 1
				Obstacles.COUNTER_OF_OBSTACLES_CROSSING_THE_Y_AXIS += 1
				self.reset_skin_and_position()

		elif Obstacles.ROUNDS_COUNTER == configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]['number_of_rounds']:
			if 0 < configs.Game.CURRENT_LEVEL < 13:
				planet = configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]["planet"]
				planet.show()
			elif configs.Game.CURRENT_LEVEL == 13:
				if configs.Game.DR_LIME_LIFE_BAR.skin_index < 10:
					configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]['alien_dr_lime'].show()
				else:
					configs.Game.draw_dr_lime_speach()
					planet = configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]["planet"]
					planet.show()

			self.reset_skin_and_position()

		# outra forma:
		# if Obstacles.COUNTER_OF_OBSTACLES_CROSSING_THE_Y_AXIS == sum(1 for asteroid in configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]['obstacles'] if asteroid.__class__.__name__ == "Asteroid"):
		if Obstacles.COUNTER_OF_OBSTACLES_CROSSING_THE_Y_AXIS == sum(isinstance(asteroid, Asteroid) and not isinstance(asteroid, PlanetEarthCollisionAsteroid) for asteroid in configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]['obstacles']):
			Obstacles.COUNTER_OF_OBSTACLES_CROSSING_THE_Y_AXIS = 0
			Obstacles.ROUNDS_COUNTER += 1

		Obstacles.draw_rounds()

	def less_than_number_of_rounds_to_play(self):
		current_level = configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]
		NUMBER_OF_ROUNDS = current_level["number_of_rounds"]
		return self.rounds_counter < NUMBER_OF_ROUNDS

	def reset_skin_and_position(self):
		self._skin = random.choice(configs.Skins.OBSTACLES["ASTEROIDS"])
		self.set_position(
			x=configs.Window.WIDTH + random.randint(5, 700),
			y=random.randint(5, configs.Window.HEIGHT - self._skin.get_height())
		)


class PlanetEarthCollisionAsteroid(Asteroid):
	def __init__(self, offset):
		super().__init__(offset)
		self._skin = random.choice(configs.Skins.OBSTACLES["PLANET_EARTH_COLLISION_ASTEROIDS"])

	def move_left(self):
		if self.less_than_number_of_rounds_to_play():
			self._x -= random.randint(4, 6)
			if self._x < -self._skin.get_width():
				self.reset_skin_and_position()

		elif Obstacles.ROUNDS_COUNTER == configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]['number_of_rounds']:
			if -self._skin.get_width() < self._x < configs.Window.WIDTH:
				self._x -= 5
			else:
				self.reset_skin_and_position()

	def reset_skin_and_position(self):
		self._skin = random.choice(configs.Skins.OBSTACLES["PLANET_EARTH_COLLISION_ASTEROIDS"])
		self.set_position(
			x=configs.Window.WIDTH + random.randint(5, 700),
			y=random.randint(5, configs.Window.HEIGHT - self._skin.get_height())
		)

	def less_than_number_of_rounds_to_play(self):
		current_level = configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]
		NUMBER_OF_ROUNDS = current_level["number_of_rounds"]
		return Obstacles.ROUNDS_COUNTER < NUMBER_OF_ROUNDS


class HumanJunk(Elements):
	def __init__(self, offset):
		skin=random.choice(configs.Skins.OBSTACLES["HUMAN_SPACE_JUNK"])
		x=configs.Window.WIDTH + offset
		y=random.randint(80, configs.Window.HEIGHT - skin.get_height())

		super().__init__(x, y, skin)

	def move_left(self):
		if self.less_than_number_of_rounds_to_play():
			self._x -= random.randint(4, 7)
			if self._x < -self._skin.get_width():
				self.reset_skin_and_position()

		elif Obstacles.ROUNDS_COUNTER == configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]['number_of_rounds']:
			if -self._skin.get_width() < self._x < configs.Window.WIDTH:
				self._x -= 5
			else:
				self.reset_skin_and_position()

	def reset_skin_and_position(self):
		self._skin = random.choice(configs.Skins.OBSTACLES["HUMAN_SPACE_JUNK"])
		self.set_position(
			x=configs.Window.WIDTH + random.randint(5, 700),
			y=random.randint(80, configs.Window.HEIGHT - self._skin.get_height())
		)

	def less_than_number_of_rounds_to_play(self):
		current_level = configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]
		NUMBER_OF_ROUNDS = current_level["number_of_rounds"]
		return Obstacles.ROUNDS_COUNTER < NUMBER_OF_ROUNDS


class AlienSpaceship(HumanJunk):
	def __init__(self, offset):
		super().__init__(offset)
		self._skin = random.choice(configs.Skins.OBSTACLES["ALIEN_SPACESHIPS"])

	def reset_skin_and_position(self):
		self._skin = random.choice(configs.Skins.OBSTACLES["ALIEN_SPACESHIPS"])
		self.set_position(
			x=configs.Window.WIDTH + random.randint(5, 700),
			y=random.randint(80, configs.Window.HEIGHT - self._skin.get_height())
		)
