# 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

import os
import random
import math
math.factorial
os.system("cls")


N = random.randint (1, 10)
list = []
for i in range(1, N+1):  
    list.append(math.factorial (i)) 
print (f'N = {N}, тогда {list}')
    # 

# import os
# import random
# os.system("cls")

# n = random.randint(6, 16)
# print(f'\n {n} \n ')

# list = [1]

# for i in range(2, n+1):
#     list.append(i * list[i-2])

# print(list, '\n')
