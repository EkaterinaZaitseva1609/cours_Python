# Работа с файлами
# file = open('file.txt', encoding='utf-8') #если в вайле содержится кириллица, то обязательно нужно указать кодировку
# print(file.read()) #считать и вывести информацию из файла

# file = open(r'/home/ekaterina/PycharmProjects/course_1/Practice/file.txt', encoding='utf-8') #если файл находится не в одной папке с вызовом, то нужно указать полный путь
# кликнуть на сам файл и выбрать Copy Path, при этом нужно обязательно поставить r перед строкой!
# print(file.read()) #считать и вывести информацию из файла

# Возможности при работе с файлами

# Функция read
# Может принимать аргументы - цифра 2 означает кол-во симыолов, которое мы хотим вывести из вайла (с учетом пробелов)
# file = open('file.txt', encoding='utf-8')
# print(file.read(2))
# print(file.read(2)) #питон запоминает, где он остановился, если снова попросить вывести 22 символа, он выведет следующие 2, идем только вперед
# file.seek(0) #если мы хотим откатиться на начало записи
# print(file.read())

# Функция readline, параметров не принимает. считывает 1 строчку целиком
# file = open('file.txt', encoding='utf-8')
# print(file.readline())

# Обойти все симфолы строки через for, за одну итерацию цикла мы получаем 1 строку нашего файла
# file = open('file.txt', encoding='utf-8')
# for row in file:
#     print(row)

# Обойти побуквенно с помощью вложенного цикла
# file = open('file.txt', encoding='utf-8')
# for row in file:
#     for letter in row:
#         print(letter)

# Создать список элементом которого будет строка файла
# file = open('file.txt', encoding='utf-8')
# s = file.readlines()
# print(s)

#ЗАПИСАТЬ В ФАЙЛ, второым оргументом к open необходимо дописать 'w'. В этом случае мы не дописываем информацию в файл, а перезатераем
# file = open('file.txt', 'w', encoding='utf-8')
# file.write('hi \n')
# file.write('hi \n')
# file.write('hi \n')

# ДОПИСАТЬ В ФАЙЛ для этого вместо w пишем а
# file = open('file.txt', 'a', encoding='utf-8')
# file.write('Chao \n')

# Режим чтения + запись
file = open('file.txt', 'a+', encoding='utf-8')
file.write('Chao \n')
file.close()
