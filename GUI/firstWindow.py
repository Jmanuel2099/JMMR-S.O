import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from Security.User import User

class firstWindow:

    def __init__(self, window):
        self.window = window
        self.window.title("JMMR")
        self.window.geometry('1000x600')
        self.fondo = None
        self.img ="GUI/Images/Logo.png"
        self.widges()

    def widges(self):
        imgFondo = tk.PhotoImage(file= self.img)
        self.fondo = tk.Label(self.window, image=imgFondo)
        self.fondo.pack(side='top', fill='both', expand='yes')

        lbEnter= tk.Label(self.window, text=" Enter as: ", fg="white", background="black")
        lbEnter.place(x=480,y=425)

        self.btnUser= tk.Button(self.window, text="   User   ", command= self.startLoginUSer)
        self.btnUser.place(x=450,y=450)
        self.btnGuest = tk.Button(self.window, text="  Guest  ", command=self.startLoginGuest)
        self.btnGuest.place(x=520, y=450)
        self.fondo.mainloop()

    def startLoginUSer(self):
        self.fondo.destroy()
        self.btnUser.destroy()
        self.btnGuest.destroy()

        self.img = "GUI/Images/Login.png"
        imgFondo = tk.PhotoImage(file=self.img)
        self.fondo = tk.Label(self.window, image=imgFondo)
        self.fondo.pack(side='top', fill='both', expand='yes')

        self.userName = StringVar()
        self.Pass = StringVar()
        lbusername = tk.Label(self.window, text="User: ", fg="white", background="black")
        lbusername.place(x=390, y=380)
        entryusernamen = tk.Entry(self.window, textvariable = self.userName, width=25)
        entryusernamen.place(x=430, y=380)
        lbPass = tk.Label(self.window, text="Pass: ", fg="white", background="black")
        lbPass.place(x=390, y=410)
        entrypass = tk.Entry(self.window, textvariable=self.Pass, width=25)
        entrypass.place(x=430, y=410)


        btn = tk.Button(self.window, text=" Login ", command= self.makeLogin)
        btn.place(x=480, y=450)

        """imgback = tk.PhotoImage(file="GUI/Images/retroceder.png"
        btnback = tk.Button(self.window, image=imgback, command = self.turn_back)"""
        btnback = tk.Button(self.window, text=" Back ", command=self.turn_back)
        btnback.place(x=70, y=543)


        self.fondo.mainloop()

    def startLoginGuest(self):
        pass

    def turn_back(self):
        self.fondo.pack_forget()

        self.img = "GUI/Images/Logo.png"
        imgFondo = tk.PhotoImage(file=self.img)
        self.fondo = tk.Label(self.window, image=imgFondo)
        self.fondo.pack(side='top', fill='both', expand='yes')

        lbEnter = tk.Label(self.window, text=" Enter as: ", fg="white", background="black")
        lbEnter.place(x=480, y=425)

        self.btnUser = tk.Button(self.window, text="   User   ", command=self.startLoginUSer)
        self.btnUser.place(x=450, y=450)

        self.btnGuest = tk.Button(self.window, text="  Guest  ", command=self.startLoginGuest)
        self.btnGuest.place(x=520, y=450)
        self.fondo.mainloop()


    def makeLogin(self):
        u = self.userName.get()
        p = self.Pass.get()

        if len(u) != 0 and len(p) != 0:
            print("login succesful whit User: "+ u)
            """if User.login(u, p):
                print("login succesful")
            else:
                print("user or password not found")"""

            """here i make the login process"""
        else:
            print("you must fill all the fields")

