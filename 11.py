# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import os
os.system("cls")

lst =[(-3)**i for i in range (0,10)]
print (lst)

# def sub (x):
#     if x in [0,1]:
#         return 1
#     else:
#         return sub (x-1)*-3
# list = []
# for N in range (1,10):
#     list.append (sub(N)) # Добавление элемента в конец списка
# print (list)


# def power(s):
#     """
#     Function will get power of number -3
#     """
#     new = (-3) ** s

#     return new

# n = 20
# spisok=[]

# for i in range(n):
#     spisok.append(power(i))

# print(f"List of elements: {spisok}")


