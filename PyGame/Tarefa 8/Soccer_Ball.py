from configs import *
from Referee import Referee

class Soccer_Ball:

    def __init__(self, x, y, img):
        self.__x = x
        self.__y = y
        self.__img = img
        self.__steps_to_increment_position = 5
        self.__slope_of_kick_has_been_found = False
        self.__slope_of_kick = None
        self.__came_from_left = False
        self.__came_from_right = False

    def set_position(self, x=100, y=100, center=None):
        if center:
            self.__x = Screen.CENTER_X_OF_SOCCER_FIELD - Screen.CENTER_X_OF_SOCCER_BALL
            self.__y = Screen.CENTER_Y_OF_SOCCER_FIELD - Screen.CENTER_Y_OF_SOCCER_BALL
        else:
            self.__x = x
            self.__y = y

    def move_right(self):
        self.__came_from_left = True
        self.__came_from_right = False

        # BETWEEN THE GOAL NET --------------------------------------------------------------
        if self.__y >= Screen.GOAL_NET_TOP_LIMIT and \
           self.__y <= Screen.GOAL_NET_BOTTOM_LIMIT - self.__img.get_height():

           if self.__x < Screen.VERTICAL_RIGHT_SOCCER_FIELD_LIMIT + Screen.GOAL_LINE_CROSSING_MARGIN_RIGHT_SIDE:
                self.__x += self.__steps_to_increment_position
           else:
                self.score_goal()
                Referee.SCORE_TEAM_ON_LEFT_SIDE += 1

        # NOT IN BETWEEN THE GOAL NET -------------------------------------------------------
        elif self.__x < Screen.VERTICAL_RIGHT_SOCCER_FIELD_LIMIT - self.__img.get_width():
            self.__x += self.__steps_to_increment_position
        else:
            self.__x = Screen.VERTICAL_RIGHT_SOCCER_FIELD_LIMIT - self.__img.get_width()

    def move_left(self):
        self.__came_from_left = False
        self.__came_from_right = True

        # BETWEEN THE GOAL NET --------------------------------------------------------------
        if self.__y >= Screen.GOAL_NET_TOP_LIMIT and \
           self.__y <= Screen.GOAL_NET_BOTTOM_LIMIT - self.__img.get_height():

            if self.__x > Screen.VERTICAL_LEFT_SOCCER_FIELD_LIMIT - self.__img.get_width() - Screen.GOAL_LINE_CROSSING_MARGIN_LEFT_SIDE:
                self.__x -= self.__steps_to_increment_position
            else:
                self.score_goal()
                Referee.SCORE_TEAM_ON_RIGHT_SIDE += 1

        # NOT IN BETWEEN THE GOAL NET -------------------------------------------------------
        else:
            if self.__x > Screen.VERTICAL_LEFT_SOCCER_FIELD_LIMIT:
                self.__x -= self.__steps_to_increment_position
            else:
                self.__x = Screen.VERTICAL_LEFT_SOCCER_FIELD_LIMIT

    def move_up(self):
        if self.__y > Screen.HORIZONTAL_TOP_SOCCER_FIELD_LIMIT:
            self.__y -= self.__steps_to_increment_position
        else:
            self.__y = Screen.HORIZONTAL_TOP_SOCCER_FIELD_LIMIT

    def move_down(self):
        if self.__y < Screen.HORIZONTAL_BOTTOM_SOCCER_FIELD_LIMIT - self.__img.get_height():
            self.__y += self.__steps_to_increment_position
        else:
            self.__y = Screen.HORIZONTAL_BOTTOM_SOCCER_FIELD_LIMIT - self.__img.get_height()

    def draw(self, surface, coords=False):
        if coords:
            surface.blit(self.__img, coords)
        else:
            surface.blit(self.__img, [self.__x, self.__y])

    def score_goal(self):
        self.__slope_of_kick = None
        World.draw_goal_wallpaper()
        goal_sound.play()
        pygame.time.wait(2500)
        self.set_position(center=True)
        Referee.whistle()

    def find_slope_of_kick(self, goal_net_on_the_right=None, goal_net_on_the_left=None):
        if goal_net_on_the_right:
            m = (self.__y + Screen.CENTER_Y_OF_SOCCER_BALL - 400)/(self.__x + Screen.CENTER_X_OF_SOCCER_BALL - 1168)

        if goal_net_on_the_left:
            m = (self.__y + Screen.CENTER_Y_OF_SOCCER_BALL - 400)/(self.__x + Screen.CENTER_X_OF_SOCCER_BALL - 27)

        return m

    def function_for_the_right_kick_trajectory(self):
        if not self.__slope_of_kick_has_been_found:
            self.__slope_of_kick = self.find_slope_of_kick(goal_net_on_the_right=True)
            self.__slope_of_kick_has_been_found = True
        new_y = self.__slope_of_kick * (self.__x + Screen.CENTER_X_OF_SOCCER_BALL - 1168) + 400
        return new_y - Screen.CENTER_Y_OF_SOCCER_BALL

    def function_for_the_left_kick_trajectory(self):
        if not self.__slope_of_kick_has_been_found:
            self.__slope_of_kick = self.find_slope_of_kick(goal_net_on_the_left=True)
            self.__slope_of_kick_has_been_found = True
        new_y = self.__slope_of_kick * (self.__x + Screen.CENTER_X_OF_SOCCER_BALL - 27) + 400
        return new_y - Screen.CENTER_Y_OF_SOCCER_BALL

    def just_go_and_score_a_goal(self):
        # RIGHT SIDE GOAL NET -----------------------------------------------------------------------------
        # if self.__x + Screen.CENTER_X_OF_SOCCER_BALL >= Screen.CENTER_X_OF_SOCCER_FIELD:
        if self.__came_from_left:

            while self.__x < 1133:
                self.__x += 1
                self.set_position(x=self.__x, y=self.function_for_the_right_kick_trajectory())
                World.draw_soccer_field_and_score_board()
                Referee.draw_score()
                self.draw(surface=screen)
                pygame.display.update()

            self.score_goal()
            self.__slope_of_kick_has_been_found = False
            Referee.SCORE_TEAM_ON_LEFT_SIDE += 1

        # LEFT SIDE GOAL NET -----------------------------------------------------------------------------
        # elif self.__x + Screen.CENTER_X_OF_SOCCER_BALL < Screen.CENTER_X_OF_SOCCER_FIELD:
        elif self.__came_from_right:

            while self.__x > 27 :
                self.__x -= 1
                self.set_position(x=self.__x, y=self.function_for_the_left_kick_trajectory())
                World.draw_soccer_field_and_score_board()
                Referee.draw_score()
                self.draw(surface=screen)
                pygame.display.update()

            self.score_goal()
            self.__slope_of_kick_has_been_found = False
            Referee.SCORE_TEAM_ON_RIGHT_SIDE += 1

