from Elements import Elements
import configs

class LifeBar(Elements):
	def __init__(self, x, y, skin, number_of_lives, skin_index=0):
		super().__init__(x, y, skin)
		self.skin_index = skin_index
		self.initial_number_of_lives = number_of_lives
		self.number_of_lives = number_of_lives


	def remove_life(self):
		self.number_of_lives -= 1
		self.skin_index += 1

		if self.skin_index < len(configs.Skins.LIFE_BAR):
			self._skin = configs.Skins.LIFE_BAR[self.skin_index]
		else:
			configs.Game.STATE = configs.GameState.OVER

	def remove_dr_lime_life(self):
		self.number_of_lives -= 1
		self.skin_index += 1

		if self.skin_index < len(configs.Skins.DR_LIME_LIFE_BAR):
			self._skin = configs.Skins.DR_LIME_LIFE_BAR[self.skin_index]

	def reset_lives(self):
		self.number_of_lives = self.initial_number_of_lives
		self.skin_index = 0
		self._skin = configs.Skins.LIFE_BAR[self.skin_index]

	def reset_dr_lime_lives(self):
		self.number_of_lives = self.initial_number_of_lives
		self.skin_index = 0
		self._skin = configs.Skins.DR_LIME_LIFE_BAR[self.skin_index]

	def get_current_number_of_lives(self):
		return self.number_of_lives
