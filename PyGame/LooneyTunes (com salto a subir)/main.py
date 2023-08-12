from configs import *
import pygame
from pygame.locals import *
from Rabbit import Rabbit
from Hunter import Hunter

#desafio:
"""Fundo move-se com 2 camadas
Player Bugsbunny que apanha cenouras evita o caçador a mandar tiros?
O caçador manda tiros e sai do ecrã"""

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))
pygame.display.set_caption(Window.TITLE)
pygame.display.set_icon(Window.ICON)

#background_sound = pygame.mixer.Sound("sounds/nature.ogg")
#background_sound.play(loops=-1)
#background_sound.set_volume(0.2)

bugs_bunny = Rabbit(10, 200)
elmer = Hunter(490, 280)

clock = pygame.time.Clock()
running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(World.BACKGROUND, [0, 0])

    key = pygame.key.get_pressed()

    if key[pygame.K_a] or key[pygame.K_LEFT]:
        bugs_bunny.move_left()
    elif key[pygame.K_d] or key[pygame.K_RIGHT]:
        bugs_bunny.move_right()

    if key[pygame.K_UP]:
        bugs_bunny.jump()

    bugs_bunny.update_jump()

    if bugs_bunny.collides_with(elmer):
       print("Colidiu!!!!!")

    bugs_bunny.draw(screen)
    elmer.draw(screen)

    pygame.display.update()

pygame.quit()
