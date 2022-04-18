# 3. Показать числа от -N до N

import os
os.system("cls")

#a = int (input ('Введите значение N: '))
#b = a
#a = -a
#num = range (a, b+1)
#num = list (num)
#print (num)

N = abs(int(input('Введите значение N: ')))
for i in range(-N, N + 1):
    print(i, end = ' ')
