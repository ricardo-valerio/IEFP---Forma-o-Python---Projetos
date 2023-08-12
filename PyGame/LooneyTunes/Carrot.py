import random
import pygame
import math

import configs
from Orientation import Direction


class Carrot:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__img = None
        self.__randomize()

        self.__total_frames_reset = 0 #cair novamente passado x frames
        self.__total_frames_next_reset = 180 #proxima vez a cair a cenoura

    def reset(self):
        self.__randomize()

    def __randomize(self):
        self.__x = random.randint(0, 1001)
        self.__y = -random.randint(0, 200)
        self.__img = random.choice(configs.Skin.CARROTS)

    def fall(self):
        self.__y += 10
        ground_y = configs.World.GROUND_POSITION - self.__img.get_height()

        if self.__y >= ground_y:
            self.__y = ground_y

        #fazer cair novamente a cenoura após x frames
        if self.__total_frames_reset < self.__total_frames_next_reset:
            self.__total_frames_reset += 1
        else:
            self.reset()
            self.__total_frames_reset = 0
            self.__total_frames_next_reset = random.randint(300, 800)

    def draw(self):
        screen = pygame.display.get_surface()
        screen.blit(self.__img, [self.__x, self.__y])

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_w(self):
        return self.__img.get_width()

    def get_h(self):
        return self.__img.get_height()

    @staticmethod
    def create_group(qt):
        #alternativa:
        #return [Carrot() for _ in range(qt)]
        carrots = []
        for pos in range(qt):
            carrots.append(Carrot())

        return carrots

    @staticmethod
    def reset_group(carrots):
        for carrot in carrots:
            carrot.reset()

    @staticmethod
    def closest_from_group(carrots, rabbit):
        closest_distance = 9999
        direction = 0

        #offset do coelho para considerar o centro dos pés
        rabit_x = rabbit.get_x() + 41
        rabit_y = rabbit.get_y() + 180

        for carrot in carrots:
            #offset
            carrot_x = carrot.get_x() + carrot.get_w() / 2 #ao centro em x
            carrot_y = carrot.get_y() + carrot.get_h() #ao fundo de y

            distance = math.sqrt((carrot_x - rabit_x) ** 2 + (carrot_y - rabit_y) ** 2)

            if distance < closest_distance:
                closest_distance = distance
                direction = Direction.RIGHT if carrot_x > rabit_x else Direction.LEFT

        #print("Distance:", closest_distance, 'direction:', direction)
        return {'distance': closest_distance, 'direction': direction}
