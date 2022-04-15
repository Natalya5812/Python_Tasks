# 4. Показать первую цифру дробной части числа

import os
os.system("cls")

print ("Введите число с точностью до десятых: ")
a = float(input())
print (int(a*10)%10)