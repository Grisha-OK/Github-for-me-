
# -*- coding: utf-8 -*-

import time
import random  #Добавляем модуль random
import json    #Добавляем модуль json

#пишет меню
def data_logging(type_of_transaction, account_number_for_logging, what_happened ,what_changed):
    numeric = time.strftime("%d", time.localtime())
    month = time.strftime("%m", time.localtime())
    year = time.strftime("%Y", time.localtime())
    hour = time.strftime("%H", time.localtime())
    menute = time.strftime("%M", time.localtime())
    calendar_date = str(year) + "-" + str(month)  + "-" + str(numeric) + " " + str(hour) + ":" + str(menute)
    
    log_stor = str(calendar_date) + " Операции: " + str(type_of_transaction) + " Номер счета: " + str(account_number_for_logging) + "," + " Что было: " + str(what_happened) + "," + " Что изменилось: " + str(what_changed) + ".  "
    with open("transaction.log", "a", encoding='utf8') as write_file: #открывает фаил (transaction.log) только в пределах каструкции with open, в режиме бодавления "a", и помещяет содержимое а переменную(write_file)
        write_file.write(log_stor) #.encode("utf-8"))

def menu_show():
    '''
    Выводит подсказку по меню
    '''
    menu_view = ['1 - Вывести данные по счету', '2 - Вывести все счета', '3 - Провести операцию со счетом',
    '4 - Добавить пользователя', '5 - Удалить пользователя по номеру счета', '6 - Редактирование пользователя' , '----------------------------------------', '7 - Выход', '----------------------------------------']                                                
    for i in range (0, 9): #для каждой i в диапазоне (0, 8)
        print (menu_view[i])
    
    print(" ")
    
#взаимодействие с меню
def specific_user_output():
    '''
    вывод конкретного пользователя 
    '''
    print ('Ведите номер счета')
    o = input()   # o присваивается введённый текст
    for q in data_base:   #перебрать элементы списка data_base, q = один из элементов списка
        if q['account_number'] == int(o):   #проверяем номер счета ведёный в консоль
               print('Фамилия:       ', q['surname'])
               print('Имя:           ', q['name'])
               print('Дата рождения: ', q['date_of_birth'])
               print('Баланс счета:  ', q['account_balance'])
               print('Номер счета:   ', q['account_number'])
    print(" ")

def all_user_output():
    '''
    вывод всех пользователя 
    '''
    for q in data_base:   #для каждой q из списка data_base (дословный перевод)
        print (q['surname'], '|',
               q['name'], '|',
               q['date_of_birth'], '|',
               q['account_balance'], '|',
               q['account_number'])
    print(" ")

def conduct_an_operation_with_an_account():
    '''
    провести операцию со счетом 
    '''    
    print ('Ведите номер счета')
    account_number_input = input() #просим ползователя вести номер счета
    print ('Ведите сумму')
    account_balance_input = input() #просим пользователя вести сумму
    account_balance = ""

    for q in data_base: #перебрать элементы списка data_base, q = один из элементов списка     
        if q['account_number'] == int(account_number_input): #роверяем номер счета ведёный в консоль 
            account_balance = str(q['account_balance'])
            q['account_balance'] = q['account_balance'] + float(account_balance_input) #выполняем математическую операцыю
            print ('Операцыя выполнена')                                                                         
    print(" ")
    
    data_logging("Монепуляцыя со счотом", account_number_input, account_balance , account_balance_input)

def add_new_user():
    '''
    добавить нового пользователя 
    '''    
    print('Ведите фамилию')
    s = input()
    print('Ведите имя')
    n = input()
    print('Ведите дату рождения')
    d = input()
    print ('Пользователь создан')
    
    def create_acc_number():
        return (account_prefix * 10000 + random.randint(1, 9999))  

    def check_acc_number(number_ac): #рекурсия(рекурсия(рекурсия(...)))   
        for account in data_base: #для каждой i в диапазоне, длина (data_base), i = порядковому номеру
            if number_ac == account["account_number"]:
                number_ac = create_acc_number()
                check_acc_number(number_ac)
    
    number_ac = create_acc_number()
    check_acc_number(number_ac)
    
    data_base.append({'surname': s, #Добавляем элемент в список
            'name': n,
            'date_of_birth': d,                                                    
            'account_balance': 0.00,
            'account_number': number_ac}) #Объединяем число 4457 с рандомным числом
    print(number_ac)
    print(" ")
    add_message = "Добавлен пользователь: Фамилия(" + s + ") Имя(" + n + ") Дата рождения(" + d + ") Баланс(" + str(0.00) + ")"
    data_logging("Добавление пользователя", number_ac, "---", add_message)

