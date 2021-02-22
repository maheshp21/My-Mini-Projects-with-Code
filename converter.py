from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry('1200x700')
root.title('Interconverter')

number=IntVar()
bin_number=StringVar()
octal_number=StringVar()
decimal_number=StringVar()
hexdecimal_number=StringVar()

#functions
def enter():
	num=number.get()
	bi=bin(num)
	bin_number.set(bi)
	
	oc=oct(num)
	octal_number.set(oc)
	
	decimal_number.set(num)
	
	he=hex(num)
	hexdecimal_number.set(he)
	
def clear():
	num=number.set('')
	
	bin_number.set('')
	
	octal_number.set('')
	
	decimal_number.set('')
	
	hexdecimal_number.set('')

def exit():
	ch=messagebox.askyesno('Alert','Are you sure that you want to exit ?')
	if ch>0:
		root.destroy()
	
#labels,texts

number_lbl=Label(root,text='Number',font='arial 25 bold',bg='green',fg='white').grid(row=0,column=0,padx=100,pady=10)
number_txt=Entry(root,width=30,bd=5,relief=GROOVE,textvariable=number).grid(row=0,column=1,padx=10,pady=10)

bin_number_lbl=Label(root,text='Binary Number',font='arial 25 bold',bg='green',fg='white').grid(row=2,column=0,padx=100,pady=10)
bin_number_txt=Entry(root,width=30,bd=5,relief=GROOVE,textvariable=bin_number).grid(row=2,column=1,padx=10,pady=10)

octal_number_lbl=Label(root,text='Octal Number',font='arial 25 bold',bg='green',fg='white').grid(row=4,column=0,padx=100,pady=10)
octal_number_txt=Entry(root,width=30,bd=5,relief=GROOVE,textvariable=octal_number).grid(row=4,column=1,padx=10,pady=10)

decimal_number_lbl=Label(root,text='Deciamal Number',font='arial 25 bold',bg='green',fg='white').grid(row=6,column=0,padx=100,pady=10)
decimal_number_txt=Entry(root,width=30,bd=5,relief=GROOVE,textvariable=decimal_number).grid(row=6,column=1,padx=10,pady=10)

hexdecimal_number_lbl=Label(root,text='Hexa Decimal Number',font='arial 25 bold',bg='green',fg='white').grid(row=8,column=0,padx=100,pady=10)
hexdecimal_number_txt=Entry(root,width=30,bd=5,relief=GROOVE,textvariable=hexdecimal_number).grid(row=8,column=1,padx=10,pady=10)

#buttons

enter_btn=Button(root,text=' Enter ',font='arial 20 bold',fg='blue',bg='gray',command=enter).grid(row=10,column=1	,padx=10,pady=10)

clear_btn=Button(root,text=' Clear ',font='arial 20 bold',fg='white',bg='gray',command=clear).grid(row=14,column=0,padx=10,pady=40)

exit_btn=Button(root,text=' Exit ',font='arial 20 bold',fg='red',bg='gray',command=exit).grid(row=14,column=1,padx=10,pady=40)

root.mainloop()
