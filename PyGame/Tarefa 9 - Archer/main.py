from configs import *
from Archer import Archer
from Arrow import Arrow
from Balloon import Balloon
from random import choice

archer = Archer(
    x=10,
    y=516,
    img_path='imgs/archer.png'
)

arrows = [
    Arrow(x=-80, y=-80, img_path='imgs/arrow.png', number=1),
    Arrow(x=-80, y=-80, img_path='imgs/arrow.png', number=2),
    Arrow(x=-80, y=-80, img_path='imgs/arrow.png', number=3),
    Arrow(x=-80, y=-80, img_path='imgs/arrow.png', number=4),
    Arrow(x=-80, y=-80, img_path='imgs/arrow.png', number=5),
    Arrow(x=-80, y=-80, img_path='imgs/arrow.png', number=6),
]

BALLOONS_COLUMNS = {
    'A': 1100,
    'B': 1200,
    'C': 1300,
    'D': 1400,
}

balloons = {
    "pink_balloon"   : Balloon(
                            x=choice(list(BALLOONS_COLUMNS.values())),
                            y=Screen.HEIGHT + 40,
                            color="pink",
                            img_path='imgs/targets/balloons/pink-balloon/1_original.png'
                       ),
    "purple_balloon" : Balloon(
                            x=choice(list(BALLOONS_COLUMNS.values())),
                            y=Screen.HEIGHT + 120,
                            color="purple",
                            img_path='imgs/targets/balloons/purple-balloon/1_original.png'
                       ),
    "orange_balloon" : Balloon(
                            x=choice(list(BALLOONS_COLUMNS.values())),
                            y=Screen.HEIGHT + 200,
                            color="orange",
                            img_path='imgs/targets/balloons/orange-balloon/1_original.png'
                       ),
    "red_balloon"    : Balloon(
                            x=choice(list(BALLOONS_COLUMNS.values())),
                            y=Screen.HEIGHT + 280,
                            color="red",
                            img_path='imgs/targets/balloons/red-balloon/1_original.png'
                       ),
    "yellow_balloon" : Balloon(
                            x=choice(list(BALLOONS_COLUMNS.values())),
                            y=Screen.HEIGHT + 360,
                            color="yellow",
                            img_path='imgs/targets/balloons/yellow-balloon/1_original.png'
                       ),
    "blue_balloon"   : Balloon(
                            x=choice(list(BALLOONS_COLUMNS.values())),
                            y=Screen.HEIGHT + 440,
                            color="blue",
                            img_path='imgs/targets/balloons/blue-balloon/1_original.png'
                       ),
}


running = True
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            archer.shoot(arrows)


    # ----------------------------------------------------------------------

    number_of_shooted_arrows = 0
    for arrow in arrows:
        if arrow.has_been_shot():
            number_of_shooted_arrows += 1

    Archer.update_number_of_shooted_arrows(value=number_of_shooted_arrows)

    # ----------------------------------------------------------------------

    key = pygame.key.get_pressed()
    if key[pygame.K_w] or key[pygame.K_UP]:
        archer.move_up()
    if key[pygame.K_s] or key[pygame.K_DOWN]:
        archer.move_down()

    # ----------------------------------------------------------------------

    World.draw_background()

    # ----------------------------------------------------------------------

    archer.draw(surface=screen)

    # ----------------------------------------------------------------------

    for balloon in balloons:
        balloons[balloon].move_up()

    # ----------------------------------------------------------------------

    all_balloons_have_been_blown = True
    for arrow in arrows:
        arrow.move_right()

        for balloon in balloons:
            if arrow.collides_with(balloons[balloon]):
                balloons[balloon].pop()

            if not balloons[balloon].has_been_blown:
                all_balloons_have_been_blown = False


        if all_balloons_have_been_blown:

            for balloon in balloons:
                balloons[balloon].has_been_blown = False

            for arrow in arrows:
                arrow.remove()

            World.draw_background()
            archer.draw(surface=screen)

            if World.CURRENT_LEVEL < 3:
                World.draw_level_complete_banner()
                level_complete.play()
            else:
                World.draw_you_win_banner()
                you_win.play()

            pygame.display.update()

            if World.CURRENT_LEVEL < 3:
                pygame.time.wait(3000)
            else:
                pygame.time.wait(8000)


            World.CURRENT_LEVEL += 1



    pygame.display.update()


    if World.CURRENT_LEVEL > 3:
        running = False

pygame.quit()
