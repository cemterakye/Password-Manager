from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_numbers + password_letters + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    if len(password_entry.get()) > 0:
        password_entry.delete(0,END)
        password_entry.insert(0, string=password)
    else:
        password_entry.insert(0,string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_passwords():
    new_data = {website_entry.get() : { "email" : username_entry.get(), "password" : password_entry.get()}}

    if len(website_entry.get()) == 0 or len(username_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title = "Error!",message= "Empty Fields!")

    else:

        is_okay = messagebox.askokcancel(title = website_entry.get(),message=f"These are the details entered : \nEmail : {username_entry.get()} \nPassword : {password_entry.get()} \nIs it okay to save ?")

        if is_okay:
            try:
                with open("data.json","r") as file:
                    data = json.load(file)
                    data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data,file,indent = 4)
                    website_entry.delete(0,END)
                    password_entry.delete(0,END)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data,file,indent = 4)
                    website_entry.delete(0,END)
                    password_entry.delete(0,END)



def search_password():
    to_search = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
            email = data[to_search]["email"]
            password = data[to_search]["password"]
            messagebox.showinfo(title = to_search,message= f"Email : {email}\nPassword : {password}")
    except FileNotFoundError:
        messagebox.showinfo(title = "Error!",message= "There is no data to search!")
        website_entry.delete(0, END)
    except KeyError:
        messagebox.showinfo(title="Error!", message="There is no website as you typed to search!")
        website_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row = 1,column = 2)

# Website Label
website_label = Label(text="Website:")
website_label.grid(row=2, column=1)

# Website Entry
website_entry = Entry(width=32)
website_entry.grid(row=2, column=2)
website_entry.focus()

# Email/Username
username_label = Label(text="Email/Username:")
username_label.grid(row=3, column=1)

# Username Entry
username_entry = Entry(width=50)
username_entry.grid(row=3, column=2, columnspan=2)
username_entry.insert(0,string="your_email@gmail.com")

# Password Label
password_label = Label(text="Password:")
password_label.grid(row=4, column=1)

# Password Entry
password_entry = Entry(width=32)
password_entry.grid(row=4, column=2)

# Button to generate password
button = Button(text = "Generate Password",width = 14,command = password_generator)
button.grid(row = 4,column = 3)

# Button to add info
button2= Button(text = "Add",width = 43,command = save_passwords)
button2.grid(row = 5,column = 2,columnspan =2)

# Button to search
button3 = Button(text = "Search",width = 14,command = search_password)
button3.grid(row = 2,column = 3)


window.mainloop()
