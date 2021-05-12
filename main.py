# Importing the required modules
import random
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """This function generates a random password."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    random.shuffle(password_list)

    random_password = "".join(password_list)

    password_entry.insert(0, random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    """This function takes the various user inputs and saves it inside a text file."""
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please make sure you do not leave any fields empty.')
    else:
        yes = messagebox.askyesno(title=website, message=f'The details entered are: \nEmail: {email} '
                                                         f'\nPassword: {password} \nDo you wish to save these ?')
        if yes:
            with open('passwords.txt', mode='a') as file:
                file.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Creating the window for the application
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Creating the canvas for the application
canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Creating the various labels for the fields using tkinter's Label class
website_label = Label(text='Website')
website_label.grid(column=0, row=1)

email_username = Label(text='Email/Username')
email_username.grid(column=0, row=2)

password = Label(text='Password')
password.grid(column=0, row=3)

# Creating the input fields using tkinter's Entry class
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, 'your_email@example.com')

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1)

# Creating the buttons using tkinter's Button class
generate_pass = Button(text='Generate Password', command=generate_password)
generate_pass.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

# To keep the window running to get the display
window.mainloop()
