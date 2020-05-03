import pygame
import sys
import random

pygame.init();

WIDTH = 800
HEIGHT = 600

FALL_STEP = 20

RED = (255,0,0)
BLUE = (0,0,255)

player_size = 20
player_pos = [WIDTH / 2 , HEIGHT - 2 * player_size]

enemy_size = 20
enemy_pos = [random.randint(0, WIDTH - enemy_size), random.randint(0, HEIGHT - enemy_size)]
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True;
    return False

def getDirectionVector(player_pos, mouse_pos):
    return pygame.Vector2(player_pos[0] - enemy_pos[0], player_pos[1] - enemy_pos[1])

clock = pygame.time.Clock()

playerImage =  pygame.image.load('images/player.jpg')
player =  pygame.transform.scale(playerImage, [32, 32])
#player =  pygame.draw.circle(screen, RED, (int(player_pos[0]), int(player_pos[1])), 10)

class Player(object):
    def __init__(self):
        playerImage =  pygame.image.load('images/player.jpg')
        self.player =  pygame.transform.scale(playerImage, [32, 32])
        #screen.blit(self.player, (player_pos))
    def update(self):
        pos = pygame.mouse.get_pos()
        self.player.x = pos[0]
        self.player.y = pos[1]

while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            vector = getDirectionVector(player_pos, pos)
            print(pos)
            player_pos = pos
            pass

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



    # Update enemy_pos
#    if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
#        enemy_pos[1] += FALL_STEP
#    else:
#        enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]

    if detect_collision(player_pos, enemy_pos):
        game_over = True
        break

    pygame.draw.circle(screen, BLUE, (enemy_pos[0], enemy_pos[1]), 10)
    screen.blit(player, (player_pos))
    #player = Player()
    #screen.blit(player, [100, 100])

    clock.tick(30)
    pygame.display.update()
