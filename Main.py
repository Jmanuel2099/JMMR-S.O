from GUI.firstWindow import firstWindow
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
from os.path import isfile, join, isdir

if __name__ == '__main__':

    Window = Tk()
    sysOperative = firstWindow(Window)
    Window.mainloop()




