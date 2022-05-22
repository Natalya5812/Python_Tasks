# 16. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

import os
import random
os.system("cls")

n = random.randint(6, 16)

num = [1+(1/i)**i for i in range(1, n+1)]
print(f'При n = {n} => последовательность = {num} => сумма чисел = {round(sum(num), 2)}')

