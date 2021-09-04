from tkinter import *

root = Tk()
#creating the label widget
label1 = Label(root,text="Hello world!").grid(row=0, column=0)
label2 = Label(root,text="My name is Payal").grid(row=1, column=5)
label3 = Label(root,text="            ").grid(row=1, column=1)

# showing it into screen
# label1.grid(row=0, column=0)
# label2.grid(row=1, column=5)
# label3.grid(row=1, column=1)
root.mainloop()