from configs import *

class Flag_Girl:
    def __init__(self, x, y, img_path):
        self.__x = x
        self.__y = y
        self.__img = pygame.image.load(img_path)

        # draw the flag girl to show it during the countdown sound effect
        self.draw(surface=screen)

    def set_coordinates(self, x, y):
        self.__x, self.__y = x, y

    def draw(self, surface, coords=None):
        if coords:
            surface.blit(self.__img, coords)
        else:
            surface.blit(self.__img, [self.__x, self.__y])

    def ready_set_go(self, surface):
    	self.__img = pygame.image.load("imgs/girl-flags-down.png")
    	self.set_coordinates(x=130, y=410)
    	self.draw(surface)
    	pygame.display.update()


