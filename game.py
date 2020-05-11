import math
import pygame
import sys
import random

pygame.init();

WIDTH = 800
HEIGHT = 600

FALL_STEP = 20

# Define some colors
RED = (255,0,0)
BLUE = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

player_size = 10
player_pos = [WIDTH / 2 , HEIGHT / 2  - 2 * player_size]

enemy_size = 25
enemy_pos = [random.randint(0, WIDTH - enemy_size), random.randint(0, HEIGHT - enemy_size )]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
score = 0
pressedTime = 0
powerCoef = 4
sideCoef = 5
speed = 4

game_over = False

def vector(x, y):
    return [y[0] - x[0], y[1] - x[1]]

def norm(x,y):
       mag=math.sqrt(x*x+y*y)
       return x/mag,y/mag

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True;
    return False

clock = pygame.time.Clock()
while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pressedTime = 0
            mousePos = pygame.mouse.get_pos()
            vectorDirection = [player_pos[0] - mousePos[0], player_pos[1] - mousePos[1]]
            print(norm(vectorDirection[0], vectorDirection[1]))

        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            # when was pressed from the right side from the player
            #  if (abs(mousePos[1] - player_pos[1]) < sideCoef and mousePos[0] > player_pos[0]):
            #      player_pos[0] += player_size + pressedTime * powerCoef
            #  # when was pressed from left side from the player
            #  elif (abs(mousePos[1] == player_pos[1]) < sideCoef and mousePos[0] < player_pos[0]):
            #      player_pos[0] -= player_size + pressedTime * powerCoef
            #  # when was pressed from the bottom side  from the player
            #  elif (abs(mousePos[0] == player_pos[0]) < sideCoef and mousePos[1] < player_pos[1]):
            #      player_pos[1] -= player_size + pressedTime * powerCoef
            #  # when was pressed from the top side from the player
            #  elif (abs(mousePos[0] == player_pos[0]) < sideCoef and mousePos[1] > player_pos[1]):
            #      player_pos[1] += player_size + pressedTime * powerCoef

            #  if (mousePos[1] > player_pos[1]):
            #      player_pos[1] -= player_size + pressedTime * powerCoef
            #  else:
            #      player_pos[1] += player_size + pressedTime * powerCoef

            #  if (mousePos[0] > player_pos[0]):
            #      player_pos[0] -= player_size + pressedTime * powerCoef
            #  else:
            #      player_pos[0] += player_size + pressedTime * powerCoef

            ss = norm(vectorDirection[0], vectorDirection[1])
            x_dir = player_pos[0] + (ss[0] * speed * pressedTime)            
            y_dir = player_pos[1] + (ss[1] * speed * pressedTime)
            print(player_pos)
            player_pos = [x_dir, y_dir]
            pressedTime = 0


        # detect user pos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= player_size
                pass
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += player_size
                pass
            elif event.key == pygame.K_UP:
                player_pos[1] -= player_size
                pass

            elif event.key == pygame.K_DOWN:
                player_pos[1] += player_size
                pass

            elif pygame.key.get_mods() & pygame.KMOD_CTRL  and  event.key == pygame.K_q:
                sys.exit()
                pass

    screen.fill((0, 0, 0))

    # Update enemy_pos
   # if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
   #     enemy_pos[1] += FALL_STEP
   # else:
   #     enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]

    if detect_collision(player_pos, enemy_pos):
        # game_over = True
        score += 1
        enemy_pos = [random.randint(0, WIDTH - enemy_size), random.randint(0, HEIGHT - enemy_size)]
        pass

    clock.tick(30)

    button_states = pygame.mouse.get_pressed()

    if button_states[0]:
        pressedTime += 1


    font = pygame.font.Font(None, 44)
    string = "Score: " + str(score)
    text = font.render(string, 1, WHITE)
#    timePressed = font.render(timeP, 1, WHITE)
    screen.blit(text, (0,10))

    pygame.draw.circle(screen, BLUE, (int(enemy_pos[0]), int(enemy_pos[1])), int(enemy_size))
    pygame.draw.circle(screen, RED, (int(player_pos[0]), int(player_pos[1])), int(player_size))
    #pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    #pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.display.update()
