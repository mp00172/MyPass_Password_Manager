import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    password = "".join(password_list)
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)

    pyperclip.copy(password)   # copies password to clipboard
    copied_label.config(text="Password copied to clipboard!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_clicked():
    search_data((website.get().strip(" ")).lower())


def search_data(website):
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="Database not found.")
    else:
        try:
            match = data[website.lower()]
        except KeyError:
            messagebox.showwarning(title="Error", message="Website '{}' not found in database.".format(website))
        else:
            messagebox.showinfo(title=website.title(),
                                message="E-mail/Username: {}\n"
                                        "Password: {}".format(match["e-mail/username"], match["password"]))
    clear_fields()


def add_clicked():
    check_empty_entries((website.get()).strip(" "), (email_username.get()).strip(" "), (password.get()).strip(" "))


def check_empty_entries(website, username, password):
    if not website.strip(" ") or not username.strip(" ") or not password.strip(" "):
        messagebox.showwarning(title="Oops!", message="Don't leave any of the fields empty!")
    else:
        ask_confirmation(website, username, password)


def ask_confirmation(website, username, password):
    confirmed = messagebox.askokcancel(title="Confirm your entry",
                                       message=f"You entered following data:\n\n" \
                                               f"Website: {website}\n" \
                                               f"E-mail/Username: {username}\n" \
                                               f"Password: {password}\n\n" \
                                               f"Is it OK to save?")
    if confirmed:
        create_new_data_dict(website, username, password)


def create_new_data_dict(website, username, password):
    new_data_dict = {
        website: {
            "e-mail/username": username,
            "password": password
        }
    }
    write_to_file(new_data_dict)


def write_to_file(new_data_dict):
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data_dict, data_file, indent=4)
    else:
        data.update(new_data_dict)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        success()


def success():
    messagebox.showinfo(title="Success", message="Data saved successfully.")
    clear_fields()


def clear_fields():
    website_entry.delete(0, 'end')
    website_entry.focus()
    email_username_entry.delete(0, 'end')
    email_username_entry.insert(0, "example@email.com")
    password_entry.delete(0, 'end')
    copied_label.config(text="")


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

logo_image = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=0, columnspan=3)

website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")

website = tk.StringVar()
website_entry = tk.Entry(width=21, textvariable=website)
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()                                       # Prilikom pokretanja programa cursor će automatski biti na ovom mjestu.

search_button = tk.Button(text="Search", width=14, command=search_clicked)
search_button.grid(row=1, column=2)

email_username_label = tk.Label(text="E-mail/Username:")
email_username_label.grid(row=2, column=0, sticky="e")

email_username = tk.StringVar()
email_username_entry = tk.Entry(width=39, textvariable=email_username)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_username_entry.insert(0, "example@email.com")         # 0 predstavlja index chara na koji se upisuje defaultni text. Također možemo koristiti END koji je tkinter konstanta, a predstavlja zadnji char.

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

password = tk.StringVar()
password_entry = tk.Entry(width=21, textvariable=password)
password_entry.grid(row=3, column=1, sticky="w")

password_button = tk.Button(text="Generate Password", width=14, command=generate_password)
password_button.grid(row=3, column=2, sticky="w")

add_button = tk.Button(text="Add", width=36, command=add_clicked)
add_button.grid(row=4, column=1, columnspan=2)

copied_label = tk.Label(text="", font=("arial", 10, "normal"), height=2, anchor="s")
copied_label.grid(row=5, column=1, columnspan=2)

window.mainloop()


