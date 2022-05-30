import data_operation


def Log_add():
    user = data_operation.add_data()
    with open ('row.csv', 'a') as ph:
        ph.write (';'.join(user))
        ph.write ('\n')
    with open ('col.csv', 'a') as ph:
        ph.write (f' Surname; {user[0]} \n')
        ph.write (f' Name; {user[1]}\n')
        ph.write (f' Phone; {user[2]}\n')
        ph.write (f' Comment; {user[3]}\n')
        ph.write ('\n')
        
def Log_show_row():
    with open ('row.csv', 'r') as ph:
        for line in ph:
            print(line)

def Log_show_col():
    with open ('col.csv', 'r') as ph:
        for line in ph:
            print(line)


    

