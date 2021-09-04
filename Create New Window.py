from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("1st window")

def open():
    global img
    top = Toplevel()
    top.title("2nd window")
    img = ImageTk.PhotoImage(Image.open("D:/Tkinter/images/red.png"))
    my_label = Label(top,image=img).pack()
    b2 = Button(top,text="close window", command=top.destroy).pack()


b = Button(root,text="Open Second window",command=open)
b.pack()


mainloop()