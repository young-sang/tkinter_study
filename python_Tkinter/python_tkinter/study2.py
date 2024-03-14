from tkinter import *
import requests
from bs4 import BeautifulSoup

win = Tk()

win.geometry("300x100")
win.option_add("*Font","궁서체 20")
win.title("로또번호")

ent = Entry(win)
ent.pack()

def ent_p():
    a = ent.get()
    print(a)

def lotto_p():
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
    #<div class="win_result">

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    txt = soup.find("div", attrs= {"class","win_result"}).get_text()
    num_list = txt.split("\n")[7:13]
    bonus = txt.split("\n")[-4]
    print("당첨번호")
    print(num_list)
    print("보너스번호")
    print(bonus)

btn = Button(win)
btn.config(text="로또 당첨 번호 확인")
btn.config(command=lotto_p)
btn.pack()

win.mainloop()
