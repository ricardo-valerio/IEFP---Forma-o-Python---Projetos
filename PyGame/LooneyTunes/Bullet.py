from configs import *

class Bullet:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__img = Skin.BULLET

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def move(self):
        self.__x -= 10

    def is_out(self):
        return self.__x < -self.__img.get_width()

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y