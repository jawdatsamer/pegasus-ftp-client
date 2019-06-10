#! /usr/bin/pyhton3

import tkinter
from tkinter import ttk
import ftplib
from tkinter import BOTH, END, LEFT
from tkinter import Tk
import os
import subprocess
import tkinter

#This variable is used for ftp connection
ftp = ftplib.FTP()

#This part is for user interface
form = tkinter.Tk()
form.title("Pegasus FTP Client")
screenwidth = form.winfo_screenwidth()
screenheight = form.winfo_screenheight()
form.geometry("{}x{}".format(screenwidth,screenheight))
form.config(background="#36393E")
form.maxsize(screenwidth,screenheight)
form.minsize(750,650)
fnt = ("tahoma",10)

#These function used to start connection with  the ftp server
def connectServer():
    ip = ip_input.get()
    getport = port_input.get()
    if getport == "":
        port = 21
    else:
        port = int(getport)
    try:
        msg = ftp.connect(ip,port)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
        login_button.place(x=277,y=130)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to connect")

#These function used to login into the server and start the session
def loginServer():
    user = username_input.get()
    password = pass_input.get()
    try:
        msg = ftp.login(user,password)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
        login_button.place_forget()
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to login")
    displayDir()

#These function used to stop connection with the ftp server and end the session    
def closeConnection():
    try:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Closing connection...")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,ftp.quit())
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to disconnect")


#These part used for connection button and textbox
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
pass_input.config(font=fnt,show="*")
pass_label.pack()
pass_input.pack()

connect_button = ttk.Button(form, text="Start Connection", command=connectServer)
connect_button.pack()
login_button = ttk.Button(form,text="Login",command=loginServer)

username_label.place(x=245,y=40)
username_input.place(x=245,y=60)
pass_label.place(x=245,y=85)
pass_input.place(x=245,y=105)
ip_label.place(x=65,y=40)
ip_input.place(x=65,y=60)
port_label.place(x=65,y=85)
port_input.place(x=65,y=105)
connect_button.place(x=85,y=130)
text_servermsg.place(x=65,y=175,width=1200,height=130)




def displayDir():
    serverdir.insert(0,"_______________________________________________________________________")
    global dirlistfull
    global dirlist
    dirlist = []
    dirlist = ftp.nlst()
    dirlistfull = []
    ftp.dir(dirlistfull.append)
    serverpath= ftp.pwd()
    serverdir.delete(0,last=END)
    serverpath_input.delete(0,last=END)
    serverpath_input.insert(END,serverpath)
    for item in dirlistfull:
        serverdir.insert(0, item)

serverdir_label = tkinter.Label(form, text="Server Directory Path:")
serverdir_label.config(font=fnt,background="#36393E",foreground="#D3D3D3")
serverdir = tkinter.Listbox(form,height=20,width=79)
serverdir_label.place(x=65,y=325)
serverdir.place(x=65,y=350)
show_button = ttk.Button(form, text="Refresh List", command=displayDir)
show_button.pack()
show_button.place(x=466,y=323)
serverpath_input = ttk.Entry(form,width=40)
serverpath_input.pack()
serverpath_input.place(x=211,y=327)

def displayhostDir():
    hostdir.insert(0,"_______________________________________________________________________")
    dirlist = []
    path = hostpath_input.get()
    dirlist = os.listdir(path)
    hostdir.delete(0,last=END)
    hostpath_input.delete(0,last=END)
    hostpath_input.insert(END,path)
    for item in dirlist:
        hostdir.insert(0, item)

hostdir_label = tkinter.Label(form, text="Home Directory Path:")
hostdir_label.config(font=fnt,background="#36393E",foreground="#D3D3D3")
hostdir = tkinter.Listbox(form,height=20,width=79)
hostdir_label.place(x=800,y=325)
hostdir.place(x=800,y=350)
show2_button = ttk.Button(form, text="Refresh List", command=displayhostDir)
show2_button.pack()
show2_button.place(x=1201,y=323)
hostpath_input = ttk.Entry(form,width=40)
hostpath_input.pack()
hostpath_input.place(x=945,y=327)

control_label = tkinter.Label(form, text="Controls :")
control_label.config(font=fnt,background="#36393E",foreground="#D3D3D3")
control_label.place(x=500,y=40)

def changeserverDirectory():
    path = serverpath_input.get()
    if path != ftp.pwd() :
        try:
            msg = ftp.cwd(path)
            text_servermsg.insert(END,"\n")
            text_servermsg.insert(END,msg)
        except:
            text_servermsg.insert(END,"\n")
            text_servermsg.insert(END,"Unable to change directory")
        displayDir()
    else :
        serverdirectory = serverdir.get("active")
        res_num = dirlistfull.index(serverdirectory)
        return_res_name = dirlist[res_num]
        try:
            msg = ftp.cwd(return_res_name)
            text_servermsg.insert(END,"\n")
            text_servermsg.insert(END,msg)
        except:
            text_servermsg.insert(END,"\n")
            text_servermsg.insert(END,"Unable to change directory")
        displayDir()

