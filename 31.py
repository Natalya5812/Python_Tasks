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






     
            



    
