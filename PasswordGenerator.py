import random

length=int(input('Enter the length of password:'))
if length>=8:
    p1='abcdefghijklmnopqrstuvwxyz'
    p2='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    p3='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    p4='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+='
    password=''
    print('Choose a level for password:')
    print('1.Basic\n2.Weak\n3.Medium\n4.Strong\n5.Very Powerful')
    a=int(input('We recommend from Medium to Very Powerful'))
    if a==1:
        for i in range(length):
            password=password+random.choice(p1)
    elif a==2:
        for i in range(length):
            password=password+random.choice(p2)
    elif a==3:
        for i in range(length):
            password=password+random.choice(p3)
    elif a==4:
        for i in range(length):
            password=password+random.choice(p4)
    elif a==5:
        for i in range(length):
            password=password+random.choice(random.choice([p1,p2,p3,p4]))
    else:
        print('Choose a level by giving 1-5')

    print("Your password is :"+password)
else:
    print('Password must be atleast 8 characters')