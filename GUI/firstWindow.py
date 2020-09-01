import tkinter
import time
from datetime import date
from datetime import datetime
from tkinter import *
import tkinter as tk
from tkinter import ttk
import threading
from Security.User import User
from FileSystem.Folder import Folder
from tkinter import messagebox
import os
from DB.LectorJSON import LectorJSON


class firstWindow:

    def __init__(self, window, listUser):
        self.window = window
        self.listUser = listUser
        self.window.resizable(0,0)
        self.window.title("JMMR")
        self.window.geometry('1000x600+30+30')
        self.fondo = None
        self.img ="GUI/Images/Logo.png"
        self.widges()

    def widges(self):
        imgFondo = tk.PhotoImage(file= self.img)
        self.fondo = tk.Label(self.window, image=imgFondo)
        self.fondo.pack(side='top', fill='both', expand='yes')

        self.lbEnter= tk.Label(self.window, text=" Enter as: ", fg="white", background="black")
        self.lbEnter.place(x=475,y=420)

        self.btnUser= tk.Button(self.window, text="Admin", command= self.startLoginAdmin)
        self.btnUser.config(width=10)
        self.btnUser.place(x=425,y=450)
        self.btnGuest = tk.Button(self.window, text="Guest", command=self.desktopGuest)
        self.btnGuest.config(width=10)
        self.btnGuest.place(x=515, y=450)

        self.btnPanel = tk.Button(self.window, text="Control panel", command=self.windowCreateUsers)
        self.btnPanel.config(width=10)
        self.btnPanel.place(x=90, y=540)

        #imgoff= tk.PhotoImage(file="GUI/Images/off.png")
        self.btnoff = tk.Button(self.window, text="Power off", command=self.powerOff)
        self.btnoff.config(width=10)
        self.btnoff.place(x=180, y=540)

        self._clock()

        self.fondo.mainloop()
#----------power operative system----------------------------------------
    def powerOff(self):
        self.window.destroy()

#-----------------Clock-------------------------------------------------
    def _clock(self):
        threadClock = threading.Thread(target=self.clock)
        threadClock.start()

    def clock(self):
        reloj = tk.Label(text=time.strftime("%H:%M:%S"), fg="white", background="black")
        reloj.place(x=920, y=540)
        now = time.strftime("%H:%M:%S")
        if reloj['text'] != now:
            reloj['text'] = now
        self.window.after(1000, self.clock)

#----------------back the first view------------------------------------------------
    def turn_back(self):
        self.fondo.destroy()
        self.lbusername.destroy()
        self.lbPass.destroy()
        self.entryusernamen.destroy()
        self.entrypass.destroy()

        self.img = "GUI/Images/Logo.png"
        imgFondo = tk.PhotoImage(file=self.img)
        self.fondo = tk.Label(self.window, image=imgFondo)
        self.fondo.pack(side='top', fill='both', expand='yes')

        lbEnter = tk.Label(self.window, text=" Enter as: ", fg="white", background="black")
        lbEnter.place(x=475, y=420)

        self.btnUser = tk.Button(self.window, text="   Admin   ", command=self.startLoginAdmin)
        self.btnUser.config(width=10)
        self.btnUser.place(x=425, y=450)

        self.btnGuest = tk.Button(self.window, text="    Guest    ", command=self.desktopGuest)
        self.btnGuest.config(width=10)
        self.btnGuest.place(x=515, y=450)

        self.btnPanel = tk.Button(self.window, text="    Control panel    ", command=self.windowUsers)
        self.btnPanel.config(width=10)
        self.btnPanel.place(x=90, y=540)

        self.btnoff = tk.Button(self.window, text="Power off", command=self.powerOff)
        self.btnoff.config(width=10)
        self.btnoff.place(x=180, y=540)
        self.fondo.mainloop()

