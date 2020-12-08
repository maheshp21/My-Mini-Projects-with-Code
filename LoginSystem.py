from tkinter import *
import tkinter.messagebox as MessageBox

def validate():
    user_name=t_uname.get()
    passwd=t_password.get()
    if user_name=='username' and passwd=='password':
        MessageBox.showinfo("logged in",'Successfully')
    else:
        MessageBox.showinfo("Sorry","Invalid Credientials")

fontchang =('Verdana',15)

root=Tk()
root.geometry("600x400")
root.configure(bg="red")

title=Label(root,text="Login Form",fg="white",bg="blue",font=("bold",25))
title.place(x=350,y=30)

uname=Label(root,text="User Name :",fg="white",bg="blue",font=("bold",15))
uname.place(x=100,y=120)

password=Label(root,text=" Password :",fg="white",bg="blue",font=("bold",15))
password.place(x=100,y=200)

t_uname=Entry(font=fontchang)
t_uname.place(x=300,y=120)

t_password=Entry(show="*",font=fontchang)
t_password.place(x=300,y=200)

submit=Button(root,text="Login",fg="white",bg="green",font=("bold",15),command=validate)
submit.place(x=350,y=300)

root.mainloop()