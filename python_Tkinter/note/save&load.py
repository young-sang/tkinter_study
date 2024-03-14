from tkinter import *
from tkinter import filedialog

win = Tk()

win.geometry("550x300")
win.title("Note")
win.option_add("*Font","고딕 16")

#ENTRY
txt = Text(win)
txt.place(x=0, y=0, width=550, height=250)

#BUTTON

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            text = txt.get("1.0", END)
            file.write(text)

def load_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            txt.delete("1.0", END)
            txt.insert(END, text)

btn1 = Button(win)
btn1.config(text="save")
btn1.config(command=save_file)
btn1.place(x=10,y=260)

btn2 = Button(win)
btn2.config(text="load")
btn2.config(command=load_file)
btn2.place(x=480,y=260)


win.mainloop()