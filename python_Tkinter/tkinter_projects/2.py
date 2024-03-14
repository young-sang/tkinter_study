import tkinter 
import pyshorteners

win = tkinter.Tk()
win.title("URL Shortener")
win.geometry("300x150")

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    shorturl_entry.insert(0, short_url)

longurl_label = tkinter.Label(win, text="Enter Long URL")
longurl_entry = tkinter.Entry(win)
shorturl_label = tkinter.Label(win, text="Output shortened URL")
shorturl_entry = tkinter.Entry(win)
shorten_button = tkinter.Button(win, text="Shorten URL", command=shorten)

longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorten_button.pack()

win.mainloop()