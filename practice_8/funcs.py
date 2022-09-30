import csv
import list_exel

def add_info():
    name = input("Name")
    phone = input('Phone')
    newline = [name, phone]
    with open ('data.csv', 'a', newline='') as data:
        writer = csv.writer(data, delimiter=':')
        writer.writerow(newline)
        list_exel.save_list(newline)



def find_num():
    name = input("Name: ")
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter=':')
        for row in reader:
            if name == row[0]:
                print(*row)


def show_all():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter=':')
        for row in reader:
            print('{:<10} {:<10}'.format(*row))


def del_num():
    name = input("Какую запись вы хотите удалить?: ")
    temp_list = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter=':')
        for row in reader:
            temp_list.append(row)
    for item in temp_list:
        if name in item:
            temp_list.remove(item)
            print('Запись удалена')
            break
    with open('data.csv', 'w') as file:
        writer = csv.writer(file, delimiter=':')
        writer.writerows(temp_list)


