from configs import *
from Elements import Elements
from Archer import Archer

class Arrow(Elements):
    def __init__(self, x, y, img_path, number):
        super().__init__(x, y, img_path)
        self.number = number
        self.__has_been_shot = False
        self.__has_shoot_balloon = False

    def move_right(self):
        if self._x > Screen.WIDTH:
            self.remove()

        if self.__has_been_shot:
            self._x += 7

        self.draw(surface=screen)

    def shoot_from(self, arch_coords):
        self.__has_been_shot = True
        x, y = arch_coords
        self.set_position(x, y)
        arrow_shoot.play()

    def has_been_shot(self):
        return self.__has_been_shot

    def has_shoot_ballon(self):
        return self.__has_shoot_balloon

    def arrow_shooted_ballon(self):
        self.__has_shoot_balloon = True

    def remove(self):
        self.__has_been_shot = False
        self.set_position(x=-80, y=-80)
