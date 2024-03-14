import tkinter as tk


class NoteGUI:
    def __init__(self):        
        self.root = tk.Tk()

        self.root.geometry("800x600")
        self.root.title("YSnote")
        self.root.resizable(True,True)

        

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="save", command=self.file_saving)

        self.menubar.add_cascade(menu=self.filemenu, label="File")

        self.root.config(menu=self.menubar)

        self.textbox = tk.Text(self.root, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.root.mainloop()

    def file_saving(self):
        print("save")

NoteGUI()