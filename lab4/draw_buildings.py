import random as r
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
width_display = 500
height_display = 800
horizont_height = 5
screen = pygame.display.set_mode((width_display, height_display))
surface_main = pygame.Surface((width_display, height_display), pygame.SRCALPHA)
surface_1 = pygame.Surface((width_display, height_display), pygame.SRCALPHA)
surface_0 = pygame.Surface((width_display, height_display), pygame.SRCALPHA)
surface_2 = pygame.Surface((width_display, height_display), pygame.SRCALPHA)
color_dict_skyscraper = {
                "dim grey": "105, 105, 105",
                "grey": "128, 128, 128",
                "dark grey": "169, 169, 169",
                "silver": "192, 192, 192",
                "light grey": "211, 211, 211",
                "color_1": "147,167,172",
                "color_2": "147,172,167",
                "color_3": "183,200,196",
                "color_4": "111,145,138"
             }
color_dict_car = {
                "gainsboro": "220, 220, 220",
                "Red": "255, 0, 0",
                "Lime": "0, 255, 0",
                "Blue": "0, 0, 255",
                "Yellow": "255, 255, 0",
                "Cyan": "0, 255, 255",
                "Magenta": "255, 0, 255"
                }
def draw_city(q_skyscrapers, q_cars):
    '''
    Draw city with q_skyscrapers skyscrapers and q_cars cars
    :param q_skyscrapers: quantity of skyscrapers
    :param q_cars:  quantity of cars
    :return: none
    '''
    rect(surface_main, (83, 108, 103), (0, 0.625 * height_display, width_display, 0.375 * height_display), 0)  # Ground
    rect(surface_main, (255, 255, 255), (0, 0.625 * height_display - horizont_height, width_display, horizont_height), 0)  # Horizont
    rect(surface_main, (183, 196, 200), (0, 0, width_display, 0.625 * height_display - horizont_height), 0)  # Sky

    for i in range(q_skyscrapers):
        skyscraper_coordinate_x = r.randint(15, width_display - 130)
        skyscraper_coordinate_y = r.randint(20, 100)
        color_list = list(color_dict_skyscraper.keys())
        color_var = color_list[r.randint(0, len(color_list) - 1)]
        skyscraper_color = list(map(int, (color_dict_skyscraper[color_var].split(","))))
        draw_skyscraper(skyscraper_coordinate_x, skyscraper_coordinate_y, 1, 1, skyscraper_color)
    for i in range(q_cars):
        car_coordinate_x = r.randint(0, width_display)
        car_coordinate_y = r.randint(int(.625 * height_display), height_display)
        color_list = list(color_dict_car.keys())
        color_var = color_list[r.randint(0, len(color_list) - 1)]
        car_color = list(map(int, (color_dict_car[color_var].split(","))))
        draw_car(car_coordinate_x, car_coordinate_y, 1, 1, 1, car_color)

    print(f"Рисую город с {q_skyscrapers} небоскребами и {q_cars} машинами")



def draw_car(car_coordinate_x, car_coordinate_y, car_width, car_height, car_orientation, car_color):
    '''
    Draw a car with parameters below
    :param car_coordinate_x: coordinate x of left up extreme point
    :param car_coordinate_y: coordinate y of left up extreme point
    :param car_width: width from left up extreme point to right
    :param car_height: height from up extreme point to bottom extreme point
    :param car_orientation: orientation of car from left to right or from right to left
    :param car_color: color of car

    :return:
    '''

    ellipse(surface_main, (0, 0, 0), (car_coordinate_x, car_coordinate_y+62, 45, 9), 0)  # Tail pipe
    rect(surface_main, (car_color), (car_coordinate_x+20, car_coordinate_y+25, 200, 50), 0)  # Car body 1
    rect(surface_main, (car_color), (car_coordinate_x+60, car_coordinate_y, 100, 25), 0)  # Car body 2
    rect(surface_main, (255, 255, 255), (car_coordinate_x+70, car_coordinate_y+7, 30, 18), 0)  # Car window 1
    rect(surface_main, (255, 255, 255), (car_coordinate_x+120, car_coordinate_y+7, 30, 18), 0)  # Car window 2
    ellipse(surface_main, (0, 0, 0), (car_coordinate_x+40, car_coordinate_y+57, 45, 30), 0)  # Car wheel 1
    ellipse(surface_main, (0, 0, 0), (car_coordinate_x+165, car_coordinate_y+57, 45, 30), 0)  # Car wheel 2


    print(f"Рисую машину с параметрами {car_coordinate_x, car_coordinate_y, car_width, car_height, car_orientation, car_color}")

def draw_skyscraper(skyscraper_coordinate_x, skyscraper_coordinate_y, skyscraper_width, skyscraper_height, skyscraper_color):
    '''
    Draw a skyscraper with parameters below
    :param skyscraper_coordinate_x: coordinate x of left up extreme point
    :param skyscraper_coordinate_y: coordinate y of left up extreme point
    :param skyscraper_width: width from left up extreme point to right
    :param skyscraper_height: height from up extreme point to bottom extreme point
    :param skyscraper_color: color of skyscraper
    :return:
    '''

    rect(surface_1, skyscraper_color, (skyscraper_coordinate_x, skyscraper_coordinate_y, 100, 495), 0)  # Skyscraper 1

    print(f"Рисую небоскреб с параметрами {skyscraper_coordinate_x, skyscraper_coordinate_y, skyscraper_width, skyscraper_height, skyscraper_color}")

draw_city(5, 1)



#surface_main

#(surface_main, (183, 200, 196), (-50,650, 700, 300), 0) # Road

#rect(surface_main, (219,227,226), (370, 20 , 115, 495), 0) # Skyscraper 3
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

#rect(surface_1, (147,172,167), (140, 40 , 100, 490), 0) # Skyscraper 2
#rect(surface_1, (183,200,196), (90, 80 , 115, 495), 0) # Skyscraper 4
#rect(surface_1, (111,145,138), (335, 100 , 115, 495), 0) # Skyscraper 5
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
