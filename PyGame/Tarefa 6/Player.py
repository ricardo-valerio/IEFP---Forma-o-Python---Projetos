from configs import *
from Ranking import Ranking
from Race import Race

class Player:
    def __init__(self, x, y, img_path, race_number=None):
        self.__img = pygame.transform.flip(pygame.image.load(img_path), True, False)
        self.__x = x
        self.__y = self.set_real_y_axis(y)
        self.__race_number = race_number
        self.__has_finished_race = False
        self.__has_been_ranked = False
        self.__race_time = None

        # draw the player to show it during the countdown sound effect
        self.draw(surface=screen)

    def set_real_y_axis(self, y_value):
        height = self.__img.get_rect().height
        return Screen.HEIGHT - (y_value + height)

    def get_img(self):
        return self.__img

    def scale_img(self, factor=1):
        width = self.__img.get_rect().width
        height = self.__img.get_rect().height
        self.__img = pygame.transform.scale(self.__img, (width*factor, height*factor))

    def get_race_number(self):
        return self.__race_number

    def get_race_time(self):
        return self.__race_time

    def get_coordinates(self):
        return [self.__x, self.__y]

    def move(self):
        self.__x += random.randint(1, 14)

        if self.__x >= Screen.PHOTOGRAPHER_LINE:
            Race().photographer_line_was_crossed()

    def draw(self, surface, coords=None):
        if coords:
            surface.blit(self.__img, coords)
        else:
            surface.blit(self.__img, self.get_coordinates())

    def race(self, surface):
        self.move()
        self.draw(surface)

    def get_ranking_position(self):
        Ranking().rank(self.__race_number, self.__race_time)
        self.__has_been_ranked = True
        # print(f"player {self.__race_number} - got ranked!")

    def has_finished_race(self):
        if self.__x >= Screen.FINISH_LINE_X:
            self.__race_time = time.time() - Race().STARTING_TIME
            self.__has_finished_race = True
            Race().finish_line_was_crossed()

        return self.__has_finished_race

    def has_been_ranked(self):
        return self.__has_been_ranked
