import pygame
import sys
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)   

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mario-Like Game")

clock = pygame.time.Clock()

player_image = pygame.Surface((40, 60))
player_image.fill(BLUE)

ground_image = pygame.Surface((SCREEN_WIDTH, 40))
ground_image.fill(GREEN)

obstacle_image = pygame.Surface((40, 40))
obstacle_image.fill(RED)

player_x = 50
player_y = SCREEN_HEIGHT - 100
player_speed = 5
player_jump = -15
player_velocity_y = 0

ground_y = SCREEN_HEIGHT - 40

gravity = 0.8
jumping = False

obstacle_x = SCREEN_WIDTH
obstacle_y = ground_y - 40
obstacle_speed = 5

score = 0
font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color=BLACK):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_SPACE] and not jumping:
        jumping = True
        player_velocity_y = player_jump

    player_velocity_y += gravity
    player_y += player_velocity_y

    if player_y >= ground_y - 60:
        player_y = ground_y - 60
        jumping = False

    obstacle_x -= obstacle_speed
    if obstacle_x < -40:
        obstacle_x = SCREEN_WIDTH
        score += 1

    player_rect = pygame.Rect(player_x, player_y, 40, 60)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, 40, 40)
    if player_rect.colliderect(obstacle_rect):
        running = False

    screen.fill(WHITE)
    screen.blit(ground_image, (0, ground_y))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(obstacle_image, (obstacle_x, obstacle_y))

    draw_text(f"Score: {score}", 10, 10)

    pygame.display.flip()

    clock.tick(30)



pygame.quit()
sys.exit()

