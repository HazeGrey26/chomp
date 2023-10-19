import sys
import pygame
import random

TILE_SIZE = 64
SCREEN_WIDTH = 8*TILE_SIZE
SCREEN_HEIGHT = 8*TILE_SIZE
SAND_HEIGHT = TILE_SIZE
SEAWEED_HEIGHT = SCREEN_HEIGHT - SAND_HEIGHT*2 - 50
PLAYER_POSITION = (SCREEN_WIDTH/2-32, SCREEN_HEIGHT/2-32)

# Colors
WATER_COLOR = "blue"

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WATER_COLOR)
pygame.display.set_caption('Chomp!', 'Chomp!')

player = pygame.image.load("assets/images/fishTile_080.png").convert()  # Convert speeds up image loading, but removes the transparency from pngs
player.set_colorkey((0,0,0))  # Adds transparency back to the converted image
sandTop = pygame.image.load("assets/images/fishTile_002.png").convert()
sandTop.set_colorkey((0,0,0))
sandFill = pygame.image.load("assets/images/fishTile_001.png").convert()
sandDebris = pygame.image.load("assets/images/fishTile_018.png").convert()
sandDebris1 = pygame.image.load("assets/images/fishTile_019.png").convert()
seaweed = pygame.image.load("assets/images/fishTile_048.png").convert()
seaweed.set_colorkey((0,0,0))

# Seaweed Drawing
for i in range(5):  # Placeholder for a random number of weeds
    seaweedPos = random.randint(0, SCREEN_WIDTH)
    screen.blit(seaweed, (seaweedPos, SEAWEED_HEIGHT))

# Top Sand Drawing
for i in range(int(SCREEN_WIDTH/TILE_SIZE)):
    screen.blit(sandTop, (i*TILE_SIZE, SCREEN_HEIGHT-SAND_HEIGHT*2))

# Sand Infill Drawing
for i in range(int(SCREEN_WIDTH/TILE_SIZE)):
    debris = random.randint(0, 10)
    if debris > 9:
        screen.blit(sandDebris1, (i*TILE_SIZE, SCREEN_HEIGHT-SAND_HEIGHT))
    elif debris > 7:
        screen.blit(sandDebris, (i*TILE_SIZE, SCREEN_HEIGHT-SAND_HEIGHT))
    else:
        screen.blit(sandFill, (i*TILE_SIZE, SCREEN_HEIGHT-SAND_HEIGHT))


screen.blit(player, PLAYER_POSITION)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()