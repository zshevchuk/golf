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

player_size = 50
player_pos = [WIDTH / 2 , HEIGHT - 2 * player_size]

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
score = 0

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

clock = pygame.time.Clock()

while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)

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
        enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
        pass

    clock.tick(30)

    font = pygame.font.Font(None, 44)
    string = "Score: " + str(score)
    text = font.render(string, 1, WHITE)
    screen.blit(text, (0,10))

    pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.display.update()
