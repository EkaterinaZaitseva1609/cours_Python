# Типы данных и переменные
# int, float, boolean, str, list, None
# value = None
# a = 123
# b = 1.23
# value = 123
# print(type(a))  # если хотим увидеть тип переменной
# print(b)
# print(type(value))
# s = 'hello \nworld'
# print(s)  # вывод строки
# print(a, b, s)  # вывод разных переменных в консоль
# print(a, '-', b, '-', s)  # вывод разных переменных и строк в консоль
# print('{} - {} - {}'.format(a, b, s)) # форматированный вывод разных переменных и строк в консоль
# print('{1} - {0} - {2}'.format(a, b, s)) # поменять порядок вывода
# print(f'{a} - {b} - {s}') # еще один вариант вывода в консоль

# f = False
# print(f)

# СПИСКИ
# list = ['1', '2', '4', 'hello', 4, 5, 6.7, True] # в List можно вносить разные типы данных, но лучше так не делать
# print(list)

# col = ['hello', 123, True]
# print(col)

# Ввод и вывод данных
# print('Введите a')
# a = int(input()) #если хотим прочитать цифры, а не строки, добавляем int, float (тип нужных данных)
# print('Введите b')
# b = int(input())
# print(a, '+', b, '=', a + b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметичекие операции
# a = 12
# b = 8
# c = a / b # c = 1.5 (ответ будет не целочисленным, а с точкой)
# print(c)
# c = a // b
# print(c) # c = 1 (ответ будет целочисленным, так как стоит знак двойного деления a // b
# c = a ** b
# print(c) # c = 429981696  = возведение в степень (знак двойного умножения **)

# a = 1.3
# b = 3
# c = a * b
# print(c)  # c = 3.9000000000000004
# c = round(a * b)
# print(c)  # c = 4 округление по математическим правилам
# c = round(a * b, 2)
# print(c)  # c = 3.9 В скобках можно указать нужное кол-во цифр после запятой

# Сокращенные операции присваивания
# a = 3
# a = a + 5
# print(a)
# a = 3
# a += 5
# print(a)
# a = 3
# a *= 5
# print(a)

# Логические операторы
# a = 1 < 4 and 5 > 2
# b = 2 == 3
# c = 1 != 2
# print(a, b, c)
#
# a = 'ngt'
# b = 'ngt'
# print(a == b) # сравнение строк
#
# a = [1, 2]
# b = [1, 2]
# print(a == b) # сравнение списка (list)
#
# a = 1 < 5 < 8
# print(a) # тройные, четверные сравнения
# f = 1 > 2 or 4 < 6
# print(f) # Оператор дизьюнкции (или), является истиной, когда хоть один их операторов истина

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f) # в ответе True, так как 2 содержится в списке f
# print(not 2 in f) # в ответе False, так как 2 содержится в списке f
#
# is_odd = not f[0] % 2 == 0
# print(is_odd)

# Управляющие конструкции if, if-else
# нахождение максимума
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите ваше имя')
# if username == 'Andrey':
#     print('Andrey, hello!')
# elif username == 'Kate':
#     print('Kate, how are you?')
# else:
#     print('Hello,', username)

# Управляющие конструкции While
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит ;)')
# print(inverted)

# конструкции for
# for i in 1, 2, 3, 4, 5:
#     print(i ** 2)

# list = [1, 2, 3, 8, 1]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(1, 10, 2): # первый аргумент 1 = это начало отсчета, 2 = 5 это завершение (-1) и третий аргумент - приращение, в консоль выводится: 1,3,5,7,9
#     print(i)

# for i in 'qwerty':
#     print(i) # побуквенная разбивка

# СТРОКИ
text = 'привет'


# help(text.istitle) # таким способом можно смотреть, ято делают различные функции, подсказка выводится в консоль
# строка как массив символов, к каждому символу можно обращаться по индексу
# print(text[0])
# print(text[-3]) # обратиться к символу с конца строки
# print(text[:]) # выводит всю строку  = привет
# print(text[2:5]) #вывести со 2 по 5 символ
# print(text[:5]) #вывести с самого начала до 5 символа = приве

# СПИСКИ
# run = range(1, 6)
# numbers = list(run)  # приводим range в список
# print(numbers)
# print(len(numbers))  # кол-во символов

# run = range(1, 6)
# numbers = list(run)
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
#     print(numbers)

# colors = ['red', 'blue', 'brown']
# for e in colors:
#     print(e)  # red, blue, brown
# for e in colors:
#     print(e * 2)  # red, blue, brownred, blue, brown
# colors.append('gray')  # добавить в конец
# print(colors == ['red', 'blue', 'brown', 'gray'])
# colors.remove('red')
# del colors[0]
# print(colors)

# ФУНКЦИИ!!!!!
# def function_name(x):
#     тело метода
#     return

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

    arg = 1
    print(f(arg))
    print(type(f(arg)))

