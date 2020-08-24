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

class firstWindow:

    def __init__(self, window):
        self.window = window
        self.window.resizable(0,0)
        self.window.title("JMMR")
        self.window.geometry('1000x600')
        self.fondo = None
        self.img ="GUI/Images/Logo.png"
        
        self.widges()

    def widges(self):
        imgFondo = tk.PhotoImage(file= self.img)
        self.fondo = tk.Label(self.window, image=imgFondo)
        self.fondo.pack(side='top', fill='both', expand='yes')

        self.lbEnter= tk.Label(self.window, text=" Enter as: ", fg="white", background="black")
        self.lbEnter.place(x=475,y=420)

        self.btnUser= tk.Button(self.window, text="   Admin   ", command= self.startLoginAdmin)
        self.btnUser.place(x=425,y=450)
        self.btnGuest = tk.Button(self.window, text="    Guest    ", command=self.desktopGuest)
        self.btnGuest.place(x=515, y=450)

        self._clock()

        self.fondo.mainloop()

    def _clock(self):
        threadClock = threading.Thread(target=self.clock)
        threadClock.start()

    def clock(self):
        reloj = tk.Label(text=time.strftime("%H:%M:%S"), fg="white", background="black")
        reloj.place(x=920, y=560)
        now = time.strftime("%H:%M:%S")
        if reloj['text'] != now:
            reloj['text'] = now
        self.window.after(1000, self.clock)


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
        self.entrypass = tk.Entry(self.window, textvariable=self.Pass, width=25)
        self.entrypass.place(x=430, y=410)

        self.btnLogin = tk.Button(self.window, text=" Login ", command= self.makeLogin)
        self.btnLogin.place(x=480, y=450)

        self.btnback = tk.Button(self.window, text=" Back ", command=self.turn_back)
        self.btnback.place(x=70, y=543)

        self.fondo.mainloop()

    def makeLogin(self):
        u = self.userName.get()
        p = self.Pass.get()

        if len(u) != 0 and len(p) != 0:
            user= User(u, p)
            if user.login(user.getUser(), user.getPassword()):
                self.makedesktop()
                print("login succesful")
            else:
                print("user or password not found")
        else:
            print("you must fill all the fields")

    def desktopGuest(self):
        self.fondo.destroy()
        self.lbEnter.destroy()
        self.btnUser.destroy()
        self.btnGuest.destroy()

        self.img = "GUI/Images/desktop.png"
        imgFondo = tk.PhotoImage(file=self.img)
        self.fondo = tk.Label(self.window, image=imgFondo)
        self.fondo.pack(side='top', fill='both', expand='yes')

        btnFileManager = tk.Button(self.window, text="Search file", command=self.makeFileSystem)
        btnFileManager.config(width=10)
        btnFileManager.place(x=20, y=30)

        btnchangeuser = tk.Button(self.window, text="Change User", command=self.turn_back)
        btnchangeuser.config(width=10)
        btnchangeuser.place(x=20, y=70)
        self.fondo.mainloop()

    def makedesktop(self):
        self.fondo.destroy()
        self.lbusername.destroy()
        self.lbPass.destroy()
        self.entryusernamen.destroy()
        self.entrypass.destroy()
        self.btnLogin.destroy()
        self.btnback.destroy()

        self.img = "GUI/Images/desktop.png"
        imgFondo = tk.PhotoImage(file=self.img)
        self.fondo = tk.Label(self.window, image=imgFondo)
        self.fondo.pack(side='top', fill='both', expand='yes')

        btnUsers = tk.Button(self.window, text= "Users", command= self.windowUsers)
        btnUsers.config(width=10)
        btnUsers.place(x=15, y=15)
        btnFileManager= tk.Button(self.window, text="FIle Manager", command=self.makeFileSystem)
        btnFileManager.config(width=10)
        btnFileManager.place(x=15, y=50)
        btnchangeuser = tk.Button(self.window, text= "Change User", command=self.changeUser)
        btnchangeuser.config(width=10)
        btnchangeuser.place(x=15, y=85)

        self.fondo.mainloop()

    def windowUsers(self):
        windowUsers = tk.Toplevel(self.window)
        windowUsers.geometry('400x400')
        windowUsers.title('Users')

        self.newUsername= StringVar()
        self.newPassword = StringVar()
        lfoptions = tk.LabelFrame(windowUsers, text="New User", padx= 10, pady=10,)
        lfoptions.grid(row=1, column=2)
        lbname= tk.Label(lfoptions, text= "Enter Username: ")
        lbname.grid(row= 2, column=2)
        self.entryNewName = tk.Entry(lfoptions, textvariable=self.newUsername, width=25)
        self.entryNewName.grid(row=2, column=4)
        lbpass= tk.Label(lfoptions, text="Enter Password: ")
        lbpass.grid(row=3, column=2)
        self.entryNewPass = tk.Entry(lfoptions, textvariable=self.newPassword, width=25)
        self.entryNewPass.grid(row=3, column=4)
        btnNewUser= tk.Button(lfoptions, text="New User")
        btnNewUser.config(width=10)
        btnNewUser.grid(row=4,column=2)

        self.deletteUser = StringVar()
        lfdelette = tk.LabelFrame(windowUsers, text="Delete User", padx=10, pady=10, )
        lfdelette.grid(row=2, column=2)
        lbdelette = tk.Label(lfdelette, text="Enter User for delete: ")
        lbdelette.grid(row=2, column=2)
        self.entryDelette = tk.Entry(lfdelette, textvariable=self.deletteUser, width=25)
        self.entryDelette.grid(row=2, column=4)
        btndelete = tk.Button(lfdelette, text="Delete")
        btndelete.config(width=10)
        btndelete.grid(row=3, column=2)

    def makeFileSystem(self):
        #windowFile = tk.Toplevel(self.window)
        #windowFile.geometry('700x600')
        #windowFile.title('Users')

        #self.path = StringVar()
        #lbPath = tk.Label(windowFile, text="Enter Path: ")
        #lbPath.grid(row=2, column=2)
        #self.pathSearch = tk.Entry(windowFile, textvariable=self.path, width=80)
        #self.pathSearch.grid(row=2, column=3)
        #btnFileManager = tk.Button(windowFile, text="Search file", command=self.searchFile)
        #btnFileManager.config(width=10)
        #btnFileManager.grid(row=2, column=4)

        #print(self.searchFile)
        self.path = StringVar()
        lbPath = tk.Label(self.window, text="Enter Path: ", fg="white", background="black")
        lbPath.place(x=120, y=30)
        self.pathSearch = tk.Entry(self.window, textvariable=self.path, width=80)
        self.pathSearch.place(x=200, y=30)
        btnFileManager = tk.Button(self.window, text="Search file", command=self.searchFile)
        btnFileManager.config(width=10)
        btnFileManager.place(x=710, y=30)





        #tk.Label(self.window, text="File System:", fg="white", background="black").place(x=230, y=30)
        #ruta = r'C:\\Users\\jmanu\\Documents\\Universidad\\Sistemas Operativos'
        #f = Folder(ruta)
        #content = f.searchContent()
        #contador= 30
        #print(content)
        #for i in content :
         #   for j in i:
          #      contador+=30
           #     print(j)
            #    tk.Button(self.window, text=j, fg="white", background="black").place(x=230, y=contador)

    def searchFile(self):
        ruta = self.path.get()
        #print(ruta)

        f= Folder(ruta)
        content= f.searchContent()
        contador = 70
        # print(content)
        for i in content:
            print(ruta+'\\'+'\\'+i)
            rabs= ruta+'\\'+'\\'+i
            if f.isfile(rabs):
                tk.Label(self.window, text="Files:", fg="white", background="black").place(x=230, y=60)
                contador += 30
                tk.Button(self.window, text=i, fg="white", background="black", command=self.fileOrFolder).place(x=230,y=contador)
            if f.isFolder(rabs):
                tk.Label(self.window, text="Folders:", fg="white", background="black").place(x=230, y=contador+30)
                contador += 60
                tk.Button(self.window, text=i, fg="white", background="black", command=self.fileOrFolder).place(x=230,y=contador)

    def fileOrFolder(self):
        pass

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
        lbEnter.place(x=475,y=420)

        self.btnUser = tk.Button(self.window, text="   Admin   ", command=self.startLoginAdmin)
        self.btnUser.place(x=425,y=450)

        self.btnGuest = tk.Button(self.window, text="    Guest    ", command=self.desktopGuest)
        self.btnGuest.place(x=515, y=450)
        self.fondo.mainloop()

    def changeUser(self):
        pass
