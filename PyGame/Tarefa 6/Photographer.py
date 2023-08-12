from configs import *
from Race import Race

class Photographer:
    def __init__(self, x, y, img_path):
        self.__img_looking_left = pygame.image.load(img_path)
        self.__img = self.__img_looking_left
        self.__img_looking_right = pygame.transform.flip(self.__img, True, False)
        self.__x = x
        self.__y = y
        self.__took_a_picture = False

        # draw the photographer to show it during the countdown sound effect
        self.draw(surface=screen)

    def get_coordinates(self):
        return [self.__x, self.__y]

    def draw(self, surface, coords=None):
        if coords:
            surface.blit(self.__img, coords)
        else:
            surface.blit(self.__img, self.get_coordinates())

    def move(self, surface):
    	if Race().PHOTOGRAPHER_LINE_HAS_BEEN_CROSSED:
    		self.__img = self.__img_looking_right
    		self.__x += random.randint(1, 2)
    	else:
            self.__img = self.__img_looking_left
            self.__x -= random.random()
    	self.draw(surface)

    def take_a_picture_of_the_winner(self, surface):
    	if not self.__took_a_picture:
    		self.move(surface)
    		self.draw(surface)
    		if Race().FINISH_LINE_HAS_BEEN_CROSSED and not self.__took_a_picture:
    			play_sound_effect("sounds/photo-shutter.mp3", second_channel=True)
    			self.__took_a_picture = True
    	else:
    		self.draw(surface)
