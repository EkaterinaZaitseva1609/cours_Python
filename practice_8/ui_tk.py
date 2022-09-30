from _csv import writer
from tkinter import *
from tkinter import messagebox
import tkinter as tk

main_lst=[]

def save_to_csv(list):
   with open("data.csv","a") as file:
      Writer=writer(file)
      Writer.writerow(["Name","Phone"])
      Writer.writerow(list)
      messagebox.showinfo("Уведомление","Saved succesfully")

def write_txt(data):
    with open('phone_book.txt','a') as file:
        file.write(data[0] + " " + data[1])
        file.write('\n')

def add_text():
    name_1 = name.get()
    phone_1 = phone.get()
    if name_1 and phone_1:
        print(name_1, phone_1)
        main_lst.clear()
        main_lst.append(name_1)
        main_lst.append(phone_1)
        save_to_csv(main_lst)
        write_txt(main_lst)
    else:
        print('Вы не указали имя контакта ')



win = tk.Tk()
h = 250
w = 200
win.config(bg = '#F8F8FF')
win.title('Phone book')
win.geometry(f'{h}x{w}+100+200')
win.minsize(300,400)
win.maxsize(700,800)

LabelL1 = Label(win, font=('Arial', 15), text = 'Name:', padx=20, pady=10, bg='#F8F8FF')
LabelL2 = Label(win, font=('Arial', 15), text = 'Phone:', padx=20, pady=10, bg='#F8F8FF')

LabelL1.grid(row=0,column=0)
LabelL2.grid(row=1,column=0)

name = tk.Entry(win, font=('Arial', 15), width=15, bd=3, bg='#E6E6FA')
name.grid(row=0,column=1, columnspan=5,stick='e')

phone = tk.Entry(win, font=('Arial', 15), width=15, bd=3, bg='#E6E6FA')
phone.grid(row=1,column=1, columnspan=5,stick='e')

tk.Button(text='Enter', bd=3, bg='#6A5ACD', font=('Arial', 15, 'bold'), command=lambda : add_text()).grid(row=3,column=5, stick= 'e', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(3, minsize=60)


win.mainloop()
