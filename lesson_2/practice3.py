# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

from time import time


# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['65h34q', 'sdg634d', '147jnbv']
# "7"
# 1. Найти числа в списке

# list_1 = input()
# numbers = []
# # n = int(input('Введите число'))
# num = ''
# for numb in list_1:
#     if numb.isdigit():
#         numbers.append(int(numb))
# print(numbers)
#
# # 2. Сравнить числа с n
# n = int(input('Введите число'))
#
# for i in numbers:
#     if n == i:
#         print(i)
#     else:
#         print(False)

# другой вариант решения

# my_list = ['65h34q', 'sdg634d', '147jnbv']
# n = '4'
# for i in my_list:
#     if i.find(n) >= 0:
#         print(i)
#     else:
#         print(False)


# 3. Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.

# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# list_1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# str_1 = "йцу"
# ind = list_1.index(str_1, 1)
# print(ind)

# list_1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# str_1 = "123"
# count = 0
# r = range(0, len(list_1))
# for i in r:
#     if list_1[i] == str_1:
#         count += 1
#         if count == 2:
#             print(i)
#             break
# else:
#     print('-1')




