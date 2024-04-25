import tkinter as tk
from tkinter import *
from tkinter import messagebox, simpledialog


def add_task():
    task = simpledialog.askstring('Add Task', 'Enter Your Task: ')
    if task is not None and len(task.strip()) > 0:
        listbox_tasks.insert(tk.END, task)
        save_tasks()
    else:
        messagebox.showerror(title="ERROR", message="Please Enter a Task.")

def edit_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        old_task = listbox_tasks.get(task_index)
        new_task = simpledialog.askstring("Edit Task", "Edit your task:", initialvalue=old_task)
        if new_task:
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, new_task)
            save_tasks()
    except IndexError:
        pass

def delete_task():
    delete_selected_task(listbox_tasks)
    delete_selected_task(listbox_completed_tasks)

def delete_selected_task(listbox):
    try:
        task_index = listbox.curselection()[0]
        input = messagebox.askyesno("Confirm Delete", "Do you really want to delete this task?")
        if input:
            listbox.delete(task_index)
            if listbox is listbox_tasks:
                save_tasks()
    except IndexError:
        pass

def clear_all():
    input = messagebox.askyesno("Confirm Clear All data", "Do you really want to clear all tasks?")
    if input:
        listbox_tasks.delete(0, tk.END)
        listbox_completed_tasks.delete(0, tk.END)
        save_tasks()

def complete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(task_index)
        listbox_tasks.delete(task_index)
        listbox_completed_tasks.insert(tk.END, task)
        save_tasks()
    except IndexError:
        pass

def uncomplete_task():
    try:
        task_index = listbox_completed_tasks.curselection()[0]
        task = listbox_completed_tasks.get(task_index)
        listbox_completed_tasks.delete(task_index)
        listbox_tasks.insert(tk.END, task)
    except IndexError:
        pass

def save_tasks():
    with open("./icons/tasks.txt", "w") as f:
        f.write("\n".join(listbox_tasks.get(0, tk.END)))

def load_tasks():
    try:
        with open("./icons/tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass


root = tk.Tk()
root.title("To-Do List")

canvas = tk.Canvas(root, width=450, height=650)
canvas.grid(row=0, column=0, columnspan=6, rowspan=5)

background = tk.PhotoImage(file="./icons/final_bg.png")
canvas.create_image(225, 325, image=background)

canvas.create_text(214, 35, text="☑ To-Do List", font=("Dancing Script", 27, "bold"), fill="#ddc29f")
canvas.create_text(70, 75, text="All Task:", font=("Josefin Sans", 14, "bold"), fill="#ddc29f")
canvas.create_text(110, 325, text="Completed Task:", font=("Josefin Sans", 15, "bold"), fill="#ddc29f")

frame_tasks = tk.Frame(canvas)
canvas.create_window(34, 92, anchor=tk.NW, window=frame_tasks)

listbox_tasks = tk.Listbox(frame_tasks, height=8, width=38, bg="#ecd5b1", font=("Josefin Sans", 12), selectbackground="#06171f")
listbox_tasks.grid(row=0, column=0)
listbox_tasks.config(foreground="#06171f")

frame_completed_task = tk.Frame(canvas)
canvas.create_window(34, 342, anchor=tk.NW, window=frame_completed_task)

listbox_completed_tasks = tk.Listbox(frame_completed_task, height=7, width=38, bg="#ecd5b1", font=("Josefin Sans", 12), selectbackground="#06171f")
listbox_completed_tasks.grid(row=1, column=0)
listbox_completed_tasks.config(foreground="#06171f")

plus = PhotoImage(file="./icons/plus_icon.png")
button_add_task = tk.Button(root, image=plus, highlightthickness=0, text="Add Task", command=add_task)
button_add_task.grid(row=4, column=0, rowspan=2)

cross = PhotoImage(file="./icons/cross_icon.png")
button_delete_task = tk.Button(root, image=cross, text="Delete Task", command=delete_task)
button_delete_task.grid(row=4, column=1, rowspan=2)

complete = PhotoImage(file="./icons/tick_icon.png")
button_complete_task = tk.Button(root, image=complete, text="Complete Task", command=complete_task)
button_complete_task.grid(row=4, column=2, rowspan=2)

uncomplete = PhotoImage(file="./icons/not_complete_icon.png")
button_uncomplete_task = tk.Button(root, image=uncomplete, text="Uncomplete Task", command=uncomplete_task)
button_uncomplete_task.grid(row=4, column=3, rowspan=2)

clear = PhotoImage(file="./icons/clear_icon.png")
button_clear_all = tk.Button(root, image=clear, text="Clear All", command=clear_all)
button_clear_all.grid(row=4, column=4, rowspan=2)

edit = PhotoImage(file="./icons/edit_icon.png")
button_edit_task = tk.Button(root, image=edit, text="Edit Task", command=edit_task)
button_edit_task.grid(row=4, column=5, rowspan=2)

load_tasks()

root.mainloop()


