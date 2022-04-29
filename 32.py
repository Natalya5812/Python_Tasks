# 32. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

import os
os.system("cls")

# Задаём некую последовательность

m, b, a, x, c = 100, 3, 2, 1, 31
lst = []
for i in range (c):
    x = (a*x + b) % m
    lst.append (x)
#print (lst)

# Разбиваем список на части

lst1 = []
lst2 = [] 
count = 0
for i in lst:
    if (count < len(lst)/2):
        lst1.append (i)
        count+=1
    else:
        lst2.append (i)
#print (lst1, '\n', lst2)

# Меняем тип данных списков на множества и сравниваем их между собой

lst1 = set (lst1)
lst2 = set (lst2)

lst_itog = lst1.union(lst2) 
lst_itog = list (lst_itog)
print (f'{lst} => {lst_itog}')