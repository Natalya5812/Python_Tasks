# # 14. Подсчитать сумму цифр в вещественном числе.

import os
os.system("cls")

# X = float (input ('Ведите вещественное число: '))
# X = str(X)
# #print (type (X))
# X = X.replace('.','')
# print (f'Заданное число состоит из цифр: {X}')

# for i in (X):
#     i = int (i)
# #print (type (i))
#     print  

num = input("Введите число: ")
sum = 0
for i in range(0, len(num)):
    if num[i] != ".":
        sum += int(num[i])
print(sum)



