# Как записывать данные в Excel

import openpyxl
import json

with open('practice.json') as file:
   data = json.load(file)

book = openpyxl.Workbook()
sheet = book.active
sheet['A1'] = 'ID'
sheet['B1'] = 'TITLE'
sheet['C1'] = 'YEAR'
sheet['D1'] = 'GENRES'
sheet['E1'] = 'DIRECTOR'
sheet['F1'] = 'ACTORS'

row = 2
for movie in data['movies']:
    sheet[row][0].value = movie['id']
    sheet[row][1].value = movie['title']
    sheet[row][2].value = movie['year']
    sheet[row][3].value = ' '.join(['genres'])
    sheet[row][4].value = movie['director']
    sheet[row][5].value = movie['actors']
    row += 1



sheet['B3'] = 'hello'


book.save("my_book.xlsx")
book.close()


