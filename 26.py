# 26.	Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
#  Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

import os
import random
os.system("cls")

def fib (x):
    if x == 0:
        return 0
    elif x == 1:
        return 1  
    elif x < 0:
        return fib(x+2) - fib (x+1)
    else:
        return fib(x-1) + fib (x-2)
k = random.randint (5,10)
lst = [fib (i) for i in range (-k, k+1)]

print (f'{k} => {lst}')
