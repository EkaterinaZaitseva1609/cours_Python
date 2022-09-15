def getMaxMin (s):
    str_list = s.split(' ')
    print(str_list)
    str_list = [int(num) for num in str_list]
    max = str_list[0]
    min = str_list[0]
    for i in str_list:
        if max < i:
            max = i
        if min > i:
            min = i

    print(max, min)

#===========================================================

def getRoot (a,b,c):
    import math
    #найти дискриминант по формуле D= b^2 - 4ac
    discr = b ** 2 - 4 * a * c
    print('дискриминант = ', discr)
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print(f'x1 = {x1:.2} x2 = {x2: .2}')
    elif discr == 0:
        x = -b / (2 * a)
        print(f'x = {x: .2}')
    else:
        print('корней нет')

#===========================================================
def getNok(a, b):
    if a > b:
        max_n = a
    else:
        max_n = b
        while(True):
            if ((max_n % a == 0) and (max_n % b == 0)):
                nok = max_n
                break
            max_n += 1
    print(nok)

    with open('file_practice4.txt', 'w') as date:
        date.write(str(nok))

