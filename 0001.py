# Найти число из диапазона 60-100 кратное 2800 и 3533

from ast import For
import os
os.system("cls")

A = int (2800)
B = int (3532)
for i in range (70,81):
    #print (f'At A = {A}; B = {B}; i = {i}; RES1 = {round (A/i,5)}; RES2 = {round(B/i,5)} - {bool (A%i== range (0,99) or B%i==range (0,99))}')
   print (f'(({B} / {i})*1000) / 1000 = {((B/i)*1000)/1000}')