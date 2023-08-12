from Elements import Elements
import configs




class HeroKid(Elements):
	def __init__(self, x, y, skin, gray_skin):
		super().__init__(x, y, skin, gray_skin)

		self.__jump_state = None
		self.__total_jump_frames = 0
		self.__initial_y = y

		self.was_hit = False
		self.has_removed_a_life = False
		self.frame_count_movement = 0
		self.frame_count_hitting = 0

	class Direction:
	    RISING = 0
	    FALLING = 1

	def update_frame_count_and_skin_if_it_was_hit(self):
		if self.has_removed_a_life:
			self.frame_count_movement += 1
			if self.frame_count_movement == 50:
				self.frame_count_movement = 0
				self.set_skin_colored()
				self.has_removed_a_life = False

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

	def jump(self):
	    if self.__jump_state != None:
	    	return
	    self.__jump_state = HeroKid.Direction.RISING
	    configs.Game.play_sound_effect('sounds/jumping.mp3')



	def update_jump(self):
		self.update_frame_count_and_skin_if_it_was_hit()
		# RISING --------------------------------
		if self.__jump_state == HeroKid.Direction.RISING:
			self._y -= 5
		# FALLING -------------------------------
		if self._y <= configs.Window.HEIGHT/4:
			self.__jump_state = HeroKid.Direction.FALLING

		if self.__jump_state == HeroKid.Direction.FALLING:
			self._y += 7
		# STOP ----------------------------------
		if self._y >= self.__initial_y:
			self.__jump_state = None
			self._y = self.__initial_y

	def has_been_hit(self):
		self.was_hit = True
		self.set_skin_gray()
		configs.Game.play_sound_effect('sounds/main-character-damage.mp3')
		self.remove_life()
		self.frame_count_hitting += 1
		if self.frame_count_hitting == 100:
			self.frame_count_hitting = 0
			self.has_removed_a_life = False
			self.set_skin_colored()

	def remove_life(self):
		if self.was_hit and not self.has_removed_a_life:
			configs.Game.LIFE_BAR.remove_life()
			self.set_skin_colored()
			self.was_hit = False
			self.has_removed_a_life = True
