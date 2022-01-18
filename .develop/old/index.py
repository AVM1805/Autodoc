from docxtpl import DocxTemplate

doc = DocxTemplate("заявлениеОБ.docx")
    
print("***")
print("ПОЖАЛУЙСТА ВВОДИТЕ ДАННЫЕ ВНИМАТЕЛЬНО")
print("***")
print("")

print("Фамилия:")
surname = input()

print("Имя:")
name = input()
if(name == '!'):
    print("Фамилия:")
    surname = input()

print("Отчество:")
otch = input()
if(otch == '!'):
    print("Имя:")
    name = input()

print("Дата рождения (ДД.ММ.ГГГГ):")
date = input()
if(date == '!'):
    print("Отчество:")
    otch = input()

print("Место рождения:")
birthPL = input()
if(birthPL == '!'):
    print("Дата рождения (ДД.ММ.ГГГГ):")
    date = input()

print("Телефон:")
tel = input()
if(tel == '!'):
    print("Место рождения:")
    birthPL = input()

print("ИНН:")
inn = input()
if(inn == '!'):
    print("Телефон:")
    tel = input()

print("СНИЛС:")
snils = input()
if(snils == '!'):
    print("ИНН:")
    inn = input()

print("Серия паспорта:")
seria = input()
if(seria == '!'):
    print("СНИЛС:")
    snils = input()
    
print("Номер паспорта:")
number = input()
if(number == '!'):
    print("Серия паспорта:")
    seria = input()

print("Кем и Когда выдан:")
getPS = input()
if(getPS == '!'):
    print("Номер паспорта:")
    number = input()

print("")
print("***Адрес проживания клиента***")
print("Область:")
obl = input()
if(obl == '!'):
    print("Кем и Когда выдан:")
    getPS = input()

print("Район:")
rajon = input()
if(rajon == '!'):
    print("Область:")
    obl = input()

print("Город:")
city = input()
if(city == '!'):
    print("Район:")
    rajon = input()

print("Населённый пункт:")
naspun = input()
if(naspun == '!'):
    print("Город:")
    city = input()

print("Улица:")
street= input()
if(street == '!'):
    print("Населённый пункт:")
    naspun = input()

print("Дом:")
dom = input()
if(dom == '!'):
    print("Улица:")
    street= input()

print("Корпус:")
corp = input()
if(corp == '!'):
    print("Дом:")
    dom = input()

print("Квартира:")
kvart = input()
if(kvart == '!'):
    print("Корпус:")
    corp = input()



context = { 'name' : name, 'sur': surname, 'otch': otch, 'seria': seria, 'tel': tel, 'date': date, 'inn': inn, 'birthPL': birthPL, 'getPS': getPS, 'naspun': naspun, 'obl': obl,'rajon': rajon, 'dom': dom, 'street': street, 'city': city, 'corp': corp, 'kvart': kvart, 'number': number, 'snils': snils}

doc.render(context)
doc.save("заявление-" + surname + ".docx")


