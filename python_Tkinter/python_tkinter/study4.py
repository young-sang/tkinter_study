from tkinter import *

win = Tk()

win.geometry("400x200")
win.title("pack")
win.option_add("*Font", "궁서 20")

ent = Entry(win)
ent.pack()

btn = Button(win)
btn.config(text = "버튼")
def mbtn():
    btn.pack(pady=ent.get())
btn.config(command=mbtn)
btn.pack()

btn2 = Button(win)
btn2.config(text="temp")
btn2.pack()

win.mainloop()