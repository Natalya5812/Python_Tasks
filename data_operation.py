

import os
os.system("cls")
from Python_Tasks.Sem7.ui import ui_f


def show_data():
    with open (ui_f.ui_f, 'r') as phonebook:
        data = phonebook.read
        print (data)

def add_data():
    with open (ui_f.ui_f, 'r') as phonebook:
        add_data = phonebook.read
    add_data = [input ('Фамилия: '), input ('Имя: '), input ('Контактный номер телефона: '), input ('Примечание: ')]
    add_data = ';'.join(add_data)
    return (add_data)


def search_data(): 
     with open (ui_f.ui_f, 'r') as phonebook:
        data = phonebook.read



#print (add_data())