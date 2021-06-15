from tkinter import Tk, mainloop
from tkinter.ttk import Label
from time import strftime


root = Tk()
root.title("Clock")


def time():

	st = strftime("%H:%M:%s %p")
	label.config(text=st)
	label.after(1000, time)


label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center")

time()
mainloop()