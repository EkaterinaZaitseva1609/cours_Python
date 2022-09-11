#1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12
import math
from cgitb import reset


# def getSum (list_1):
#     sum = 0
#     r = range(0, len(list_1))
#     for i in r:
#         if i % 2 != 0:
#             sum += list_1[i]
#     print(sum)
#
#
# list_1 = [2, 3, 5, 9, 3]
# getSum(list_1)


# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def getRes (list_2):
#     res = []
#     is_dev = len(list_2) % 2 != 0
#     size = int(len(list_2))
#     stop_2 = int(len(list_2) // 2)
#     for i in range(0, stop_2):
#         res.append(list_2[i] * list_2[size-i - 1])
#     if is_dev:
#         res.append(list_2[stop_2] ** 2)
#     print(res)
#
# list_2 = [2, 3, 5, 6]
# getRes(list_2)

#3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

# def get_difference(list_3):
#     min_fract = list_3[0]
#     max_fract = list_3[0]
#     fraction = [math.modf(i)[0] for i in list_3]
#     min_fract = min(fraction)
#     max_fract = max(fraction)
#
#     print(round(max_fract - min_fract, 2))
#
# list_3 = [1.1, 1.2, 3.1, 10.01]
# get_difference(list_3)

# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# def getConvert (n):
#     res = ''
#     while n > 0:
#         res = str(n % 2) + res
#         n = n // 2
#     print(res)
#
#
# n = int(input('введите число'))
# getConvert(n)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def getFib (n):
    list_poz = []
    list_neg = []
    list_res = []
    fib1 = fib2 = 1
    list_poz.append(0)
    list_poz.append(fib1)
    list_poz.append(fib2)
    i = 2
    while i < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1
        list_poz.append(fib_sum)
    list_neg = list(reversed(list_poz))
    for i in range (0, len(list_poz), 2):
        list_neg[i] = -list_neg[i]
    list_poz.pop(0)
    list_res.extend(list_neg)
    list_res.extend(list_poz)
    print(list_res)


n = int(input('введите число'))
getFib(n)




