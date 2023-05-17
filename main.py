# import pygame
# from random import randint
# from copy import deepcopy
# import math
#
#
# RES = WIDTH, HEIGHT = 1500, 700
# TILE = 5
# W, H = WIDTH // TILE, HEIGHT // TILE
# FPS = 30
#
#
# pygame.init()
# surface = pygame.display.set_mode(RES)
# clock = pygame.time.Clock()
#
#
# class Node:
#     def __init__(self, food, life, age):
#         self.food = food
#         self.life = life
#         self.age = age
#
#
# next_field = [[Node(0, 0, 0) for i in range(W + 1)] for j in range(H + 1)]  # массив для следующего состояния
#
#
# # Разные варианты заполнения поля, текущий массив:
# # current_field = [[0 for i in range(W)] for j in range(H)] # пустое поле
# # current_field = [[1 if i == W // 2 or j == H // 2 else 0 for i in range(W)] for j in range(H)]
# # current_field = [[1 if not i % 9 else 0 for i in range(W)] for j in range(H)] # 2,5,8,9,10,11,13,18,21,22,26,30,33,65
# # current_field = [[1 if not (2 * i + j) % 4 else 0 for i in range(W + 1)] for j in range(H + 1)] # (2,4),(4,4)
# # current_field = [[1 if not (i * j) % 22 else 0 for i in range(W)] for j in range(H)] # 5,6,9,22,33
# # current_field = [[1 if not i % 7 else randint(0, 1) for i in range(W)] for j in range(H)]
#
# current_field = [[Node(0, 0, 0) for w in range(W + 1)] for h in range(H + 1)]
#
# # Заполнение массива начальными состояниями:
# for i in range(W + 1):
#     for j in range(H + 1):
#         current_field[j][i].life = randint(0, 1)
#         next_field[j][i].food = randint(60, 80)
#         next_field[j][i].age = 1
#
#
#
# def check_cell(current_field, x, y):
#     # # Коэфициенты сохраненния:
#     # k11 = 3
#     # k12 = 2
#     # # Коэфициенты зарождения:
#     # k21 = 2
#     # k22 = 1
#     # # Границы сохранение:
#     # min_save = 6
#     # max_save = 10
#     # # Границы зарождение:
#     # min_born = 7
#     # max_born = 9
#
#     # # Коэфициенты сохраненния:
#     # k11 = 6
#     # k12 = 3
#     # # Коэфициенты зарождения:
#     # k21 = 5
#     # k22 = 2
#     # # Границы сохранение:
#     # min_save = 7
#     # max_save = 14
#     # # Границы зарождение:
#     # min_born = 9
#     # max_born = 13
#     # # Условия для еды:
#     # how_to_eat = 6
#     # increasing_food = 1
#
#     # При увеличении всего в 10 раз, надо увеличить начальное количество еды тоже в 10 раз
#     # Коэфициенты сохраненния:
#     k11 = 60
#     k12 = 30
#     # Коэфициенты зарождения:
#     k21 = 50
#     k22 = 20
#     # Границы сохранение:
#     min_save = 70
#     max_save = 140
#     # Границы зарождение:
#     min_born = 90
#     max_born = 130
#     # Условия для еды:
#     how_to_eat = 25
#     increasing_food = 3
#     # Условия для возраста:
#     max_live = 1000
#
#     count_save = 0
#     count_born = 0
#     for j in range(y - 2, y + 3):
#         for i in range(x - 2, x + 3):
#             if current_field[j][i].life == 1 and math.sqrt(((j - y) ** 2) + ((i - x) ** 2)) <= math.sqrt(2):
#                 count_save += k11
#                 count_born += k21
#             elif current_field[j][i].life == 1 and math.sqrt(((j - y) ** 2) + ((i - x) ** 2)) > math.sqrt(2):
#                 count_save += k12
#                 count_born += k22
#
#     if current_field[y][x].life == 1:
#         count_save -= (k11 + k21) / 2
#         if min_save <= count_save <= max_save and next_field[y][x].food >= how_to_eat and next_field[y][x].age <= max_live:
#             next_field[y][x].food -= how_to_eat
#             next_field[y][x].age += 1
#             return 1
#         next_field[y][x].age = 0
#         next_field[y][x].food = increasing_food
#         return 0
#     elif current_field[y][x].life == 0:
#         if min_born <= count_born <= max_born and next_field[y][x].food >= how_to_eat:
#             next_field[y][x].age = 1
#             next_field[y][x].food -= how_to_eat
#             return 1
#         next_field[y][x].age = 0
#         next_field[y][x].food += increasing_food
#         return 0
#
#
# while True:
#     surface.fill(pygame.Color('black'))  # Закраска фона
#     for event in pygame.event.get():     # Условие выхода из программы
#         if event.type == pygame.QUIT:
#             exit()
#
#     [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
#     [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
#     # draw life
#     for x in range(1, W - 1):
#         for y in range(1, H - 1):
#             if current_field[y][x].life:
#                 pygame.draw.rect(surface, pygame.Color('orange'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
#             next_field[y][x].life = check_cell(current_field, x, y)
#
#     current_field = deepcopy(next_field)
#
#     # print(clock.get_fps())
#     pygame.display.flip()
#     clock.tick(FPS)

