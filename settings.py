import pygame

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
sandDebris2 = pygame.image.load("assets/images/fishTile_098.png").convert()
sandDebris2.set_colorkey((0,0,0))
seaweed = pygame.image.load("assets/images/fishTile_048.png").convert()
seaweed.set_colorkey((0,0,0))
coral = pygame.image.load("assets/images/fishTile_012.png").convert()
coral.set_colorkey((0,0,0))