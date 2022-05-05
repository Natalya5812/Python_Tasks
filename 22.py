# 21. Найти сумму чисел списка стоящих на нечетной позиции (индекс)
import os
import random
os.system("cls")

N = random.randint (1,10)
spisok = [random.randint (1,10) for i in range (N)]
print (spisok)
sum = 0
for i in range (N):
    if i % 2 > 0: sum += spisok [i]
print (sum)