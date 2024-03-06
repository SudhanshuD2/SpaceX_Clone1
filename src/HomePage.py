import tkinter as tk
from Labels import Label_Fr
from Canva import Canvass

class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.config(bg='black')

        label_frame = Label_Fr(self)
        label_frame.pack(side="top", fill=tk.X, ipady=30)

        canvas_frame = Canvass(self)
        canvas_frame.pack(side="left", fill="both", expand=True)

        tk.Label(self, text="Home Page").pack()
        tk.Button(self, text="Go to Page 1", command=self.go_to_page1).pack()
        tk.Button(self, text="Go to Page 2", command=self.go_to_page2).pack()
        tk.Button(self, text="Go to Page 3", command=self.go_to_page3).pack()

    def go_to_page1(self):
        from Page1 import Page1
        self.master.switch_frame(Page1)

    def go_to_page2(self):
        from Page2 import Page2
        self.master.switch_frame(Page2)

    def go_to_page3(self):
        from Page3 import Page3
        self.master.switch_frame(Page3)
