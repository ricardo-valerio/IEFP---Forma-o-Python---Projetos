from configs import *
from Soccer_Ball import Soccer_Ball
from Referee import Referee

soccer_ball = Soccer_Ball(
    x   = Screen.CENTER_X_OF_SOCCER_FIELD - Screen.CENTER_X_OF_SOCCER_BALL,
    y   = Screen.CENTER_Y_OF_SOCCER_FIELD - Screen.CENTER_Y_OF_SOCCER_BALL,
    img = World.SOCCER_BALL
)

# start the game!
Referee.whistle()

running = True
while running:
    pygame.time.Clock().tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    key = pygame.key.get_pressed()

    if key[pygame.K_w] or key[pygame.K_UP]:
        soccer_ball.move_up()
    if key[pygame.K_s] or key[pygame.K_DOWN]:
        soccer_ball.move_down()
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        soccer_ball.move_left()
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        soccer_ball.move_right()
    if key[pygame.K_SPACE]:
        soccer_ball.just_go_and_score_a_goal()


    World.draw_soccer_field_and_score_board()

    Referee.draw_score()

    soccer_ball.draw(surface=screen)

    pygame.display.update()

pygame.quit()
