from tkinter import *
import qrcode
from turtle import title
from PIL import Image

root=Tk()
root.title("QR Generator")
root.geometry("1000x600")
root.resizable(False,False)
root.configure(bg="lightgreen")
#icon
root.iconbitmap("qr_icon.ico")

def generate():
    name=title.get()
    text=entry.get() 
    qr=qrcode.make(text)
    qr.save("C:/Users/ahnaf/Documents/Pycharm Projects/QR_generator/"+ str(name)+".png")

    global Image
    Image = PhotoImage(file="C:/Users/ahnaf/Documents/Pycharm Projects/QR_generator/"+str(name)+".png")
    Image_view.config(image=Image)

Image_view=Label(root,bg="lightblue")
Image_view.pack(padx=50,pady=10,side=RIGHT)

Label(root,text="Title",fg="white",bg="black",font=15).place(x=50,y=170)

title=Entry(root,width=13,font="arial 15")
title.place(x=50,y=200)

entry=Entry(root,width=28,font="arial 15")
entry.place(x=50,y=250)


button=Button(root,text="Generate",width=20,height=2,bg="black",fg="white",command=generate).place(x=50,y=300)

root.mainloop()