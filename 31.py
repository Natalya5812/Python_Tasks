# # 31. Составить список простых множителей натурального числа N

import os
import random
os.system("cls")

N = random.randint (2, 10000)
print (f'N = {N} состоит из простых множителей:') 
P = 2
Mult_N = []
i = P
while i <= N:
    if N % i == 0:
        Mult_N.append (i)
        N = N / i  
        i = P
    else:
        i += 1
print (Mult_N)



# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")



     
            



    
