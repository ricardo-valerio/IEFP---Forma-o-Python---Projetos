from configs import *

pygame.init()


running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    World.draw_background()



    pygame.display.update()

pygame.quit()
