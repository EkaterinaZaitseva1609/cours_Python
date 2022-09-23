# Функция map(func, *iterables) принимает функцию и итерабельную последовательность (списки, кортежи, словари, функция range, строки и т.д.)
# результатом функции map будет объект этого типа = map object
# он представляет собой итератор, который вычисляет результат работы функции, которую мы передали
# на каждый аргумент из этой последовательности

# например есть список а
# a = [-1, 2, -3, 4, 5]
# b = map(abs, a) #map в которую передаем функцию abc (она возвращает модуль числа = отбрасывает знаки и все числа становятся положительными), второй параметр = к кому мы хотим это использовать
# print(b) в консоли <map object at 0x7f2ca8c64b50>  = объект map
# b = list(map(abs, a))
# print(b) завернули в лист и получили спиок [1, 2, 3, 4, 5]

#Какие функции можно передавать в качестве первого аргумента
# функция, которую мы напишем сами

# def f(x):
#     return x ** 2
# a = [-1, 2, -3, 4, 5]
# b = list(map(f, a))
# print(b) #[1, 4, 9, 16, 25]

# пример со строками
# a = ['hello', 'hi', 'chao', 'privet']
# b = list(map(len, a))
# print(b) # [5, 2, 4, 6]

#в качестве функции можно передавать не только функции и самописные функции, но и методы этих объектов, обращаемся к методу через str.
# a = ['hello', 'hi', 'chao', 'privet']
# b = list(map(str.upper, a))
# print(b) #['HELLO', 'HI', 'CHAO', 'PRIVET']

#можно использовать анонимные функции, которые создаются при момощи lambda
# a = ['hello', 'hi', 'chao', 'privet']
# b = list(map(lambda x: x[::-1], a))
# print(b) #строки развернулись в обратном порядке ['olleh', 'ih', 'oahc', 'tevirp']

# a = ['hello', 'hi', 'chao', 'privet']
# b = list(map(lambda x: x + '!', a))
# print(b) #к каждой строке добавился восклицательный знак ['hello!', 'hi!', 'chao!', 'privet!']

#Строки можно преобразовывать к списку ( кажда строка разобъется на список)
# a = ['hello', 'hi', 'chao', 'privet']
# b = list(map(list, a))
# print(b)  [['h', 'e', 'l', 'l', 'o'], ['h', 'i'], ['c', 'h', 'a', 'o'], ['p', 'r', 'i', 'v', 'e', 't']]

#для считывание чисел из консоли через пробел, потребуется функция map

# s = list(map(int, input().split()))
# print(s)

# Задача
# Напишите программу, которая возводит в квадрат и в куб каждое число из списка numbers пользуясь при этом функциями map и lambda.
# В результате у вас должно получится два отдельных списка: в одном квадраты, в другом кубы. Их необходимо вывести на экран.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = list(map(lambda x: x**2, numbers))
# c = list(map(lambda x: x**3, numbers))
# print(b)
# print(c)

# map это как конвеер, элементы не удаляются, они преобразуются
list_1 = ['234', 'hjkh', '2', 'aaa']
res = list(map(lambda x: int(x) if x.isdigit() else x, list_1))
print(res)