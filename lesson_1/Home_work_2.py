# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

# n = input('Введите число N')
# x = n.replace(".", "")
# res = 0
# for i in x:
#     res += int(i)
# print(f'{n} -> {res}')

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите число N'))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
#     print(factorial, end=', ')
#

# 3. Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.
# k = 5
# a = [(1 + 1 / i) ** i for i in range(1, k + 1)]
# my_rounded_list = [round(elem, 2) for elem in a]
# print(my_rounded_list)

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# n = int(input("Введите размер списка: "))
# res = list(range(-n, n + 1))
# print(res)
#
# k = (input('Укажите позици элементов через пробел'))
# elements = (k.split(" "))
# result = 1
# for (i) in elements:
#     result *= (res[int(i) - 1])
# print(result)

#5 Реализуйте алгоритм перемешивания списка.

import random
rand_list = ['апельсин', 'банан', 'виноград', 'груша', 'дыня']
random.shuffle(rand_list)
print(rand_list)

