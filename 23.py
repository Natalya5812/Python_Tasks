#23. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

import os
import random
os.system("cls")

lst = [random.randint (1,10) for item in range (5)]

lst1 = []
for i in range ((len(lst) + 1 ) // 2):
    lst1.append (lst [i] * lst [-1 - i]) 
print (f'{lst} => {lst1}')



