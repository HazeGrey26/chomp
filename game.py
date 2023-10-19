import sys
import pygame
import random
from settings import *

# Plants Drawing
for i in range(5):  # Placeholder for a random number of weeds
    plantPos = random.randint(0, SCREEN_WIDTH)
    if random.randint(1,2) == 1:
        screen.blit(seaweed, (plantPos, SEAWEED_HEIGHT))
    else:
        screen.blit(coral, (plantPos, SEAWEED_HEIGHT))

# Top Sand Drawing
for i in range(int(SCREEN_WIDTH/TILE_SIZE)):
    screen.blit(sandTop, (i*TILE_SIZE, SCREEN_HEIGHT-SAND_HEIGHT*2))

# Sand Infill Drawing
for i in range(int(SCREEN_WIDTH/TILE_SIZE)):
    debris = random.randint(0, 10)
    if debris > 9:
        screen.blit(sandFill, (i * TILE_SIZE, SCREEN_HEIGHT - SAND_HEIGHT))
        screen.blit(sandDebris2, (i*TILE_SIZE, SCREEN_HEIGHT-SAND_HEIGHT+10))
    elif debris > 7:
        screen.blit(sandDebris1, (i*TILE_SIZE, SCREEN_HEIGHT-SAND_HEIGHT))
    elif debris > 6:
        screen.blit(sandDebris, (i * TILE_SIZE, SCREEN_HEIGHT - SAND_HEIGHT))
    else:
        screen.blit(sandFill, (i*TILE_SIZE, SCREEN_HEIGHT-SAND_HEIGHT))


screen.blit(player, PLAYER_POSITION)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()