# import pygame
# from random import randint
# from copy import deepcopy
# import math
#
#
# def check_cell(current_field, x, y):
#     # # Коэфициенты сохраненния:
#     # k11 = 3
#     # k12 = 2
#     # # Коэфициенты зарождения:
#     # k21 = 2
#     # k22 = 1
#     # # Границы сохранение:
#     # min_save = 6
#     # max_save = 10
#     # # Границы зарождение:
#     # min_born = 7
#     # max_born = 9
#
#     # # Коэфициенты сохраненния:
#     # k11 = 6
#     # k12 = 3
#     # # Коэфициенты зарождения:
#     # k21 = 5
#     # k22 = 2
#     # # Границы сохранение:
#     # min_save = 7
#     # max_save = 14
#     # # Границы зарождение:
#     # min_born = 9
#     # max_born = 13
#     # # Условия для еды:
#     # how_to_eat = 6
#     # increasing_food = 1
#
#     # При увеличении всего в 10 раз, надо увеличить начальное количество еды тоже в 10 раз
#     # Коэфициенты сохраненния:
#     k11 = 60
#     k12 = 30
#     # Коэфициенты зарождения:
#     k21 = 50
#     k22 = 20
#     # Границы сохранение:
#     min_save = 70
#     max_save = 140
#     # Границы зарождение:
#     min_born = 90
#     max_born = 130
#     # Условия для еды:
#     how_to_eat = 25
#     increasing_food = 3
#     # Условия для возраста:
#     max_live = 1000
#
#     count_save = 0
#     count_born = 0
#     for j in range(y - 2, y + 3):
#         for i in range(x - 2, x + 3):
#             if current_field[j][i].life == 1 and math.sqrt(((j - y) ** 2) + ((i - x) ** 2)) <= math.sqrt(2):
#                 count_save += k11
#                 count_born += k21
#             elif current_field[j][i].life == 1 and math.sqrt(((j - y) ** 2) + ((i - x) ** 2)) > math.sqrt(2):
#                 count_save += k12
#                 count_born += k22
#
#     if current_field[y][x].life == 1:
#         count_save -= (k11 + k21) / 2
#         if min_save <= count_save <= max_save and next_field[y][x].food >= how_to_eat and next_field[y][x].age <= max_live:
#             next_field[y][x].food -= how_to_eat
#             next_field[y][x].age += 1
#             return 1
#         next_field[y][x].age = 0
#         next_field[y][x].food = increasing_food
#         return 0
#     elif current_field[y][x].life == 0:
#         if min_born <= count_born <= max_born and next_field[y][x].food >= how_to_eat:
#             next_field[y][x].age = 1
#             next_field[y][x].food -= how_to_eat
#             return 1
#         next_field[y][x].age = 0
#         next_field[y][x].food += increasing_food
#         return 0
#
#
# # Размеры экрана:
# RES = WIDTH, HEIGHT = 1500, 700
# TILE = 5
# W, H = WIDTH // TILE, HEIGHT // TILE
# FPS = 30
# count_of_cells = W * H
#
#
# # Структура клетки:
# class Node:
#     def __init__(self, food, life, age):
#         self.food = food
#         self.life = life
#         self.age = age
#
#
# # Создание массивовнеобходиных массивов:
# next_field = [[Node(0, 0, 0) for i in range(W + 1)] for j in range(H + 1)]
# current_field = [[Node(0, 0, 0) for w in range(W + 1)] for h in range(H + 1)]
# percent_of_ife = []  # Массив с вероятностями для определенных коэфициентов
#
# for M in range(0, 100):
#     # Инициация окна:
#     pygame.init()
#     surface = pygame.display.set_mode(RES)
#     clock = pygame.time.Clock()
#
#     # Заполнение массива начальными состояниями:
#     for i in range(W + 1):
#         for j in range(H + 1):
#             current_field[j][i].life = randint(0, 1)
#             next_field[j][i].food = randint(60, 80)
#             next_field[j][i].age = 1
#
#     # Запуск жизни по 50 итериций:
#     for N in range(0, 50):
#         surface.fill(pygame.Color('black'))  # Закраска фона
#         for event in pygame.event.get():     # Условие выхода из программы
#             if event.type == pygame.QUIT:
#                 exit()
#
#         [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
#         [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
#         # draw life
#         for x in range(1, W - 1):
#             for y in range(1, H - 1):
#                 if current_field[y][x].life:
#                     pygame.draw.rect(surface, pygame.Color('orange'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
#                 next_field[y][x].life = check_cell(current_field, x, y)
#
#         current_field = deepcopy(next_field)
#
#         # print(clock.get_fps())
#         pygame.display.flip()
#         clock.tick(FPS)
#
#     count_life = 0
#     for x in range(1, W - 1):
#         for y in range(1, H - 1):
#             if current_field[y][x].life == 1:
#                 count_life += 1
#
#     print("Количество выживших клеток -", count_life)
#     percent = count_life / count_of_cells * 100
#     percent_of_ife.append(percent)
#     print(percent_of_ife)

