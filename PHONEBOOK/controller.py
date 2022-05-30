import ui
import data_operation
import log

def run():
    num = ui.ui_operation()
    while num not in range (1,4):
        print ('Введено неверное значение, введите номер операции от 1, 2 или 3')
    else:
        print('Ok')
    if num == 1:
        print ('Введите данные')
        log.Log_add()

    if num == 2:
        log.Log_show_row()

    if num == 3:
        log.Log_show_col() 
