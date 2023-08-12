from configs import *


class Plane:
    def __init__(self, x, y, img_path):
        self.__x = x
        self.__y = y
        self.__img = pygame.image.load(img_path)
        self.__alpha = 100

    def get_img(self):
        return self.__img

    def get_coordinates(self):
        return [self.__x, self.__y]

    def move(self):
        self.__x -= random.randint(1,4)
        self.__y -= random.random()

    def draw(self, surface, coords=None):
    	self.__img.set_alpha(self.__alpha)
    	self.__alpha += 5 if self.__alpha < 255 else 0
    	if coords:
    		surface.blit(self.__img, coords)
    	else:
    		surface.blit(self.__img, self.get_coordinates())

    def fly(self, surface):
        self.move()
        self.draw(surface)
