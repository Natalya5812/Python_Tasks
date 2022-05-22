# # Написать программу получающую набор произведений чисел от 1 до N.
# # Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

import os
import random
import math
os.system("cls")


n = random.randint(5, 20)
print (f'При N = {n} => {list(map(lambda i: math.factorial (i), range (1, n+1)))} ')








# n = random.randint(6, 16)
# print(n)

# list = [1]

# for i in range(2, n+1):
#     list.append(i * list[i-2])

# print(list, '\n')


# import math
# a = math.factorial(5)
# print(a)
