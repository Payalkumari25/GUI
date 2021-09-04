from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def info():
     messagebox.showinfo("This is my Popup!","Welcome to TizenRT")
    
def warning():
    messagebox.showwarning("This is my Popup!","Welcome to TizenRT")

def error():
    messagebox.showerror("This is my Popup!","Welcome to TizenRT")

def question():
    response = messagebox.askquestion("This is my Popup!","Welcome to TizenRT")
    Label(root,text=response).pack()

def okcancel():
    response = messagebox.askokcancel("This is my Popup!","Welcome to TizenRT")
    Label(root,text=response).pack()

def yesno():
    response = messagebox.askyesno("This is my Popup!","Welcome to TizenRT")
    #Label(root,text=response).pack()
    # if response == 1:
    #      Label(root,text="You clicked Yes!").pack()
    # else:
    #      Label(root,text="You clicked No!").pack()

Button(root,text="Info",command=info).pack()
Button(root,text="Warning",command=warning).pack()
Button(root,text="Error",command=error).pack()
Button(root,text="Question",command=question).pack()
Button(root,text="okCancel",command=okcancel).pack()
Button(root,text="yesno",command=yesno).pack()


root.mainloop()