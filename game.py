import pygame
import time

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption(('Chomp!'), ('Chomp!'))

screen.fill("blue")
pygame.draw.rect(screen, ("brown"), (0, 380, 400, 400))
pygame.draw.rect(screen, ("green"), (200, 220, 30, 10))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == 256:
            print("NO")