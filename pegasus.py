#! /usr/bin/pyhton3

import tkinter
from src import login
from tkinter import ttk
import ftplib

ftp = login.ftp

form = tkinter.Tk()
form.title("Pegasus FTP Client")
screenwidth = form.winfo_screenwidth()
screenheight = form.winfo_screenheight()
form.geometry("{}x{}".format(screenwidth,screenheight))
form.config(background="#36393E")
form.maxsize(screenwidth,screenheight)
form.minsize(750,650)
fnt = ("tahoma",10)

def displayDir():
    serverdir.insert(0,"--------------------------------------------")
    dirlist = []
    dirlist = ftp.nlst()
    for item in dirlist:
        serverdir.insert(0, item)

show_button = ttk.Button(form, text="Refresh List", command=displayDir)
show_button.pack()
show_button.place(x=656,y=23)

dir_label = tkinter.Label(form, text="Directory list:")
dir_label.config(font=fnt,background="#36393E",foreground="#D3D3D3")
serverdir = tkinter.Listbox(form,height=38,width=90)
dir_label.place(x=15,y=25)
serverdir.place(x=15,y=50)

login.login_form()

displayDir()

form.mainloop()