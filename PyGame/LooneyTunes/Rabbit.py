import pygame
from Orientation import *
from configs import *

class Rabbit:
    def __init__(self, x, y, genode, net):
        self.__x = x
        self.__y = y
        self.__img = Skin.BUGS_BUNNY
        self.__initial_x = x #novo
        self.__initial_y = y
        self.__jump_state = None
        self.__total_carrots = 0
        self.__lives = 1 #só vai ter 1 vida

        # AI - Para gestão da rede neuronal
        self.__genode = genode  # genoma
        self.__net = net  # rede neural
        self.__last_movement_x = 9999 #último x onde esteve
        self.__last_movement = None #último movimento feito
        self.__total_frames_no_catch = 0 #total de frames em que não apanhou uma cenoura

    # Retornar genoma
    def get_genode(self):
        return self.__genode

    # Retornar rede neural
    def get_net(self):
        return self.__net

    def add_fitness(self, val):
        self.__genode.fitness += val

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_w(self):
        return self.__img.get_width()

    def get_h(self):
        return self.__img.get_height()

    def get_times_no_catch(self):
        return self.__total_frames_no_catch

    def draw_fitness(self, surface):
        txt = Font.MAIN.render(f"{self.__genode.fitness:.2F} FT", True, 'white', 'black')
        surface.blit(txt, [self.__x + 20, self.__y + 20])

    #novo
    def reset(self):
        self.__x = self.__initial_x
        self.__y = self.__initial_y
        self.__jump_state = None
        self.__total_carrots = 0
        self.__lives = 3

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def draw_lives(self, surface):
        for x in range(self.__lives):
            surface.blit(Skin.HEART, [(20 + self.__x) + 20 * x, self.__y - 20])

    def draw_total_carrots(self, surface):
        txt = Font.MAIN.render(f"{self.__total_carrots} cenouras", True, 'white', 'black')
        surface.blit(txt, [self.__x + 20, self.__y])

    def move_left(self):
        self.__last_movement = Direction.LEFT
        self.__x -= 5

        if self.__x < 10:
            self.__x = 10

    def move_right(self):
        self.__last_movement = Direction.RIGHT
        self.__x += 5

    def jump(self):
        if self.__jump_state != None:
            return

        self.__jump_state = Direction.RISING

    def is_moving_left(self):
        return self.__last_movement == Direction.LEFT

    def is_moving_right(self):
        return self.__last_movement == Direction.RIGHT

    def is_jumping(self):
        return self.__jump_state != None

    #coloca a indicação de que o coelho ficou parado
    def update_stagnant_state(self):
        self.__total_frames_no_catch += 1 #contar frames até apanhar uma cenoura

        if self.__x == self.__last_movement_x:
            self.__last_movement = None
        else:
            self.__last_movement_x = self.__x

    def update_jump(self):
        if self.__jump_state == Direction.RISING:
            self.__y -= 10
            if self.__y <= 10:
                self.__jump_state = Direction.FALLING
        elif self.__jump_state == Direction.FALLING:
            self.__y += 10
            if self.__y >= self.__initial_y:
                self.__jump_state = None

    def lose_life(self, die_instantly=False):
        if die_instantly:
            self.__lives = 0
            return

        self.__lives -= 1

    def get_lives(self):
        return self.__lives

    def is_dead(self):
        return self.__lives <= 0

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def totalize_carrot(self):
        self.__total_carrots += 1

        #reiniciar a contagem de frames em que não apanhou uma cenoura
        self.__total_frames_no_catch = 0

    def get_total_carrots(self):
        return self.__total_carrots







