from GUI.firstWindow import firstWindow
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
from os.path import isfile, join, isdir

if __name__ == '__main__':

    #C:\Users\jmanu\Documents\Universidad\Sistemas Operativos\S.O
    #print(os.listdir('C:\\Users\\jmanu\\Documents\\Universidad\\Sistemas Operativos'))
    #rutabase= 'C:\\Users\\jmanu\\Documents\\Universidad\\Sistemas Operativos'
    #rutacarperta = 'C:\\Users\\jmanu\\Documents\\Universidad\\Sistemas Operativos\\S.O'
    #rutaabs= os.path.join(rutabase,rutacarperta)
    #r= os.path.abspath(rutaabs)

    #contenido = os.listdir(r)
    #files = [nombre for nombre in contenido if isfile(join(r, nombre))]
    #print(len(files))

    #a= os.listdir('C:\\Users\\jmanu\\Documents\\Universidad\\Sistemas Operativos')
    #a= os.path.isfile('C:\\Users\\jmanu\\Documents\\Universidad\\Sistemas Operativos\\i')
    #a = os.path.isfile('C:\\Users\\jmanu\\Documents\\Universidad\\certificado JOSE MANUEL MARIN RAMIREZ.pdf')
    #print(a)

    #os.system('notepad.exe')
    #ruta ="C:\\Users\\jmanu\\Documents\\Universidad\\Sistemas Operativos"
    #print(ruta.split("\\"))
    #s=ruta.split("\\")
    #nueva=""
    #for i in range(len(s)-1):
       # print (i)
      #  nueva= nueva+s[i]+"\\"+"\\"
     #   print(nueva)

    #print("---"+nueva)

    Window = Tk()
    sysOperative = firstWindow(Window)
    Window.mainloop()




