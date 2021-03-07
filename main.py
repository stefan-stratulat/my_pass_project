from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)
    global password
    password = "".join(password_list)
    password_input.insert(0,f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()

    if len(website_data)== 0 or len(password_data):
        messagebox.showerror(title="Oops!", message="Please don't leave any empy fields!")

    else:
        is_ok = messagebox.askokcancel(title=website_input,
            message=f"There are the details entered:\nEmail: {email_data}\nPassword:{password_data}\nIs it ok to save?")

        if is_ok:
            with open('data.txt','a+') as file:
                file.write(website_data+" | "+email_data+" | "+ password_data+"\n")

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

#WINDOW
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#CANVAS
lock_image = PhotoImage(file = "logo.png")
canvas = Canvas(width = 200, height = 200)
canvas.create_image(100,100, image=lock_image)

#LABELS
website_label = Label(text="Website")
email_label = Label(text="Email/Username")
password_label = Label(text="Password")

#ENTRY WIDGETS
website_input = Entry(width=40)
website_input.focus()
email_input = Entry(width=40)
email_input.insert(0,"example@gmail.com")
password_input = Entry(width=22)

#BUTTONS
password_button = Button(text="Generate Password",command=generate_password)
add_button = Button(text="Add",width=35,command=save_data)

#GRID
#col 0
website_label.grid(row=1,column=0)
email_label.grid(row=2,column=0)
password_label.grid(row=3,column=0)
#col 1
canvas.grid(row=0,column=1)
website_input.grid(row=1,column=1,columnspan=2)
email_input.grid(row=2,column=1,columnspan=2)
password_input.grid(row=3,column=1)
add_button.grid(row=4,column=1,columnspan=2)
#col 2
password_button.grid(row=3,column=2)

window.mainloop()
