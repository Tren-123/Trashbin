import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
count = 0
screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
coordinate_x = 15  # Координата x смещения шарика
coordinate_y = 15  # Координата y смещения шарика
NORTH = 0, -coordinate_y
SOUTH = 0, coordinate_y
EAST = -coordinate_x, 0
WEST = coordinate_x, 0
NORTH_WEST = coordinate_x, -coordinate_y
NORTH_EAST = -coordinate_x, -coordinate_y
SOUTH_WEST = coordinate_x, coordinate_y
SOUTH_EAST = -coordinate_x, coordinate_y
DIRECTIONS = [NORTH, EAST, NORTH_EAST, NORTH_WEST, SOUTH, WEST, SOUTH_WEST, SOUTH_EAST]

def new_ball_one():
    """рисует новый шарик №1 """
    global x, y, r, color, direction
    x = randint(100, 1100)
    y = randint(100, 800)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    direction = DIRECTIONS[randint(0, 7)]


def new_ball_two():
    """рисует новый шарик №2 """
    global x1, y1, r1, color1, direction1
    x1 = randint(100, 1100)
    y1 = randint(100, 800)
    r1 = randint(10, 100)
    color1 = COLORS[randint(0, 5)]
    circle(screen, color1, (x1, y1), r1)
    direction1 = DIRECTIONS[randint(0, 7)]


def ball_motion_one_1():
    """перемещает шарик №1 в рандомном направлении от точки появления до ударения в край экрана"""
    global x, y
    x += direction[0]
    y += direction[1]
    circle(screen, color, (x, y), r)


def ball_motion_two_1():
    """перемещает шарик  №2 в рандомном направлении от точки появления до ударения в край экрана"""
    global x1, y1
    x1 += direction1[0]
    y1 += direction1[1]
    circle(screen, color1, (x1, y1), r1)

def ball_motion_one_2():
    """после ударения края экрана рандомно меняет направление движения шарика №1"""
    global x, y
    x += direction[0]
    y += direction[1]
    circle(screen, color, (x, y), r)


def ball_motion_two_2():
    """после ударения края экрана рандомно меняет направление движения шарика №2"""
    global x1, y1
    x1 += direction1[0]
    y1 += direction1[1]
    circle(screen, color1, (x1, y1), r1)


def ball_motion_main_one():
    """
    проверяет коснулся ли шарик №1 края экрана. Если нет, двигает шарик по изначальному направлению
    если да, то выбирает другое рандомное направление
    если шарик ушел за край экрана полностью - удалет его и создает новый шарик
    """
    if screen_width - r > x - r > 0 and screen_height - r > y - r > 0:
        ball_motion_one_1()
    elif x < -r or y < -r:
        new_ball_one()
    elif x > screen_width + r or y > screen_height + r:
        new_ball_one()
    else:
        global direction
        direction = DIRECTIONS[randint(0, 7)]
        ball_motion_one_2()


def ball_motion_main_two():
    """
    проверяет коснулся ли шарик №2 края экрана. Если нет, двигает шарик по изначальному направлению
    если да, то выбирает другое рандомное направление
    если шарик ушел за край экрана полностью - удалет его и создает новый шарик
    """
    if screen_width - r1 > x1 - r1 > 0 and screen_height - r1 > y1 - r1 > 0:
        ball_motion_two_1()
    elif x1 < -r1 or y1 < -r1:
        new_ball_two()
    elif x1 > screen_width + r1 or y1 > screen_height + r1:
        new_ball_two()
    else:
        global direction1
        direction1 = DIRECTIONS[randint(0, 7)]
        ball_motion_two_2()

def click(event):
    """проверяет расстояние от точки клика до шарика, если клик в тело шарика, то засчитывает попадание
       считает попадание, и прибавляет за каждое попадание 50 очков к глобальному результату
       за каждый промах отнимает 100 очков
    """
    try:
        global count
        if ((event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2) ** 0.5 > r \
                and ((event.pos[0] - x1) ** 2 + (event.pos[1] - y1) ** 2) ** 0.5 > r1:
            count -= 100
            print(f"Miss! HA-HA! Your score {count}")  # Фраза при промахе
        else:
            count += 50
            print(f"Ouch! You done me! Your score {count}")  # Фраза при попадании
    except NameError:
        print("False start, wait for the circle!!!")  # Фраза при клике до появления первого шарика



pygame.display.update()
clock = pygame.time.Clock()
finished = False
new_ball_one()
new_ball_two()
screen.fill(BLACK)
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    ball_motion_main_one()
    ball_motion_main_two()
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
