from tkinter import *
from tkinter import messagebox
import base64

screen = Tk()
screen.geometry("480x480")
screen.title("Encryption And Decryption GUI")
screen.configure(bg="grey")

def encrypt():
    password=code.get()
    if password=="2902":
        screen1=Toplevel(screen)
        screen1.title("Encrypt")
        screen1.geometry("320x320")
        screen1.configure(bg="green")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")
        Label(screen1,text="Your text is encrypted",font="impack 14 bold").place(x=5,y=6)
        text2=Text(screen1,font="30",bd=4,wrap=WORD)
        text2.place(x=5,y=50,width="300",height="180")
        text2.insert(END,encrypt)
    elif(password==""):
        messagebox.showerror("Error","Please enter the secret key")
    elif(password!="2902"):
        messagebox.showerror("Error","Invalid secret key")
def decrypt():
    password=code.get()
    if password=="2902":
        screen2=Toplevel(screen)
        screen2.title("Decrypt")
        screen2.geometry("320x320")
        screen2.configure(bg="red")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(encode_message)
        encrypt = base64_bytes.decode("ascii")
        Label(screen2,text="Your text is decrypted",font="impack 14 bold").place(x=5,y=6)
        text2=Text(screen2,font="30",bd=4,wrap=WORD)
        text2.place(x=5,y=30,width="280",height="180")
        text2.insert(END,encrypt)
    elif (password == ""):
        messagebox.showerror("Error", "Please enter the secret key")
    elif (password != "2902"):
        messagebox.showerror("Error", "Invalid secret key")
def reset():
    text1.delete(1.0,END)
    code.set("")
def show():
    Entry(textvariable=code, bd=4, font="impack 20 ").place(x=80, y=250)



Label(screen,text="Enter the text for encryption and decryption",font="impack 14 bold").place(x=30 ,y=4)
text1=Text(screen,font="18")
text1.place(x=8,y=45,height="150",width="460")
Label(screen,text="Enter Secrect key",font="impack 14 bold").place(x=150,y=220)
code=StringVar()
Entry(textvariable=code,bd=4,font="impack 20 ",show="*").place(x=80,y=250)
Button(screen,text="Encrypt",font="impack 15 bold",bg="green",fg="white",command=encrypt
       ).place(x=15,y=330,width="150")
Button(screen,text="Decrypt",font="impack 15 bold",bg="red",fg="white",command=decrypt).place(x=312,y=330,width="150")
Button(screen,text="Reset",font="impack 15 bold",bg="Yellow",fg="white",command=reset).place(x=165,y=400,width="150")
Button(screen,text="Show",font="impack 10 bold",bg="Black",fg="white",command=show).place(x=340,y=220)

mainloop()