import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from Labels import Label_Fr
from HomePage import HomePage

class Rideshare_page(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.bg_color = 'black'
        self.fg_color = '#FFFFFF'
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.current_image_index = 0

        label_frame = Label_Fr(self)
        label_frame.pack(side="top", fill=tk.X, ipady=20)

        global canvas
        canvas = tk.Canvas(self, bg=self.bg_color, borderwidth=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)
        canvas.configure(scrollregion=canvas.bbox('all'))
        canvas.pack(fill=tk.BOTH, expand=tk.YES, ipady=205)

        back_button = tk.Button(canvas, text='<',bd=0,padx=0,pady=0,bg=self.bg_color, fg=self.fg_color,
                                font=('Arial',9, 'bold'),command=lambda: self.master.switch_frame(HomePage))
        canvas.create_window(110, 20, anchor=tk.NW, window= back_button)
# IMAGES
        rds_img = Image.open('assets/images/Labels/rds_1.jpg')
        rds_img = rds_img.resize((self.screen_width, self.screen_height-150), Image.LANCZOS)
        rds_p = ImageTk.PhotoImage(rds_img)

        canvas.image1 = rds_p
        canvas.create_image(880, 370, image=rds_p)

# LABELS and BUTTONS
        canvas.create_text(self.screen_width//2-80, 80, text='SMALLSAT',fill=self.fg_color, font=('Bahnschrift',56, 'bold'), anchor=tk.NW)
        canvas.create_text(self.screen_width//2-280, 160, text='RIDESHARE PROGRAM',fill=self.fg_color, font=('Bahnschrift',56, 'bold'), anchor=tk.NW)
        canvas.create_text(self.screen_width//2+100, 280, text='DEDICATED RIDESHARE MISSIONS AS LOW AS $300K*. SEARCH FLIGHTS BELOW.', fill=self.fg_color, font=('Bahnschrift',12))
        
        canvas.create_text(self.screen_width//2-250, 350, text='DESIRED ORBIT',fill='#ADADAD', font=('Bahnschrift',10, 'bold'), anchor=tk.NW)
        canvas.create_text(self.screen_width//2-60, 350, text='NO EARLIER THAN',fill='#ADADAD', font=('Bahnschrift',10, 'bold'), anchor=tk.NW)
        canvas.create_text(self.screen_width//2+160, 350, text='INPUT PAYLOAD MASS',fill='#ADADAD', font=('Bahnschrift',10, 'bold'), anchor=tk.NW)
        canvas.create_text(self.screen_width//2+340, 350, text='ESTIMATED PRICE',fill='#ADADAD', font=('Bahnschrift',10, 'bold'), anchor=tk.NW)
        
        canvas.create_text(self.screen_width//2-250, 380, text='SSO',fill=self.fg_color, font=('Bahnschrift',24, 'bold'), anchor=tk.NW)
        # self.buttons1()
# Write any code above
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox('all'))
        canvas.bind('<Configure>', self.on_canvas_configure)

    def on_mouse_wheel(self, event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def on_canvas_configure(self, event):
        canvas.configure(scrollregion=canvas.bbox('all'))
    
    def disp_imgs(self):
        image = self.images[self.current_image_index].resize((self.screen_width-100, self.screen_height-150), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(image)
        canvas.create_image(145, 370*5.8, anchor=tk.NW, image=self.image)

    def swipe(self, dirn):
        if dirn == 'left':
            self.current_image_index = (self.current_image_index - 1) % len(self.images)
            self.disp_imgs()
            # canvas.delete('text')

        else:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.disp_imgs()
            # canvas.delete('text')
    
    def go_to_page2(self):
        from Falcon9 import Falcon_9
        self.master.switch_frame(Falcon_9)

    def go_to_page3(self):
        from Falcon_heavy import Falcon_Heavy
        self.master.switch_frame(Falcon_Heavy)

    def go_to_page4(self):
        from Dragon import Dragon_page
        self.master.switch_frame(Dragon_page)
    
    def go_to_page5(self):
        from Starship import Starship_page
        self.master.switch_frame(Starship_page)
    def go_to_page7(self):
        messagebox.showinfo('Same page', 'You are on the same page only')
    
    # def buttons1(self):
    #     lbl1 = tk.Label(canvas, text='DESIRED ORBIT',fg='#ADADAD', bg='#272727', font=('Bahnschrift',10, 'bold'))
    #     lbl1.pack(padx=0, pady=5, anchor='nw')

    #     lbl2 = tk.Label(canvas, text='SSO', fg=self.fg_color, bg=self.bg_color, font=('Bahnschrift',24, 'bold'))
    #     lbl2.pack(padx=5, pady=5, anchor='center')