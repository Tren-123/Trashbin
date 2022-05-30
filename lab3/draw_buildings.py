import pygame
from pygame.draw import *


def draw_city_view():
    """
     To call input requests for user.
     Ask user to input:
        number of skyscrapers and parameter for each skyscraper: surface, x, y, width, height, color
        number of cars and parameters for each car: surface, x, y, width, height, color
        number of smog clouds and parameters for each smog cloud: surface, x, y, width, height, color
        draw each object after input all parameters for it
     :return:
     """
    print("Please input number of skyscrapers\n")
    number_of_skyscrapers = int(input())
    for skyscraper in range(number_of_skyscrapers):
        print(f"Please input № of surface"
              f" of skyscraper № {range(number_of_skyscrapers).index(skyscraper)+1} \n")
        surface_of_skyscraper = surfaces[int(input())]
        print(f"Please input coordinate x of extreme low middle point"
              f" of skyscraper № {range(number_of_skyscrapers).index(skyscraper)+1} \n")
        coordinate_x_of_skyscraper = int(input())
        print(f"Please input coordinate y of extreme low middle point"
              f" of skyscraper № {range(number_of_skyscrapers).index(skyscraper)+1} \n")
        coordinate_y_of_skyscraper = int(input())
        print(f"Please input width"
              f" of skyscraper № {range(number_of_skyscrapers).index(skyscraper) + 1} \n")
        width_of_skyscraper = int(input())
        print(f"Please input height"
              f" of skyscraper № {range(number_of_skyscrapers).index(skyscraper) + 1} \n")
        height_of_skyscraper = int(input())
        print(f"Please input color"
              f" of skyscraper № {range(number_of_skyscrapers).index(skyscraper) + 1} \n")
        color_of_skyscraper = list(map(int, (input().split(","))))
        draw_skyscraper(surface_of_skyscraper, coordinate_x_of_skyscraper,
                       coordinate_y_of_skyscraper, width_of_skyscraper, height_of_skyscraper, color_of_skyscraper)
        #print(surface_of_skyscraper)

def draw_skyscraper(surface, x, y, width, height, color):  #FIX ME HARD PLEASE!!!!!!!
    """
     Draw a skyscraper on the surface <surface> from coordinates x, y with width <width>, height <height> and color <color>
     :param surface: choose surface from list
     :param x: coordinate x of skyscraper - extreme low middle point of skyscraper
     :param y: coordinate y of skyscraper - extreme low middle point of skyscraper
     :param width: width from extreme left point to extreme right point of the skyscraper
     :param height:  height from extreme low point to extreme up point of the skyscraper
     :param color: color of skyscraper in RGB format
     :return: none
     """

    rect(surface, color, (x, y, width, height*(-1)), 0)  # Skyscraper
    screen.blit(surface, (0, 0))
    pygame.display.update()


    #print(f"surface = {surface}\nx = {x}\ny = {y}\nwidth = {width}\nheight = {height}\ncolor = {color}")

pygame.init()
FPS = 1
screen = pygame.display.set_mode((500, 800))


surface_main = pygame.Surface((500, 800), pygame.SRCALPHA)
surface_1 = pygame.Surface((500, 800), pygame.SRCALPHA)
surface_2 = pygame.Surface((500, 800), pygame.SRCALPHA)
surface_3 = pygame.Surface((500, 800), pygame.SRCALPHA)
surfaces = [surface_main, surface_1, surface_2, surface_3]


draw_city_view()



"""
# surface_main
rect(surface_main, (83, 108, 103), (0, 500, 500, 300), 0)  # Ground
rect(surface_main, (255, 255, 255), (0, 495, 500, 5), 0)  # Horizont
rect(surface_main, (183, 196, 200), (0, 0, 500, 495), 0)  # Sky
ellipse(surface_main, (183, 200, 196), (-50, 650, 700, 300), 0)  # Road
ellipse(surface_main, (0, 0, 0), (185, 707, 45, 9), 0)  # Tail pipe
rect(surface_main, (0, 204, 255), (205, 670, 200, 50), 0)  # Car body 1
rect(surface_main, (0, 204, 255), (245, 645, 100, 25), 0)  # Car body 2
rect(surface_main, (255, 255, 255), (255, 652, 30, 18), 0)  # Car window 1
rect(surface_main, (255, 255, 255), (305, 652, 30, 18), 0)  # Car window 2
ellipse(surface_main, (0, 0, 0), (225, 702, 45, 30), 0)  # Car wheel 1
ellipse(surface_main, (0, 0, 0), (350, 702, 45, 30), 0)  # Car wheel 2
rect(surface_main, (219, 227, 226), (370, 20, 115, 495), 0)  # Skyscraper 3

screen.blit(surface_main, (0, 0))

# surface_0
ellipse(surface_0, (167, 167, 167, 100), (-120, 45, 450, 120), 0)  # Smog in the sky 1
screen.blit(surface_0, (0, 0))

# surface_1
ellipse(surface_1, (167, 167, 167, 100), (160, -30, 450, 120), 0)  # Smog in the sky 2
ellipse(surface_1, (167, 167, 167, 100), (-150, 370, 450, 120), 0)  # Smog in the sky 4
ellipse(surface_1, (167, 167, 167, 100), (30, 670, 160, 50), 0)  # Waste gas 1
ellipse(surface_1, (167, 167, 167, 100), (27, 605, 160, 50), 0)  # Waste gas 2
ellipse(surface_1, (167, 167, 167, 100), (-80, 540, 160, 50), 0)  # Waste gas 3
rect(surface_1, (147, 167, 172), (15, 20, 100, 495), 0)  # Skyscraper 1
rect(surface_1, (147, 172, 167), (140, 40, 100, 490), 0)  # Skyscraper 2
rect(surface_1, (183, 200, 196), (90, 80, 115, 495), 0)  # Skyscraper 4
rect(surface_1, (111, 145, 138), (335, 100, 115, 495), 0)  # Skyscraper 5
screen.blit(surface_1, (0, 0))

# surface_2
ellipse(surface_2, (167, 167, 167, 100), (120, 200, 450, 120), 0)  # Smog in the sky 3
screen.blit(surface_2, (0, 0))
"""
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
