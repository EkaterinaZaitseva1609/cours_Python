# Цикл while
# i = 1
# while i <= 10:
#     print(i, end=' ')
#     i += 1
#     break # останавливает цикл, считается плохой практикой, лучше завершать цикл условием
# else:
#     print('END!')

# i = 1
# while i <= 10:
#     print(i, end=' ')
#     i += 1
#     continue
#     print(123)
# else:
#     print('END!')

# 1. Напишите программу, которая принимает на вход число N и
# выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81  (5 , * - 3;  -3 * 1 = -3, -3 * -3 = 9)

# n = int(input('Введите число N'))
# res = 1
# print(res, end=' ')
# r = range(n-1)
# for i in r:
#     res = res * -3
#     print(res, end=' ')

# 2. Для натурального n создать последовательности 3n + 1.
# *Пример:*
# - Для n = 6:
# 1: 4,
# 2: 7,
# 3: 10,
# 4: 13,
# 5: 16,
# 6: 19

# n = int(input('Введите число N'))
# i = 1
# while i <= n:
#     res = i * 3 + 1
#     print(f' {i}: {res} ')
#     i += 1

# 3. Напишите программу, в которой пользователь будет задавать две
# строки, а программа - определять количество вхождений одной строки в другой.
#
# *Пример:*
# 'Я люблю Питон!'
# 'лю'

# str1 = input('Введите первую строку')
# str2 = input('Введите вторую строку')
# count = str1.count(str2)
# print(f'{count} раз')
#
# другой вариант решения
# a = input('Введите первую строку')
# b = input('Введите вторую строку')
# count = 0
#
# for i in range (0, len(a) - len(b)):
#     if b == a[i:i + len(b)]:
#         count += 1
#
# print(f'{count}  раз')


# a = 6
# print(a, id(a))

# day_sales = [1589.5, 2687.5, 5478.2, 1236.5, 4756.5]
# idx = 0
# total_sales = 0
# while idx < len(day_sales): # pre-condition
#     total_sales = total_sales + day_sales[idx]
#     idx = idx + 1
# price_per_product = total_sales / len(day_sales)
# print(price_per_product)

# day_sales = [1589.5, 2687.5, 5478.2, 1236.5, 4756.5]
# for idx, item in enumerate(day_sales, start=1):
#     print('товар №', idx, '-', item)

# Написать программу, определяющую, что число
# трёхзначное и средняя цифра равна 5.
# num = 354
# res = 0
# if (num < 99) and (num > 999):
#     print(f'{num} не является трехзначным ')
# else:
#     res = (num % 100) // 10
#     print(res == 5)

# другой вариант решения
# num = 457
# is_three_digits = 0 < num // 100 <= 9
# print(is_three_digits)
#
# tens = num % 100 // 10
# print(tens == 5)

num = int(input('Введите цифру от 0 до 100'))
singularNom= 'процент'
singularGen = 'процента'
pluralGen = 'процентов'
if(num == 1) or (num % 10 == 1):
    print(f'{num} {singularNom}')
elif (num == 0) or (num % 10 == 0):
    print(f'{num} {pluralGen}')
elif (num > 10) and (num < 20):
    print(f'{num} {pluralGen}')
else:
    print(f'{num} {singularGen}')





