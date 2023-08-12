from Elements import Elements

class Characters(Elements):
    def __init__(self, x, y, img):
        super().__init__(x, y, img)

    def draw(self, surface):
        surface.blit(self._img, [self._x, self._y])