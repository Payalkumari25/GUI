from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Images and Icons")

#Icons
#root.iconbitmap("rose.ico")

img = ImageTk.PhotoImage(Image.open(r"D:/Tkinter/images/pink.png"))
my_label = Label(image=img)
my_label.pack()

button = Button(root,text="Exit",command=root.quit)
button.pack()


root.mainloop()