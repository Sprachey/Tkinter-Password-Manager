#JSON is JavaScript Object Notation. It means that a script (executable) file which is made of text 
# in a programming language, is used to store and transfer the data. Python supports JSON through a 
# built-in package called JSON. To use this feature, we import the JSON package in Python script.
#The text in JSON is done through quoted-string which contains the value in key-value mapping within { }.

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    
    password_letters=[random.choice(letters) for c in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_symbols=[random.choice(symbols) for s in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_numbers=[random.choice(numbers) for n in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)  
    pyperclip.copy(password)

# ---------------------------- Find PASSWORD ------------------------------- #    

def find_password():
    website=website_entry.get()
    try:
        with open("data.json","r") as datafile:
            data=json.load(datafile) #load() is used to read data in json file
            
    except FileNotFoundError:        
        messagebox.showerror(title="Error",message=f"No Data File found")
    
    else:
        if website in data:
                email=data[website]["email"]
                password=data[website]["Password"]
                messagebox.showinfo(title=website,message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showerror(title=website,message=f"No details for {website} exists")
        
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    email=email_entry.get()
    website=website_entry.get()
    password=password_entry.get()
    new_data={
        website:
    {
        "email":email,
        "Password":password,}}

    if len(website)==0 or len(password)==0 or len(email)==0:
        messagebox.showerror(title="Oops",message="Please don't leave any field empty.")
    
    else:
        try:
            with open("data.json","r") as datafile:
                data=json.load(datafile)
                data.update(new_data) #update() is used to update data in json file
            

            with open("data.json","w") as datafile:
                json.dump(data,datafile,indent=4) #dump() is used to add data in json file
        except FileNotFoundError:
            with open("data.json","w") as datafile:
                json.dump(new_data,datafile,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

    
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.minsize(width=400,height=400)
window.title("Password Manager")
window.config(padx=50,pady=50)

img=PhotoImage(file="logo.png")
canvas=Canvas(width=200,height=200,bg="yellow")
canvas.create_image(110,110,image=img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:",bg="yellow")
website_label.grid(row=1,column=0)

website_entry=Entry(width=29)
website_entry.grid(row=1,column=1,columnspan=1)
website_entry.focus()

email_label=Label(text="Email|Username:",bg="yellow")
email_label.grid(row=2,column=0)

email_entry=Entry(width=50)
email_entry.insert(0,"sheikh@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)

password_label=Label(text="Password:",bg="yellow")
password_label.grid(row=3,column=0)

password_entry=Entry(width=29)
password_entry.grid(row=3,column=1,columnspan=1)

generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

search_button=Button(text="Search",width=15,command=find_password)
search_button.grid(row=1,column=2)

window.mainloop()