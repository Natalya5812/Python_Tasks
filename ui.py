
import Python_Tasks.Sem7.data_operation


def ui_f():
    format = (input('С каким справочником работаем? 1 - row; 2 - col'))
    while format!= '1' or '2':
        format = input ('Введите число 1, если хотите работать со справочником в формате "row" или число 2, если хотите работать со справочником в формате "col"')
    if format == '1':
        return ('row.csv')
    if format == '2':
        return ('col.csv')

def ui_op():
    a = input ('Введите команду: Просмотр - 1; Добавление - 2; Поиск - 3')
    while a!= '1' or '2' or '3':
        a = input ('Введите число 1, если хотите просмотреть справочник, число 2 - если хотите добавить информацию в справочник, число 3 - если хотите найти информацию в справочнике')
    if a ==1:
        return Python_Tasks.Sem7.data_operation.show_data()
    if a ==2:
        Python_Tasks.Sem7.data_operation.add_data()
    if a ==3:
        Python_Tasks.Sem7.data_operation.search_data()

    

