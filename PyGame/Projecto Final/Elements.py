import pygame
import configs

class Elements:
    def __init__(self, x, y, skin, gray_skin=None):
        self._x = x
        self._y = y
        self._skin = skin
        self._gray_skin = gray_skin
        self.skin_is_gray = False

    def draw(self, at_coords=None):
        if self.skin_is_gray:
            if at_coords:
                configs.screen.blit(self._gray_skin, at_coords)
            else:
                configs.screen.blit(self._gray_skin, [self._x, self._y])
        else:
            if at_coords:
                configs.screen.blit(self._skin, at_coords)
            else:
                configs.screen.blit(self._skin, [self._x, self._y])

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self._skin)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self._x - offset_x, self._y - offset_y])

    def collides_with(self, who):
        return who.get_overlaping_area(self._skin, self._x, self._y) > 0

    def get_skin(self):
        return self._skin

    def get_position(self):
        return (self._x, self._y)

    def set_position(self, x, y):
        self._x = x
        self._y = y

    def set_skin_gray(self):
        self.skin_is_gray = True

    def set_skin_colored(self):
        self.skin_is_gray = False
