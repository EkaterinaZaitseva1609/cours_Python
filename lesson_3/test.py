import random
import time
from tkinter import *



while True:
    player_turn = 'Person'


    if player_turn < 1 or player_turn > 9:
        print('Ошибка игрока ')
    elif board[player_turn - 1] == player_turn:
        if current_gamer == gamer_1:
         board[player_turn - 1] = 'X'
        else:
            board[player_turn - 1] = '0'
    else:
        print('Данное поле заполнено, введите другое число')
        continue
    if getWin(board) == True:
        print(f'Поздравляю! Победил игрок {current_gamer}')
        printMap(board)
        break
    else:
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1




# encoding = ''
# i = 0
# while i < len(n_str):
#     count = 1
#     while i + 1 < len(n_str) and n_str[i] == n_str[i + 1]:
#         count = count + 1
#         i = i + 1
#     encoding += str(count) + n_str[i]
#     i = i + 1
# print(encoding)

















game = [None] * 9
game_left = list(range(9))
turn = 0

root = Tk()
root.title('Крестики-нолики')



buttons = [Button(width=5, height=2, font=('Arial', 20, 'bold'), bg='lightblue', command=lambda x=i: push(x)) for i in
           range(9)]

myLabel = Label()
myLabel.grid(row=0, column=0, columnspan=3)
row = 1;
col = 0
for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0

root.mainloop()
