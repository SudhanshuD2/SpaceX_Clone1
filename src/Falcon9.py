import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser as wb
from PIL import Image, ImageTk
from Labels import Label_Fr
from HomePage import HomePage

class Falcon_9(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.bg_color = '#000000'
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
        canvas.pack(fill=tk.BOTH, expand=tk.YES, ipady=200)

        back_button = tk.Button(canvas, text='<',bd=0,padx=0,pady=0,bg=self.bg_color, fg=self.fg_color,
                                font=('Arial',9, 'bold'),command=lambda: self.go_to_home())
        canvas.create_window(110, 20, anchor=tk.NW, window= back_button)

        fal_9_img = Image.open('assets/images/f9_main1.jpg')
        fal_9_img = fal_9_img.resize((self.screen_width-250, self.screen_height-200), Image.LANCZOS)
        fal_9_p = ImageTk.PhotoImage(fal_9_img)

        f9_2 = Image.open('assets/images/f9_21.png')
        f9_2 = f9_2.resize((self.screen_width, self.screen_height-80), Image.LANCZOS)
        f9_2p = ImageTk.PhotoImage(f9_2)

        f9_21 = Image.open('assets/images/f9_22.png')
        f9_21 = f9_21.resize((self.screen_width, self.screen_height-100), Image.LANCZOS)
        f9_21p = ImageTk.PhotoImage(f9_21)

        f9_22 = Image.open('assets/images/Merlin.jpg')
        f9_22 = f9_22.resize((self.screen_width, self.screen_height-100), Image.LANCZOS)
        f9_22p = ImageTk.PhotoImage(f9_22)

        text1 = ['Falcon 9 is a reusable, two-stage rocket designed and manufactured by', 
                'SpaceX for the reliable and safe transport of people and payloads into Earth',
                'orbit and beyond. Falcon 9 is the world\'s first orbital class reusable rocket.',
                'Reusability allows SpaceX to refly the most expensive parts of the rocket,',
                'which in turn drives down the cost of space access.']

        canvas.image1 = fal_9_p
        canvas.create_image(760, 360, image=fal_9_p)

        canvas.image2 = f9_2p
        canvas.create_image(760, 360*3.7, image=f9_2p)

        canvas.imag3 = f9_21p
        canvas.create_image(760, 360*5.7, image=f9_21p)
        
        canvas.imag4 = f9_22p
        canvas.create_image(760, 360*7.6, image=f9_22p)

        canvas.create_text(self.screen_width//2-220, 200, text='FALCON 9',fill='#FFFFFF', font=('Bahnschrift',72, 'bold'), anchor=tk.NW)
        canvas.create_text(self.screen_width//2, 330, text='FIRST ORBITAL CLASS ROCKET CAPABLE OF REFLIGHT', fill='#FFFFFF', font=('Bahnschrift',11))

        canvas.create_text(self.screen_width//2-400, 780, text='306', fill=self.fg_color, font=("Bahnschrift", 100))
        canvas.create_text(self.screen_width//2-30, 780, text='264', fill=self.fg_color, font=("Bahnschrift", 100))
        canvas.create_text(self.screen_width//2+400, 780, text='237', fill=self.fg_color, font=("Bahnschrift", 100))

        canvas.create_text(370, 870, text='TOTAL LAUNCHES', fill=self.fg_color, font=("Bahnschrift", 16))
        canvas.create_text(740, 870, text='TOTAL LANDINGS', fill=self.fg_color, font=("Bahnschrift", 16))
        canvas.create_text(1160, 870, text='TOTAL REFLIGHTS', fill=self.fg_color, font=("Bahnschrift", 16))

        canvas.create_text(390, 1150, text=f'{text1[0]}\n{text1[1]}\n{text1[2]}\n{text1[3]}\n{text1[4]}',
                          fill=self.fg_color, font=("Bahnschrift", 12))
        
        
        canvas.create_text(155, 1760, text='FALCON 9', fill=self.fg_color, font=("Bahnschrift", 16))
        canvas.create_text(220, 1800, text='OVERVIEW', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))
        
        canvas.create_text(130, 1920, text='HEIGHT', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(140, 1920+50, text='DIAMETER', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(125, 1920+50*2, text='MASS', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(165, 1920+50*3, text='PAYLOAD TO LEO', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(165, 1920+50*4, text='PAYLOAD TO GTO', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(175, 1920+50*5, text='PAYLOAD TO MARS', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))

        canvas.create_text(560, 1920, text='70 m / 229.6 ft', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1920+50, text='3.7 m / 12 ft', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1920+50*2, text='549,054 kg / 1,207,920 lb', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1920+50*3, text='22,800 kg / 50,265 lb', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1920+50*4, text='8,300 kg / 18,300 lb', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1920+50*5, text='4,020 kg / 8,860 lb', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))

        text2 = ['Merlin is a family of rocket engines developed by SpaceX for use on its Falcon\n',
        '1, Falcon 9 and Falcon Heavy launch vehicles. Merlin engines use a rocket\n',
        'grade kerosene (RP-1) and liquid oxygen as rocket propellants in a gas-\n',
        'generator power cycle. The Merlin engine was originally designed for recovery\n',
        'and reuse.\n']
        canvas.create_text(140, 2470, text='ENGINES', fill=self.fg_color, font=("Bahnschrift", 11, 'bold'))
        canvas.create_text(195, 2500, text='MERLIN', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))

        canvas.create_text(150, 2600, text='SEA LEVEL', fill=self.fg_color, font=("Bahnschrift", 12))
        canvas.create_text(240, 2600, text='| VACUUM', fill='grey', font=("Bahnschrift", 12))
        
        canvas.create_text(400, 2730, text=f'{text2[0]}{text2[1]}{text2[2]}{text2[3]}{text2[4]}', 
                           fill=self.fg_color, font=("Bahnschrift", 12))
        
        canvas.create_text(165, 2980, text='PROPELLANT', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(145, 2980+40, text='THRUST', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 2980, text='LOX / RP-1', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 2980+40, text='845 kN / 190,000 lbf', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))

        self.images = [Image.open('assets/images/F9_DM2_LAUNCH_Last.jpg'), Image.open('assets/images/F9_last2.jpg'),
                       Image.open('assets/images/F9_last3.jpg'), Image.open('assets/images/F9_last4.jpg'),
                       Image.open('assets/images/F9_last5.jpg'),Image.open('assets/images/F9_last6.jpg'),
                       Image.open('assets/images/F9_last7.jpg'),Image.open('assets/images/F9_last8.jpg'),]
        # self.descs = ['Falcon 9 launches Dragon to the International Space Station from Launch Complex 39A',
        #               'Falcon 9 first and second stages after separating in flight', 'Falcon 9 lifts off with its Iridium-5 payload',
        #               'Falcon 9 lands on the droneship Just Read the Instructions','Close-up of Falcon 9\'s Merlin engines during liftoff',
        #               'Falcon 9 leaves a trail of light as it lifts off from Vandenberg Air Force Base',
        #               'Falcon 9 lifts off with Dragon for an in-flight test of the Crew Dragon abort system',
        #               'Falcon 9 with its Radarsat payload at sunset before launch',]
        
        self.disp_imgs()
        
        left_button = tk.Button(self, text='<', bd=0, padx=0, pady=0, bg=self.bg_color, fg=self.fg_color,
                                font=('Arial', 18, 'bold'), command=lambda: self.swipe('left'))
        canvas.create_window(100, 3700, anchor=tk.NW, window= left_button)
        
        right_button = tk.Button(self, text='>', bd=0, padx=0, pady=0, bg=self.bg_color, fg=self.fg_color,
                                 font=('Arial', 18, 'bold'), command=lambda: self.swipe('right'))
        canvas.create_window(self.screen_width-130, 3700, anchor=tk.NW, window= right_button)

        canvas.create_text(self.screen_width/2-100, 3800, text='For information about our launch services, contact', fill='grey', font=("Bahnschrift", 12))
        canvas.create_text(self.screen_width/2+165, 3800, text='sales@spacex.com', fill=self.fg_color, font=("Bahnschrift", 12))
        
        usr_gd = tk.Button(self, text='DOWNLOAD USER\'S GUIDS', bd=0, padx=5, pady=10, bg=self.bg_color, fg=self.fg_color,
                                font=('Arial',11, 'bold'), command= lambda: wb.open('https://www.spacex.com/media/falcon-users-guide-2021-09.pdf'))
        canvas.create_window(self.screen_width/2-270, 3820, anchor=tk.NW, window= usr_gd)
        usr_gd.bind('<Enter>', lambda event: usr_gd.config(bg=self.fg_color, fg=self.bg_color))
        usr_gd.bind('<Leave>', lambda event: usr_gd.config(bg=self.bg_color, fg=self.fg_color))
        srvcs = tk.Button(self, text='CAPABILITIES AND SERVICES', bd=0, padx=5, pady=10, bg=self.bg_color, fg=self.fg_color,
                                font=('Arial', 11, 'bold'), command= lambda: wb.open('https://www.spacex.com/media/Capabilities&Services.pdf'))
        canvas.create_window(self.screen_width/2, 3820, anchor=tk.NW, window= srvcs)
        srvcs.bind('<Enter>', lambda event: srvcs.config(bg=self.fg_color, fg=self.bg_color))
        srvcs.bind('<Leave>', lambda event: srvcs.config(bg=self.bg_color, fg=self.fg_color))

        # Bottom most frame and buttons
        canvas.create_text(self.screen_width//2-150, 3920, text="SpaceX © 2024", fill=self.fg_color, anchor=tk.SW)
        pp_button = tk.Button(canvas, text='PRIVACY POLICY', bd=0, bg=self.bg_color, fg=self.fg_color,
                               command=lambda: wb.open('https://www.spacex.com/media/privacy_policy_spacex.pdf'))
        canvas.create_window(self.screen_width//2-50, 3925, anchor=tk.SW, window=pp_button)
        sup_button = tk.Button(canvas, text='SUPPLIERS',bd=0,  bg=self.bg_color, fg=self.fg_color,
                                command=lambda: wb.open('https://www.spacex.com/supplier/'))
        canvas.create_window(self.screen_width//2+60, 3925, anchor=tk.SW, window=sup_button)
        canvas.create_text(1300, 3915, text="@ SudhanshuD\tSelf", fill=self.fg_color, anchor=tk.SW)

        # Write any code above
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox('all'))
        canvas.bind('<Configure>', self.on_canvas_configure)

    def disp_imgs(self):
        image = self.images[self.current_image_index].resize((self.screen_width, self.screen_height-250), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(image)
        canvas.create_image(0, 360*8.57, anchor=tk.NW, image=self.image)
        # canvas.create_text(self.screen_width//2, 3700 ,text=self.descs[self.current_image_index],
        #                                   fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))

    def swipe(self, dirn):
        if dirn == 'left':
            self.current_image_index = (self.current_image_index - 1) % len(self.images)
            self.disp_imgs()
            # canvas.delete(f'{self.descs[self.current_image_index]}')

        else:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.disp_imgs()
            # canvas.delete(f'{self.descs[self.current_image_index]}')

    def go_to_home(self):
        self.master.switch_frame(HomePage)

    def on_mouse_wheel(self, event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def on_canvas_configure(self, event):
        canvas.configure(scrollregion=canvas.bbox('all'))