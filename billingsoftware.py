from tkinter import *
import random
from tkinter import messagebox

root=Tk()
root.title('Billing Software')
root.geometry('1280x720')

#variables
c_name=StringVar()
c_phone=StringVar()

item=StringVar()
rate=IntVar()
quantity=IntVar()

bill_no=StringVar()


global l
l=[]

#functions
def welcome():
	x=random.randint(1000,9999)
	bill_no.set(str(x))
	textarea.delete(1.0,END)
	textarea.insert(INSERT,"\t Welcome to Sample SuperMarket")
	textarea.insert(INSERT,f'\n\nBill Number:\t\t{bill_no.get()}')
	textarea.insert(END,f'\nCustomer Name:\t\t{c_name.get()}')
	textarea.insert(END,f'\nPhone Number:\t\t{c_phone.get()}')	
	textarea.insert(END,f'\n====================================')
	textarea.insert(END,'\n Product\t\t QTY\t\t Price')
	textarea.insert(END,f'\n====================================')
	textarea.configure(font='arial 15 bold')
	
def additm():
	n=rate.get()
	m=quantity.get()*n
	l.append(m)
	if item.get()=='':
		messagebox.showerror('Error','Please Enter the item')
	else:
		textarea.insert(END,f'\n{item.get()}\t\t{quantity.get()}\t\t{m}')
	
	

def gbill():
	if c_name.get()=='' or c_phone.get()=='':
		messagebox.showerror('Error','Customer Details are must')
	else:
		tex=textarea.get(8.0,END)
		welcome()
		textarea.insert(END,tex)
		textarea.insert(END,f'\n====================================')
		textarea.insert(END,f'\nTotal Paybill Amount :\t\t{sum(l)}')
		textarea.insert(END,f'\n====================================')
		savebill()

def savebill():
	op=messagebox.askyesno('Save bill','Do you want to save the bill')
	if op>0:
		bill_details=textarea.get(1.0,END)
		f1=open("bills/"+str(bill_no.get())+'.txt','w')
		f1.write(bill_details)
		f1.close()
		messagebox.showinfo('Saved ',f'Bill Number :{bill_no.get()}')
	else:
		return

def clear():
	c_name.set('')
	c_phone.set('')
	item.set('')
	rate.set(0)
	quantity.set(0)
	welcome()
	l.clear()
	
def exit():
	op=messagebox.askyesno('Exit','Do you really want to exit ')
	if op>0:
		root.destroy()
	

title=Label(root,text='Billing Software',bd=12,relief=GROOVE,font=('times new roman',20,'bold'),bg='blue',fg='white')
title.pack(fill=X)

#customer details

F1=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),bg='blue',fg='white',bd=10,relief=GROOVE)
F1.place(x=0,y=80,relwidth=1)

cname_lbl=Label(F1,text='Customer Name',font=('times new roman',15,'bold'),bg='green',fg='white').grid(row=0,column=0,padx=10,pady=10)
cname_txt=Entry(F1,width=20,bd=5,relief=GROOVE,textvariable=c_name).grid(row=0,column=1,padx=10,pady=10)

cphone_lbl=Label(F1,text='Phone Number',font=('times new roman',15,'bold'),bg='green',fg='white').grid(row=0,column=2,padx=10,pady=10)
cphone_txt=Entry(F1,width=20,bd=5,relief=GROOVE,textvariable=c_phone).grid(row=0,column=3,padx=10,pady=10)

#Product Details
F2=LabelFrame(root,text='Product Details',font=('times new roman',15,'bold'),bg='blue',fg='white',bd=10,relief=GROOVE)
F2.place(x=20,y=180,width=630,height=500)

itm_lbl=Label(F2,text='Product Name',font=('times new roman',18,'bold'),bg='green',fg='white',bd=10,relief=GROOVE).grid(row=0,column=0,padx=10,pady=10)
itm_txt=Entry(F2,width=20,bd=5,relief=GROOVE,textvariable=item).grid(row=0,column=1,padx=30,pady=10)

rate_lbl=Label(F2,text='Product Rate',font=('times new roman',18,'bold'),bg='green',fg='white',bd=10,relief=GROOVE).grid(row=1,column=0,padx=10,pady=10)
rate_txt=Entry(F2,width=20,bd=5,relief=GROOVE,textvariable=rate).grid(row=1,column=1,padx=30,pady=10)

quantity_lbl=Label(F2,text='Product Quantity',font=('times new roman',18,'bold'),bg='green',fg='white',bd=10,relief=GROOVE).grid(row=2,column=0,padx=10,pady=10)
quantity_txt=Entry(F2,width=20,bd=5,relief=GROOVE,textvariable=quantity).grid(row=2,column=1,padx=30,pady=10)

#buttons

btn1=Button(F2,text='Add Item',font='arial 15 bold',bd=8,relief=GROOVE,bg='gold',fg='blue',width=15,command=additm)
btn1.grid(row=3,column=0,padx=10,pady=30)

btn2=Button(F2,text='Generate Bill',font='arial 15 bold',bd=8,relief=GROOVE,bg='gold',fg='blue',width=15,command=gbill)
btn2.grid(row=3,column=1,padx=10,pady=30)

btn3=Button(F2,text='Clear',font='arial 15 bold',bd=8,relief=GROOVE,bg='gold',fg='blue',width=15,command=clear)
btn3.grid(row=4,column=0,padx=10,pady=30)

btn4=Button(F2,text='Exit',font='arial 15 bold',bd=8,relief=GROOVE,bg='gold',fg='blue',width=15,command=exit)
btn4.grid(row=4,column=1,padx=10,pady=30)

#bill area
F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=700,y=175,width=500,height=500)

bill_title=Label(F3,text='Bill Area',font='arial 15 bold',bd=10,relief=GROOVE).pack(fill=X)
scroll_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scroll_y)
scroll_y.pack(side=RIGHT)
scroll_y.config(command=textarea.yview)
textarea.pack()
welcome()
root.mainloop()
