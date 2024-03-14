from tkinter import *

win = Tk()

win.geometry("600x300")
win.title("grid")
win.option_add("*Font", "궁서 20")

# 4x3 버튼 array
btn_list = []
col_num = 4
row_num = 3

for j in range(0,row_num):
    for i in range(0,col_num):
        btn = Button(win)
        btn.config(text="({},{})".format(i,j))
        btn.grid(column=i, row=j, padx=10, pady=10)
        btn_list.append(btn)

btn = Button(win)
btn.config(text="new")
btn.grid(column=3, row=0, rowspan=2)

win.mainloop()