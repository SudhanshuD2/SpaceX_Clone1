import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser as wb
from PIL import Image, ImageTk
from Labels import Label_Fr
from HomePage import HomePage

class Starship_page(tk.Frame):
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
        Sp1_img = Image.open('assets/images/Labels/SP1.jpg')
        Sp1_img = Sp1_img.resize((self.screen_width, self.screen_height-150), Image.LANCZOS)
        Sp1_p = ImageTk.PhotoImage(Sp1_img)

        Sp2_img = Image.open('assets/images/SP_21.png')
        Sp2_img = Sp2_img.resize((self.screen_width, self.screen_height-150), Image.LANCZOS)
        Sp2_p = ImageTk.PhotoImage(Sp2_img)

        Sp3_img = Image.open('assets/images/Labels/SP_3.jpg')
        Sp3_img = Sp3_img.resize((self.screen_width, self.screen_height-150), Image.LANCZOS)
        Sp3_p = ImageTk.PhotoImage(Sp3_img)

        self.images = [Image.open('assets/images/Labels/SP_4.jpg'),Image.open('assets/images/Labels/SP_42.jpg'),
                       Image.open('assets/images/Labels/SP_43.jpg'),Image.open('assets/images/Labels/SP_44.jpg'),
                       Image.open('assets/images/Labels/SP_45.jpg')]
        self.disp_imgs()
        left_button = tk.Button(self, text='<', bd=0, padx=0, pady=0, bg=self.bg_color, fg=self.fg_color,
                                font=('Arial', 18, 'bold'), command=lambda: self.swipe('left'))
        canvas.create_window(110, 370*6.6, anchor=tk.NW, window= left_button)
        
        right_button = tk.Button(self, text='>', bd=0, padx=0, pady=0, bg=self.bg_color, fg=self.fg_color,
                                 font=('Arial', 18, 'bold'), command=lambda: self.swipe('right'))
        canvas.create_window(self.screen_width+50, 370*6.6, anchor=tk.NW, window= right_button)
        # Sp4_img = Image.open('assets/images/Labels/SP_4.jpg')
        # Sp4_img = Sp4_img.resize((self.screen_width, self.screen_height-150), Image.LANCZOS)
        # Sp4_p = ImageTk.PhotoImage(Sp4_img)

        Sp5_img = Image.open('assets/images/Labels/SP_5.jpg')
        Sp5_img = Sp5_img.resize((self.screen_width, self.screen_height-150), Image.LANCZOS)
        Sp5_p = ImageTk.PhotoImage(Sp5_img)

        Last_img = Image.open('assets/images/Labels/SP_L.jpg')
        Last_img = Last_img.resize((self.screen_width, self.screen_height-150), Image.LANCZOS)
        Last_p = ImageTk.PhotoImage(Last_img)

        canvas.image1 = Sp1_p
        canvas.create_image(880, 370, image=Sp1_p)
        canvas.image2 = Sp2_p
        canvas.create_image(880, 370*2.93, image=Sp2_p)
        canvas.image3 = Sp3_p
        canvas.create_image(880, 370*4.86, image=Sp3_p)
        # canvas.image4 = Sp4_p
        # canvas.create_image(880, 370*6.8, image=Sp4_p)
        canvas.image5 = Sp5_p
        canvas.create_image(880, 370*8.74,image=Sp5_p)
        canvas.image6 = Last_p
        canvas.create_image(880, 370*10.68, image=Last_p)
