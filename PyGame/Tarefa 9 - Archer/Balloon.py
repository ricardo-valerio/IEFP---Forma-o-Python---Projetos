from configs import *
from Elements import Elements
import random

class Balloon(Elements):
    def __init__(self, x, y, color, img_path):
        super().__init__(x, y, img_path)
        self.__initial_x = x
        self.__initial_y = y
        self.color = color
        self.has_been_blown = False

    def move_up(self):
        if not self.has_been_blown:

            if self._y <= -85:
                self.set_position(
                    x=self.__initial_x,
                    y=Screen.HEIGHT + 85
                )
            else:
                random_increment = random.random()
                self._x += -0.2 if random_increment <= 0.5 else 0.2
                self._y -= 3

        else:
            self._x = self.__initial_x
            self._y = self.__initial_y

        self.draw(surface=screen)

    def pop(self):
        self.has_been_blown = True
        balloon_pop.play()

