from docxtpl import DocxTemplate

doc = DocxTemplate("заявлениеОБ.docx")

print("Фамилия:")
surname = input()

print("Имя:")
name = input()

print("Отчество:")
otch = input()

print("Дата рождения (ДД.ММ.ГГГГ):")
date = input()

print("Место рождения:")
birthPL = input()

print("Телефон:")
tel = input()

print("ИНН:")
inn = input()

print("СНИЛС:")
snils = input()

print("Серия паспорта:")
seria = input()

print("Номер паспорта:")
number = input()

print("Кем выдан:")
getPS = input()

print("")
print("***Адрес проживания клиента***")
print("Район:")
rajon = input()

print("Город:")
city = input()

print("Населённый пункт:")
naspun = input()

print("Улица:")
street= input()

print("Дом:")
dom = input()

print("Корпус:")
corp = input()

print("Квартира:")
kvart = input()



context = { 'name' : name, 'sur': surname, 'otch': otch, 'seria': seria, 'tel': tel, 'date': date, 'inn': inn, 'birthPL': birthPL, 'getPS': getPS, 'naspun': naspun, 'rajon': rajon, 'dom': dom, 'street': street, 'city': city, 'corp': corp, 'kvart': kvart, 'number': number, 'snils': snils}

doc.render(context)
doc.save("заявление-" + surname + ".docx")


