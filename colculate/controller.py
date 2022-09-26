def save_data(data):
    path = 'data_base'
    f = open(path, 'a')
    f.write(data + '\n')
    f.close()