#------------------- Login as user---------------------------------------------
    def startLoginAdmin(self):
        self.fondo.destroy()
        self.lbEnter.destroy()
        self.btnUser.destroy()
        self.btnGuest.destroy()

        self.img = "GUI/Images/Login.png"
        imgFondo = tk.PhotoImage(file=self.img)
        self.fondo = tk.Label(self.window, image=imgFondo)
        self.fondo.pack(side='top', fill='both', expand='yes')

        self.userName = StringVar()
        self.Pass = StringVar()

        self.lbusername = tk.Label(self.window, text="User: ", fg="white", background="black")
        self.lbusername.place(x=390, y=380)
        self.entryusernamen = tk.Entry(self.window, textvariable = self.userName, width=25)
        self.entryusernamen.place(x=430, y=380)
        self.lbPass = tk.Label(self.window, text="Pass: ", fg="white", background="black")
        self.lbPass.place(x=390, y=410)
        self.entrypass = tk.Entry(self.window, textvariable=self.Pass, width=25,show="*")
        self.entrypass.place(x=430, y=410)

        self.btnLogin = tk.Button(self.window, text=" Login ", command= self.makeLogin)
        self.btnLogin.config(width=10)
        self.btnLogin.place(x=465, y=450)

        self.btnback = tk.Button(self.window, text=" Back ", command=self.turn_back)
        self.btnback.config(width=10)
        self.btnback.place(x=70, y=543)

        self.fondo.mainloop()

    def makeLogin(self):
        u = self.userName.get()
        p = self.Pass.get()
        #data = LectorJSON()
        #listUser = data.reader()

        if len(u) != 0 and len(p) != 0:
            user= User(u, p)
            if user.login(user.getUser(), user.getPassword(), self.listUser):
                self.makedesktop()
                #print("login succesful")
            else:
                messagebox.showinfo(message="user or password not found", title="ERROR")
        else:
            messagebox.showinfo(message="you must fill all the fields", title="ERROR")

    def makedesktop(self):
        self.fondo.destroy()
        self.lbusername.destroy()
        self.lbPass.destroy()
        self.entryusernamen.destroy()
        self.entrypass.destroy()
        self.btnLogin.destroy()
        self.btnback.destroy()

        self.img = "GUI/Images/fondoevolution.png"
        imgFondo = tk.PhotoImage(file=self.img)
        self.fondo = tk.Label(self.window, image=imgFondo)
        self.fondo.pack(side='top', fill='both', expand='yes')

        self.lbname = tk.Label(self.window, text=self.userName.get(), fg="white", background="black")
        self.lbname.config(width=10)
        self.lbname.place(x=20, y=20)

        self.btnUsers = tk.Button(self.window, text= "Control panel", command= self.WindowupdateUser)
        self.btnUsers.config(width=10)
        self.btnUsers.place(x=15, y=50)

        self.btnFileManager= tk.Button(self.window, text="File Browser", command=self.makeDirectory)
        self.btnFileManager.config(width=10)
        self.btnFileManager.place(x=15, y=90)

        self.btnBonusWord= tk.Button(self.window, text="Word", command=self.bonusWord)
        self.btnBonusWord.config(width=10)
        self.btnBonusWord.place(x=15, y=130)

        self.btnBonusExcel = tk.Button(self.window, text="Excel", command=self.bonusExcel)
        self.btnBonusExcel.config(width=10)
        self.btnBonusExcel.place(x=15, y=170)

        self.btnchangeuser = tk.Button(self.window, text= "Exit", command=self.changeUser)
        self.btnchangeuser.config(width=10)
        self.btnchangeuser.place(x=15, y=210)

        self.fondo.mainloop()



    #------------------- login(view) as Guest-----------------------------------------
    def desktopGuest(self):
        self.fondo.destroy()
        self.lbEnter.destroy()
        self.btnUser.destroy()
        self.btnGuest.destroy()

        self.img = "GUI/Images/fondoevolution.png"
        imgFondo = tk.PhotoImage(file=self.img)
        self.fondo = tk.Label(self.window, image=imgFondo)
        self.fondo.pack(side='top', fill='both', expand='yes')

        self.lbnameG = tk.Label(self.window, text="Guest ", fg="white", background="black")
        self.lbnameG.config(width=10)
        self.lbnameG.place(x=20, y=20)

        self.btnFileManagerG = tk.Button(self.window, text="File Browser", command=self.makeDirectory)
        self.btnFileManagerG.config(width=10)
        self.btnFileManagerG.place(x=20, y=50)

        self.btnchangeuserG = tk.Button(self.window, text="Exit", command=self.changeUserG)
        self.btnchangeuserG.config(width=10)
        self.btnchangeuserG.place(x=20, y=90)

        self.fondo.mainloop()