def changehostDirectory():
    path = hostpath_input.get()
    hostpath_input.insert(END,os.getcwd())
    hostdirectory = hostdir.get("active")
    try:
        msg = os.listdir(hostpath_input.get() + hostdirectory )
        hostdir.insert(0,"_______________________________________________________________________")
        dirlist = []
        dirlist = os.listdir(hostpath_input.get() + hostdirectory)
        for item in dirlist:
                hostdir.insert(0, item)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to change directory")
 
chserverdir_button = ttk.Button(form, text="Change Directory",command=changeserverDirectory)
chserverdir_button.pack()
chserverdir_button.place(x=500,y=60,width=150,height=40)

def backserverDirectory():
    directory = ".."
    try:
        msg = ftp.cwd(directory)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to change directory")
    displayDir()


chdirback_button = ttk.Button(form, text="Parent Directory",command=backserverDirectory)
chdirback_button.pack()
chdirback_button.place(x=650,y=60,width=150,height=40)

dirname_label = ttk.Label(form, text="Enter File or Directory name to create or delete:")
dirname_label.config(font=fnt,background="#36393E",foreground="#D3D3D3")
dirname_label.pack()
dirname_label.place(x=500,y=105,width=300,height=25)
dirname_input = ttk.Entry(form)
dirname_input.pack()
dirname_input.place(x=500,y=130,width=400,height=22)


def createDirectory():
    directory = dirname_input.get()
    try:
        msg = ftp.mkd(directory)
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,msg)
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to create directory")
    displayDir()

crdir_button = ttk.Button(form, text="Create Directory",command=createDirectory)
crdir_button.pack()
crdir_button.place(x=800,y=60,width=150,height=40)

def deleteDirectory():
    directory = dirname_input.get()
    if directory == " " :
        try:
            msg = ftp.rmd(directory)
            text_servermsg.insert(END,"\n")
            text_servermsg.insert(END,msg)
        except:
            text_servermsg.insert(END,"\n")
            text_servermsg.insert(END,"Unable to delete directory")
    else:
        directory = serverdir.get("active")
        res_num = dirlistfull.index(directory)
        return_res_name = dirlist[res_num]
        try:
            msg = ftp.rmd(return_res_name)
            text_servermsg.insert(END,"\n")
            text_servermsg.insert(END,msg)
        except:
            text_servermsg.insert(END,"\n")
            text_servermsg.insert(END,"Unable to delete directory")
    displayDir()

deldir_button = ttk.Button(form, text="Delete Directory",command=deleteDirectory)
deldir_button.pack()
deldir_button.place(x=950,y=60,width=150,height=40)

def uploadFile():
    file = hostdir.get("active")
    try:
        up = open("{}\{}".format(hostpath_input.get(),file), "rb")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Uploading " + file + "...")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,ftp.storbinary("STOR " + file,up))
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to upload file")
    displayDir()

upfile_button = ttk.Button(form, text="< Upload",command=uploadFile)
upfile_button.pack()
upfile_button.place(x=600,y=350,width=150,height=40)

def downloadFile():
    file = serverdir.get("active")
    res_num = dirlistfull.index(file)
    return_res_name = dirlist[res_num]
    down = open("{}\{}".format(hostpath_input.get(),return_res_name), "wb")
    try:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Downloading " + return_res_name + "...")
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,ftp.retrbinary("RETR " + return_res_name, down.write))
    except:
        text_servermsg.insert(END,"\n")
        text_servermsg.insert(END,"Unable to download file")
    displayDir()

downfile_button = ttk.Button(form, text="Download >" , command=downloadFile)
downfile_button.pack()
downfile_button.place(x=600,y=391,width=150,height=40)

def deleteFile():
    file = dirname_input.get()
    if file == " " :
        try:
            msg = ftp.delete(file)
            text_servermsg.insert(END,"\n")
            text_servermsg.insert(END,msg)
        except:
            text_servermsg.insert(END,"\n")
            text_servermsg.insert(END,"Unable to delete file")
    else:
        file = serverdir.get("active")
        res_num = dirlistfull.index(file)
        return_res_name = dirlist[res_num]
        try:
            msg = ftp.delete(return_res_name)
            text_servermsg.insert(END,"\n")
            text_servermsg.insert(END,msg)
        except:
            text_servermsg.insert(END,"\n")
            text_servermsg.insert(END,"Unable to delete file") 
    displayDir()

delfile_button = ttk.Button(form, text="Delete File", command=deleteFile)
delfile_button.pack()
delfile_button.place(x=1100,y=60,width=150,height=40)

closeconn_button = ttk.Button(form, text="Close connection",command=closeConnection)
closeconn_button.pack()
closeconn_button.place(x=600,y=622,width=150,height=40)

form.mainloop()
