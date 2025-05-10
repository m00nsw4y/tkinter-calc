import tkinter as tk

root = tk.Tk()
root.title('Calculator')

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

calc_state = {
    "first_num": None,
    "operation": None
}

def button_click(num):
    entry.insert(tk.END, str(num))

def button_clear():
    entry.delete(0, tk.END)

def set_operation(op):
    try:
        calc_state["first_num"] = float(entry.get())
        calc_state["operation"] = op
        entry.delete(0, tk.END)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro")

def button_equal():
    try:
        second_num = float(entry.get())
        entry.delete(0, tk.END)
        result = None
        if calc_state["operation"] == "add":
            result = calc_state["first_num"] + second_num
        elif calc_state["operation"] == "sub":
            result = calc_state["first_num"] - second_num
        elif calc_state["operation"] == "mul":
            result = calc_state["first_num"] * second_num
        elif calc_state["operation"] == "div":
            result = calc_state["first_num"] / second_num
        if result is not None:
            entry.insert(0, str(result))
    except (ValueError, TypeError, ZeroDivisionError):
        entry.insert(0, "Erro")

# Botões numéricos
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0)
]

for (text, row, col) in buttons:
    tk.Button(root, text=text, padx=40, pady=20,
              command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Outros botões
tk.Button(root, text='Limpar', bg='#BECAE5', padx=79, pady=20, command=button_clear).grid(row=4, column=1, columnspan=2)
tk.Button(root, text='+', bg='#F6B4C3', padx=39, pady=20, command=lambda: set_operation('add')).grid(row=5, column=0)
tk.Button(root, text='=', bg='#F4F4DC', padx=91, pady=20, command=button_equal).grid(row=5, column=1, columnspan=2)
tk.Button(root, text='-', bg='#F1D4C8', padx=40, pady=20, command=lambda: set_operation('sub')).grid(row=6, column=0)
tk.Button(root, text='x', bg='#C3BAD6', padx=41, pady=20, command=lambda: set_operation('mul')).grid(row=6, column=1)
tk.Button(root, text='/', bg='#C9DDD5', padx=40, pady=20, command=lambda: set_operation('div')).grid(row=6, column=2)

root.mainloop()