import pygame
import pandas as pd
from random import randint
from copy import deepcopy
import math


def check_cell(current_field, x, y, k11, k12, k21, k22, min_save, max_save, min_born, max_born, how_to_eat,
               increasing_food, max_live):
    count_save = 0
    count_born = 0
    for j in range(y - 2, y + 3):
        for i in range(x - 2, x + 3):
            if current_field[j][i].life == 1 and math.sqrt(((j - y) ** 2) + ((i - x) ** 2)) <= math.sqrt(2):
                count_save += k11
                count_born += k21
            elif current_field[j][i].life == 1 and math.sqrt(((j - y) ** 2) + ((i - x) ** 2)) > math.sqrt(2):
                count_save += k12
                count_born += k22

    if current_field[y][x].life == 1:
        count_save -= (k11 + k21) / 2
        if min_save <= count_save <= max_save and next_field[y][x].food >= how_to_eat and next_field[y][
            x].age <= max_live:
            next_field[y][x].food -= how_to_eat
            next_field[y][x].age += 1
            return 1
        next_field[y][x].age = 0
        next_field[y][x].food = increasing_food
        return 0
    elif current_field[y][x].life == 0:
        if min_born <= count_born <= max_born and next_field[y][x].food >= how_to_eat:
            next_field[y][x].age = 1
            next_field[y][x].food -= how_to_eat
            return 1
        next_field[y][x].age = 0
        next_field[y][x].food += increasing_food
        return 0


# Размеры экрана:
RES = WIDTH, HEIGHT = 1500, 700
TILE = 5
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 50
count_of_cells = W * H


# Структура клетки:
class Node:
    def __init__(self, food, life, age):
        self.food = food
        self.life = life
        self.age = age


# Создание необходимых массивов:
next_field = [[Node(0, 0, 0) for i in range(W + 1)] for j in range(H + 1)]
current_field = [[Node(0, 0, 0) for w in range(W + 1)] for h in range(H + 1)]
percent_of_life = []  # Массив с процентами для определенных коэффициентов
final_array = []  # Окончательная матрица всех процентов

# При увеличении всего в 10 раз, надо увеличить начальное количество еды тоже в 10 раз
# Коэффициенты сохранения:
k11 = 60
k12 = 30
# Коэффициенты зарождения:
k21 = 50
k22 = 20
# Границы сохранение:
min_save = 70
max_save = 140
# Границы зарождение:
min_born = 90
max_born = 130
# Условия для еды:
how_to_eat = 50
increasing_food = 2
# Условия для возраста:
max_live = 3

for next_data in range(0, 100):
    for M in range(0, 100):
        # Инициация окна:
        # pygame.init()
        # surface = pygame.display.set_mode(RES)
        # clock = pygame.time.Clock()

        # Заполнение массива начальными состояниями:
        for i in range(W + 1):
            for j in range(H + 1):
                current_field[j][i].life = randint(0, 1)
                next_field[j][i].food = randint(60, 80)
                next_field[j][i].age = 1

        # Запуск жизни по 50 итериций:
        for N in range(0, 50):
            # surface.fill(pygame.Color('black'))  # Закраска фона
            # for event in pygame.event.get():  # Условие выхода из программы
            #     if event.type == pygame.QUIT:
            #         exit()

            # [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in
            #  range(0, WIDTH, TILE)]
            # [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in
            #  range(0, HEIGHT, TILE)]
            # draw life
            for x in range(1, W - 1):
                for y in range(1, H - 1):
                    # if current_field[y][x].life:
                        # pygame.draw.rect(surface, pygame.Color('orange'),
                        #                  (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
                    next_field[y][x].life = check_cell(current_field, x, y, k11, k12, k21, k22, min_save, max_save,
                                                       min_born, max_born, how_to_eat, increasing_food, max_live)

            current_field = deepcopy(next_field)

            # print(clock.get_fps())
            # pygame.display.flip()
            # clock.tick(FPS)

        count_life = 0
        for x in range(W + 1):
            for y in range(H + 1):
                if current_field[y][x].life == 1:
                    count_life += 1

        print("Количество выживших клеток -", count_life)
        percent = count_life / count_of_cells * 100
        percent_of_life.append(percent)
        print(percent_of_life)

    tmp_array = deepcopy(percent_of_life)
    final_array.append(tmp_array)
    print("Финальный массив -", final_array)
    percent_of_life.clear()

    # Условия для еды:
    increasing_food += 1
    if next_data == 49:
        # Границы сохранение:
        min_save = 60
        max_save = 150
        # Границы зарождение:
        min_born = 100
        max_born = 130
        # Условия для еды:
        how_to_eat = 100
        # Условия для возраста:
        max_live = 5

df = pd.DataFrame(final_array)
df.to_csv("output.csv")