# LABELS AND BUTTONS
        
        canvas.create_text(self.screen_width//2-115, 220, text='STARSHIP',fill=self.fg_color, font=('Bahnschrift',72, 'bold'), anchor=tk.NW)
        canvas.create_text(self.screen_width//2+100, 350, text='SERVICE TO EARTH ORBIT, MOON, MARS AND BEYOND', fill=self.fg_color, font=('Bahnschrift',12))

        text1 = ['SpaceX\'s Starship spacecraft and Super Heavy rocket -\n',
                'collectively referred to as Starship - represent a fully reusable\n',
                'transportation system designed to carry both crew and cargo to\n',
                'Earth orbit, the Moon, Mars and beyond. Starship is the world\'s\n',
                'most powerful launch vehicle ever developed, capable of carrying\n',
                'up to 150 metric tonnes fully reusable and 250 metric tonnes\nexpendable.']
        canvas.create_text(455, 1020, text=f'{text1[0]}{text1[1]}{text1[2]}{text1[3]}{text1[4]}{text1[5]}', fill=self.fg_color, font=("Bahnschrift", 13))

        canvas.create_text(440, 880, text='STARSHIP OVERVIEW', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))
        
        canvas.create_text(235, 1180, text='HEIGHT', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(245, 1180+55, text='DIAMETER', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(280, 1180+55*2, text='PAYLOAD CAPACITY', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))

        canvas.create_text(760, 1180, text='121 m / 397 ft', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(760, 1180+55, text='9 m / 29.5 ft', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(760, 1180+55*2, text='100 - 150 t (fully reusable)', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))

        text2 = ['Starship leverages tanker vehicles (essentially the Starship\n',
                'spacecraft minus the windows) to refill the Starship spacecraft in\n',
                'low-Earth orbit prior to departing for Mars. Refilling on-orbit\n',
                'enables the transport of up to 100 tons all the way to Mars. And if\n',
                'the tanker ship has high reuse capability, the primary cost is just\n',
                'that of the oxygen and methane, which is extremely low.']
        canvas.create_text(440, 3280, text='ON-ORBIT REFILLING', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))
        canvas.create_text(455, 3390, text=f'{text2[0]}{text2[1]}{text2[2]}{text2[3]}{text2[4]}{text2[5]}', fill=self.fg_color, font=("Bahnschrift", 13))

        text3 = ['Development and manufacturing of Starship takes place at Starbase, one of\n',
                 'the world\'s first commercial spaceports designed for orbital missions.']
        canvas.create_text(325, 4000, text='STARBASE', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))
        canvas.create_text(460, 4070, text=f'{text3[0]}{text3[1]}', fill=self.fg_color, font=("Bahnschrift", 11))

        Watch_btn = tk.Button(self, text='WATCH VIDEO', bd=0, padx=20, pady=10, bg='#044707', fg=self.fg_color,
                                font=('Arial',10, 'bold'))  # watch video link
        canvas.create_window(220,4120, anchor=tk.NW, window= Watch_btn)
        Watch_btn.bind('<Enter>', lambda event: Watch_btn.config(bg=self.fg_color, fg='#044707'))
        Watch_btn.bind('<Leave>', lambda event: Watch_btn.config(bg='#044707', fg=self.fg_color))

        Learn_mre = tk.Button(self, text='LEARN MORE ABOUT STARBASE', bd=0, padx=20, pady=10, bg=self.bg_color, fg=self.fg_color,
                                font=('Arial',10, 'bold'))  # watch video link
        canvas.create_window(self.screen_width//2-30,4460, anchor=tk.NW, window= Learn_mre)
        Learn_mre.bind('<Enter>', lambda event: Learn_mre.config(bg=self.fg_color, fg=self.bg_color))
        Learn_mre.bind('<Leave>', lambda event: Learn_mre.config(bg=self.bg_color, fg=self.fg_color))

        # Bottom most frame and buttons
        canvas.create_text(self.screen_width//2-30, 4850, text="SpaceX © 2024", fill=self.fg_color, anchor=tk.SW)
        pp_button = tk.Button(canvas, text='PRIVACY POLICY', bd=0, bg=self.bg_color, fg=self.fg_color,
                               command=lambda: wb.open('https://www.spacex.com/media/privacy_policy_spacex.pdf'))
        canvas.create_window(self.screen_width//2+80, 4855, anchor=tk.SW, window=pp_button)
        sup_button = tk.Button(canvas, text='SUPPLIERS',bd=0,  bg=self.bg_color, fg=self.fg_color,
                                command=lambda: wb.open('https://www.spacex.com/supplier/'))
        canvas.create_window(self.screen_width//2+200, 4855, anchor=tk.SW, window=sup_button)
        canvas.create_text(1300, 4845, text="@ SudhanshuD\tSelf", fill=self.fg_color, anchor=tk.SW)

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

        if self.current_image_index == 0:
            canvas.create_text(375, 370*6.9, text='STARSHIP\nCAPABILITIES', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))
            txt1 = ['As the most powerful launch system ever developed, Starship will\n',
                    'be able to carry up to 100 people on long-duration, interplanetary\n',
                    'flights. Starship will also help enable satellite delivery, the\n',
                    'development of a Moon base, and point-to-point transport here on\nEarth.']
            canvas.create_text(440, 370*7.2, text=f'{txt1[0]}{txt1[1]}{txt1[2]}{txt1[3]}', fill=self.fg_color, font=("D-DIN", 12))
        elif self.current_image_index == 1:
            canvas.create_text(435, 370*6.1, text='PAYLOAD DELIVERY', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))
            txt1 = ['Starship is designed to deliver payloads farther and at a lower\n',
                    'marginal cost per launch than our current Falcon vehicles. With a\n',
                    'payload compartment larger than any fairing currently in operation\n',
                    'or development, Starship will enable transport of many satellites,\n',
                    'large space telescopes, and significant amounts of cargo to Earth\n',
                    'orbit, the Moon, Mars and beyond.']
            canvas.create_text(435, 370*6.4, text=f'{txt1[0]}{txt1[1]}{txt1[2]}{txt1[3]}{txt1[4]}{txt1[5]}', fill=self.fg_color, font=("D-DIN", 12))
        
        elif self.current_image_index == 2:
            canvas.create_text(435, 370*6.1, text='MOON MISSIONS', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))
            txt1 = ['Developing a Moon base to support future space exploration\n',
                    'requires the transport of large amounts of cargo to the surface of\n',
                    'the Moon. Starship is designed to carry these building blocks,\n',
                    'further enabling research and human spaceflight development.\n',
                    'SpaceX is providing the lunar lander which will return astronauts\n',
                    'to the Moon’s surface for the first time in 50 years under NASA\'s\nArtemis missions.']
            canvas.create_text(465, 370*6.4, text=f'{txt1[0]}{txt1[1]}{txt1[2]}{txt1[3]}{txt1[4]}{txt1[5]}', fill=self.fg_color, font=("D-DIN", 12))

        elif self.current_image_index == 3:
            canvas.create_text(435, 370*6.85, text='INTERPLANETARY\nTRANSPORTATION', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))
            txt1 = ['Building cities on Mars will require affordable delivery of\n',
                    'significant quantities of cargo and crew. The fully reusable\n',
                    'Starship system uses on-orbit propellent transfer to enable the\n',
                    'transport of up to 100 people to Mars or other distant destinations.']
            canvas.create_text(450, 370*7.2, text=f'{txt1[0]}{txt1[1]}{txt1[2]}{txt1[3]}', fill=self.fg_color, font=("D-DIN", 12))
        
        elif self.current_image_index == 4:
            canvas.create_text(435, 370*6.2, text='EARTH-TO-EARTH\nTRANSPORTATION', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))
            txt1 = ['Imagine traveling to anywhere in the world in an hour or less. With\n',
                    'Starship and Super Heavy, most international trips could be\n',
                    'completed in under 30 minutes. In addition to vastly increased\n',
                    'speed, one great benefit to traveling outside of Earth’s atmosphere\n',
                    'is the lack of friction as well as turbulence and weather.']
            canvas.create_text(455, 370*6.5, text=f'{txt1[0]}{txt1[1]}{txt1[2]}{txt1[3]}{txt1[4]}', fill=self.fg_color, font=("D-DIN", 12))
        
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
        messagebox.showinfo('Same page', 'You are on the same page only')

    def go_to_page7(self):
        from Rideshare import Rideshare_page
        self.master.switch_frame(Rideshare_page)
