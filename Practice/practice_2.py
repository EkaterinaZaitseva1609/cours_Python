 # Строки
# n = '''Я стану крутым программистом!
# Я стану крутым программистом!
# Я стану крутым программистом!
# '''
# print(n)
# n = 'W'
# print(n * 777)

# a = input()
# a.split(',')
# print(ord(a))

#Методы строк
 # s = 'hello'
# print(s.upper()) # переводит в верхний регистр
# print(s.upper()) #нижний регистр
# print(s.count('l',0,4)) #кол-во раз встречается какое-то значение, первый аргумент (что ищем) обязателен, другие два (срез поиска) по жеданию.
# print(s.find('h')) #первый раз найден символ, в консоль выводит его индекс
# print(s.rfind('l')) #первый раз найден символ, поиск ведется справа
# print(s.replace('l', 'yyy', 2)) #замена символов (что меняем, на что меняем) третий параметр не обязателен, сколько раз замену хотим сделать - 'hello' - heyyyyyyo
# print(s.isalpha()) #проверка, состоит ли строка целиком из букв - возвращает True / False ( если есть пробелы, вернет ложь)
# print(s.isdigit())#проверка, состоит ли строка целиком из цифр

# d = '111'
# print(d.rjust(5)) #принимает параметр ширина, дополняет наш элемент до указанной длины, в данном случае перед 111 будут  2 пробела
# print(d.rjust(5, '0')) #второым аргументом можно указать, чем заполнить расширение 00111, несколько символов передавать нельзя

# w = 'Ivanon Ivan Ivanovich'
# print(len(w.split())) #узнать, сколько слов в строке
# print(w.split('n')) #['Iva', 'o', ' Iva', ' Iva', 'ovich']  разбить строку по символу, в данном случае 'n'

# a = '234,56,789,234,5'
# print(a.split(',')) #['234', '56', '789', '234', '5'] получаем список
# t = '234,56,789,234,5'
# print('='.join(t)) #2=3=4=,=5=6=,=7=8=9=,=2=3=4=,=5 объединяем в строку
w = 'Ivanon Ivan Ivanovich'
# print(','.join(w.split())) #Ivanon,Ivan,Ivanovich
# print(w.lower().replace('n', 'v', 2))
#
#
# q = '    hello    \n'
# print(q)
# print(q.strip()) #удаляет пробелы и переносы
# print(q. rstrip())#удаляет пробелы и переносы справа
# print(q. lstrip())#удаляет пробелы и переносы слева











