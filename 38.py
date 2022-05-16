# 38. Напишите программу, удаляющую из текста все слова содержащие "абв".

from ntpath import join
import os
os.system("cls")

Data = 'абврулоп абырваалк абвлсгпгнп аопыабвлаг ыфловпашвгп шакгпоарп абвпашкп'
Data = Data.split (' ')
D = []
for i in Data:
    if 'абв' not in (i):
        D.append (i)
print (' '.join(Data) + ' => ' + ' '.join(D))