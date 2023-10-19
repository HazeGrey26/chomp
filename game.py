import sys
import pygame

TILE_SIZE = 64
SCREEN_WIDTH = 8*TILE_SIZE
SCREEN_HEIGHT = 8*TILE_SIZE
SAND_HEIGHT = TILE_SIZE
PLAYER_POSITION = (SCREEN_WIDTH/2-32, SCREEN_HEIGHT/2-32)

# Colors
WATER_COLOR = "blue"

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chomp!', 'Chomp!')

screen.fill(WATER_COLOR)
player = pygame.image.load("assets/images/fishTile_080.png").convert()  # Convert speeds up image loading, but removes the transparency from pngs
player.set_colorkey((0,0,0))  # Adds transparency back to the converted image
sandTop = pygame.image.load("assets/images/fishTile_002.png").convert()
sandTop.set_colorkey((0,0,0))
sandFill = pygame.image.load("assets/images/fishTile_001.png").convert()
sandDebris = pygame.image.load("assets/images/fishTile_018.png").convert()
sandDebris1 = pygame.image.load("assets/images/fishTile_019.png").convert()

screen.blit(player, PLAYER_POSITION)

for i in range(int(SCREEN_WIDTH/TILE_SIZE)):
    screen.blit(sandTop, (i*TILE_SIZE, SCREEN_HEIGHT-SAND_HEIGHT*2))
for i in range(int(SCREEN_WIDTH/TILE_SIZE)):
    screen.blit(sandFill, (i*TILE_SIZE, SCREEN_HEIGHT-SAND_HEIGHT))

screen.blit(sandDebris1, (5*TILE_SIZE, SCREEN_HEIGHT-SAND_HEIGHT))
screen.blit(sandDebris, (1*TILE_SIZE, SCREEN_HEIGHT-SAND_HEIGHT))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()