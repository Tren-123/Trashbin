import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

#code here

circle(screen, (255,255,0), (200, 200), 75, 0)
circle(screen, (255, 0, 0), (165, 185), 18, 0)
circle(screen, (255, 0, 0), (235, 185), 14, 0)
circle(screen, (0,0,0), (165, 185), 8, 0)
circle(screen, (0,0,0), (235, 185), 8, 0)
rect(screen, (0,0,0), (170, 235 , 60, 15), 0)
line(screen, (0,0,0), (150,150), (186, 170), 10 )
line(screen, (0,0,0), (250,150), (215, 170), 10 )

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
