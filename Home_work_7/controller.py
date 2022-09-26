import list_to_exel

def process_command(list_str):
    if list_str[0] == 'add':
        file = open('file.txt', 'a', encoding='utf-8')
        for i in range (1, len(list_str)):
            file.write(list_str[i] + ' ')
        file.write('\n')
        file.close()
        list_to_exel.save_list(list_str)
    elif list_str[0] == 'read':
        file = open('file.txt', 'r', encoding='utf-8')
        print(file.read())
        file.close()







