from Elements import Elements
import configs

class Planet(Elements):
	def __init__(self, skin_index):
		skin = configs.Skins.PLANETS[skin_index]
		x = configs.Window.WIDTH + 5
		y = configs.Window.HEIGHT / 4
		super().__init__(x, y, skin)


	def show(self):
		if self._x > configs.Window.WIDTH - self.get_skin().get_width() * 1.3:
			self._x -= 1

		self.draw()
