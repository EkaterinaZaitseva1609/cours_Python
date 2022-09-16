# 1. Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141

# def getPi (count):
#     import math
#     pi = math.pi
#     from decimal import Decimal
#     number = Decimal(pi)
#     number = number.quantize(Decimal(count))
#     print(number)
#
# count = (input('Введите кол-во нулей после запятой в числе пи'))
# getPi(count)

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

# def getRes(n):
#     while n > 1:
#         min = 2
#         f = 0
#         while 1:
#             if n % min == 0:
#                 n = n // min
#                 print(min, end=' ')
#                 f = 1
#                 break
#             else:
#                 min += 1
#         if f == 1:
#             continue
#     print()
#
#
# n = int(input('Задайте натуральное число N'))
# getRes(n)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]


# def getUnicList(list_1):
#     res = []
#     for elem in list_1:
#        if list_1.count(elem) == 1:
#           res.append(elem)
#     print(res)
#
#
# list_1 = [1, 1, 2, 3, 4, 5, 5]
# getUnicList(list_1)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
#
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# def getDegree(degree):
#     import random
#     print('k =', degree, '=> ', end = '')
#     res = 0
#     for i in reversed(range(0, degree + 1)):
#         num = random.randint(0, 1)
#         if num == 0:
#             continue
#         if i == 0:
#             print(num, end = '')
#         else:
#             print(num, '*x^',i, end = ' + ')
#     print(' = 0')
#
#
# degree = int(input('введите натуральную степень числа'))
# getDegree(degree)

# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

m1 = '2*x^2+4*x+5'
m2 = '2*x^3+4*x^2+5*x+6'

s_1 = m1.replace('*', '').replace('^', '')
print(s_1)
s_2 = m2.replace('*', '').replace('^', '')
print(s_2)

list1 = s_1.split('+')
for (index, _) in enumerate(list1):
    if list1[index][-1] == 'x':
        list1[index] += '1'
#     elif 'x' not in list1[index]:
#         list1[index] + 'x0'
print(list1)


list2 = s_2.split('+')
for (index, _) in enumerate(list2):
    if list2[index][-1] == 'x':
        list2[index] += '1'
print(list2)

if len(list1) > len(list2):
    max_len = len(list1)
    min_len = len(list2)
else:
    max_len = len(list2)
    min_len = len(list1)
    # print(max_len)
    # print(list1[0][0], list2[0][0])

for i in range(0, max_len):
    for j in range(0, min_len):
      if list1[i][-1] == list2[j][-1]:
          print(list1[i][-1])
          print(list2[j][-1])
          print('*****')
          res = int(list1[i][0]) + int(list2[j][0])
    print(res)


# print(list1, list2)


# data = open('home_work_4.txt', 'a')
# data.writelines('m1 =  [2*x² + 4*x + 5] \n')
# data.write('m2 = [2*x3 + 4*x2 + 5*x1 + 6]')
# data.close()
# path = 'home_work_4.txt'
# data = open(path, 'r')
