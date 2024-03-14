import tkinter as tk

def show_text():
    for i in range(len(text_boxes)):
        text = text_boxes[i].get("1.0", tk.END)
        print("Textbox", i+1, "내용:")
        print(text)

# Tkinter 창 생성
win = tk.Tk()
win.geometry("400x300")
win.title("여러 개의 텍스트 상자")

# 여러 개의 텍스트 상자 생성
text_boxes = []
for i in range(3):  # 예시로 세 개의 텍스트 상자 생성
    text_box = tk.Text(win, height=5, width=40)
    text_box.pack(pady=5)
    text_boxes.append(text_box)

# 버튼 생성
btn_show = tk.Button(win, text="텍스트 상자 내용 표시", command=show_text)
btn_show.pack(pady=10)

win.mainloop()
