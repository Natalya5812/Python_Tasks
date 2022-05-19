# 41. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# - входные и выходные данные хранятся в отдельных текстовых файлах

import os
import itertools
os.system("cls")

def RLE_coding (text):
    for char, same in itertools.groupby (text):
        count = sum(1 for i in same)
        #yield char if count == 1 else str(count)+char # yield - Генератор (возвращает из функции Генератор)
        yield str(count)+char # yield - Генератор (возвращает из функции Генератор)


def RLE_decoding(text_rle):
    count = ''
    char = ''
    for i in text_rle:
        if i.isdigit():
            count += i
        else:
            char += i * int(count)
            count = ''
    return char

Text = 'ggh;djlllllll lkyhiuy'
print (f'{Text} => {len(Text)}')

Text_RLE = ''.join(RLE_coding(Text))
print (f'{Text_RLE} => {len(Text_RLE)}')

T = ''.join(RLE_decoding(Text_RLE))

with open('41_source.txt', 'w') as Data:
     Data.write(Text)

with open('41_source.txt', 'r') as Data:
     Data.read = Text
     Text = Text_RLE
     with open('41_compression.txt', 'w') as Data:
         Data.write(Text)


with open('41_compression.txt', 'r') as Data:
     Data.read = Text_RLE
     Text_RLE = T
     print (f'{T} => {len(T)}')

print (f'Исходный текст после восстановления данных остался без изменений? - {Text_RLE==T}')












