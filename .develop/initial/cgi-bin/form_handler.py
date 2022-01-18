#!/usr/bin/env python3
import cgi
from docxtpl import DocxTemplate

doc = DocxTemplate("заявлениеОБ.docx")

form = cgi.FieldStorage()

context = {}
fields = ["surname", "name", "patronymic", "birthDate", "birthPlace", "telephone", "inn", "snils", "passportSeries", "passportNumber", "issuedBy", "region", "district", "city", "locality", "street", "home", "houseBody", "flat"]

for field in fields:
        fieldText = form.getfirst(field, "")
        context.update({field: format(fieldText)})
doc.render(context)
doc.save("заявление-готовое.docx")