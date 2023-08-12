import pygame
import math, random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Basketball")

ball_image = pygame.image.load("imgs/bola.png")

x = WINDOW_WIDTH // 2
y = WINDOW_HEIGHT // 2

INITIAL_SPEED = 5
ANGLE = 75
GRAVITY = 0.2

ball_is_moving_up = False
ball_is_moving_to_the_left = False


BALL_WIDTH = ball_image.get_width()
BALL_HEIGHT = ball_image.get_height()

initial_velocity_x = INITIAL_SPEED * math.cos(math.radians(ANGLE))
initial_velocity_y = INITIAL_SPEED * math.sin(math.radians(ANGLE))


clock = pygame.time.Clock()

running = True
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("darkgray")


    # Update ball position
    x += initial_velocity_x
    y -= initial_velocity_y + 0.5 * GRAVITY

    # Update vertical velocity with GRAVITY
    initial_velocity_y -= GRAVITY

    # Check for collision with window borders
    if x <= 0:
        ball_is_moving_to_the_left = True
        x = 0
        initial_velocity_x *= -1
    elif x >= WINDOW_WIDTH - BALL_WIDTH:
        ball_is_moving_to_the_left = True
        x = WINDOW_WIDTH - BALL_WIDTH
        initial_velocity_x *= -1

        print(
            f"x: {x}\n"
            f"y: {y}\n"
            f"initial_velocity_x: {x}\n"
            f"initial_velocity_y: {y}\n"
        )

    # Check for collision with ground
    if y <= 0:
        ball_is_moving_up = True
        y = 0
        initial_velocity_y *= -1
    elif y >= WINDOW_HEIGHT - BALL_HEIGHT:
        ball_is_moving_up = True
        y = WINDOW_HEIGHT - BALL_HEIGHT
        initial_velocity_y *= -1

        print(
            f"x: {x}\n"
            f"y: {y}\n"
            f"initial_velocity_x: {x}\n"
            f"initial_velocity_y: {y}\n"
        )



    screen.blit(ball_image, (x, y))

    pygame.display.update()

pygame.quit()