#----------------control panel without login, first view--------------------------
    def windowCreateUsers(self):
        windowUsers = tk.Toplevel(self.window)
        windowUsers.geometry('400x130+40+60')
        windowUsers.title('Panel de control')

        self.newUsername= StringVar()
        self.newPassword = StringVar()
        tk.Label(windowUsers, text="      ").grid(row=2, column=1)
        lfoptions = tk.LabelFrame(windowUsers, text="Options User", padx=10, pady=10, )
        lfoptions.config(width=50)
        lfoptions.grid(row=2, column=2)
        tk.Label(lfoptions, text="      ").grid(row=2, column=1)
        lbUname = tk.Label(lfoptions, text="Enter Username: ")
        lbUname.grid(row=2, column=2)
        self.entryName = tk.Entry(lfoptions, textvariable=self.newUsername, width=25)
        self.entryName.grid(row=2, column=4)
        lbpass = tk.Label(lfoptions, text="Enter Password: ")
        lbpass.grid(row=4, column=2)
        self.entryPass = tk.Entry(lfoptions, textvariable=self.newPassword, width=25)
        self.entryPass.grid(row=4, column=4)
        btnNewUser = tk.Button(lfoptions, text="New User", command=self.createNewUser)
        btnNewUser.config(width=10)
        btnNewUser.grid(row=6, column=2)
        #tk.Label(lfoptions, text="      ").grid(row=6, column=3)
        #btnDelUser = tk.Button(lfoptions, text="Delete User")
        #btnDelUser.config(width=10)
        #btnDelUser.grid(row=6, column=4)
        tk.Label(lfoptions, text="      ").grid(row=2, column=5)

#--------------------------Create user-----------------------------------------
    def createNewUser(self):
        newU = self.newUsername.get()
        newP = self.newPassword.get()
        lista = self.listUser
        encontro= True
        #print(newP+" "+ newU)

        if len(newU) !=0 and len(newP)!=0:
            newUser = User(newU, newP)
            self.listUser.append(newUser)
            messagebox.showinfo(message="User created", title="SUCCESFUL")

        else:
            messagebox.showinfo(message="you must fill all the fields", title="ERROR")


#----------------------control panel login as user succesful-----------------------------
    def WindowupdateUser(self):
        self.windowUpdate = tk.Toplevel(self.window)
        self.windowUpdate.geometry('420x180+180+90')
        self.windowUpdate.title('Panel de control')
        tk.Label(self.windowUpdate, text="      ").grid(row=2, column=1)
        lfoptions = tk.LabelFrame(self.windowUpdate, text="Delete user", padx=10, pady=10, )
        lfoptions.grid(row=2, column=2)

        tk.Label(lfoptions, text="      ").grid(row=2, column=1)
        tk.Label(lfoptions, text="Delete this user:").grid(row=2, column=2)
        tk.Label(lfoptions, text=self.userName.get()).grid(row=2, column=3)
        btnDelUser = tk.Button(lfoptions, text="Delete", command= self.deleteUser)
        btnDelUser.config(width=10)
        btnDelUser.grid(row=2, column=4)
        tk.Label(lfoptions, text="      ").grid(row=2, column=5)

        self.ChUsername= StringVar()
        self.ChPass = StringVar()
        lfUpdate = tk.LabelFrame(self.windowUpdate, text="Update user", padx=10, pady=10, )
        lfUpdate.grid(row=3, column=2)

        lbChname = tk.Label(lfUpdate, text="Change Username: ")
        lbChname.grid(row=2, column=2)
        self.entryChName = tk.Entry(lfUpdate, textvariable=self.ChUsername, width=25)
        self.entryChName.grid(row=2, column=3)
        #btnChUser = tk.Button(lfUpdate, text="Update")
        #btnChUser.config(width=10)
        #btnChUser.grid(row=2, column=4)

        lbChPass = tk.Label(lfUpdate, text="Change Password: ")
        lbChPass.grid(row=3, column=2)
        self.entryChPass = tk.Entry(lfUpdate, textvariable=self.ChPass, width=25)
        self.entryChPass.grid(row=3, column=3)
        btnChPass = tk.Button(lfUpdate, text="Update", command=self.updateUser)
        btnChPass.config(width=10)
        btnChPass.grid(row=3, column=4)

#------------------- Delete User----------------------------------------------------------
    def deleteUser(self):
        userDel = self.userName.get()
        passDel = self.Pass.get()
        okDelete = False
        userDelete = None
        #for j in self.listUser:
         #   print("lista sin actualizar   " + j.user)


        for data in self.listUser:
            if userDel == data.user and passDel ==  data.password:
                okDelete = True
                userDelete = data

        if okDelete:
            self.listUser.remove(userDelete)
            messagebox.showinfo(message="User delete", title="SUCCESFUL")
            self.windowUpdate.destroy()
            self.changeUser()

        #for i in self.listUser:
         #   print("list actualizada    " + i.user)

