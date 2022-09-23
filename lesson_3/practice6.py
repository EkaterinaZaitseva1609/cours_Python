# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;

#Решение через встроенную функцию eval

# print(eval('1-2*3'))


#Решение через циклы

# def calculator(task):
#     # solution = 0
#     res = 0
#     str_1 = task.split()
#     print(str_1, type(str_1))
#     while str_1.__contains__('*') or str_1.__contains__('/'):
#         for i in range(len(str_1)):
#             if str_1[i] == '*' or str_1[i] == '/':
#                 a = float(str_1[i-1])
#                 b = float(str_1[i + 1])
#                 if str_1[i] == '*':
#                     solution = a * b
#                 else:
#                     solution = a / b
#                 str_1.pop(i-1)
#                 str_1.pop(i - 1)
#                 str_1[i-1] = str(solution)
#                 break
#     while len(str_1) > 1:
#         for i in range(len(str_1)):
#             if str_1[i] == '+' or str_1[i] == '-':
#                 c = float(str_1[i-1])
#                 d = float(str_1[i + 1])
#                 if str_1[i] == '+':
#                     solution = c + d
#                 else:
#                     solution = c - d
#                 str_1.pop(i-1)
#                 str_1.pop(i - 1)
#                 str_1[i-1] = str(solution)
#                 break
#     return str_1
#
#
# task = input("напишите математическое выражение")
# res = calculator(task)
# print(f'=> {res}')

# string = '1 + 2 * 3'.split()
# for i in range(len(string)):
#     if string[i].isdigit():
#        string[i] = int(string[i])


# index = -1
# if '*' in string or '/' in string:
#     tmp = 0


# С ИСПОЛЬЗОВАНИЕМ lambda

# def calculator(task):
#     op_1 = {'+': lambda x, y: x + y,
#             '-': lambda x, y: x - y}
#     op_2 = {'*': lambda x, y: x * y,
#             '/': lambda x, y: x / y}
#
#     solution = 0
#     res = 0
#     str_1 = task.split()
#     print(str_1, type(str_1))
#     while str_1.__contains__('*') or str_1.__contains__('/'):
#         for i in range(len(str_1)):
#             if str_1[i] in op_2:
#                 a = float(str_1[i-1])
#                 b = float(str_1[i + 1])
#                 solution = op_2[str_1[i]](a, b)
#                 str_1.pop(i-1)
#                 str_1.pop(i - 1)
#                 str_1[i-1] = str(solution)
#                 break
#     while len(str_1) > 1:
#         for i in range(len(str_1)):
#             if str_1[i] in op_1:
#                 c = float(str_1[i-1])
#                 d = float(str_1[i + 1])
#                 solution = op_1[str_1[i]](c, d)
#                 str_1.pop(i-1)
#                 str_1.pop(i - 1)
#                 str_1[i-1] = str(solution)
#                 break
#     return str_1
#
#
# task = input("напишите математическое выражение")
# res = calculator(task)
# print(f'=> {res}')

# Как быстро перевести строки в целые числа
# 1. через функцию map
# a = ['456', '76', '8']
# b = list(map(int, a))
# print(b)

# 2. через лист комперхешен, если не только числа в строке даны
# a = ['456', 'bhg', '76', 'g', '8']
# a = [int(item) for item in a if item.isdigit()]
# print(a)

# 3.или так
# a = ['456', '+', '76', '*', '8']
# a = list(map(lambda x: int(x) if x.isdigit() else x, a))
# print(a)


# 2. Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.
#
# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# def getUnicList(list_1):
#     res = []
#     for elem in list_1:
#        if list_1.count(elem) == 1:
#           res.append(elem)
#     print(res)
#
#
# list_1 = [1, 2, 3, 5, 1, 5, 3, 10]
# getUnicList(list_1)
#
# через генератор строк
# list_1 = [1, 2, 3, 5, 1, 5, 3, 10]
# a = [elem for elem in list_1 if list_1.count(elem) == 1]
# print(a)

#  через filter
list_1 = [1, 2, 3, 5, 1, 5, 3, 10]
a = list(filter(lambda x: list_1.count(x)==1, list_1))
print(a)