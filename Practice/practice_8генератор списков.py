# [выражение for val(переменная) in коллекция]
# a = [] начало и конец генератора
# a = [i%4 for i in range(1, 15)]
# print(a)

# a = [i for i in 'hello']
# print(a)

# a = [i*2 for i in 'hello']
# print(a)

import random

# внутри выражения можно использовать и другие функции
# a = [random.randint(-10, 10) for i in range(10)]
# print(a)
# b = [abs(elem) for elem in a]
# print(b)

# При помощи генераторов можно изменять элементы списка
# a = [random.randint(-10, 10) for i in range(10)]
# print(a)
# a = [elem+1 for elem in a]
# print(a)

# В генераторах списка можно использовать условные конструкции
# [выражение for val(переменная) in коллекция if условия]
# a = [random.randint(-10, 10) for i in range(10)]
# print(a)
# a = [elem for elem in a if elem % 2 == 0]
# print(a)


# a = [random.randint(-10, 10) for i in range(10)]
# print(a)
# a = [elem for elem in a if elem % 2 == 0 or elem % 3 == 0]
# print(a)

# Преобразовать эелементы списка к целым числам

# n = input().split()
# n = [int(i) for i in n]
# print(n)

#Инициализация двумерного списка (матрицы)
# n = 5
# m = 4
# a = [[1]* m for i in range(n)]
# for i in a:
#     print(i)

# В генераторах цикла можно использовать двойные циклы
# a = [(i, j) for i in 'abc' for j in [1, 2, 3]]
# print(a)


# a = [i* j for i in [2, 3, 4, 5] for j in [1, 2, 3] if i* j>10]
# print(a)

# что сделать с элементом, с каким элементом и при каком условии
list_1 = [1, 2, 3, 4, 5, 5, 2]
res = [item for item in list_1 if list_1.count(item)==1]
print(res)