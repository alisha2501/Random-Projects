import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arcade Shooter")

# Set the clock for controlling the frame rate
clock = pygame.time.Clock()

# Set up the player
player_size = 50
player_pos = [SCREEN_WIDTH / 2, SCREEN_HEIGHT - 2 * player_size]
player_speed = 40

# Set up the enemy
enemy_size = 50
enemy_pos = [random.randint(0, SCREEN_WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]
enemy_speed = 10

# Set up bullets
bullet_size = 10
bullet_speed = 20
bullet_list = []

# Define functions
def draw_player(player_pos):
    pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], player_size, player_size))

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def draw_bullets(bullet_list):
    for bullet_pos in bullet_list:
        pygame.draw.rect(screen, WHITE, (bullet_pos[0], bullet_pos[1], bullet_size, bullet_size))

def move_enemies(enemy_list):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < SCREEN_HEIGHT:
            enemy_pos[1] += enemy_speed
        else:
            enemy_list.pop(idx)

def move_bullets(bullet_list):
    for idx, bullet_pos in enumerate(bullet_list):
        if bullet_pos[1] > 0:
            bullet_pos[1] -= bullet_speed
        else:
            bullet_list.pop(idx)

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

def main():
    game_over = False
    score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_pos[0] -= player_speed
                elif event.key == pygame.K_RIGHT:
                    player_pos[0] += player_speed
                elif event.key == pygame.K_SPACE:
                    bullet_pos = [player_pos[0] + player_size / 2, player_pos[1]]
                    bullet_list.append(bullet_pos)
        

        screen.fill(BLACK)

        # Move enemies
        move_enemies(enemy_list)

        # Move bullets
        move_bullets(bullet_list)

        # Draw everything
        draw_player(player_pos)
        draw_enemies(enemy_list)
        draw_bullets(bullet_list)

        # Collision detection
        for enemy_pos in enemy_list:
            if detect_collision(player_pos, enemy_pos):
                game_over = True
                break

        # Increase score
        for bullet_pos in bullet_list:
            for enemy_pos in enemy_list:
                if detect_collision(bullet_pos, enemy_pos):
                    enemy_list.remove(enemy_pos)
                    bullet_list.remove(bullet_pos)
                    score += 1
                    break

        # Add new enemies
        if len(enemy_list) < 10:
            enemy_pos = [random.randint(0, SCREEN_WIDTH - enemy_size), 0]
            enemy_list.append(enemy_pos)

        pygame.display.update()
        clock.tick(30)

    print("Final Score:", score)
    pygame.quit()

if __name__ == "__main__":
    main()
