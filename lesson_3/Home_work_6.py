# Задача: предложить улучшения кода для уже решённых задач (3-5 задач):
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
import math
from functools import reduce
from random import randint

# 1. (лямбда и list comprehension) (задание из 2 семинара) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

# n = input().replace(".", "")
# res = 0
# n = [int(i) for i in n]
# res = reduce(lambda a, b: a + b, n)
# print(res)

# 2. (map) Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# def getConvert (n):
#     res = ''
#     while n > 0:
#         res = str(n % 2) + res
#         n = n // 2
#     return res
#
# list_1 = [1, 10, 20]
# list_2 = list(map(getConvert, list_1))
# print(list_2)


# 3. (list comprehension) Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

# list_1 = [1, 1, 2, 3, 4, 5, 5]
# a = [elem for elem in list_1 if list_1.count(elem) == 1]
# print(a)

#4.(map) Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

# def getMod(a):
#     return math.modf(a)[0]
#
# def get_difference(list_3):
#     min_fract = list_3[0]
#     max_fract = list_3[0]
#     min_fract = min(list_3)
#     max_fract = max(list_3)
#
#     print(round(max_fract - min_fract, 2))
#
# list_3 = [1.1, 1.2, 3.1, 10.01]
# res_list = list(map(getMod, list_3))
# get_difference(res_list)

 # 5. (filter) Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def f(list_2):
    x = list_2[0]
    y = list_2[1]
    z = list_2[2]
    return (not(x and y and z)) == (not x or not y or not z)


list_1 = [[0, 0, 0],
          [0, 0, 1],
          [0, 1, 0],
          [0, 1, 1],
          [1, 0, 0],
          [1, 0, 1],
          [1, 1, 0],
          [1, 1, 1]]
list_2 = list(filter(f, list_1))
print(f'{len(list_1)} == {len(list_2)}')




