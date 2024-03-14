from tkinter import *
from datetime import datetime

def what_time():
    dnow = datetime.now()
    btn.config(text=dnow)

win = Tk()

win.geometry("1000x500")
win.title("title")
win.option_add("*Font", "맑은고딕 25")

btn = Button(win)

btn.config(text="현재시각")
btn.config(width=50)
btn.config(command=what_time)

btn.pack()

win.mainloop()

