import tkinter as tk
from tkinter import *

# Group Members
#1. Faith Lomuk 
#2.Goodluck Miniph 
#3.James Ng'ang'a
def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        message="All fields are required"
        label_message.config(text=message, fg ="red")
    elif "@" not in username or "." not in username:
        message="Invalid email address"
        label_message.config(text=message, fg="red")
    elif len(password) <= 8:
        message= "Password must be more than 8 characters."
        label_message.config(text=message, fg="red")
    else:
        message= "Login successful!"
        label_message.config(text=message, fg="green")
    
# Tkinter GUI
root = tk.Tk()
root.title("Login Application - Functional Programming")
root.geometry('1166x718')
datailFlame=Frame(root,width='520',height=600,bg='black').place(x=200,y=20)
label_title = tk.Label(datailFlame, text="SIGN IN", bg="#000", font=("tahoma", 25),fg="lightgreen")
label_title.place(x=400,y=60)


label_username = tk.Label(datailFlame, text="Username (Email):", bg="#000",fg="#FF3399", font=("tahoma", 18))
label_username.place(x=240,y=130)
entry_username = tk.Entry(datailFlame,bg="#FFF",font=("tahoma", 18))
entry_username.place(x=240,y=170,width=400,height=50)


#PASSWORD
label_password = tk.Label(datailFlame, text="password", bg="#000",fg="#FF3399", font=("tahoma", 18))
label_password.place(x=240,y=250)
entry_password = tk.Entry(datailFlame,font=("tahoma", 18),show="*")
entry_password.place(x=240,y=300,width=400,height=50)

#forgot password
label_forgot_password = tk.Label(datailFlame, text="Forgot Password",  bg="#000",fg="#FF3399", font=("tahoma", 18))
label_forgot_password.place(x=240,y=390)

#signup
label_signup = tk.Label(datailFlame, text="Signup", bg="#000",fg="lightgreen", font=("tahoma", 18))
label_signup.place(x=560,y=390)

#login 
btn_login = tk.Button(datailFlame, text="Login",bg = "lightgreen", fg="#FF3399",font=("robboto",18,'bold'),command=validate_login)
btn_login.place(x=240,y=450,width='400')

#sec_error message
label_message = tk.Label(datailFlame, text="",  bg="#000",fg="#FF3399", font=("tahoma", 18))
label_message.place(x=240,y=530)
root.mainloop()