import tkinter as tk

'''Change file name and class name for
testing individual pages insted of oening homepage repetedly'''
from Rideshare import Rideshare_page

class Sample(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SpaceX")
        self.state('zoomed')
        self.config(bg='black')

        # change the class name for testing the single page
        canvas_frame = Rideshare_page(self)
        canvas_frame.pack(fill=tk.BOTH, expand=True, ipady=205)

if __name__ == "__main__":
    app = Sample()
    app.mainloop()