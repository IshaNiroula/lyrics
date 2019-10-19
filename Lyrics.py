            # LYRICS #

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import lyricwikia

root = Tk()
root.config(bg = 'powder blue')
root.title("Lyrics")
dec = Label(root,text = " Get the lyrics of the song you want ",fg = "Red" , bg = "powder blue" , font = ("" , 24)).place(relx = 0.0 , rely = 0.0)
root.geometry("500x250")
root.resizable(0,0)

name = StringVar()
ask = Label(root,text = "Name of the singer " , fg = "black" , bg = "powder blue" , font = ("",15)).place(relx = 0.0,rely = 0.3)
fill = Entry(root,textvariable = name , relief = "groove" ,bd = 15,width = 22 , bg = "Pink" , font = ("",15)).place(relx = 0.38,rely = 0.3)

song = StringVar()
get = Label(root,text = "Name of the song " , bg = "powder blue" , fg = "black" , font = ("", 15)).place(relx = 0.0 , rely = 0.55)
full = Entry(root , textvariable = song , relief = "groove", bd = 15 , width = 22 , bg = "Pink" , font = ("",15)).place(relx = 0.38,rely = 0.55)

def show_details():
    toplevel = Toplevel(root)
    toplevel.title("Lyrics")
    toplevel.geometry("1000x700")

    s = Scrollbar(toplevel)
    t = Text(toplevel, height = 100 , width = 1000)
    s.pack(side=RIGHT, fill=Y)
    t.pack(side=LEFT, fill=Y)
    s.config(command=t.yview)
    t.config(yscrollcommand=s.set)
    t.insert(END, lyricwikia.get_lyrics(name.get(),song.get()))

sub = Button(root , text = "Get it" , bd = 15 , bg = "Red" , fg = "White" , command = lambda: show_details()).place(relx = 0.45 , rely = 0.8)

root.mainloop()
