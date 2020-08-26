import os
from os.path import isfile, join, isdir
from tkinter import messagebox

class Folder:

    def __init__(self, path):
        self.path = path

    def getPath(self):
        return self.path

    def searchContent(self):
        #ruta = r'C:\Users\jmanu\Documents\Universidad\Sistemas Operativos'
        ruta= self.path
        try:
            contenido = os.listdir(ruta)
            return contenido
        except:
            messagebox.showinfo(message="Path invalid", title="ERROR")
            return []


    def isfile(self,ruta):
        return os.path.isfile(ruta)

    def isFolder(self,ruta):
        return os.path.isdir(ruta)

    def getFies(self):
        c= self.searchContent()
        files = [nombre for nombre in c if isfile(join(self.path, nombre))]
        return files
    def getFolders(self):
        c = self.searchContent()
        folders = [nombre for nombre in c if isdir(join(self.path, nombre))]
        return folders
