def calculator(task):
    # solution = 0
    res = 0
    str_1 = task.split()
    print(str_1, type(str_1))
    while str_1.__contains__('*') or str_1.__contains__('/'):
        for i in range(len(str_1)):
            if str_1[i] == '*' or str_1[i] == '/':
                a = float(str_1[i-1])
                b = float(str_1[i + 1])
                if str_1[i] == '*':
                    solution = a * b
                else:
                    solution = a / b
                str_1.pop(i-1)
                str_1.pop(i - 1)
                str_1[i-1] = str(solution)
                break
    while len(str_1) > 1:
        for i in range(len(str_1)):
            if str_1[i] == '+' or str_1[i] == '-':
                c = float(str_1[i-1])
                d = float(str_1[i + 1])
                if str_1[i] == '+':
                    solution = c + d
                else:
                    solution = c - d
                str_1.pop(i-1)
                str_1.pop(i - 1)
                str_1[i-1] = str(solution)
                break
    return str_1
