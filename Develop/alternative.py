from docxtpl import DocxTemplate

doc = DocxTemplate("заявлениеОБ.docx")

def check(tasks):
    print('***')
    print('Проверьте, если нашли ошибку - укажите строку, в другом случае ENTER:')
    print('***')
    print('')
    i = 1
    for key, val in tasks.items():
        print(str(i)+'. '+key+tasks[key])
        i += 1
    check = input()
    if check.isdigit() :
        num = int(check) - 1
        elem = list(tasks)[num]
        print(elem)
        tasks[elem] = input()
        ''''''
        for key, val in tasks.items():
            print(str(i)+'. '+key+tasks[key])
            i += 1
        print('***')
        print('Проверьте, если нашли ошибку - укажите строку, в другом случае ENTER:')
        print('***')
        print('')
        i = 1
        for key, val in tasks.items():
            print(str(i)+'. '+key+tasks[key])
            i += 1
        check = input()
        if check.isdigit():
            num = int(check) - 1
            elem = list(tasks)[num]
            print(elem)
            tasks[elem] = input()
            ''''''
            for key, val in tasks.items():
                print(str(i)+'. '+key+tasks[key])
                i += 1
            print('***')
            print('Проверьте, если нашли ошибку - укажите строку, в другом случае ENTER:')
            print('***')
            print('')
            i = 1
            for key, val in tasks.items():
                print(str(i)+'. '+key+tasks[key])
                i += 1
            check = input()
            if check.isdigit():
                num = int(check) - 1
                elem = list(tasks)[num]
                print(elem)
                tasks[elem] = input()
                
            else:
                print('Готово!')
        else:
            print('Готово!')
        

    
print("***")
print("ПОЖАЛУЙСТА ВВОДИТЕ ДАННЫЕ ВНИМАТЕЛЬНО")
print("***")
print("")
'''Создаём переменные:'''
surname = ''
name = ''
otch = ''
date = ''
birthPL = ''
tel = ''
inn = ''
snils = ''
seria = ''
number = ''
getPS = ''
obl = ''
rajon = ''
city = ''
naspun = ''
street = ''
dom = ''
corp = ''
kvart = ''
'''Ассоциативный массив'''
tasks = {'Фамилия:': surname, 'Имя:': name, 'Отчество:': otch, 'Дата рождения (ДД.ММ.ГГГГ):': date, 'Место рождения:': birthPL, 'Телефон:': tel, 'ИНН:': inn, 'СНИЛС:': snils, 'Серия паспорта:': seria, 'Номер паспорта:': number, 'Кем и Когда выдан:': getPS, 'Область ПРОЖИВАНИЯ:': obl, 'Район ПРОЖИВАНИЯ:': rajon, 'Город ПРОЖИВАНИЯ:': city, 'Населённый пункт ПРОЖИВАНИЯ:': naspun, 'Улица ПРОЖИВАНИЯ:': street, 'Дом ПРОЖИВАНИЯ:': dom, 'Корпус ПРОЖИВАНИЯ:': corp, 'Квартира ПРОЖИВАНИЯ:': kvart,}

'''Ввод'''
for key, val in tasks.items():
    print(key)
    tasks[key] = input()
    
'''Проверка'''    
check(tasks)

context = { 'name' : tasks['Имя:'], 'sur': tasks['Фамилия:'], 'otch': tasks['Отчество:'], 'seria': tasks['Серия паспорта:'], 'tel': tasks['Телефон:'], 'date': tasks['Дата рождения (ДД.ММ.ГГГГ):'], 'inn': tasks['ИНН:'], 'birthPL': tasks['Место рождения:'], 'getPS': tasks['Кем и Когда выдан:'], 'naspun': tasks['Населённый пункт ПРОЖИВАНИЯ:'], 'obl': tasks['Область ПРОЖИВАНИЯ:'],'rajon': tasks['Район ПРОЖИВАНИЯ:'], 'dom': tasks['Дом ПРОЖИВАНИЯ:'], 'street': tasks['Улица ПРОЖИВАНИЯ:'], 'city': tasks['Город ПРОЖИВАНИЯ:'], 'corp': tasks['Корпус ПРОЖИВАНИЯ:'], 'kvart': tasks['Квартира ПРОЖИВАНИЯ:'], 'number': tasks['Номер паспорта:'], 'snils': tasks['СНИЛС:']}

doc.render(context)
doc.save("заявление-" + tasks['Фамилия:'] + ".docx")
