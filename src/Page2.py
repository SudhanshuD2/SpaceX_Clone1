import tkinter as tk
from HomePage import HomePage

class Page2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        tk.Label(self, text="Page 2").pack()
        tk.Button(self, text="Back to Home", command=self.go_to_home).pack()

    def go_to_home(self):
        self.master.switch_frame(HomePage)
