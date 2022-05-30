import pygame
from pygame.draw import *

pygame.init()

FPS = 1

screen = pygame.display.set_mode((500, 800))

surface_main = pygame.Surface((500, 800), pygame.SRCALPHA)
surface_1 = pygame.Surface((500, 800), pygame.SRCALPHA)
surface_2 = pygame.Surface((500, 800), pygame.SRCALPHA)
surface_3 = pygame.Surface((500, 800), pygame.SRCALPHA)
surfaces = [surface_main, surface_1, surface_2, surface_3]
z = ''
w = ''

def inpute_z():
    z = int(input())
    print("here\n")
    w = int(input())
    y = int(input())

    for i in range(z):

        rect(surfaces[1], (255, 255, 255), (w, y, 50*z, 100), 0)  # Skyscraper
        screen.blit(surfaces[1], (0, 0))
        pygame.display.update()
inpute_z()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()