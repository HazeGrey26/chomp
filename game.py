import sys
import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SAND_HEIGHT = SCREEN_HEIGHT-20
PLAYER_POSITION = (SCREEN_WIDTH/2-32, SCREEN_HEIGHT/2-32)

# Colors
WATER_COLOR = "blue"
SAND_COLOR = "brown"

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chomp!', 'Chomp!')

screen.fill(WATER_COLOR)
sand = pygame.image.load("assets/images/fishTile_080.png")  #.convert()  # Convert speeds up image loading, but removes the transparency from pngs
screen.blit(sand, PLAYER_POSITION)
pygame.draw.rect(screen, SAND_COLOR, (0, SAND_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()