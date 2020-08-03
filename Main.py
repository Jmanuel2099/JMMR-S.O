from GUI.firstWindow import firstWindow
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import time

if __name__ == '__main__':
    Window = Tk()
    sysOperative = firstWindow(Window)
    """ Window.resizable(0, 0)
    Window.title("JMMR")
    Window.geometry('1000x600')
    reloj = tk.Label(text=time.strftime("%H:%M:%S"), fg="white", background="black")
    reloj.place(x=920, y=560)
    print(reloj['text'])

    def clock():
        now = time.strftime("%H:%M:%S")
        if reloj['text'] != now:
            reloj['text'] = now
        Window.after(1000, clock)
    clock()"""

    Window.mainloop()




