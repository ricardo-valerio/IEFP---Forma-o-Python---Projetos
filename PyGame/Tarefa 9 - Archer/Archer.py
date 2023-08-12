from configs import *
from Elements import Elements

class Archer(Elements):
    MAX_NUMBER_OF_ARROWS_ALLOWED_ON_SCREEN = 6
    NUMBER_OF_SHOOTED_ARROWS = 0

    def __init__(self, x, y, img_path):
        super().__init__(x, y, img_path)

    def move_up(self):
        if self._y >= 540 - self._img.get_height():
            self._y -= 3

    def move_down(self):
        if self._y <= 820 - self._img.get_height():
            self._y += 3

    def get_coords_to_arrow(self):
        return [self._x + 55, self._y + 95]

    def shoot(self, arrows):
        if Archer.NUMBER_OF_SHOOTED_ARROWS < Archer.MAX_NUMBER_OF_ARROWS_ALLOWED_ON_SCREEN and \
           not arrows[Archer.NUMBER_OF_SHOOTED_ARROWS].has_been_shot():

                arrows[Archer.NUMBER_OF_SHOOTED_ARROWS].shoot_from(arch_coords=self.get_coords_to_arrow())
        else:
            e_oh.play()


    def update_number_of_shooted_arrows(value):
        Archer.NUMBER_OF_SHOOTED_ARROWS = value


