from tkinter import *
from tkinter.ttk import *

def createWindow():
    master = Tk()

    master.geometry("500x500")
    master.title("Vocal Math Program")

    master.label = Label(master, text="Vocal Math Program")



    return master