from Elements import Elements
import configs

class LaserBeam(Elements):
	def __init__(self, x, y, skin):
		super().__init__(x, y, skin)

	def move_right(self):
		self._x += 10
		self.draw()

	def is_out_of_window(self):
		return self._x > configs.Window.WIDTH
