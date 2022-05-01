# 34. Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.

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

with open('34.txt','w') as data:
    data.write (P)

with open('33.txt','r') as data:
    first=data.readline().split(' = ')

with open('34.txt','r') as data:
    second=data.readline().split(' = ')

with open('34_summ.txt','w') as data:
    data.write(first[0]+' + '+second[0]+' = '+first[1]+' + '+second[1])