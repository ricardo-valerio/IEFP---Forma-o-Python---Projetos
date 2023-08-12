import pygame

class Elements:
    def __init__(self, x, y, img):
        self._x = x
        self._y = y
        self._img = img

    def get_bounds(self):
        return pygame.Rect(self._x, self._y, self._img.get_width(),  self._img.get_height())

    def collides_with(self, who):
        return self.get_bounds().colliderect(who.get_bounds())
