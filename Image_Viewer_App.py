from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer App")

#Create image
img1 = ImageTk.PhotoImage(Image.open("D:/Tkinter/images/red.png"))
img2 = ImageTk.PhotoImage(Image.open("D:/Tkinter/images/pink.png"))
img3 = ImageTk.PhotoImage(Image.open("D:/Tkinter/images/yellow.png"))

#List all the img
img_list = [img1, img2, img3]

#Create status bar
status = Label(root,text="Image 1 of " + str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)

# display  img1 into screen
myLabel = Label(image=img1)
myLabel.grid(row=0,column=0,columnspan=3)

#Forward function
def forward(img_number):
    global myLabel
    global button_forward
    global button_back

    # Forget the 1st img so that no overlapping happens
    myLabel.grid_forget()
    # Label the img
    myLabel = Label(image=img_list[img_number-1])
    # Creating button
    button_forward = Button(root,text=">>",command= lambda: forward(img_number+1))
    button_back = Button(root,text="<<",command= lambda: backward(img_number-1))

    # corner case when it reached to the end
    if img_number == 3:
        button_forward = Button(root,text=">>",state=DISABLED)

    # display img , button into screen
    myLabel.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    #update status bar
    status = Label(root,text="Image " + str(img_number) + " of " + str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)



#backward function
def backward(img_number):
    global myLabel
    global button_forward
    global button_back

    # Forget the latest img so that no overlapping happens
    myLabel.grid_forget()
     # Label the img
    myLabel = Label(image=img_list[img_number-1])
     # Creating button
    button_forward = Button(root,text=">>",command= lambda: forward(img_number+1))
    button_back = Button(root,text="<<",command= lambda: backward(img_number-1))

     # corner case when it reached to the begining
    if img_number == 1:
        button_back = Button(root,text="<<",state=DISABLED)

    # display img , button into screen
    myLabel.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    #Update status bar
    status = Label(root,text="Image " + str(img_number) + " of " + str(len(img_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)




# Create Button
button_back = Button(root,text="<<",command=backward,state=DISABLED)
button_exit = Button(root,text="Exit",command=root.quit)
button_forward = Button(root,text=">>",command=lambda: forward(2))

#Display Button
button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)


root.mainloop()