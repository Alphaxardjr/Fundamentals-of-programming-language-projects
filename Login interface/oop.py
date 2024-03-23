import tkinter as tk
from tkinter import *
import re


class LoginApplication:
    def __init__(self, master):
        self.master = master
        root.title("Login Application -oop")
        root.geometry('1166x718')
        self.datailFlame=Frame(root,width='520',height=600,bg='black').place(x=200,y=20)

        self.label_title = tk.Label(self.datailFlame, text="SIGN IN", bg="#000", font=("tahoma", 25),fg="lightgreen")
        self.label_title.place(x=400,y=60)


        self.label_username = tk.Label(self.datailFlame, text="Username (Email):", bg="#000",fg="#FF3399", font=("tahoma", 18))
        self.label_username.place(x=240,y=130)
        self.entry_username = tk.Entry(self.datailFlame,bg="#FFF",font=("tahoma", 18))
        self.entry_username.place(x=240,y=170,width=400,height=50)


        #PASSWORD
        self.label_password = tk.Label(self.datailFlame, text="password", bg="#000",fg="#FF3399", font=("tahoma", 18))
        self.label_password.place(x=240,y=250)
        self.entry_password = tk.Entry(self.datailFlame,font=("tahoma", 18),show="*")
        self.entry_password.place(x=240,y=300,width=400,height=50)

        #forgot password
        self.label_forgot_password = tk.Label(self.datailFlame, text="Forgot Password",  bg="#000",fg="#FF3399", font=("tahoma", 18))
        self.label_forgot_password.place(x=240,y=390)

        #signup
        self.label_signup = tk.Label(self.datailFlame, text="Signup", bg="#000",fg="lightgreen", font=("tahoma", 18))
        self.label_signup.place(x=560,y=390)

        #login 
        self.btn_login = tk.Button(self.datailFlame, text="Login",bg = "lightgreen", fg="#FF3399",font=("robboto",18,'bold'),command=self.validate_input)
        self.btn_login.place(x=240,y=450,width='400')

        #sec_error message
        self.label_message = tk.Label(self.datailFlame, text="",  bg="#000",fg="#FF3399", font=("tahoma", 18))
        self.label_message.place(x=240,y=530)

    def validate_input(self):
        # Get input values from entry fields
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Validate input fields
        if not username or not password:
            message= "Username and password are required."
            self.label_message.config(text=message,fg="red")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", username):
            message= "Username must be a valid email address."
            self.label_message.config(text=message,fg="red")
        elif len(password) <= 8:
            message="Password must be more than 8 characters."
            self.label_message.config(text=message,fg="red")
        else:
            message="Login successful!"
            self.label_message.config(text=message,fg="green")

root = Tk()
app = LoginApplication(root)
root.mainloop()



