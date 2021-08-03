from tkinter import *
from functools import partial
def validateLogin(username,password):
    print("user name entered:",username.get())
    print("user name password:",password.get())
    return
tkWindow=Tk()
#tkWindow.geometry('400*150')
tkWindow.title('Tkinter Login Form - pythonexamples.org')
usernameLabel=Label(tkWindow,text="user name").grid(row=0,col=0)
username=StringVar()
usernameEntry=Entry(tkWindow,textvariable=username).grid(row=0,col=0)


passwordLabel=Label(tkWindow,text="password").grid(row=0,col=0)
password=StringVar()
passwordEntry=Entry(tkWindow,textvariable=password,show='*').grid(row=1,col=1)
validateLogin=partial(validateLogin,username,password)
loginButton=Button(tkWindow,text="Login",command=validateLogin).grid(row=4,col=0)
tkwindow.mainloop()

    