#--------------update User------------------------------------------------

    def updateUser(self):
        userDel = self.userName.get()
        passDel = self.Pass.get()
        userUpdate= self.ChUsername.get()
        passUpdate= self.ChPass.get()
        okDelete = False
        userDelete = None
        # for j in self.listUser:
        #   print("lista sin actualizar   " + j.user)
        if len(userUpdate) != 0 and len(passUpdate) != 0:
            for data in self.listUser:
                if userDel == data.user and passDel == data.password:
                    #self.listUser.remove(data)
                    okDelete = True
                    userDelete = data

            if okDelete:
                self.listUser.remove(userDelete)
                updateUser = User(userUpdate, passUpdate)
                self.listUser.append(updateUser)
                messagebox.showinfo(message="updated user. now log in with your new data.", title="SUCCESFUL")
                self.windowUpdate.destroy()
                self.changeUser()

#---------------back the first view for choose login(user or guest)-------------------------

    def changeUser(self):
        self.fondo.destroy()
        self.lbname.destroy()
        self.btnUsers.destroy()
        self.btnFileManager.destroy()
        self.btnchangeuser.destroy()
        self.img = "GUI/Images/Logo.png"
        self.widges()

    def changeUserG(self):
        self.fondo.destroy()
        self.lbnameG.destroy()
        self.btnFileManagerG.destroy()
        self.btnchangeuserG.destroy()
        self.img = "GUI/Images/Logo.png"
        self.widges()

#-----------------------File Browser------------------------------------------------------------------
    def makeDirectory(self):
        self.windowFile = tk.Toplevel(self.window)
        self.windowFile.geometry('800x500+180+90')
        self.windowFile.title('File System')
        self.windowFile.configure(background='gray10')

        # C:\\Users\\jmanu\\Documents\\Universidad\\Sistemas Operativos
        self.path = StringVar()
        self.path.set("C:\\Users\\jmanu\\Documents\\PruebaDirectoryOS")
        lbPath = tk.Label(self.windowFile, text="Enter Path: ",fg="white", background="gray10")
        lbPath.grid(row=2, column=2)
        self.pathSearch = tk.Entry(self.windowFile, textvariable=self.path, width=60)
        self.pathSearch.grid(row=2, column=3)
        lbespace = tk.Label(self.windowFile, text="    ", fg="white", background="gray10")
        lbespace.grid(row=2, column=4)
        btnFileManager = tk.Button(self.windowFile, text="Search directory", command=self.getPath,fg="white", background="gray10")
        btnFileManager.config(width=13)
        btnFileManager.grid(row=2, column=5)

    def getPath(self):
        ruta = self.path.get()
        #print("ruta"+ruta)
        self.openFolder(ruta)

    def searchDirectoryNext(self,ruta):
        #print("rrrr"+ruta)
        self.path.set(ruta)
        tk.Label(self.windowFile, text="content: ", fg="white", background="gray10")
        f= Folder(ruta)
        pos=0
        contador = 30
        listrutaabs = []
        pathback = self.getpathback(ruta)
        listrutaabs.append(pathback)
        for i in f.searchContent():
            listrutaabs.append(ruta+'\\'+i)
            contador += 30
            pos += 1
            btnfile = tk.Button(self.windowFile, text=i,fg="white", background="black",
                      command=lambda u=listrutaabs[pos]: self.openFolder(u))
            btnfile.config(width=50)
            btnfile.place(x=20,y=contador)

        btnBack= tk.Button(self.windowFile, text='Back', fg="white", background="black",
                  command=lambda j= listrutaabs[0]:self.openFolder(j))
        btnBack.config(width=7)
        btnBack.place(x=700, y=450)

    def openFolder(self,ruta):
        #print(ruta)
        d = Folder(ruta)
        r = d.getPath()
        if d.isFolder(r):
            self.windowFile.destroy()
            self.makeDirectory()
            self.searchDirectoryNext(ruta)
        elif d.isfile(r):
            #print(r.split("\\"))
            s = r.split("\\")
            a = s[len(s)-1].split(".")
            ext= a[len(a)-1]
            #print(ext)
            if ext == "txt":
                file= "notepad" + " " + ruta
                os.system(file)
            elif ext == "jpg" or ext=="png":
                file= "mspaint" + " " + ruta
                os.system(file)
            else:
                messagebox.showinfo(message="file not allowed", title="ERROR")
        else:
            messagebox.showinfo(message="file not allowed", title="ERROR")

    def getpathback(self, ruta):
        pathback=""
        s = ruta.split("\\")
        for i in range(len(s) - 1):
            pathback = pathback + s[i] +"\\"
        return pathback
    
#-----------Bonus--------------------------------------------------------------------
    def bonusWord(self):
        os.system('start WinWord' )

    def bonusExcel(self):
        os.system('start Excel.exe')