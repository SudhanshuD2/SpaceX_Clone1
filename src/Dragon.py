import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser as wb
from PIL import Image, ImageTk
from Labels import Label_Fr
from HomePage import HomePage

class Dragon_page(tk.Frame):
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
# Image labels
        drag_img = Image.open('assets/images/Labels/dr_1.jpg')
        drag_img = drag_img.resize((self.screen_width-100, self.screen_height-200), Image.LANCZOS)
        drag_p = ImageTk.PhotoImage(drag_img)

        drag2_img = Image.open('assets/images/Labels/Dr_2.png')
        drag2_img = drag2_img.resize((self.screen_width+50, self.screen_height-100), Image.LANCZOS)
        drag2_p = ImageTk.PhotoImage(drag2_img)

        drag3_img = Image.open('assets/images/Labels/dr_3.jpg')
        drag3_img = drag3_img.resize((self.screen_width, self.screen_height-50), Image.LANCZOS)
        drag3_p = ImageTk.PhotoImage(drag3_img)

        drag4_img = Image.open('assets/images/Labels/dr_4.jpg')
        drag4_img = drag4_img.resize((self.screen_width, self.screen_height-140), Image.LANCZOS)
        drag4_p = ImageTk.PhotoImage(drag4_img)

        drag5_img = Image.open('assets/images/Labels/Draco_5.jpg')
        drag5_img = drag5_img.resize((self.screen_width, self.screen_height-100), Image.LANCZOS)
        drag5_p = ImageTk.PhotoImage(drag5_img)

        drag6_img = Image.open('assets/images/Labels/dr_6_right.jpg')
        drag6_img = drag6_img.resize((self.screen_width//2+50, self.screen_height-200), Image.LANCZOS)
        drag6_p = ImageTk.PhotoImage(drag6_img)

        canvas.image1 = drag_p
        canvas.create_image(880, 370, image=drag_p)

        canvas.image2 = drag2_p
        canvas.create_image(760, 370*3.7, image=drag2_p)

        canvas.image3 = drag3_p
        canvas.create_image(760, 370*5.84, image=drag3_p)

        canvas.image4 = drag4_p
        canvas.create_image(760, 370*7.98, image=drag4_p)

        canvas.image5 = drag5_p
        canvas.create_image(760, 370*10.05, image=drag5_p)

        canvas.image6 = drag6_p
        canvas.create_image(1040, 370*12.10, image=drag6_p)

        self.images = [Image.open('assets/images/Labels/dr_l1.jpg'),Image.open('assets/images/Labels/dr_l2.jpg'),
                       Image.open('assets/images/Labels/dr_l3.jpg'),Image.open('assets/images/Labels/dr_l4.jpg'),
                       Image.open('assets/images/Labels/dr_l5.jpg')]
        self.disp_imgs()

        left_button = tk.Button(self, text='<', bd=0, padx=0, pady=0, bg=self.bg_color, fg=self.fg_color,
                                font=('Arial', 18, 'bold'), command=lambda: self.swipe('left'))
        canvas.create_window(100, 370*15.6, anchor=tk.NW, window= left_button)
        
        right_button = tk.Button(self, text='>', bd=0, padx=0, pady=0, bg=self.bg_color, fg=self.fg_color,
                                 font=('Arial', 18, 'bold'), command=lambda: self.swipe('right'))
        canvas.create_window(self.screen_width-130, 370*15.6, anchor=tk.NW, window= right_button)

# Text and Buttons
        canvas.create_text(self.screen_width//2-180, 220, text='DRAGON',fill=self.fg_color, font=('Bahnschrift',72, 'bold'), anchor=tk.NW)
        canvas.create_text(self.screen_width//2, 350, text='SENDING HUMANS AND CARGO INTO SPACE', fill=self.fg_color, font=('Bahnschrift',11))

        canvas.create_text(self.screen_width//2-400, 780, text='45', fill=self.fg_color, font=("Bahnschrift", 100))
        canvas.create_text(self.screen_width//2-30, 780, text='40', fill=self.fg_color, font=("Bahnschrift", 100))
        canvas.create_text(self.screen_width//2+380, 780, text='24', fill=self.fg_color, font=("Bahnschrift", 100))

        canvas.create_text(370, 870, text='TOTAL LAUNCHES', fill=self.fg_color, font=("Bahnschrift", 16))
        canvas.create_text(740, 870, text='VISITS TO THE ISS', fill=self.fg_color, font=("Bahnschrift", 16))
        canvas.create_text(1160, 870, text='TOTAL REFLIGHTS', fill=self.fg_color, font=("Bahnschrift", 16))

        text1 = ['The Dragon spacecraft is capable of carrying up to 7 passengers to and from\n',
                'Earth orbit, and beyond. It is the only spacecraft currently flying that is\n',
                'capable of returning significant amounts of cargo to Earth, and is the first\n',
                'private spacecraft to take humans to the space station.']
        canvas.create_text(390, 975, text=f'{text1[0]}{text1[1]}{text1[2]}{text1[3]}', fill=self.fg_color, font=("Bahnschrift", 13))

        canvas.create_text(145, 1145, text='DRAGON', fill=self.fg_color, font=("Bahnschrift", 16))
        canvas.create_text(215, 1190, text='OVERVIEW', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))
        
        canvas.create_text(130, 1320, text='HEIGHT', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(140, 1320+55, text='DIAMETER', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(185, 1320+55*2, text='SPACECRAFT VOLUME', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(160, 1320+55*3, text='TRUNK VOLUME', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(193, 1320+55*4, text='LAUNCH PAYLOAD MASS', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(193, 1320+55*5, text='RETURN PAYLOAD MASS', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))

        canvas.create_text(560, 1320, text='8.1 m / 26.7 ft', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1320+55, text='4 m / 13 ft', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1320+55*2, text='9.3 m³ / 328 ft³', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1320+55*3, text='37 m³ / 1300 ft³', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1320+55*4, text='6,000 kg / 13,228 lbs', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1320+55*5, text='3,000 kg / 6,614 lbs', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))

        canvas.create_text(130, 2270, text='VIDEO', fill=self.fg_color, font=("Bahnschrift", 14, 'bold'))
        canvas.create_text(270, 2350, text='CREW DRAGON\nINTERIOR', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))

        canvas.create_text(1080, 2770, text='TAKING HUMANS TO\nSPACE', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))
        text1 = ['In 2020, SpaceX returned America’s ability to fly NASA astronauts to and from\n',
                'the International Space Station on American vehicles for the first time since\n',
                '2011. In addition to flying astronauts to space for NASA, SpaceX’s Dragon\n',
                'spacecraft can also carry commercial astronauts to Earth orbit, the ISS or\n',
                'beyond.']
        canvas.create_text(1140, 2900, text=f'{text1[0]}{text1[1]}{text1[2]}{text1[3]}{text1[4]}', 
                           fill=self.fg_color, font=("Bahnschrift", 12))
        Learn_mre = tk.Button(self, text='LEARN MORE', bd=0, padx=5, pady=10, bg=self.bg_color, fg=self.fg_color,
                                font=('Arial',10, 'bold'))  # , command= lambda: link to the Human spaceflight page
        canvas.create_window(870, 3000, anchor=tk.NW, window= Learn_mre)
        Learn_mre.bind('<Enter>', lambda event: Learn_mre.config(bg=self.fg_color, fg=self.bg_color))
        Learn_mre.bind('<Leave>', lambda event: Learn_mre.config(bg=self.bg_color, fg=self.fg_color))

        text2 = ['The Dragon spacecraft is equipped with 16 Draco thrusters used to orient the\n',
        'spacecraft during the mission, including apogee/perigee maneuvers, orbit\n',
        'adjustment and attitude control. Each Draco thruster is capable of generating\n',
        '90 pounds of force in the vacuum of space.\n']
        canvas.create_text(135, 3470, text='ENGINES', fill=self.fg_color, font=("Bahnschrift", 11, 'bold'))
        canvas.create_text(180, 3500, text='DRACO', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))

        canvas.create_text(130, 3630, text='DRACO', fill=self.fg_color, font=("Bahnschrift", 12))
        canvas.create_text(220, 3630, text='| SUPERDRACO', fill='grey', font=("Bahnschrift", 12))
        
        canvas.create_text(385, 3720, text=f'{text2[0]}{text2[1]}{text2[2]}{text2[3]}', 
                           fill=self.fg_color, font=("Bahnschrift", 12))
        
        canvas.create_text(185, 3830, text='NUMBER OF ENGINES', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(180, 3830+50, text='THRUST IN VACUUM', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(580, 3830, text='16', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(580, 3830+50, text='400 N / 90 lbf', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))

        canvas.create_text(235, 4350, text='DRAGON\nPARACHUTE\nSYSTEM', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))
        text1 = ['The Dragon spacecraft is equipped with two drogue parachutes to\n',
                'stabilize the spacecraft following reentry and four main parachutes\n',
                'to further decelerate the spacecraft prior to landing.']
        canvas.create_text(350, 4480, text=f'{text1[0]}{text1[1]}{text1[2]}', 
                           fill=self.fg_color, font=("Bahnschrift", 12))
        Learn_mre = tk.Button(self, text='WATCH VIDEO', bd=0, padx=5, pady=10, bg=self.bg_color, fg=self.fg_color,
                                font=('Arial',10, 'bold'))  # watch video link
        canvas.create_window(100, 4550, anchor=tk.NW, window= Learn_mre)
        Learn_mre.bind('<Enter>', lambda event: Learn_mre.config(bg=self.fg_color, fg=self.bg_color))
        Learn_mre.bind('<Leave>', lambda event: Learn_mre.config(bg=self.bg_color, fg=self.fg_color))

        # Bottom most frame and buttons
        canvas.create_text(self.screen_width//2-150, 5950, text="SpaceX © 2024", fill=self.fg_color, anchor=tk.SW)
        pp_button = tk.Button(canvas, text='PRIVACY POLICY', bd=0, bg=self.bg_color, fg=self.fg_color,
                               command=lambda: wb.open('https://www.spacex.com/media/privacy_policy_spacex.pdf'))
        canvas.create_window(self.screen_width//2-50, 5955, anchor=tk.SW, window=pp_button)
        sup_button = tk.Button(canvas, text='SUPPLIERS',bd=0,  bg=self.bg_color, fg=self.fg_color,
                                command=lambda: wb.open('https://www.spacex.com/supplier/'))
        canvas.create_window(self.screen_width//2+60, 5955, anchor=tk.SW, window=sup_button)
        canvas.create_text(1300, 5945, text="@ SudhanshuD\tSelf", fill=self.fg_color, anchor=tk.SW)
# Write any code above
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox('all'))
        canvas.bind('<Configure>', self.on_canvas_configure)

    def on_mouse_wheel(self, event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def on_canvas_configure(self, event):
        canvas.configure(scrollregion=canvas.bbox('all'))
    
    def disp_imgs(self):
        image = self.images[self.current_image_index].resize((self.screen_width, self.screen_height), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(image)
        canvas.create_image(0, 370*13.2, anchor=tk.NW, image=self.image)
        
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
        messagebox.showinfo('Same page', 'You are on the same page only')
    
    def go_to_page5(self):
        from Starship import Starship_page
        self.master.switch_frame(Starship_page)
    
    def go_to_page7(self):
        from Rideshare import Rideshare_page
        self.master.switch_frame(Rideshare_page)