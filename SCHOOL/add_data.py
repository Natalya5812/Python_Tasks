from get_data import get_data
from get_data import push_data

def add_data():
    result_list = get_data()
    id = int(len(result_list))
    string = ''
    string += str(id)+';'      # list[0] - это Id ученика)
    string += input('Введите фамилию: ')+';'
    string += input('Введите имя: ')+';'
    string += input('Введите класс: ')+';'
    string += input('Введите статус успеваемости: ')+';'
    string += input('Введите ряд: ')+';'
    string += input('Введите номер парты: ')+';'
    string += input('Введите город проживания: ') + ';'
    string += input('Введите адрес: ')+';'
    string += input('Введите примечание: ')+';'
    print('Добавляем ученика: ', string)
    push_data(string)

# def add_data ():
#     result_list = get_data()
#     ID = int(len(result_list))
#     user  = []
#     user.append (ID)
#     user.append (input ('Введите фамилию ученика: '))
#     user.append (input ('Введите имя ученика: '))
#     user.append (input ('Введите Класс: '))
#     user.append (input ('Введите статус успеемости '))
#     user.append (input ('Введите ряд: '))
#     user.append (input ('Введите номер парты: '))
#     user.append (input ('Введите город проживания: '))
#     user.append (input ('Введите адрес: '))
#     user = ';'.join(user)
#     push_data(user)