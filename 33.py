# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os
import random
os.system("cls")

k = random.randint (1,5)
print (k)
K = []
for i in reversed(range(1, k+1)):
    K.append (i)
#print (K)    

lst = [random.randint(0, 100) for j in range(k + 1)]
if lst [0] == 0:
    lst [0] = random.randint (1,100)
print (lst)

P = str('')
for x in range (k):
    P = P + str(lst[x]) + 'x^' + str(K[x]) + ' + '
P = P + str(lst[-1]) + ' = 0'
print (P)

with open('33.txt','w') as data:
    data.write (P)
    
     
        
 







