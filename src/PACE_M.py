import tkinter as tk
from tkinter import ttk, messagebox
from HomePage import HomePage
from Labels import Label_Fr
import webbrowser as wb
from PIL import Image, ImageTk

class pace_info(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.bg_color = '#000000'
        self.fg_color = '#FFFFFF'

        label_frame = Label_Fr(self)
        label_frame.pack(side="top", fill=tk.X, ipady=20)

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        global canvas
        canvas = tk.Canvas(self, bg=self.bg_color, borderwidth=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)
        canvas.configure(scrollregion=canvas.bbox('all'))
        canvas.pack(fill=tk.BOTH, expand=tk.YES, ipady=200)

        pace_img = Image.open('assets/images/PACE_enginecurb.jpg')
        pace_img = pace_img.resize((self.screen_width, self.screen_height-180), Image.LANCZOS)
        pace_p = ImageTk.PhotoImage(pace_img)

        back_button = tk.Button(canvas, text='<  BACK TO LAUNCHES',bd=0,padx=0,pady=0,bg=self.bg_color, fg=self.fg_color,
                                font=('Arial',9),command=lambda: self.go_to_home())
        canvas.create_window(110, 20, anchor=tk.NW, window= back_button)

        back_button.bind('<Enter>', lambda event: back_button.config(text='<    BACK TO LAUNCHES'))
        back_button.bind('<Leave>', lambda event: back_button.config(text='<  BACK TO LAUNCHES'))

        canvas.image1 = pace_p
        canvas.create_image(790, 390, image=pace_p)
        text11 = 'On Thursday, February 8 at 1:33 a.m. ET, Falcon 9 launched NASA’s PACE (Plankton, Aerosol, Cloud,'
        text12 = 'ocean Ecosystem) mission to a sun-synchronous orbit from Space Launch Complex 40 (SLC-40)'
        text13 = 'at Cape Canaveral Space Force Station in Florida.'
        text21 = 'This was the fourth flight of the first stage booster supporting this mission, which'
        text22 = 'previously launched Crew-7, CRS-29, and one Starlink mission.'
        canvas.create_text(110, 750, text='FEBRUARY 8, 2024',fill='#858585', font=('Bahnschrift',14), anchor=tk.NW)
        canvas.create_text(200, 825, text='PACE MISSION', fill=self.fg_color, font=('Agency FB', 28, 'bold'))
        canvas.create_text(460, 950, text=f'{text11}\n{text12}\n{text13}', fill=self.fg_color, font=('Bahnschrift', 13))
        canvas.create_text(1200, 940, text=f'{text21}\n{text22}', fill=self.fg_color, font=('Bahnschrift', 13))

        # Bottom most frame and buttons
        canvas.create_text(self.screen_width//2-150, 1055, text="SpaceX © 2024", fill=self.fg_color, anchor=tk.SW)
        pp_button = tk.Button(canvas, text='PRIVACY POLICY', bd=0, bg=self.bg_color, fg=self.fg_color,
                               command=lambda: wb.open('https://www.spacex.com/media/privacy_policy_spacex.pdf'))
        canvas.create_window(self.screen_width//2-50, 1060, anchor=tk.SW, window=pp_button)
        sup_button = tk.Button(canvas, text='SUPPLIERS',bd=0,  bg=self.bg_color, fg=self.fg_color,
                                command=lambda: wb.open('https://www.spacex.com/supplier/'))
        canvas.create_window(self.screen_width//2+60, 1060, anchor=tk.SW, window=sup_button)
        canvas.create_text(1300, 1050, text="@ SudhanshuD\tSelf", fill=self.fg_color, anchor=tk.SW)

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox('all'))
        canvas.bind('<Configure>', self.on_canvas_configure)

    def on_canvas_configure(self, event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    def go_to_home(self):
        self.master.switch_frame(HomePage)
    
    def on_mouse_wheel(self, event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")
