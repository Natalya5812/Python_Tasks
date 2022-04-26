# 16. Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

import os
import random
os.system("cls")

list = []
for N in range (1,6):
    list.append ((1+1*N)*N)
print (f'При последовательности {list} из {N} чисел, сумма членов данной последовательности = {sum (list)}')