import tkinter as tk
from HomePage import HomePage

class SampleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SpaceX")
        self.state('zoomed')
        self.config(bg='black')
        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if hasattr(self, "current_frame"):
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
