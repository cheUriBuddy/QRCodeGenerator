from tkinter import *
import png
import pyqrcode
from pyqrcode import QRCode
from PIL import Image, ImageTk


def qr_generate():
    cont = url_content.get()
    create_qr = pyqrcode.create(cont)
    qr_code = create_qr.png("qr.png",scale=5)

    image = Image.open("qr.png")
    photo = ImageTk.PhotoImage(image)
    image_section.config(image=photo)
    image_section.image = photo
    
    '''     In Tkinter, image objects like PhotoImage or ImageTk.PhotoImage are handled differently than other widgets. If you don't keep a reference to     
    these image objects, Python’s garbage collector will clean them up (i.e., remove them from memory) even though you may have displayed the image in your Tkinter window.

            Why does this happen?
            When you create an image (e.g., qr_img = ImageTk.PhotoImage(...)) and assign it to a widget (like qr_label.config(image=qr_img)), the config method only stores a reference to the image temporarily. Since there is no permanent reference in your code, Python's garbage collector assumes the image is no longer needed after the config method is called and removes it from memory. This causes the image to disappear or never show up in the widget.

            Solution: Keeping a reference
            By assigning the image object to an attribute of a widget (in this case qr_label.image = qr_img), you create a persistent reference. This prevents the garbage collector from cleaning up the image while it's still needed.

            qr_label.image = qr_img  # Keep a reference to prevent garbage collection
            This ensures that qr_img remains in memory as long as qr_label exists. As a result, the QR code image will remain displayed in the Tkinter label.
    '''
   
    qr_desc.config(text=f"{title_entry.get()}")

    title_entry.delete(0,END)
    root.clipboard_append(url_content.get())
    url_content.delete(0,END)
    

root = Tk()
root.geometry("400x500")
Label(text="Welcome to Qr Code Generator",font=("calibri 20 bold"),fg="#00c9a7").pack()

tilte_label = Label(text="Enter Title For Your QR Code",padx=5,pady=10)
tilte_label.pack() 

title_entry = Entry(width=30)
title_entry.pack()

content_label = Label(text="Enter Your URL or Contents",padx=5,pady=10)
content_label.pack()

url_content = Entry(width=50)
url_content.pack()

subimt_button = Button(text="Generate",command=qr_generate)
subimt_button.pack(pady=10)


image_section = Label()
image_section.pack()

qr_desc = Label()
qr_desc.pack()


root.mainloop()