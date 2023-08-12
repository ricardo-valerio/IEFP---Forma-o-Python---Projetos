from random import randint

from Bullet import Bullet
from configs import *

class Hunter:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__initial_x = x #novo
        self.__initial_y = y #novo
        self.__img = Skin.ELMER
        self.__total_shoot_frames = 0
        self.__bullets = []

        #para IA
        self.__cooldown_frames = 60

    #novo
    def reset(self):
        self.__x = self.__initial_x
        self.__y = self.__initial_y
        self.__total_shoot_frames = 0
        self.__bullets.clear()

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def shoot_if_ready(self):
        self.__total_shoot_frames += 1
        if self.__total_shoot_frames == 120:
            if randint(0, 100) < 40: #probabilidade de x% de disparar um tiro
                self.__bullets.append(Bullet(self.__x - 5, self.__y + 68))

            self.__total_shoot_frames = 0

    def shot_now(self):
        if self.__cooldown_frames == 60:
            self.__bullets.append(Bullet(self.__x - 5, self.__y + 68))
            self.__cooldown_frames = 0

    def move_shootings(self):
        #contabilizar frames para poder disparar
        if self.__cooldown_frames < 60:
            self.__cooldown_frames += 1

        for bullet in self.__bullets:
            bullet.move()

            if bullet.is_out():
                self.__bullets.remove(bullet)

    #novo metodo
    def hits(self, rabbit):
        for bullet in self.__bullets:
            if bullet.colides_with(rabbit):
                #self.__bullets.remove(bullet)
                return True

        return False

    def draw_shootings(self, surface):
        for bullet in self.__bullets:
            bullet.draw(surface)

    def distance_from(self, rabbit):
        return self.__x - rabbit.get_x()

    def get_closest_bullet_distance_from(self, rabbit):
        closest_bullet_x = 999
        for bullet in self.__bullets:
            #ignorar balas que estejam atrás do coelho
            if bullet.get_x() < rabbit.get_x():
                continue

            #           x da bala    -   x do coelho   + comprimento do coelho (para contabilizar as balas do lado direito do coelho)
            distance = bullet.get_x() - rabbit.get_x() + rabbit.get_w()

            if distance < closest_bullet_x:
                closest_bullet_x = distance

        return closest_bullet_x

    def get_reachable_bullents(self, rabbit):
        pass
