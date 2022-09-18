# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 4 5

# data = open('1Task.txt', 'r')
# n_list_str = data.read()
# list_1 = n_list_str.split(' ')
# numb_list = [int(x) for x in list_1]
# print(numb_list)

# for i in range (1, len(numb_list)):
#     if numb_list[i] - 1 != numb_list[i-1]:
#         number = numb_list[i] - 1
#         print(number)


# numb_list = [int(list_1[i])-1 for i in range(1, len(list_1)) if int(list_1[i]) - 1 != int(list_1[i-1])]
# print(f' index = {list_1} = {numb_list}')

# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.
# data = open('2Task.txt', 'r')
# list_str = data.read()
# list_2 = list_str.split(',')
#
# list_numb = [int(x) for x in list_2]
# print(list_numb)
#
# max = list_numb[0]
# max_list = []
# max_list.append(max)
# for i in range(len(list_numb)):
#     if max < list_numb[i]:
#         max = list_numb[i]
#         max_list.append(max)
# print(max_list)

4
# my_list = [1, 5, 2, 3, 4, 6, 1, 7]
# count = 0
# new_list = [my_list[i] for i in range (1, len(my_list)) if my_list[i] > max(my_list[0:i])]
# new_list.insert(0, my_list[0])
# print(new_list)

# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавабв'
# 'Мы очень любим Питон'

str_1 = 'Мы неабв очень любим Питон иабв Джавабв'
str_2 = "абв"
list_3 = str_1.split(' ')
print(list_3)
# for elem in list_3:
#     if not str_2 in elem:
#         print(elem, end=' ')

list_res = [item for item in list_3 if str_2 not in item]
print(list_res)


#!!!! библиотека sympy