import os
from os.path import isfile, join, isdir

class Folder:

    def __init__(self, path):
        self.path = path

    def getPath(self):
        return self.path

    def searchContent(self):
        #ruta = r'C:\Users\jmanu\Documents\Universidad\Sistemas Operativos'
        ruta= self.path
        contenido = os.listdir(ruta)

        # Archivos
        files = [nombre for nombre in contenido if isfile(join(ruta, nombre))]
        #print('Archivos')
        #print(files)

        # Carpetas
        folders = [nombre for nombre in contenido if isdir(join(ruta, nombre))]
        #print('Carpetas')
        #print(folders)

        return [files,folders]