import os
import pickle
import time
import pygame
from pygame.locals import *
from Orientation import Direction
from configs import *
from Carrot import Carrot
from Rabbit import Rabbit
from Hunter import Hunter
import neat


pygame.init()
pygame.mixer.init()

screen = Window.create()

#background_sound = pygame.mixer.Sound("sounds/nature.ogg")
#background_sound.play(loops=-1)
#background_sound.set_volume(0.2)

gen = 0 #total de gerações já criadas

clock = pygame.time.Clock()

def save_checkpoint(genomes):
    global config
    checkpoint = {
        'genomes': genomes,
        'configuration': config
    }
    with open('checkpoint.pkl', 'wb') as arquivo:
        pickle.dump(checkpoint, arquivo)

    print("Treino guardado!")
    time.sleep(0.5) #Aguardar meio segundo para não gravar o treino multiplas vezes

def restore_checkpoint():
    global config
    with open('checkpoint.pkl', 'rb') as arquivo:
        checkpoint = pickle.load(arquivo)

    config = checkpoint['configuration']
    print("Treino carregado!")
    time.sleep(0.5)  # Aguardar meio segundo para não ler o treino multiplas vezes

    return checkpoint['genomes']

#função para executar o jogo
def evalGame(genomes, config):
    global gen, screen, clock
    gen += 1 #totalizar geração

    #objetos
    elmer = Hunter(1090, 280)
    carrots = Carrot.create_group(2)

    bugs_bunnies = [] #lista com todos os coelhos

    for genome_id, genome in genomes:
        genome.fitness = 0  # Todos os genomas começam com 0 de aptidão
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        bugs_bunnies.append(Rabbit(500, 200, genome, net)) # criar várias instâncias do nosso coelho

    #manter o jogo ativo enquanto existirem genomas
    while len(bugs_bunnies) > 0:
        dt = clock.tick(60)

        #evento de encerrar a janela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        #Mapear todas as teclas premidas
        key = pygame.key.get_pressed()

        #Desenhar fundo
        screen.blit(World.BACKGROUND, [0, 0])

        #permitir que seja eu a decidir quando disparar
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            elmer.shot_now()

        #gravar treino
        if key[pygame.K_F1]:
            save_checkpoint(genomes)

        #ler treino
        if key[pygame.K_F2]:
            genomes = restore_checkpoint()
            break

        #reinciar geração
        if key[pygame.K_r]:
            del(bugs_bunnies)
            break

        #realizar disparos por parte do caçador
        #elmer.shoot_if_ready()

        #mover todos os disparos do caçador
        elmer.move_shootings()

        # percorrer todas as cenouras para verificar quais foram apanhadas e desenhar as restantes
        for carrot in carrots:
            carrot.fall()  # mover cenoura
            for bugs_bunny in bugs_bunnies:
                if bugs_bunny.colides_with(carrot):
                    bugs_bunny.totalize_carrot()  # Contabilizar mais uma cenoura
                    carrot.reset()  # reposicionar a cenoura novamente

                    bugs_bunny.add_fitness(5) #recompensar este coelho por ter apanhado uma cenoura

                    continue  # se a cenoura foi apanhada, não vai ser necessário desenhá-la

            carrot.draw()  # desenhar cenoura

        for bugs_bunny in bugs_bunnies:
            #bugs_bunny.addFitness(0.0001)  # recompensar por ainda estar vivo
            closest_carrot = Carrot.closest_from_group(carrots, bugs_bunny)

            #Obter os outputs da rede neuronal com base nos inputs
            output = bugs_bunny.get_net().activate(
                (
                    # distância da cenoura mais próxima
                    closest_carrot['distance'],

                    # posição x e y do coelho
                    bugs_bunny.get_x(),
                    bugs_bunny.get_y(),

                    #distãncia da bala do mais próxima do lado direito do coelho
                    elmer.get_closest_bullet_distance_from(bugs_bunny),

                    #Distância do caçador
                    elmer.distance_from(bugs_bunny),
                )
            )

            moveLeft = output[0] > 0
            moveRight = output[1] > 0
            jump = output[2] > 0

            # A nossa rede neuronal passa a ter o controlo dos movimentos, já não seremos nós!!

            """if key[pygame.K_LEFT]:
                bugs_bunny.move_left()
            elif key[pygame.K_RIGHT]:
                bugs_bunny.move_right()

            if key[pygame.K_SPACE]:
                bugs_bunny.jump()"""

            if moveLeft:
                bugs_bunny.move_left()
            elif moveRight:
                bugs_bunny.move_right()

            if jump:
                bugs_bunny.jump()

                # castigar o coelho por ter saltado desnecessariamente (não havia uma bala a 200px de distância)
                if elmer.get_closest_bullet_distance_from(bugs_bunny) > 200:
                    bugs_bunny.add_fitness(-10)

            # recompensar porque o coelho se está a mover na direção da cenoura mais próxima
            if closest_carrot['direction'] == Direction.LEFT and bugs_bunny.is_moving_left() or \
                closest_carrot['direction'] == Direction.RIGHT and bugs_bunny.is_moving_right():
                bugs_bunny.add_fitness((1 / closest_carrot['distance']) * 1000) #distância calculada com proporcionalidade inversa (Quanto mais próximo = mais fitness)
            else:
                #castigar o coelho por não se estar a mover ou não estar a seguir o sentido certo
                bugs_bunny.add_fitness(-5)

            #castigar por não estar a apanhar cenouras
            bugs_bunny.add_fitness(-bugs_bunny.get_times_no_catch() / 100)

            #atualizar o salto de cada coelho
            bugs_bunny.update_jump()

            #atualizar se o coelho ficar parado
            bugs_bunny.update_stagnant_state()

            #quando o caçador acerta no coelho
            if elmer.hits(bugs_bunny):
                bugs_bunny.lose_life() #coelho perde 1 vida
                bugs_bunny.add_fitness(-100) # Castigar por cada vida perdida (o pior dos castigos)

            # Matar o coelho quando tocar no caçador
            if bugs_bunny.colides_with(elmer):
                bugs_bunny.lose_life(True)  # coelho pede as vidas todas
                bugs_bunny.add_fitness(-100)

            if bugs_bunny.is_dead():
                bugs_bunnies.remove(bugs_bunny) #remover o genoma morto
                continue

            #remover todos os coelhos quando alguém atingir um valor extremamente baixo
            if bugs_bunny.get_genode().fitness < -100000:
                #bugs_bunnies.remove(bugs_bunny)
                bugs_bunnies.clear()
                break

            #desenhar coelho
            bugs_bunny.draw(screen)

            # apresentar vidas e total de cenouras apanhadas pelo coelho
            bugs_bunny.draw_lives(screen)
            bugs_bunny.draw_total_carrots(screen)
            bugs_bunny.draw_fitness(screen)

        #Desenhar caçador
        elmer.draw(screen)

        #apresentar os tiros disparados pelo caçador
        elmer.draw_shootings(screen)

        #apresentar frame
        pygame.display.update()

#------------------------------------------

config_file = os.path.join(os.path.dirname(__file__), 'neat-config.txt')

config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_file)

# Create the population, which is the top-level object for a NEAT run.
population = None

population = neat.Population(config)

# Add a stdout reporter to show progress in the terminal.
population.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
population.add_reporter(stats)
# p.add_reporter(neat.Checkpointer(5))

# Run for up to 999 generations.
winner = population.run(evalGame, 999)

# show final stats
print('\nBest genome:\n{!s}'.format(winner))
pygame.quit()