from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# # ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list= password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password="".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    pas.insert(0,password)
    pyperclip.copy(password)
    
    
def otp_generator():
    otp_list=[]
    numbers=[0,1,2,3,4,5,6,7,8,9]
    for i in range(6):
        i=random.choice(numbers)
        otp_list.append(i)
    joined_integer = int(''.join(map(str, otp_list))) 
        
      
    otp.insert(0,joined_integer)
    pyperclip.copy(joined_integer)
    
        
        

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    webi=web.get()
    emai=ema.get()
    pasi=pas.get()
    new_data={webi:
        {
            "email":emai,
            "password":pasi
        }
        }
    
    if webi=="" or pasi=="":
        messagebox.showerror(title="Oops",message="Please don't leave any fields empty")
    
    else:
        try:
            with open ("data.json","r") as data_file:
                # Reading old data
                data=json.load(data_file)
        except FileNotFoundError:
                with open ("data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)    
        else:
                # Updating old data
                data.update(new_data)
            
                with open ("data.json","w") as data_file:
                    # Saving updated datd
                    json.dump(data,data_file,indent=4)
        finally:
                web.delete(0,END)
                pas.delete(0,END)
                

def search():
  
    search_website=web.get()
    try:
        with open ("data.json","r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found!")
    else:
            if  search_website in data:
                email=data[search_website]["email"]
                password=data[search_website]["password"]
                messagebox.showinfo(title=website,message=f"Email : {email}\nPassword:{password}")
            else:
                messagebox.showinfo(title="Error",message=f"No Details for {search_website} exists.")
        
# # ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas=Canvas(height=200,width=200)
# logo_img=PhotoImage(file="logo.png")
# canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)


website=Label(text="Website:")
website.grid(column=0,row=1)


email=Label(text="Email/Username:")
email.grid(column=0,row=2)

password=Label(text="Password:")
password.grid(column=0,row=3)

web=Entry(width=30)
web.grid(column=1,row=1,columnspan=2)
web.focus()

ema=Entry(width=40)
ema.grid(column=1,row=2,columnspan=2)
ema.insert(0,"smithdoshi1002@gmail.com")

pas=Entry(width=25)
pas.grid(column=1,row=3)

otp=Entry(width=25)
otp.grid(column=1,row=4)

gen_pas=Button(text="Generate Password",command=generate_password)
gen_pas.grid(column=2,row=3)
gen_pas=Button(text="Generate OTP",command=otp_generator)
gen_pas.grid(column=2,row=4)

add_pas=Button(text="Add",width=36,command=save)
add_pas.grid(column=1,row=5,columnspan=2)

sea_but=Button(text="Search",command=search,width=15)
sea_but.grid(column=2,row=1)

window.mainloop()