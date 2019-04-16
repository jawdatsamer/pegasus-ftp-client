#! /usr/bin/pyhton3

import tkinter
from tkinter import ttk
from tkinter import BOTH, END, LEFT
import ftplib


form = tkinter.Tk()
ftp = ftplib.FTP()

form.title("Start Connection")
w = 600
h = 550
sh = form.winfo_screenheight()
sw = form.winfo_screenwidth()
x = (sw - w) / 2
y = ( sh - h ) / 2
form.geometry("{}x{}+{}+{}".format(w,h,int(x),int(y)))
form.resizable(False,False)
form.config(background="#36393E")
fnt = ("tahoma",10)

def connectServer():
    ip = ip_input.get()
    port = int(port_input.get())
    try:
        msg = ftp.connect(ip,port)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
        username_label.place(x=200,y=20)
        username_input.place(x=200,y=40)
        pass_label.place(x=200,y=65)
        pass_input.place(x=200,y=85)
        login_button.place(x=222,y=110)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to connect")

def loginServer():
    user = username_input.get()
    password = pass_input.get()
    try:
        msg = ftp.login(user,password)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
        username_label.place_forget()
        username_input.place_forget()
        pass_label.place_forget()
        pass_input.place_forget()
        login_button.place_forget()
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to login")


    
def closeConnection():
    try:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Closing connection...")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,ftp.quit())
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to disconnect")


#Server response text box
text_servermsg = tkinter.Text(form)

ip_label = ttk.Label(form,text = "IP or Hostname")
ip_input = ttk.Entry(form)
ip_label.config(font=fnt,background="#36393E",foreground="#D3D3D3")
ip_input.config(font=fnt)
ip_label.pack()
ip_input.pack()

port_label = ttk.Label(form,text = "Port")
port_input = ttk.Entry(form)
port_label.config(font=fnt,background="#36393E",foreground="#D3D3D3")
port_input.config(font=fnt)
port_label.pack()
port_input.pack()

username_label = ttk.Label(form,text = "Username")
username_input = ttk.Entry(form)
username_label.config(font=fnt,background="#36393E",foreground="#D3D3D3")
username_input.config(font=fnt)
username_label.pack()
username_input.pack()

pass_label = ttk.Label(form,text = "Password")
pass_input = ttk.Entry(form)
pass_label.config(font=fnt,background="#36393E",foreground="#D3D3D3")
pass_input.config(font=fnt)
pass_label.pack()
pass_input.pack()

connect_button = ttk.Button(form, text="Start Connection", command=connectServer)
connect_button.pack()
login_button = ttk.Button(form,text="Connect",command=loginServer)


#Place widgits
username_label.place(x=200,y=20)
username_input.place(x=200,y=40)
pass_label.place(x=200,y=65)
pass_input.place(x=200,y=85)
ip_label.place(x=20,y=20)
ip_input.place(x=20,y=40)
port_label.place(x=20,y=65)
port_input.place(x=20,y=85)
connect_button.place(x=40,y=110)
text_servermsg.place(x=20,y=150)

def login_form():
    form.mainloop()