from Elements import Elements
import configs

class Diamond(Elements):
	def __init__(self, skin_index):
		skin = configs.Skins.DIAMONDS[skin_index]
		x = configs.Window.WIDTH + 5
		y = configs.Window.HEIGHT / 4
		super().__init__(x, y, skin)

	def move_left(self):
		if self._x > configs.Window.WIDTH - self.get_skin().get_width() * 2.5:
			self._x -= 1
