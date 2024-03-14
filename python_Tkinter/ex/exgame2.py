#계산기 만들기
from tkinter import *

#비즈니스 로직
def click(key):
    if key == '=' :
        try :
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except:
            entry.insert(END, '오류!')
    elif key == 'C' :
        entry.delete(0, END)
    else:
        entry.insert(END, key)

#그래픽 디자인
window = Tk()
window.title('간단한 계산기')

buttons = [
'7', '8', '9', '+', 'C',
'4', '5', '6', '-', ' ',
'1', '2', '3', '*', ' ',
'0', '.', '=', '/', ' ' ]

#반복문으로 버튼 생성.
i = 0
for b in buttons :
    cmd = lambda x = b: click(x)
    b = Button(window, text=b, width=5, relief='ridge', command=cmd)
    b.grid(row=i // 5 +1, column=i % 5)
    i += 1

# 엔트리 위젯은 맨 윗줄의 5개의 셀에 걸쳐서 배치
entry = Entry(window, width = 33, bg='yellow')
entry.grid(row=0, column=0, columnspan=5) #columnspan=5는 5개의 컬럼을 전체적으로 적용하겠다는 말.

window.mainloop()