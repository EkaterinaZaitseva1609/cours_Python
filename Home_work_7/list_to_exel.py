import openpyxl

def save_list(list_str):
    book = openpyxl.Workbook()
    sheet = book.active
    sheet['A1'] = 'Фамилия'
    sheet['B1'] = 'Номер телефона'
    sheet['C1'] = 'комментарии'

    row = 2
    sheet[row][0].value = list_str[1]
    sheet[row][1].value = list_str[2]
    sheet[row][2].value = list_str[3]
    row += 1

    book.save("my_book.xlsx")
    book.close()