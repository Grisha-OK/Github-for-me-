

import json    #Добавляем модуль json

data_base_extras = [{'surname': 'Петрасенко',                             #База данных мосовки
                     'name': 'Барис',
                     'date_of_birth': '29.05.65',
                     'account_balance': 4731.73,
                     'account_number': 44578130
                     },
                     {'surname': 'Некифорова',
                      'name': 'Валентина',
                      'date_of_birth': '13.01.80',
                      'account_balance': 9504.9,
                      'account_number': 44573785
                     }]

with open("data_base_file.json", "a") as write_file: #Открываем фаил в режиме записи
    json.dump(data_base_extras, write_file)  #Конвертирует данные из переменной data в стороку json и записывает в фаил
