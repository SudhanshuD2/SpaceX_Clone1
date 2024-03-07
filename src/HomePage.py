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
        label_frame.pack(side="top", fill=tk.X, ipady=20)

        canvas_frame = Canvass(self)
        canvas_frame.pack(fill=tk.BOTH, expand=True, ipady=200)

    def go_to_page1(self):
        from PACE_M import pace_info
        self.master.switch_frame(pace_info)

    def go_to_page2(self):
        from Falcon9 import Falcon_9
        self.master.switch_frame(Falcon_9)

    def go_to_page3(self):
        from Falcon_heavy import Falcon_Heavy
        self.master.switch_frame(Falcon_Heavy)

    def go_to_home(self):
        self.master.switch_frame(HomePage)
