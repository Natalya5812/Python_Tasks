# 17. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

import os
import random
os.system("cls")

N = random.randint (5,20)
Lst = list(i for i in range (-N, N+1))
result = 1
print (f'{N} => {Lst}')

with open('17.txt', 'w') as Data:
    for i in range (1,random.randint(2, N)):
        Data.write(f'{random.randint(1, N*2)}\n')
   

with open('17.txt', 'r') as Data:
     for Line in Data:
        result = result * int(Lst[int(Line)])
        #print (f'Индекс: {Line}')  
print(result)
         
            
            
           





