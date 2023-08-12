from Elements import Elements
import configs
import random

class Star(Elements):
	def __init__(self, x, y, skin):
		super().__init__(x, y, skin)
		self.y_is_set = False

	def set_y_according_to_current_level(self):
		match configs.Game.CURRENT_LEVEL:
		    case 1 | 3 | 5 | 7 | 9 | 11 | 13:
		    	self._y = random.randint(5, configs.Window.HEIGHT - self._skin.get_height())
		    	self.y_is_set = True

		    case 2 | 4 | 6 | 8 | 10 | 12:
		    	self._y = configs.Window.HEIGHT/3
		    	self.y_is_set = True

	def move_left(self):
		if self._x > -self._skin.get_width():
			self._x -= 3
		else:
			self.reset_position()

	def reset_position(self):
		self.y_is_set = False
		self.set_position(
			x=1405,
			y=785
		)


