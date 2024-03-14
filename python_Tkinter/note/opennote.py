from tkinter import *
from tkinter import filedialog
import os

win = Tk()

win.geometry("550x300")
win.title("Note")
win.option_add("*Font", "맑은고딕 18")

def load_file(file_path):
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            txt.delete("1.0", END)
            txt.insert(END, text)

def save_file(file_path):
    if file_path:
        with open(file_path, 'w') as file:
            text = txt.get("1.0", END)
            file.write(text)
            
def on_closing(file_path):
    save_file(file_path)
    win.destroy()

desktop_path = os.path.join(os.path.join(os.path.sep, 'D:'))
file_path = os.path.join(desktop_path + '/Study_Code' + '/python_Tkinter' + '/1.txt')
# file_path = r"D:\Study_Code\python_Tkinter\1.txt"

#txt
txt = Text(win)
txt.pack(expand=True)

load_file(file_path)

win.protocol("WM_DELETE_WINDOW", lambda:on_closing(file_path))


win.mainloop()