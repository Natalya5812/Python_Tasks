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

###Человек против бота c "интеллектом"
All = 2021 #Количество конфет
Move = 28 #Максимальное количество конфет, которое можно взять 1 игроку за 1 ход
print (f'На столе лежит {All} конфета', '\n')


Player = ['Пользователь','Бот Василий Иванович']
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
       First = All % (Move+1)
       if First == 0:
           First = random.randint (1,28)  
           print (f'{Lottery}: {First}')
    while First not in range (1,Move+1):
        print ('Введено неверное значение, введите число от 1 до 28')
        First = int (input(f'{Lottery}: '))
    else:
        print ('\n',f'На столе осталось {All-First}', '\n') 
    All = All - First
    if All <= Move:
        print (f'Выиграл {Player_2}, ему осталось взять {All} конфет/конфеты')
        break
    Second = int ()
    if Player_2 == Player[0]:
        Second = int(input(f'{Player_2}: '))
    else:
        Second = All % (Move+1)
        if Second == 0:
            Second = random.randint (1,28)
        print (f'{Player_2}: {Second}')
    while Second not in range (1,Move+1):
        print ('Введено неверное значение, введите число от 1 до 28')
        Second = int (input(f'{Player_2}: '))
    else:
        print ('\n', f'На столе осталось {All-Second}', '\n') 
    All = All - Second
    if All <= Move:
        print (f'Выиграл {Lottery}, ему осталось взять {All} конфет/конфеты')
        break
