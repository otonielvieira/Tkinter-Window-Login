from tkinter import *

window = Tk()

def clean():
    btn_login.delete(0, END)
    passwd_login.delete(0, END)

#window measures
largura = 400
altura = 360
largura_window = window.winfo_screenwidth()
altura_window = window.winfo_screenheight()
posx = largura_window/2 - largura/2
posy = altura_window/2 - altura/2
#fonts
font18 = "{U.S. 101} 22 bold"
font11 = "{U.S. 101} 28 bold"
font15 = "{U.S. 101} 17 bold"
font13 = "{U.S. 101} 13 bold"
# Colors
color = "#f0f3f5"
color2 = "#4a88e8"

# main window
espace = " "

window.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
window.title(0 * espace + '@BuziosCloudTecnologia ')
window.configure(bg=color2)
window.resizable(width=False, height=False)

lbl = Label(text="Login", font=font11, bg=color2)
lbl.place(x=150, y=30)

login = Label(text="User", font=font15, bg=color2)
login.place(x=170, y=100)
btn_login = Entry(font=font13, bg=color2, fg='white')
btn_login.place(x=80, y=140, width=250, height=35)

passwd = Label(text="Password", font=font15, bg=color2)
passwd.place(x=150, y=180)
passwd_login = Entry(font=font13, bg=color2, fg='white', show='*')
passwd_login.place(x=80, y=220, width=250, height=35)

btn = Button(text='Enter', font=font13, bg=color2, fg='white', anchor=CENTER, command=clean)
btn.place(x=155, y=280, width=100, height=40)


window.mainloop()