import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
count = 0
game_count = FPS * 5
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


def new_polygon():
    """рисует новый треугольник"""
    global color2, x_1_poly, x_2_poly, x_3_poly, y_1_poly, y_2_poly,\
        y_3_poly, rad_poly, x_centr_poly, y_centr_poly, direction2
    x_1_poly = randint(100, 1100)  # Координата х верхней левой точки треугольника
    y_1_poly = randint(-200, -100)  # Координата у верхней левой точки треугольника
    x_2_poly = x_1_poly + 70  # Координата х верхней правой точки треугольника
    y_2_poly = y_1_poly  # Координата у верхней правой точки треугольника
    x_3_poly = x_1_poly + 35  # Координата х нижней точки треугольника
    y_3_poly = y_1_poly + 70  # Координата у нижней точки треугольника
    rad_poly = (70 ** 2 - 35 ** 2) ** 0.5*2/3  # Радиус описанной окружности вокруг треугольника
    x_centr_poly = x_1_poly + 35  # Координата х центра описанной окружности вокруг треугольника
    y_centr_poly = y_1_poly + rad_poly/2  # Координата у центра описанной окружности вокруг треугольника
    color2 = COLORS[randint(0, 5)]
    polygon(screen, color2, ((x_1_poly, y_1_poly), (x_2_poly, y_2_poly), (x_3_poly, y_3_poly)))
    direction2 = DIRECTIONS[randint(4, 7)]

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


def polygon_motion():
    """"описывает движение многоугольника сверху вниз из-за верхнего края экрана"""
    global x_1_poly, y_1_poly, x_centr_poly, y_centr_poly
    if screen_width > x_1_poly > 0 and screen_height > y_1_poly > -300:
        x_1_poly += direction2[0]
        y_1_poly += direction2[1]
        x_2_poly = x_1_poly + 70
        y_2_poly = y_1_poly
        x_3_poly = x_1_poly + 35
        y_3_poly = y_1_poly + 70
        x_centr_poly += direction2[0]
        y_centr_poly += direction2[1]
        polygon(screen, color2, ((x_1_poly, y_1_poly), (x_2_poly, y_2_poly), (x_3_poly, y_3_poly)))
    else:
        new_polygon()


def click(event):
    """проверяет расстояние от точки клика до шарика, если клик в тело шарика, то засчитывает попадание
       считает попадание, и прибавляет за каждое попадание 50 очков к глобальному результату
       за каждый промах отнимает 100 очков
    """
    try:
        global count
        if ((event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2) ** 0.5 > r \
                and ((event.pos[0] - x1) ** 2 + (event.pos[1] - y1) ** 2) ** 0.5 > r1 \
                and ((event.pos[0] - x_centr_poly) ** 2 + (event.pos[1] - y_centr_poly) ** 2) ** 0.5 > rad_poly:
            count -= 100
            print(f"Miss! HA-HA! Your score: {count}")  # Фраза при промахе
        elif ((event.pos[0] - x_centr_poly) ** 2 + (event.pos[1] - y_centr_poly) ** 2) ** 0.5 < rad_poly:
            count += 100
            print(f"Ouch! You score THE SUPER SHAPE! Your score: {count}")  # Фраза при попадании в треугольник
        else:
            count += 50
            print(f"Not bad. You score the regular one! Your score: {count}")  # Фраза при попадании в круг
    except NameError:
        print("False start, wait for the shape!!!")  # Фраза при клике до появления первого шарика


def update_leadrs_list(gamer_name):
    """
    Печатает результат и имя игрока в файл <leaders_list> в формате <score>:<gamer_name>
    Сортирует список от наибольшего количества очков к меньшему
    :param gamer_name:
    :return:
    """
    with open("leaders_list.txt", "a") as f:
        print(count, ":", gamer_name, sep='', file=f)
    with open("leaders_list.txt", "r+") as f:
        list_of_gamers = []
        for line in f:
            list_of_gamers.append(line.rstrip())
    list_of_gamers_1 = []
    for element in list_of_gamers:
        element = element.split(":")
        list_of_gamers_1.append(element)
    list_of_gamers_1.sort(reverse=True)
    list_of_gamers_2 = []
    for element in list_of_gamers_1:
        list_of_gamers_2.append(element)
    with open("leaders_list.txt", "w") as f:
        pass
    with open("leaders_list.txt", "a") as f:
        for element in list_of_gamers_2:
            f.write(element[0])
            f.write(":")
            f.write(element[1])
            f.write("\n")


pygame.display.update()
clock = pygame.time.Clock()
finished = False
new_ball_one()
new_ball_two()
new_polygon()
screen.fill(BLACK)
while not finished and game_count != 0:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    ball_motion_main_one()
    ball_motion_main_two()
    polygon_motion()
    pygame.display.update()
    screen.fill(BLACK)
    game_count -= 1
if finished:
    pygame.quit()
else:
    print(f"\nGAME OTHER! Your final score: {count}")
    print("Please write your name to save results:")
    gamer_name = input()
    update_leadrs_list(gamer_name)
    pygame.quit()
