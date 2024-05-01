import tkinter as tk
from tkinter import *

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_backspace():
    current = entry.get()[:-1]
    entry.delete(0, END)
    entry.insert(0, current)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")

def button_percentage():
    try:
        value = float(entry.get()) / 100
        entry.delete(0, END)
        entry.insert(0, str(value))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

canvas = tk.Canvas(root, width=450, height=650)
canvas.grid(row=0, column=0, columnspan=4, rowspan=7)
canvas.create_image(225, 325)

canvas.create_text(225, 35, text="🧮 Calculator", font=("Dancing Script", 28, "bold"))

entry = Entry(width=22, font=("Dancing Script", 20, "bold"), justify="right")
entry.grid(column=0, row=1, columnspan=4)
entry.focus()

c = PhotoImage(file="./icons/c.png")
C_button = tk.Button(root, image=c, command=button_clear, borderwidth=0, highlightthickness=0)
C_button.grid(row=2, column=0)

per = PhotoImage(file="./icons/per.png")
per_button = tk.Button(root, image=per, command=button_percentage, borderwidth=0, highlightthickness=0)
per_button.grid(row=2, column=1)

erase = PhotoImage(file="./icons/erase.png")
erase_button = tk.Button(root, image=erase, command=button_backspace, borderwidth=0, highlightthickness=0)
erase_button.grid(row=2, column=2)

divide = PhotoImage(file="./icons/divide.png")
divide_button = tk.Button(root, image=divide, command=lambda: button_click("/"), borderwidth=0, highlightthickness=0)
divide_button.grid(row=2, column=3)

seven = PhotoImage(file="./icons/7.png")
button_7 = tk.Button(root, image=seven, command=lambda: button_click(7), borderwidth=0, highlightthickness=0)
button_7.grid(row=3, column=0)

eight = PhotoImage(file="./icons/8.png")
button_8 = tk.Button(root, image=eight, command=lambda: button_click(8), borderwidth=0, highlightthickness=0)
button_8.grid(row=3, column=1)

nine = PhotoImage(file="./icons/9.png")
button_9 = tk.Button(root, image=nine, command=lambda: button_click(9), borderwidth=0, highlightthickness=0)
button_9.grid(row=3, column=2)

multiple = PhotoImage(file="./icons/x.png")
multiply_button = tk.Button(root, image=multiple, command=lambda: button_click("*"), borderwidth=0, highlightthickness=0)
multiply_button.grid(row=3, column=3)

four = PhotoImage(file="./icons/4.png")
button_4 = tk.Button(root, image=four, command=lambda: button_click(4), borderwidth=0, highlightthickness=0)
button_4.grid(row=4, column=0)

five = PhotoImage(file="./icons/5.png")
button_5 = tk.Button(root, image=five, command=lambda: button_click(5), borderwidth=0, highlightthickness=0)
button_5.grid(row=4, column=1)

six= PhotoImage(file="./icons/6.png")
button_6 = tk.Button(root, image=six, command=lambda: button_click(6), borderwidth=0, highlightthickness=0)
button_6.grid(row=4, column=2)

sub = PhotoImage(file="./icons/sub.png")
sub_button = tk.Button(root, image=sub, command=lambda: button_click("-"), borderwidth=0, highlightthickness=0)
sub_button.grid(row=4, column=3)

one = PhotoImage(file="./icons/1.png")
button_1 = tk.Button(root, image=one, command=lambda: button_click(1), borderwidth=0, highlightthickness=0)
button_1.grid(row=5, column=0)

two = PhotoImage(file="./icons/2.png")
button_2 = tk.Button(root, image=two, command=lambda: button_click(2), borderwidth=0, highlightthickness=0)
button_2.grid(row=5, column=1)

three = PhotoImage(file="./icons/3.png")
button_3 = tk.Button(root, image=three, command=lambda: button_click(3), borderwidth=0, highlightthickness=0)
button_3.grid(row=5, column=2)

add = PhotoImage(file="./icons/add.png")
add_button = tk.Button(root, image=add, command=lambda: button_click("+"), borderwidth=0, highlightthickness=0)
add_button.grid(row=5, column=3)

double_zero = PhotoImage(file="./icons/00.png")
button_00 = tk.Button(root, image=double_zero, command=lambda: button_click("00"), borderwidth=0, highlightthickness=0)
button_00.grid(row=6, column=0)

zero = PhotoImage(file="./icons/0.png")
button_0 = tk.Button(root, image=zero, command=lambda: button_click(0), borderwidth=0, highlightthickness=0)
button_0.grid(row=6, column=1)

dot = PhotoImage(file="./icons/dot.png")
button_dot = tk.Button(root, image=dot, command=lambda: button_click("."), borderwidth=0, highlightthickness=0)
button_dot.grid(row=6, column=2)

equal = PhotoImage(file="./icons/equal.png")
equal_button = tk.Button(root, image=equal, command=button_equal, borderwidth=0, highlightthickness=0)
equal_button.grid(row=6, column=3)

root.mainloop()
