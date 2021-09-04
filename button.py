from tkinter import *

root = Tk()

def myClick():
    mylabel = Label(root,text="Welcome to TizenRt").pack()


#Create button
myButton1 = Button(root,text="Click me!",command=myClick,bg="blue",fg="white").pack()
myButton2 = Button(root,text="Disabled button!", state=DISABLED).pack()
myButton3 = Button(root,text="Run!",padx = 50, pady=10).pack()


root.mainloop()