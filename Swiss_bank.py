import random  #Добавляем модуль random
import json    #Добавляем модуль json

data_base = []             #Переменная не сохраняющая данные с прошлого запуска

try:
    with open("data_base_file.json", "r") as write_file:        #зкрывает фаил написи вне отступа
        variable_with_read = write_file.read()                  #Читает строку из файла
        data_base = json.loads(variable_with_read)     #Преобразует строку в python обект.
except FileNotFoundError:
    print("Создаю новую базу")

account_prefix = 4457

#пишет меню
menu_view = ['1 - Вывести данные по счету', '2 - Вывести все счета', '3 - Провести операцию со счетом',
'4 - Добавить пользователя', '5 - Удалить пользователя по номеру счета','6 - Выход', '----------------------------------------']                                                
for i in range (0, 7): #для каждой i в диапазоне (0, 7)
    print (menu_view[i])
    
#абрабатевает меню
menu_program = ''
while menu_program != '6': #до тех пор пока выполняется условие (в данном случее menu_program НЕ РАВНО 6)
    menu_program = input()
    if menu_program == '1': #если выполняется условие
        print ('Ведите номер счета')
        o = input()
        for q in data_base: #перебрать элементы списка data_base, q = один из элементов списка
            if q['account_number'] == int(o): #проверяем номер счета ведёный в кансоль
                   print('Фамилия:       ', q['surname'])
                   print('Имя:           ', q['name'])
                   print('Дата рождения: ', q['date_of_birth'])
                   print('Баланс счета:  ', q['account_balance'])
                   print('Номер счета:   ', q['account_number'])
        
    elif menu_program == '2': #иначе, если не какое из условий if или (elif) не выполнено
        for q in data_base:#для каждой q из списка data_base
            print (q['surname'], '|',
                   q['name'], '|',
                   q['date_of_birth'], '|',
                   q['account_balance'], '|',
                   q['account_number'])
            
    elif menu_program == '3':
        print ('Ведите номер счета')
        y = input() #просим ползователя вести номер счета
        print ('Ведите сумму')
        x = input() #просим ползователя вести сумму
        for q in data_base: #перебрать элементы списка data_base, q = один из элементов списка
            if q['account_number'] == int(y): #роверяем номер счета ведёный в кансоль
                q['account_balance'] = q['account_balance'] + float(x) #выполняем математическую аперацыю
                print ('Операцыя выполнена')

    elif menu_program == '4':
        print('Ведите фамилию')
        s = input()
        print('Ведите имя')
        n = input()
        print('Ведите дату рождения')
        d = input()
        print ('Пользователь создан')
        u = (account_prefix * 10000 + random.randint(1, 9999))
        data_base.append({'surname': s, #Добавляем элемент в список
              'name': n,
              'date_of_birth': d,                                                    
              'account_balance': 0.00,
              'account_number': u}) #Объединяем число 4457 с рандомным числом
        print(u)

    elif menu_program == '5':
        print ('Ведите номер счета для удаления')
        f = input()
        for i in range(len(data_base)): #для каждой i в диапазоне, длиня (data_base), i = арядковому номеру
            q = data_base[i]            #приравневаем q к атдельно взятм элиментам, как в конструкции < for q in data_base: >
            if q['account_number'] == int(f):
                del data_base[i]
                
        
    elif menu_program == '6':
        with open("data_base_file.json", "w") as write_file: #Открываем фаил в режиме записи
            json.dump(data_base, write_file)  #Конвертирует данные из переменной data в стороку json и записывает в фаил

        print ('Выход выполнен')
        exit(0)

    elif menu_program == '666':
        print("you entered debug mode")
        print(" ")
        print(" ")
        print(data_base)
