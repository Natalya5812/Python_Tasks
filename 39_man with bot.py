# # 39.	Создайте программу для игры с конфетами человек против человека.
# # Условие задачи: 
# # На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# # Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# # Все конфеты оппонента достаются сделавшему последний ход. 
# # Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# # a) Добавьте игру против бота
# # b) Подумайте, как наделить бота "интеллектом"

from ntpath import join
import os
import random
os.system("cls")

###Человек против бота
All = 150
print (f'На столе лежит {All} конфета', '\n')


Player = ['Пользователь','Бот Василий']
Lottery = random.choice (Player)
print(f'Первым ходит: {Lottery}', '\n')
Player_2 = []
for i in Player:
    if Lottery not in (i):
        Player_2.append (i)
Player_2 = ''.join(Player_2)   

for i in reversed (range (1, All+1)):
    First = int ()
    if Lottery == Player[0]:
       First = int (input(f'{Lottery}: '))
    else:
       First = random.randint (1,28)
       print (f'{Lottery}: {First}')
    while First not in range (1,29):
        print ('Введено неверное значение, введите число от 1 до 28')
        First = int (input(f'{Lottery}: '))
    else:
        print ('\n',f'На столе осталось {All-First}', '\n') 
    All = All - First
    if All <= 28:
        print (f'Выиграл {Player_2}, ему осталось взять {All} конфет/конфеты')
        break
    Second = int ()
    if Player_2 == Player[0]:
        Second = int(input(f'{Player_2}: '))
    else:
        Second = random.randint (1,28) 
        print (f'{Player_2}: {Second}')
    while Second not in range (1,29):
        print ('Введено неверное значение, введите число от 1 до 28')
        Second = int (input(f'{Player_2}: '))
    else:
        print ('\n', f'На столе осталось {All-Second}', '\n') 
    All = All - Second
    if All <= 28:
        print (f'Выиграл {Lottery}, ему осталось взять {All} конфет/конфеты')
        break