from tkinter import * 
from tkinter import filedialog

def save_text():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            for text_box in text_boxes:
                text = text_box.get("1.0", END).strip()
                file.write(text)
                file.write('\n---\n')

def load_text():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            contents = file.read().split('---')  # '---'를 기준으로 파일을 분할하여 리스트에 저장
            for i in range(len(contents)):
                if i < len(text_boxes):  # 파일에서 읽은 내용이 텍스트 상자보다 많으면 초과된 부분은 무시
                    text_boxes[i].delete("1.0", END)  # 텍스트 상자의 내용 지우기
                    text_boxes[i].insert(END, contents[i].strip())  # 파일에서 읽은 내용을 텍스트 상자에 삽입
                



win = Tk()

win.geometry("400x300")
win.title("여러 개의 텍스트 상자")

text_boxes = []
for i in range(3):
    text_box = Text(win, height=5, width=40)
    text_box.pack(pady=5)
    text_boxes.append(text_box)

btn_save = Button(win)
btn_save.config(text="저장")
btn_save.config(command=save_text)
btn_save.pack(pady=5)

btn_load = Button(win)
btn_load.config(text="불러오기")
btn_load.config(command=load_text)
btn_load.pack(pady=5)

win.mainloop()