def delete_user():
    '''
    удолить пользователя 
    '''    
    del_index = None
    print ('Ведите номер счета для удаления')
    f = input()
    for i in range(len(data_base)): #для каждой i в диапазоне, длина (data_base), i = порядковому номеру
        q = data_base[i]            #приравневаем q к отдельно взятым элементам, как в конструкции < for q in data_base: >
        if q['account_number'] == int(f):
            del_index = i
            s = str(q['surname'])
            n = str(q['name'])
            d = str(q['date_of_birth'])
            a = str(q['account_balance'])
            
    if del_index != None:   
        del data_base[del_index]
        print("Пользователь удалён")
    else:
        print("Пользователь не найден")
    print(" ")
    del_message = "Удолён пользователь: Фамилия(" + s + ") Имя(" + n + ") Дата рождения(" + d + ") Баланс(" + a + ")"
    data_logging("Удоление пользователя", f, del_message, "---")

def exit_the_program():
    '''
    выйти из программы 
    '''    
    with open("data_base_file.json", "w") as write_file: #Открываем файл в режиме записи
        json.dump(data_base, write_file)  #Конвертирует данные из переменной data в строку json и записывает в файл

    print ('Выход выполнен')
    exit(0)

def user_edit():
    print("Ведите номер счота:")
    account_number_for_editing = input()
    
    for i in range(len(data_base)): #для каждой i в диапазоне, длина (data_base), i = порядковому номеру
        q = data_base[i]            #приравневаем q к отдельно взятым элементам, как в конструкции < for q in data_base: >
        if q['account_number'] == int(account_number_for_editing):
            print(" ")
            print('Фамилия:       ', q['surname'])
            print('Имя:           ', q['name'])
            print('Дата рождения: ', q['date_of_birth'])
            print('Номер счета:   ', q['account_number'])
            print(" ")

            s = str(q['surname'])
            n = str(q['name'])
            d = str(q['date_of_birth'])

            default_surname = (q['surname'])
            default_name = (q['name'])
            default_date_of_birth = (q['date_of_birth'])
                
            input_change_surname = input((default_surname + " : ")) or default_surname
            input_change_name = input((default_name + " : ")) or default_name
            input_change_default_date_of_birth = input((default_date_of_birth + " : ")) or  default_date_of_birth
            
            print(" ")
            print("Сохринить изменение?: yes/no")
            print(" ")
            print(input_change_surname)
            print(input_change_name)
            print(input_change_default_date_of_birth)
            print(" ")

            choice = input()
            if choice == "yes":
                for q in data_base: #для каждой i в диапазоне, длина (data_base), i = порядковому номеру
                    if q['account_number'] == int(account_number_for_editing):
                        q['surname'] = input_change_surname
                        q['name'] = input_change_name
                        q['default_date_of_birth'] = input_change_default_date_of_birth
    before_edit_message = s + " " + n + " " + d
    after_edit_message = input_change_surname + " " + input_change_name + " " + input_change_default_date_of_birth
    data_logging("Редактирование пользоватля", account_number_for_editing, before_edit_message, after_edit_message)
    print(" ")

def debugger(): #отлодчик_666
    '''
    выводиться заготовленные действия из функции отладчика 
    '''    
    print("you entered debug mode")
    print(" ")
    print(" ")
    print(data_base)
    print(" ")

data_base = []             #переменная хранящая данные из файла и не добавленные в файл

try:                                                     #если произойдёт исключение выполнится except
    with open("data_base_file.json", "r") as write_file: #фаил открыт только в конструкции with open
        variable_with_read = write_file.read()           #Читает строку из файла
        data_base = json.loads(variable_with_read)       #Преобразует строку в python объект.
except FileNotFoundError:                                #выполнется если произойдёт ошибка в try
    print("Создаю новую базу")

account_prefix = 4457

menu_show()

menu_program = ''

while True: #до тех пор пока выполняется условие 
    menu_program = input()
    
    if menu_program == '1':    #если выполняется условие...
        specific_user_output() #то вызывается функция вывода конкретного пользователя
        
    elif menu_program == '2':  #иначе, если не одно из условий if или (elif) не выполнено...
        all_user_output()     #то вызывается функция вывода всех пользователей
        
    elif menu_program == '3':  #иначе, если не одно из условий if или (elif) не выполнено...
        conduct_an_operation_with_an_account() #то вызывается функция проведения операции со счетом 

    elif menu_program == '4':  #иначе, если не одно из условий if или (elif) не выполнено...
        add_new_user()          #то вызывается функция добавления нового пользователя

    elif menu_program == '5':  #иначе, если не одно из условий if или (elif) не выполнено...
        delete_user()          #то вызывается функция удоления пользователя

    elif menu_program == '6':  #иначе, если не одно из условий if или (elif) не выполнено...
        user_edit()         #то вызывается функцию редактирование пользователя
    
    elif menu_program == '7':  #иначе, если не одно из условий if или (elif) не выполнено...
        exit_the_program()     #то вызывается функцию выхода

    elif menu_program == '666':#иначе, если не одно из условий if или (elif) не выполнено...
        debugger()             #то вызывается за резервирования функция под отладку.

    else:
        menu_show()
