# Подсчитать сумму цифр в вещественном числе.


import os
import random
os.system("cls")


a = random.uniform (1,1001)
print (f'Сумма цифр числа {a} = {sum(map(int, str(a).replace(".", ""))) }')









# # задаем случайное вещественное число из диапазона
# a = random.uniform(1, 1001)
# print('Задано число:', a)

# a = str(a).replace('.', '')     # переводим в строковый тип, убираем точку
# print(a)
# summa = sum(map(int, a))        # переводим в числовой тип, считаем сумму
# print('Сумма цифр данного числа равна:', summa, '\n')






# #Способ 2
# string_number = str(float(input('Enter a real number: '))).replace('.', '')
# list_number = [int(a) for a in string_number]
# print(f'Sum of all digits in the real number is {sum(list_number)}.')
