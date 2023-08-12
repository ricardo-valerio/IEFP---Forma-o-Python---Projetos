from configs import *
from Player import Player
from Ranking import Ranking
from Plane import Plane
from Ballon import Ballon
from Flag_Girl import Flag_Girl
from Race import Race
from Photographer import Photographer


###################################################################
# Draw the main background stage that contains:
#   - Track
#   - Public crowd
#   - Finish Line
#   - Time Counter Board
###################################################################
World.draw_background()

###################################################################
# Write "00:00" onto the time counter board
###################################################################
Race().draw_time_zero_onto_the_board()

#######################################################################################
# Create characters and objects
#######################################################################################
player1      = Player(x=30, y=185, img_path='imgs/zombies/z4.png', race_number=1)
player2      = Player(x=30, y=109, img_path='imgs/zombies/z5.png', race_number=2)
player3      = Player(x=30, y=37, img_path='imgs/zombies/z6.png', race_number=3)
plane        = Plane(x=1000, y=40, img_path='imgs/plane-zombie-race-banner.png')
ballon       = Ballon(x=240, y=110, img_path='imgs/ballon.png')
flag_girl    = Flag_Girl(x=140, y=300, img_path='imgs/girl-flags-up.png')
photographer = Photographer(x=830, y=350, img_path='imgs/photographer-zombie.png')

###################################################################
# show the background and all of the characters already so they
# are showing during the countdown sound effect
###################################################################
pygame.display.update()

###################################################################
# - play countdown sound effect
# - wait 4 seconds for it to end
# - draw the girl with the flags down
# - start the race!
# - play the sound effect of the crowd cheering
###################################################################
play_sound_effect("sounds/countdown.mp3")
pygame.time.wait(4000)  # 4 secs for the countdown sound effect
flag_girl.ready_set_go(surface=screen)
Race().start()
play_sound_effect("sounds/crowd-cheer.mp3")


running = True
while running:

    #############################################################
    # Event Manager Section
    #------------------------------------------------------------
    # - TO ASK PROF:
    # - Why can't it run if i put this code on a function and then
    # call it here?...it freezes the window...
    #############################################################
    dt = clock.tick(10) # zombie speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ###################################################################
    # if all of the players have been ranked but the ranking
    # was not shown:
    # - keep drawing them after the finish-line
    # so they are standing there, while the ranking board is showing
    # - draw the ranking board
    # - show/draw players rank on the board
    ###################################################################
    if player1.has_been_ranked() and \
       player2.has_been_ranked() and \
       player3.has_been_ranked() and \
       not Ranking().has_been_shown:
        player1.draw(surface=screen)
        player2.draw(surface=screen)
        player3.draw(surface=screen)

        World.draw_ranking_board()

        Ranking().show_rank(
            players={
                "Player 1": player1,
                "Player 2": player2,
                "Player 3": player3
            }
        )

    #######################################################################
    # All of the players have been ranked and the ranking board have been
    # shown so everything is done...
    #######################################################################
    elif player1.has_been_ranked() and \
         player2.has_been_ranked() and \
         player3.has_been_ranked() and \
         Ranking().has_been_shown:
        pass  # doesn't make a thing until the user closes the window!

    ######################################################################
    # keep drawing the background and all of the characters if
    # the players have not finished the race and have not been ranked
    ######################################################################
    else:
        World.draw_background()
        Race().draw_elapsed_time_onto_the_board()
        photographer.take_a_picture_of_the_winner(surface=screen)
        flag_girl.draw(surface=screen)
        plane.fly(surface=screen)
        ballon.fly(surface=screen)

    #############################################################
    # if a player have not finished the race:
    #   - keep him racing
    #
    # But if he has finished the race but has not been ranked:
    # - keep drawing him
    # - get him his ranking position
    #############################################################
    if not player1.has_finished_race():
        player1.race(surface=screen)
    elif not player1.has_been_ranked():
        player1.draw(surface=screen)
        player1.get_ranking_position()

    if not player2.has_finished_race():
        player2.race(surface=screen)
    elif not player2.has_been_ranked():
        player2.draw(surface=screen)
        player2.get_ranking_position()

    if not player3.has_finished_race():
        player3.race(surface=screen)
    elif not player3.has_been_ranked():
        player3.draw(surface=screen)
        player3.get_ranking_position()

    #############################################################
    # if the players have finished the race:
    # keep drawing them after the finish line
    # so they are standing there, while the ranking is showing
    #############################################################
    if player1.has_finished_race():
        player1.draw(surface=screen)
    if player2.has_finished_race():
        player2.draw(surface=screen)
    if player3.has_finished_race():
        player3.draw(surface=screen)


    pygame.display.update()


pygame.quit()
