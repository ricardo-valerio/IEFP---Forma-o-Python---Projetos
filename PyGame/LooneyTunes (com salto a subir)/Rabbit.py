from Characters import Characters
from Orientation import Direction, Position
from configs import *

class Rabbit(Characters):
    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            Skins.BUGS_BUNNY
        )
        self.__jump_state = None
        self.__total_jump_frames = 0
        self.__initial_y = y

    def move_left(self):
        self._x -= 5

    def move_right(self):
        self._x += 5

    def jump(self):
        if self.__jump_state != None:
            return

        self.__jump_state = Direction.RISING

    def update_jump(self):
        # RISING .-------------------------------
        if self.__jump_state == Direction.RISING:
            self._y -= 5
        # FALLING -------------------------------
        if self._y <= 50:
            self.__jump_state = Direction.FALLING
            if self.__jump_state == Direction.FALLING:
                self._y += 5
        # STOP ----------------------------------
        if self._y >= self.__initial_y:
            self.__jump_state = None
            self._y = self.__initial_y
