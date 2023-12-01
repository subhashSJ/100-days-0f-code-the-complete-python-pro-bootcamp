from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + [choice(
        symbols) for _ in range(randint(2, 4))] + [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \n Email: {email} \n Password: {password} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(
                    f"{website} | {email} | {password} \n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)

            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, pady=5)

website_entry = Entry(width=45)
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0, pady=5)

email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "jadhavsubhash511@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0, pady=5)

password_entry = Entry(width=34)
password_entry.grid(row=3, column=1, pady=5)

generate_pwd_btn = Button(text="Generate", command=generate_password)
generate_pwd_btn.grid(row=3, column=2, pady=5)

add_pwd_btn = Button(text="Add", width=38, command=save_data)
add_pwd_btn.grid(row=4, column=1, columnspan=2, pady=5)


window.mainloop()
