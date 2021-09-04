from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frame")

#Create frame
frame = LabelFrame(root,padx=50,pady=50)
#Display frame
frame.pack(padx=10,pady=10)

# Create button
b1 = Button(frame, text="Click Here")
b2 = Button(frame, text="Don't Click Here")
# Display button
b1.grid(row=0,column=1)
b2.grid(row=1,column=1)


root.mainloop()