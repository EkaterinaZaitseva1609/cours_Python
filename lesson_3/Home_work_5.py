# 2.  Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# 1. Игра на 2-х игроков
from random import randint

def gamers (gamer_1, gamer_2):
    current_gamer = randint(1, 2)
    if current_gamer == 1:
        current_gamer = gamer_1
    else:
        current_gamer = gamer_2
    return current_gamer

# gamer_1 = input('Игрок 1, введите ваше имя')
# gamer_2 = input('Игрок 2, введите ваше имя')
# current_gamer = gamers (gamer_1, gamer_2)

# print(f' первый ход - игрок {current_gamer}')
# candies = 2021
# while candies > 0:
#     while True:
#         player_turn = int(input(f'игрок {current_gamer} введите число от 1 до 28 включительно'))
#         if player_turn < 1 or player_turn > 28:
#             print('ошибка игрока ')
#             break
#         candies -= player_turn
#         print(f'конфет осталось {candies}')
#         if candies == 0:
#             print(f'победу одержал игрок {current_gamer}')
#             break
#         else:
#             current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
# print(f'игра окончена')




# 2. Игра против бота
# gamer_1 = input('Привет, я бот! Сегодня удача на твоей стороне, ты сможешь сравнить свой интеллект с искусственным, начнем? Напиши свое имя')
# gamer_2 = 'Bot'
# candies = 2021
# current_gamer = randint(1, 2)
# if current_gamer == 1:
#     current_gamer = gamer_1
# else:
#     current_gamer = gamer_2
#
# print(f'Первый ход - игрок {current_gamer}')
# first_step = current_gamer
# while candies > 0:
#     while True:
#         if current_gamer == gamer_2:
#             if first_step == gamer_2:
#                 player_turn = candies % 29
#                 print(f'Бот вводит число: {player_turn}')
#             else:
#                 player_turn = randint(1, 28)
#                 print(f'Бот вводит число: {player_turn}')
#         else:
#             player_turn = int(input(f'Игрок {current_gamer} введите число от 1 до 28 включительно'))
#         if player_turn < 1 or player_turn > 28:
#             print('Ошибка игрока ')
#             break
#         candies -= player_turn
#         print(f'Конфет осталось {candies}')
#         if candies == 0:
#             if current_gamer == gamer_2:
#                 print(f'Совершеннейшее существо победило!!!')
#             else:
#                 print(f'Победу одержал игрок {current_gamer}')
#             break
#         else:
#             current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
# print(f'Игра окончена')



# 3. Создайте программу для игры в ""Крестики-нолики""

def printMap(board):
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-------------")


def getWin(board):
    win_game = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_game:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return True
    else:
       return False


# gamer_1 = input('Игрок 1, введите ваше имя')
# gamer_2 = input('Игрок 2, введите ваше имя')
# current_gamer = gamers (gamer_1, gamer_2)

#
# board = list(range(1, 10))
# while True:
#     printMap(board)
#     player_turn = int(input(f'игрок {current_gamer} введите число от 1 до 9 включительно'))
#     if player_turn < 1 or player_turn > 9:
#         print('Ошибка игрока ')
#     elif board[player_turn - 1] == player_turn:
#         if current_gamer == gamer_1:
#          board[player_turn - 1] = 'X'
#         else:
#             board[player_turn - 1] = '0'
#     else:
#         print('Данное поле заполнено, введите другое число')
#         continue
#     if getWin(board) == True:
#         print(f'Поздравляю! Победил игрок {current_gamer}')
#         printMap(board)
#         break
#     else:
#         current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1


# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def getRes(n_str):
    res = ''
    i = 0
    while i < len(n_str):
        count = 1
        while i + 1 < len(n_str) and n_str[i] == n_str[i + 1]:
            count = count + 1
            i = i + 1
        res += str(count) + n_str[i]
        i = i + 1
    print(res)
    return res

data = open('4Task_homeWork.txt', 'r+')
n_str = data.read()
encoding = getRes(n_str)
data.write(encoding)

data.close()

