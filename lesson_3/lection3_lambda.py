#Анонимные, lambda функции

#********************************************************
#List Comprehension (понимание)
# [exp for item in iterable]
    # [exp for item in iterable (if conditional)]

# list = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         list.append(i)
# print(list)

# list = [i for i in range(1, 21)] #эта запись равна двум строкам ниже:
# list = []
# for i in range(1, 21):
# list = [i for i in range(1, 21) if i % 2 == 0] #данна строка равна строкам ниже
# print(list)
# вот этим:
# list = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         list.append(i)
# print(list)

##############################################
# path = 'file_3.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()
#
# numbers = []
#
# while data != ' ':
#     space_pos = data.index(' ')
#     numbers.append(int(data[: space_pos]))
#     data = data[space_pos + 1]
#
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e,e**2))
# print(out)

#######################################################
# def select(f, col):
#     return [f(x) for x in col]
#
# def  where (f, col):
#     return [x for x in col if f(x)]
#
# data = '1 2 3 5 8 15 23 38'.split()
#
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

#********************************************************
#Функция map()
#функция map() применяет указанную функцию к каждому элемнту итерируемого объекта и
#возвращает итератор с новыми объектами
# f(x) => x + 10
# map(f,[1, 2, 3, 4, 5])
#     [11, 12, 13, 14, 15]
# Нельзя пройтись дважды

# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x + 10, li))
# print(li)

#*******************************************************
#Функция filter
# применяет указанную функцию к каждому элементу итерируемого объекта
# и возвращает итератор с теми объектами, для которых функция вернула True

# f(x) => x - четное
#filter (f, [1, 2, 3, 4, 5])
          # [   2,    4    ]

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x%2, data))
# print(res)
#*******************************************************
#Функция zip
# применяется к набору итерируемых объектов
#и возвращает итератор с кортежами из элементов входных данных
# users = ['users1', 'users2', 'users3', 'users4', 'users5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data)
#*******************************************************
#Функция enumerate
#позволяет передать на вход какой-то набор данных, на выходе получаем  кортежи с пронумерованными элементами

users = ['users1', 'users2', 'users3', 'users4', 'users5']
data = list(enumerate(users))
print(data) # в консоли [(0, 'users1'), (1, 'users2'), (2, 'users3'), (3, 'users4'), (4, 'users5')]




