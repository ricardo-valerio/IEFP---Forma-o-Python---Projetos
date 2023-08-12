from Elements import Elements
import configs
from LaserBeam import LaserBeam
from Obstacles import Obstacles, HumanJunk, PlanetEarthCollisionAsteroid
from AlienDrLime import AlienDrLime
import random

class Spaceship(Elements):
	def __init__(self, x, y, skin, gray_skin):
		super().__init__(x, y, skin, gray_skin)

		self.was_hit = False
		self.has_removed_a_life = False
		self.frame_count_movement = 0
		self.frame_count_hitting = 0
		self.laser_beams = list()
		self.total_shoot_frames = 10

	def update_frame_count_and_skin_if_it_was_hit(self):
		if self.has_removed_a_life:
			self.frame_count_movement += 1
			if self.has_removed_a_life and self.frame_count_movement == 20:
				self.frame_count_movement = 0
				self.set_skin_colored()
				self.has_removed_a_life = False

	def move_up(self):
		self.update_frame_count_and_skin_if_it_was_hit()

		if self._y > 1:
			self._y -= 5
		else:
			self._y = 1

	def move_down(self):
		self.update_frame_count_and_skin_if_it_was_hit()

		if self._y < configs.Window.HEIGHT - self._skin.get_height():
			self._y += 5
		else:
			self._y = configs.Window.HEIGHT - self._skin.get_height()

	def move_left(self):
		self.update_frame_count_and_skin_if_it_was_hit()

		if self._x > 1:
			self._x -= 5
		else:
			self._x = 1

	def move_right(self):
		self.update_frame_count_and_skin_if_it_was_hit()

		if self._x < configs.Window.WIDTH - self._skin.get_width():
			self._x += 5
		else:
			self._x = configs.Window.WIDTH - self._skin.get_width()

	def has_been_hit(self):
		self.was_hit = True
		self.set_skin_gray()
		if not self.has_removed_a_life:
			configs.Game.play_sound_effect('sounds/main-character-damage.mp3')
			self.remove_life()

	def remove_life(self):
		if self.was_hit and not self.has_removed_a_life:
			configs.Game.LIFE_BAR.remove_life()
			self.set_skin_colored()
			self.was_hit = False
			self.has_removed_a_life = True

	def shoot_laser_beam(self):
		self.total_shoot_frames += 1

		delay_of_shooting = 20
		if "alien_dr_lime" in configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL] and \
			Obstacles.ROUNDS_COUNTER == configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]['number_of_rounds']:
			delay_of_shooting = 100

		if self.total_shoot_frames >= delay_of_shooting:

			laser_x_shoot_origin = self._x + self._skin.get_width()
			laser_y_shoot_origin = self._y + self._skin.get_height()/1.3

			laser_beam = LaserBeam(
				x=laser_x_shoot_origin,
				y=laser_y_shoot_origin,
				skin=random.choice(configs.Skins.LASER_BEAMS)
			)

			self.laser_beams.append(laser_beam)
			configs.Game.play_sound_effect('sounds/laser-beam-blast.mp3')
			self.total_shoot_frames = 0


	def draw_and_move_laser_beams_if_shooted(self, against_who):
		for laser_beam in self.laser_beams:
			laser_beam.move_right()

			if laser_beam.is_out_of_window():
				self.laser_beams.remove(laser_beam)


			if laser_beam.collides_with(against_who):
				if isinstance(against_who, PlanetEarthCollisionAsteroid):
					against_who.reset_skin_and_position()
					configs.Game.GAME_POINTS += configs.Game.Points.PLANET_EARTH_COLLISION_ASTEROIDS
					configs.Game.Points.Counter.PLANET_EARTH_COLLISION_ASTEROIDS += 1

					if laser_beam in self.laser_beams:
						self.laser_beams.remove(laser_beam)

				elif against_who.__class__.__name__ == "AlienSpaceship":
					against_who.reset_skin_and_position()
					configs.Game.GAME_POINTS += configs.Game.Points.ALIEN_SPACESHIPS
					configs.Game.Points.Counter.ALIEN_SPACESHIPS += 1

					if laser_beam in self.laser_beams:
						self.laser_beams.remove(laser_beam)

				elif against_who.__class__.__name__ == "AlienMarble":
					against_who.reset_skin_and_position()
					configs.Game.GAME_POINTS += configs.Game.Points.ALIEN_MARBLES
					configs.Game.Points.Counter.ALIEN_MARBLES += 1

					if laser_beam in self.laser_beams:
						self.laser_beams.remove(laser_beam)

				elif isinstance(against_who, HumanJunk):
					against_who.reset_skin_and_position()
					configs.Game.GAME_POINTS += configs.Game.Points.HUMAN_SPACE_JUNK
					configs.Game.Points.Counter.HUMAN_SPACE_JUNK += 1

					if laser_beam in self.laser_beams:
						self.laser_beams.remove(laser_beam)

				elif isinstance(against_who, AlienDrLime):
					configs.GAME_LEVELS[configs.Game.CURRENT_LEVEL]["alien_dr_lime"].has_been_hit()

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



	def clear_laser_beams_list(self):
		self.laser_beams.clear()
