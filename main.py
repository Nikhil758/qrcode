import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pyqrcode


wn = Tk()
wn.title('QR Code Generator')
wn.geometry('1000x1000')
wn.config(bg='black')

headingFrame = Frame(wn,bg="azure",bd=5)
headingFrame.place(relx=0.13,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR Code", fg='white', bg='black', font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

canvas1 = Canvas(wn, relief=RIDGE, bd=2,bg='black')
canvas1.place(relx=0.35,rely=0.67,  relwidth=0.25, relheight=0.21)
def generate():
    if text.get() != '' and name.get() != '':
        qr = pyqrcode.create(text.get())
        img = qr.png(name.get() + ".png", scale=5)
        info = Label( text="Generated QR code:", font=('ariel 15 bold'),bg='black',fg='white')
        info.place(x=60, y=580)
        img = Image.open(name.get() + ".png")
        img = ImageTk.PhotoImage(img)
        canvas1.create_image(125,87,anchor=CENTER,image=img)
        canvas1.image = img

    else:
        info = Label( text="Please enter the\n data for QR code", font=('ariel 15 bold'),bg='black',fg='white')
        info.place(x=80, y=580)

Frame1 = Frame(wn,bg="black")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)

label1 = Label(Frame1,text="Enter the text/URL: ",bg="black",fg='white',font=('Courier',13,'bold'))
label1.place(relx=0.05,rely=0.2, relheight=0.08)

text = Entry(Frame1,font=('Century 12'))
text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

Frame3 = Frame(wn,bg="black")
Frame3.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)

label3 = Label(Frame3,text="Enter the name of the QR Code: ",bg="black",fg='white',font=('Courier',13,'bold'))
label3.place(relx=0.05,rely=0.2, relheight=0.08)

name = Entry(Frame3,font=('Century 12'))
name.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

button = Button(wn, text='Generate Code',font=('Courier',15,'normal'),command=generate)
button.place(relx=0.35,rely=0.6, relwidth=0.25, relheight=0.05)

wn.mainloop()