# 9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

import os
os.system("cls")

QR = (input('Введите номер четверти прямоугольной системы координат: '))
qr = str.lower (QR)

if qr in ['1', 'i']:
    print (f'В четверти номер {QR} допустимы значения координат: (Х>0,Y>0)')
elif qr in ['2', 'ii']:
    print (f'В четверти номер {QR} допустимы значения координат: (Х<0,Y>0)')
elif qr in ['3', 'iii']:
    print (f'В четверти номер {QR} допустимы значения координат: (Х<0,Y<0)')
elif qr in ['4', 'iv']:
    print (f'В четверти номер {QR} допустимы значения координат: (Х>0,Y<0)')
else:
    print ('Введено некорректное значение, введите номер четверти 1-4')
