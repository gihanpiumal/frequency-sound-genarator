import sounddevice as sd
import numpy as np
from math import pi
import tkinter as tk


window=tk.Tk()
window.title("Mission")
window.geometry('500x250')
window.configure(bg='#004E60')


def printInput():
    inp1 = frequency.get(1.0, "end-1c")
    inp2 = time.get(1.0, "end-1c")
    Fs = 16000
    
    t=int(inp2)
    n=np.arange(0,t,1/Fs)
    f=int(inp1)

    x=np.sin(2*pi*f*n)

    sd.play(x,Fs)
  



frequencyTxt=tk.Label(window,text="Frequency :",padx='10',font=("Arial Bold",25),background="#004E60",foreground="white")

timeTxt=tk.Label(window,text="Time(sec) :",padx='10',font=("Arial Bold",25),background="#004E60",foreground="white")



frequency = tk.Text(window,height = 1,width = 10)
time = tk.Text(window,height = 1,width = 10)


printButton = tk.Button(window,text = "Genarate",font=("Arial Bold",10),bg="#100BF7",fg="white",borderwidth = '4',activebackground="red"
                        ,bd='7',relief='raised', command = printInput)
printButton.pack()

frequencyTxt.place(x=10,y=50)
frequency.place(x=250,y=65)
timeTxt.place(x=10,y=150)
time.place(x=250,y=165)




window.mainloop()  