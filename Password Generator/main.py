from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog, Text, Tk
from random import choice, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    pass_len = simpledialog.askstring('Generating Password', 'Enter numbers of Letter, Numbers and '
                                                             'Symbols?\n(Seperate by comma)').split(",")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(int(pass_len[0]))]
    pass_symbols = [choice(symbols) for _ in range(int(pass_len[1]))]
    pass_num = [choice(numbers) for _ in range(int(pass_len[2]))]

    password_list = pass_letters + pass_symbols + pass_num

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(1.0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    website = website_entry.get("1.0", "end-1c").strip()
    emails = email_entry.get("1.0", "end-1c").strip()
    passwords = password_entry.get("1.0", "end-1c").strip()

    if len(website) == 0 or len(passwords) == 0:
        messagebox.showerror(title="ERROR", message="Please make sure you haven't left any field empty.")
        return

    new_data = {
        website.upper(): {
            "Email": emails,
            "Password": passwords,
        }
    }

    try:
        with open("saved_password.json", "r") as pass_file:
            data = json.load(pass_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # If file doesn't exist or is empty, initialize an empty dictionary

    data.update(new_data)

    with open("saved_password.json", 'w') as pass_file:
        json.dump(data, pass_file, indent=4)

    # Clear entry fields and focus on website entry for convenience
    website_entry.delete(1.0, END)
    password_entry.delete(1.0, END)
    website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("PASSWORD MANAGER")
window.config(padx=5, pady=5)

canvas = tk.Canvas(window, width=500, height=500)
canvas.grid(row=0, column=0, columnspan=4, rowspan=9)
# my_pass_img = PhotoImage(file="LOGOO.png")
background = PhotoImage(file="NGBG.png")
canvas.create_image(250, 250, image=background)
# canvas.grid(column=1, row=0)

# LABELS
website_label = Label(text="Website :", font=("Josefin Sans", 12, "bold"),
                      bg="#ECE8DF", fg="#033C68")
website_label.grid(sticky=W, column=1, row=4, rowspan=2)


email = Label(text="Email/Username :", font=("Josefin Sans", 12, "bold"),
                      bg="#ECE8DF", fg="#033C68")
email.grid(sticky=W, column=1, row=5, rowspan=2)


password_label = Label(text="Password :", font=("Josefin Sans", 12, "bold"),
                      bg="#ECE8DF", fg="#033C68")
password_label.grid(sticky=W, column=1, row=6, rowspan=2)


# ENTRY
website_entry = Text(window, height=1, width=25, font=("Josefin Sans", 12, "bold", "italic"), bg="#ECE8DF",
                     fg="#033C68")
website_entry.focus()
website_entry.grid(column=2, row=4, rowspan=2)

# email_entry = Entry(width=25)
email_entry = Text(window, height=1, width=25, font=("Josefin Sans", 12, "bold", "italic"), bg="#ECE8DF",
                   fg="#033C68")
email_entry.grid(column=2, row=5, rowspan=2)

password_entry = Text(window, height=1, width=25, font=("Josefin Sans", 12, "bold", "italic"), bg="#ECE8DF",
                      fg="#033C68")
password_entry.grid(column=2, row=6, rowspan=2)

# BUTTONS
generate_button = Button(text="Generate Password", command=generate_pass, font=("Dancing Script", 15, "bold"),
                         bg="#FFF757", fg="#033C68", width=18)
generate_button.grid( column=2, row=7, rowspan=2, columnspan=2)

add_button = Button(text="Add", command=add_data, font=("Dancing Script", 15, "bold"), bg="#FFF757", fg="#033C68",
                    width=11)
add_button.grid(sticky=E, column=1, row=7, rowspan=2)

window.mainloop()
