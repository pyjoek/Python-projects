from tkinter import messagebox
from tkinter import *
from functools import partial
import os

root = Tk()
root.title("HACK THE BOX")
root.geometry("700x400")

root.resizable(False, False)

# username
user = Label(text="USER NAME",fg="white",font=(60)).place(x=310,y=100)
username = StringVar()
usernames = Entry(root,width=30,textvariable = username).place(x=250,y=123)

# password
password = Label(text="PASSWORD",fg="white",font=(60)).place(x=310,y=160)
password = StringVar()
passwords = Entry(root,width=30,textvariable = password,show="*").place(x=250,y=185)



def dead():
    toor = Tk()
    toor.title("longer")
    toor.geometry("700x400")
    toor.resizable(False,False)
    gamelabel = Label(toor,text = "CHOOSE A GAME TO PLAY").place(x = 310, y = 80)

    def tetriss():
        import tetris

    frame = Frame(toor, width=700,height = 400,bg = "black").pack()
    games = Label(toor, text = "CHOOSE A GAME TO PLAY",fg = "white",bg = "black", width = 40).place(x = 300, y = 10)
    ttetris = Button(toor,text = "tetris",command = tetriss, width = 40).place(x = 300, y = 10``)

    mainloop()

def validate(username, password):
    if username.get() == "joel" and password.get() == "vero":
        messagebox.showinfo("succesful","Access Granted")
        root.destroy()
        dead()
    else:
        messagebox.showwarning("warning","Authentication failed")

def exit():
    root.destroy()

validate = partial(validate, username, password)

# login
loginbtn = Button(root,text="Login",fg="white",font=(40),command=validate).place(x=250,y=230)

# exit
exitbtn = Button(root,text="Exit",fg="white",font=(40),command=exit).place(x=400,y=230)

root.mainloop()
