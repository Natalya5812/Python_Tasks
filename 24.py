# 24. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
from random import*
os.system("cls")

Spisok = [round (uniform (0, 20),3) for i in range (5)]
Diff = []
for i in Spisok:
    if i % 1 != 0:
        Diff.append (round (i % 1, 3))
   
print (f'{Spisok} => max = {max (Diff)}, min =  {min(Diff)} => Diff = {max (Diff) - min(Diff)}')
