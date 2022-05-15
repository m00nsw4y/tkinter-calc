from tkinter import *

root = Tk()
root.title('Calculadora')

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(num):
    e.delete(0, END)
    e.insert(0, str(e.get()) + str(numero))

def button_clear():
    e.delete(0, END)

def button_sum():
    num_1 = e.get()
    global f_num 
    global math
    math = 'sum'
    f_num = int(num_1)
    e.delete(0, END)

def button_equal():
    num_2 = e.get()
    e.delete(0, END)
    if math=='sum':
        e.insert(0, f_num + int(num_2))
    elif math=='subtract':
        e.insert(0, f_num - int(num_2))
    elif math=='multiply':
        e.insert(0, f_num * int(num_2))
    elif math=='divide':
        e.insert(0, f_num / int(num_2))

def button_sub():
    num_1 = e.get()
    global f_num 
    global math
    math = 'subtract'
    f_num = int(num_1)
    e.delete(0, END)

def button_mult():
    num_1 = e.get()
    global f_num 
    global math
    math = 'multiply'
    f_num = int(num_1)
    e.delete(0, END)

def button_divide():
    num_1 = e.get()
    global f_num 
    global math
    math = 'divide'
    f_num = int(num_1)
    e.delete(0, END)


#Setting buttons
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text='+', bg = '#F6B4C3', padx=39, pady=20, command=button_sum)
button_equal = Button(root, text='=', bg = '#F4F4DC', padx=91, pady=20, command=button_equal)
button_clear = Button(root, text='Limpar', bg = '#BECAE5', padx=79, pady=20, command= button_clear)
button_subtract = Button(root, text='-', bg='#F1D4C8', padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text='x', bg = '#C3BAD6', padx=41, pady=20, command=button_mult)
button_divide = Button(root, text='/', bg='#C9DDD5', padx=40, pady=20, command=button_divide)

#Buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row= 2, column=0)
button_5.grid(row= 2, column=1)
button_6.grid(row= 2, column=2)

button_7.grid(row= 1, column=0)
button_8.grid(row= 1, column=1)
button_9.grid(row= 1, column=2)

button_0.grid(row= 4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column =1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
        
