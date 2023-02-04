from tkinter import *
from tkinter.ttk import *
from window.speech.record import recordAudio

def createWindow():
    master = Tk()

    master.geometry("500x500")
    master.title("Vocal Math Program")

    Label(master, text="Vocal Math Program")


    startRecordingButton = Button(master, 
        text="Start",
        command = recordAudio())
    
    startRecordingButton.grid(row=0, column=2, columnspan=2, rowspan=2,
       padx=5, pady=5)



    return master