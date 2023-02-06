from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

WHITE = "#FFFFFF"
BLACK = "black"
FONT_NAME = "Arial"
LABEL_FONT_SIZE = 8
BUTTON_FONT_SIZE = 8


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    random_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    random_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    # you can use .extend() or use '+' to extend an existing list with another list
    password_list = random_letters + random_symbols + random_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Generated Password Has Been Copied", message=f"Newly generated password "
                                                                            f"has been copied to the clipboard.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "username": username,
        "password": password,
    }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Missing Field", message="Please populate all the fields.")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {username} "
                                                              f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    # saving data in a brand new file
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ----------------------------- FIND PASSWORD ---------------------------#
def find_password():
    website = website_entry.get()
    try:
        file = open("data.json", "r")
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message=f"No Data File Found.")
    else:
        data = json.load(file)
        if website not in data:
            messagebox.showinfo(title="Website Not Found", message=f"{website} is not in the password library."
                                                                   f"\nPlease add a new entry.")
        else:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title="Website Found", message=f"Website Name: {website}\n"
                                                               f"Username: {username}"
                                                               f"\nWebsite Password: {password}")
        file.close()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg=WHITE)

# Canvas
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg=WHITE, width=20)
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", bg=WHITE, width=20)
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg=WHITE, width=20)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky=EW, padx=10)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky=EW, padx=10)
username_entry.insert(0, "dummyemail@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky=EW, padx=10)

# Button
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1, sticky=EW, padx=(0, 10))

generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3, sticky=EW, padx=(0, 10))

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW, padx=10)

window.mainloop()
