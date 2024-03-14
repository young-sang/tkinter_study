from tkinter import *

def show_text():
    for i in range(len(text_boxes)):
        text = text_boxes[i].get("1.0", END)
        print("Textbox", i+1, "내용:")
        print(text)

win = Tk()

win.geometry("400x300")
win.title("MULTIPLE_NOTE")
win.option_add("*Font", "맑은고딕")

text_boxes = []
for i in range(3):
    text_box = Text(win)
    text_box.config(height=4, width=40)
    text_box.pack(pady=5)
    text_boxes.append(text_box)

btn = Button(win)
btn.config(text="텍스트 상자 내용 표시")
btn.config(command=show_text)
btn.pack(pady=10)

win.mainloop()