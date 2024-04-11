import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import webbrowser as wb

class Canvass(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.frame = self
        self.delay = 15
        self.bg_color = '#000000'
        self.fg_color = '#FFFFFF'
        self.button_hover_color = 'white'

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        AX_3_img = Image.open('assets/images/AX_3.jpeg')
        AX_3_img = AX_3_img.resize((self.screen_width+15, self.screen_height), Image.ANTIALIAS)
        AX_3_p = ImageTk.PhotoImage(AX_3_img)

        starlink_img = Image.open('assets/images/Starlink_G7_2.jpg')
        starlink_img = starlink_img.resize((self.screen_width+15, self.screen_height-100), Image.ANTIALIAS)
        starlink_p = ImageTk.PhotoImage(starlink_img)

        pace_img = Image.open('assets/images/PACE_curbh_3.jpg')
        pace_img = pace_img.resize((self.screen_width+15, self.screen_height), Image.ANTIALIAS)
        pace_p = ImageTk.PhotoImage(pace_img)

        ng_20_img = Image.open('assets/images/NG_20_4.jpg')
        ng_20_img = ng_20_img.resize((self.screen_width+15,self.screen_height), Image.ANTIALIAS)
        ng_20_p = ImageTk.PhotoImage(ng_20_img)

        global canvas
        canvas = tk.Canvas(self, bg=self.bg_color, borderwidth=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)
        canvas.configure(scrollregion=canvas.bbox('all'))
        canvas.pack(fill=tk.BOTH, expand=tk.YES)
        
        canvas.image1 = AX_3_p
        canvas.create_image(780, 140, image = AX_3_p)

        canvas.create_text(100, 265, text='DRAGON RETURNS TO EARTH', fill=self.fg_color, font=('Mangal', 15), anchor=tk.SW)
        canvas.create_text(100, 335, text='AX-3 MISSION', fill=self.fg_color, font=('Mangal', 36), anchor=tk.SW)

        watch_button = tk.Button(canvas, text='  REWATCH  ',bd=0,padx=35,pady=15,bg='#6E9DFF', fg=self.fg_color, font=('Arial',11),
                                  command=lambda: self.on_watch_click('AX-3 Launch', self))
        canvas.create_window(100, 400, anchor=tk.SW, window=watch_button)   # watch_button.place(x=100, y=480, anchor=tk.SW)

        watch_button.bind('<Enter>', lambda event: watch_button.config(bg=self.button_hover_color, fg=self.bg_color))
        watch_button.bind('<Leave>', lambda event: watch_button.config(bg='#6E9DFF', fg=self.fg_color))

        canvas.image2 = starlink_p
        canvas.create_image(780, 140*6.81, image = starlink_p)

        canvas.create_text(108, 1055, text='RECENT LAUNCH', fill=self.fg_color, font=('Mangal', 15), anchor=tk.SW)
        canvas.create_text(108, 1120, text='STARLINK MISSION', fill=self.fg_color, font=('Mangal', 34), anchor=tk.SW)

        watch_button2 = tk.Button(canvas, text='  REWATCH  ',bd=0,padx=35,pady=15,bg='#2C4E31', fg=self.fg_color, font=('Arial',11),
                                   command=lambda: self.on_watch_click('Starlink Launch', self))
        canvas.create_window(108, 1190, anchor=tk.SW, window=watch_button2)   # watch_button.place(x=100, y=480, anchor=tk.SW)

        watch_button2.bind('<Enter>', lambda event: watch_button2.config(bg=self.button_hover_color, fg=self.bg_color))
        watch_button2.bind('<Leave>', lambda event: watch_button2.config(bg='#2C4E31', fg=self.fg_color))

        canvas.image3 = pace_p
        canvas.create_image(780, 140*12.62, image= pace_p)

        canvas.create_text(100, 1905, text='RECENT LAUNCH', fill=self.fg_color, font=('Mangal', 15), anchor=tk.SW)
        canvas.create_text(100, 1975, text='PACE MISSION', fill=self.fg_color, font=('Mangal', 36), anchor=tk.SW)

        watch_button3 = tk.Button(canvas, text='LEARN MORE',bd=0,padx=35,pady=15,bg='#411D1D', fg=self.fg_color, font=('Arial',11), 
                                  command=lambda:self.on_watch_click('PACE Launch', self))
        canvas.create_window(100, 2050, anchor=tk.SW, window=watch_button3)   # watch_button.place(x=100, y=480, anchor=tk.SW)

        watch_button3.bind('<Enter>', lambda event: watch_button3.config(bg=self.button_hover_color, fg=self.bg_color))
        watch_button3.bind('<Leave>', lambda event: watch_button3.config(bg='#411D1D', fg=self.fg_color))

        canvas.image4 = ng_20_p
        canvas.create_image(780, 140*18.8, image= ng_20_p)

        canvas.create_text(100, 2750, text='RECENT LAUNCH', fill=self.fg_color, font=('Mangal', 15), anchor=tk.SW)
        canvas.create_text(100, 2820, text='NG-20 MISSION', fill=self.fg_color, font=('Mangal', 38), anchor=tk.SW)

        watch_button4 = tk.Button(canvas, text='  REWATCH  ',bd=0,padx=35,pady=15,bg='#125C8F', fg=self.fg_color, font=('Arial',11), 
                                  command=lambda: self.on_watch_click('NG-20 Launch', self))
        canvas.create_window(100, 2900, anchor=tk.SW, window=watch_button4)   # watch_button.place(x=100, y=480, anchor=tk.SW)

        watch_button4.bind('<Enter>', lambda event: watch_button4.config(bg=self.button_hover_color, fg=self.bg_color))
        watch_button4.bind('<Leave>', lambda event: watch_button4.config(bg='#125C8F', fg=self.fg_color))
     
        watch_button5 = tk.Button(canvas, text='LEARN MORE',bd=0,padx=35,pady=15,bg='#262342', fg=self.fg_color, font=('Arial',11),
                                   command=lambda: self.on_watch_click('Starship-2 Test', self))
        canvas.create_window(110, 3660, anchor=tk.SW, window=watch_button5)

        watch_button5.bind('<Enter>', lambda event: watch_button5.config(bg=self.button_hover_color, fg=self.bg_color))
        watch_button5.bind('<Leave>', lambda event: watch_button5.config(bg='#262342', fg=self.fg_color))

        # Bottom most frame and buttons
        canvas.create_text(self.screen_width//2-150, 3860, text="SpaceX © 2024", fill=self.fg_color, anchor=tk.SW)
        pp_button = tk.Button(canvas, text='PRIVACY POLICY', bd=0, bg=self.bg_color, fg=self.fg_color,
                               command=lambda: wb.open('https://www.spacex.com/media/privacy_policy_spacex.pdf'))
        canvas.create_window(self.screen_width//2-50, 3865, anchor=tk.SW, window=pp_button)
        sup_button = tk.Button(canvas, text='SUPPLIERS',bd=0,  bg=self.bg_color, fg=self.fg_color,
                                command=lambda: wb.open('https://www.spacex.com/supplier/'))
        canvas.create_window(self.screen_width//2+60, 3865, anchor=tk.SW, window=sup_button)
        canvas.create_text(1300, 3860, text="@ SudhanshuD\tSelf", fill=self.fg_color, anchor=tk.SW)

        self.video_src = 'assets/images/starship_vid.mp4'
        self.video = cv2.VideoCapture(self.video_src)

        canvas.create_image(0, 140*21.89, anchor=tk.NW)

        self.update()

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox('all'))

        # Set the maximum scroll region
        canvas.bind('<Configure>', self.on_canvas_configure)

    def on_canvas_configure(self, event):
        canvas.configure(scrollregion=canvas.bbox('all'))
    
    def on_mouse_wheel(self, event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def update(self):
        ret, frame = self.video.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (self.screen_width, self.screen_height-100))
            photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            canvas.create_image(0, 140*21.89, image=photo, anchor=tk.NW)
            canvas.image = photo
        else:
            self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.frame.after(self.delay, self.update)
        
    def on_watch_click(self, mission, fr):
        messagebox.showinfo('Watch', f'Will Redirect to watch {mission}!!!')

        if mission == 'AX-3 Launch':
            wb.open('https://twitter.com/i/broadcasts/1jMJgmndrAPKL')

        elif mission == 'Starlink Launch':
            wb.open('https://twitter.com/i/broadcasts/1yNGaZRVeLgJj')
        
        elif mission == 'NG-20 Launch':
            wb.open('https://twitter.com/i/broadcasts/1yoKMwYaNPlJQ')
        
        elif mission == 'PACE Launch':
            self.master.go_to_page1()