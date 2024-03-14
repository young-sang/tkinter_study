from tkinter import *

win = Tk()

win.geometry("600x300")
win.title("place")
win.option_add("*Font", "궁서 20")

xx = 0.3
yy = 0.4

btn = Button(win)
btn.config(text="({},{})".format(xx,yy))
btn.place(relx=xx,rely=yy)

win.mainloop()