from tkinter import *

root = Tk()

e = Entry(root,width=50,borderwidth=5)
e.pack()
e.insert(0,"Enter your name: ")

def click():
    x = "Welcome " + e.get()
    label = Label(root,text=x)
    label.pack()

b = Button(root,text="Enter your name", command=click)
b.pack()

root.mainloop()