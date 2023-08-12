from Elements import Elements
import configs
import random

class AlienDrLime(Elements):

	def __init__(self, x, y, skin, gray_skin):
		super().__init__(x, y, skin, gray_skin)
		self.did_show = False
		self.is_dead = False
		self.STOPPING_Y_VALUES = [
			configs.Window.HEIGHT/12,
			configs.Window.HEIGHT/4,
			configs.Window.HEIGHT/3,
			configs.Window.HEIGHT/2,
			configs.Window.HEIGHT/1.3,
		]
		self.current_stopping_y_value = y
		self.did_it_pick_a_current_stopping_y_value = False
		self.has_shooted_marble = False
		self.marbles = list()
		self.total_shoot_frames = 0
		self.was_hit = False
		self.has_removed_a_life = False
		self.frame_count_hitting = 0


	def pick_a_stopping_y_value(self):
		temp_y = random.choice(self.STOPPING_Y_VALUES)
		if self.current_stopping_y_value == temp_y:
			self.pick_a_stopping_y_value()
		else:
			self.current_stopping_y_value = temp_y
			self.did_it_pick_a_current_stopping_y_value = True

	def shoot_marble(self):
		self.total_shoot_frames += 1

		if self.total_shoot_frames >= 60:
			marble_x_shoot_origin = self._x + 50
			marble_y_shoot_origin = self._y + 130
			marble = AlienMarble(
						x=marble_x_shoot_origin,
						y=marble_y_shoot_origin,
						skin=random.choice(configs.Skins.OBSTACLES["ALIEN_MARBLES"]),
						hero_spaceship_position=configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]["main_character"].get_position()
					 )
			self.marbles.append(marble)

			self.total_shoot_frames = 0

	def move_vertically_in_a_random_fashion_and_shoot_marbles(self):

		if configs.Game.DR_LIME_LIFE_BAR.skin_index == 10:
			configs.Game.draw_dr_lime_speach()
			return None

		if not self.did_it_pick_a_current_stopping_y_value:
			self.pick_a_stopping_y_value()

		if self._y < self.current_stopping_y_value:
			# moving down
			self._y += random.randint(7, 12)
			if self._y >= self.current_stopping_y_value:
				self._y = self.current_stopping_y_value
		elif self._y > self.current_stopping_y_value:
			# moving up
			self._y -= random.randint(7, 12)
			if self._y <= self.current_stopping_y_value:
				self._y = self.current_stopping_y_value

		self.draw_shooted_marbles()

		self.frame_count_hitting += 1
		if self.has_removed_a_life and self.frame_count_hitting == 5:
			self.has_removed_a_life = False
			self.set_skin_colored()

	def draw_shooted_marbles(self):
		if not self.has_shooted_marble:
			self.shoot_marble()
			self.has_shooted_marble = True

		for marble in self.marbles:
			marble.draw_and_move_marbles()

			if marble.collides_with(configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]["main_character"]):
				configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]["main_character"].has_been_hit()

			if marble.get_x() < -marble.get_skin().get_width():
				self.marbles.remove(marble)
				self.did_it_pick_a_current_stopping_y_value = False

		self.has_shooted_marble = False

	def has_been_hit(self):
		self.was_hit = True
		self.set_skin_gray()
		self.remove_life()
		self.frame_count_hitting = 0

	def remove_life(self):
		if self.was_hit and not self.has_removed_a_life:
			configs.Game.DR_LIME_LIFE_BAR.remove_dr_lime_life()
			self.set_skin_colored()
			self.was_hit = False
			self.has_removed_a_life = True

	def is_dead(self):
		return self.is_dead

	def dies(self):
		self.is_dead = True

	def show(self):
		self.did_show = True
		if configs.Game.DR_LIME_LIFE_BAR.skin_index == 10:
			self.is_dead = True
			return None

		if self._x > configs.Window.WIDTH - 200:
			self._x -= 2
		else:
			self._x = configs.Window.WIDTH - 200

		self.draw()

	def reset_position(self):
		self.set_position(
			x=configs.Window.WIDTH + 5,
			y=configs.Window.HEIGHT/2
		)

	def clear_marbles_list(self):
		self.marbles.clear()


class AlienMarble(Elements):
	def __init__(self, x, y, skin, hero_spaceship_position):
		super().__init__(x, y, skin)
		self.initial_x = x
		self.initial_y = y
		self.hero_spaceship_position = hero_spaceship_position

	def get_x(self):
		return self._x

	def calculate_y_value_for_the_line_trajectory_marbles(self):
		m = self.calculate_slope_of_line_trajectory_for_marbles()
		# point-slope formula, solving for y:
		y = m*(self._x - self.initial_x) + self.initial_y
		return y

	def calculate_slope_of_line_trajectory_for_marbles(self):
		hero_spaceship_x, hero_spaceship_y = self.hero_spaceship_position
		# compensante to get closer to the center of the spaceship
		hero_spaceship_x += 20
		hero_spaceship_y += 30
		return (self.initial_y - hero_spaceship_y) / (self.initial_x - hero_spaceship_x)

	def draw_and_move_marbles(self):
		self._x -= 6
		self.set_position(
			x=self._x,
			y=self.calculate_y_value_for_the_line_trajectory_marbles()
		)
		self.draw()

