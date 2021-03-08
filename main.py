from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

# ---------------------------- SEARCH DATA ------------------------------- #

def search_data():
    website_data = website_input.get()
    try:
        with open('data.json','r') as file:
            #Read old data
            data = json.load(file)
    #error could happpen at first use if file not created
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File not found. Try adding data first!")
    else:
        if website_data in data:
                email = data[website_data]["email"]
                password = data[website_data]["password"]
                messagebox.showinfo(title="Password info",
                message=f"{website_data} info:\n Email:{email}\nPassword:{password}")
        else:
            messagebox.showerror(title="Error", message=f"Not details for {website_data}.")

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

    new_data = {website_data: {
        "email": email_data,
        "password": password_data
    }}

    if len(website_data)== 0 or len(password_data)==0:
        messagebox.showerror(title="Oops!", message="Please don't leave any empy fields!")
    else:
        try:
            with open('data.json','r') as file:
                #Read old data
                data = json.load(file)
                #Update old data with new data
                data.update(new_data)
        #error could happpen at first use if file not created
        except FileNotFoundError:
            with open('data.json', "w") as file:
                json.dump(new_data, file, indent=4)
        #error could happen if file exists but empty
        except json.decoder.JSONDecodeError:
            with open('data.json', "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open('data.json', "w") as file:
                json.dump(data, file, indent=4)
        finally:
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
website_input = Entry(width=22)
website_input.focus()
email_input = Entry(width=40)
email_input.insert(0,"example@gmail.com")
password_input = Entry(width=22)

#BUTTONS
password_button = Button(text="Generate Password",command=generate_password)
add_button = Button(text="Add",width=35,command=save_data)
search_button = Button(text="Search",width=15,command=search_data)

#GRID
#col 0
website_label.grid(row=1,column=0)
email_label.grid(row=2,column=0)
password_label.grid(row=3,column=0)
#col 1
canvas.grid(row=0,column=1)
website_input.grid(row=1,column=1)
email_input.grid(row=2,column=1,columnspan=2)
password_input.grid(row=3,column=1)
add_button.grid(row=4,column=1,columnspan=2)
#col 2
password_button.grid(row=3,column=2)
search_button.grid(row=1,column=2)

window.mainloop()
