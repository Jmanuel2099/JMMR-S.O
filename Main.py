from GUI.firstWindow import firstWindow
from DB.LectorJSON import LectorJSON
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

    #blok de notas
    #os.system('notepad C:\\Users\\jmanu\\Documents\\Universidad\\Sistemas Operativos\\linksMaquinaVirtual.txt')
    #os.system('notepad C:\\Users\\jmanu\\Documents\\Universidad\\certificado JOSE MANUEL MARIN RAMIREZ.pdf')
    #paint
    #os.system('mspaint C:\\Users\\jmanu\\Documents\\20190128_203035.jpg')

    #word
    #os.system('start WinWord )
    #Excel
    #os.system('start Excel.exe')
    #ruta ="C:\\Users\\jmanu\\Documents\\Universidad\\Sistemas Operativos"
    #print(ruta.split("\\"))
    #s=ruta.split("\\")
    #nueva=""
    #for i in range(len(s)-1):
       # print (i)
      #  nueva= nueva+s[i]+"\\"+"\\"
     #   print(nueva)
    #os.system('internet-Explorer.exe')
    #print("---"+nueva)

    data = LectorJSON()
    listUser = data.reader()
    Window = Tk()
    sysOperative = firstWindow(Window, listUser)
    Window.mainloop()