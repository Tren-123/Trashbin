import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 800))
surface_main = pygame.Surface((500, 800), pygame.SRCALPHA)
surface_1 =  pygame.Surface((500, 800), pygame.SRCALPHA)
surface_0 =   pygame.Surface((500, 800), pygame.SRCALPHA)
surface_2 =  pygame.Surface((500, 800), pygame.SRCALPHA)


#surface_main
rect(surface_main, (83,108,103), (0, 500 , 500, 300), 0) # Ground
rect(surface_main, (255,255,255), (0, 495 , 500, 5), 0) # Horizont
rect(surface_main, (183,196,200), (0, 0 , 500, 495), 0) # Sky
ellipse(surface_main, (183, 200, 196), (-50,650, 700, 300), 0) # Road
ellipse(surface_main, (0, 0, 0), (185, 707, 45, 9), 0) # Tail pipe
rect(surface_main, (0,204,255), (205, 670, 200, 50), 0) # Car body 1
rect(surface_main, (0,204,255), (245, 645, 100, 25), 0) # Car body 2
rect(surface_main, (255,255,255), (255, 652, 30, 18), 0)  # Car window 1
rect(surface_main, (255,255,255), (305, 652, 30, 18), 0) # Car window 2
ellipse(surface_main, (0, 0, 0), (225, 702, 45, 30), 0) # Car wheel 1
ellipse(surface_main, (0, 0, 0), (350, 702, 45, 30), 0) # Car wheel 2
rect(surface_main, (219,227,226), (370, 20 , 115, 495), 0) # Skyscraper 3
screen.blit(surface_main, (0,0))


#surface_0
ellipse(surface_0, (167, 167, 167, 100), (-120, 45, 450, 120), 0) # Smog in the sky 1
screen.blit(surface_0, (0,0))

#surface_1
ellipse(surface_1, (167, 167, 167, 100), (160, -30, 450, 120), 0) # Smog in the sky 2
ellipse(surface_1, (167, 167, 167, 100), (-150, 370, 450, 120), 0) # Smog in the sky 4
ellipse(surface_1, (167, 167, 167, 100), (30, 670, 160, 50), 0) # Waste gas 1
ellipse(surface_1, (167, 167, 167, 100), (27, 605, 160, 50), 0) # Waste gas 2
ellipse(surface_1, (167, 167, 167, 100), (-80, 540, 160, 50), 0) # Waste gas 3
rect(surface_1, (147,167,172), (15, 20 , 100, 495), 0) # Skyscraper 1
rect(surface_1, (147,172,167), (140, 40 , 100, 490), 0) # Skyscraper 2
rect(surface_1, (183,200,196), (90, 80 , 115, 495), 0) # Skyscraper 4
rect(surface_1, (111,145,138), (335, 100 , 115, 495), 0) # Skyscraper 5
screen.blit(surface_1, (0,0))


#surface_2
ellipse(surface_2, (167, 167, 167, 100), (120, 200, 450, 120), 0) # Smog in the sky 3
screen.blit(surface_2, (0,0))












pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
