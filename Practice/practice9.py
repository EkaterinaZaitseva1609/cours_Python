# def add_label():
#     label = tk.Label(win, text='new')
#     label.pack()
#
# def say_hello():
#     print('hello!')
#
# def counter():
#     global count
#     count +=1
#     btn4['text'] =f"Счетчик: {count}"
#
# count = 0

import tkinter as tk

def get_entery():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entery')

def delete_entery():
    name.delete(0)




win = tk.Tk()
h = 500
w = 600
win.config(bg = 'blue')
win.title('phone book')
win.geometry(f'{h}x{w}+100+200')
win.minsize(300,400)
win.maxsize(700,800)
win.resizable(True, True)

# btn5 = tk.Button(win,text='Hello_5')
# btn6 = tk.Button(win,text='Hello_6')
# btn7 = tk.Button(win,text='Hello_7')
# btn8 = tk.Button(win,text='Hello_world')
# btn9 = tk.Button(win,text='Hello_9')
# btn10 = tk.Button(win,text='Hello_10')
# btn11 = tk.Button(win,text='Hello_11')
# btn12 = tk.Button(win,text='Hello_12')
#
#
# btn5.grid(row=0, column=0)
# btn6.grid(row=0, column=1, stick= 'we')
# btn7.grid(row=1, column=0, stick='we')
# btn8.grid(row=1, column=1)
# btn9.grid(row=2, column=0)
# btn10.grid(row=2, column=1, stick='ew')
# btn11.grid(row=3, column=0, columnspan=2, stick='we')
# btn12.grid(row=0, column=2, rowspan=4, stick='ns')

# for i in range(5):
#     for j in range(2):
#         tk.Button(win, text=f'Hello {i} {j}').grid(row=i, column=j, stick='we')

tk.Label(win, text='Имя').grid(row=0, column=0, stick='w')
name = tk.Entry(win)
name.grid(row=0, column=1)
tk.Button(win,text='get', command=get_entery).grid(row=1, column=0, stick='we')
tk.Button(win,text='delete', command=delete_entery).grid(row=1, column=1, stick='we')
tk.Button(win,text='insert', command=lambda : name.insert(0, 'hello'))\
    .grid(row=1, column=2, stick='we')

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)




# btn1=tk.Button(win, text="Start",
#                command=say_hello
#                )
# btn2=tk.Button(win, text="Add new label",
#                command=add_label
#                )
# btn3=tk.Button(win, text="Add new label lambda",
#                command=lambda: tk.Label(win, text='new lambda').pack()
#                )
# btn4=tk.Button(win, text=f"Счетчик: {count}",
#                command=counter,
#                activebackground='pink',
#                bg = 'yellow'
#                )
#
# btn1.pack()
# btn2.pack()
# btn3.pack()
# btn4.pack()

# label_1=tk.Label(win, text='Hello!',
#                  bg='blue',
#                  fg='pink',
#                  font=('Arial', 20, 'bold'),
#                  padx=10,
#                  pady=40
#                  )
# label_1.pack()




win.mainloop()


