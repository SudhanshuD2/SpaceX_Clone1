import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser as wb
from Labels import Label_Fr
from HomePage import HomePage
from PIL import Image, ImageTk

class Falcon_Heavy(tk.Frame):
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
        canvas.pack(fill=tk.BOTH, expand=tk.YES, ipady=205)

        back_button = tk.Button(canvas, text='<',bd=0,padx=0,pady=0,bg=self.bg_color, fg=self.fg_color,
                                font=('Arial',9, 'bold'),command=lambda: self.master.switch_frame(HomePage))
        canvas.create_window(110, 20, anchor=tk.NW, window= back_button)

# images
        fal_h_img = Image.open('assets/images/Labels/Falcon_heavy1.jpg')
        fal_h_img = fal_h_img.resize((self.screen_width, self.screen_height-200), Image.LANCZOS)
        fal_h_p = ImageTk.PhotoImage(fal_h_img)

        FH1_img = Image.open('assets/images/Labels/FH_S1_1.png')
        FH1_img = FH1_img.resize((self.screen_width-200, self.screen_height-100), Image.LANCZOS)
        FH1_p = ImageTk.PhotoImage(FH1_img)

        FH3_img = Image.open('assets/images/Labels/fh_3.jpg')
        FH3_img = FH3_img.resize((self.screen_width, self.screen_height-100), Image.LANCZOS)
        FH3_p = ImageTk.PhotoImage(FH3_img)

        FH4_img = Image.open('assets/images/Labels/fh_4.jpg')
        FH4_img = FH4_img.resize((700, self.screen_height-200), Image.LANCZOS)
        FH4_p = ImageTk.PhotoImage(FH4_img)

        FH5_img = Image.open('assets/images/Merlin.jpg')
        FH5_img = FH5_img.resize((self.screen_width, self.screen_height-100), Image.LANCZOS)
        FH5_p = ImageTk.PhotoImage(FH5_img)

        canvas.image1 = fal_h_p
        canvas.create_image(760, 370, image=fal_h_p)

        canvas.image2 = FH1_p
        canvas.create_image(740, 370*3.7, image=FH1_p)

        canvas.image3 = FH3_p
        canvas.create_image(740, 370*5.7, image=FH3_p)

        canvas.image4 = FH4_p
        canvas.create_image(455, 370*7.7, image=FH4_p)

        canvas.image5 = FH5_p
        canvas.create_image(740, 370*9.7, image=FH5_p)

        self.images = [Image.open('assets/images/Labels/FH_l1.jpg'),Image.open('assets/images/Labels/FH_l2.jpg'),
                       Image.open('assets/images/Labels/FH_l3.jpg'),Image.open('assets/images/Labels/FH_l4.jpg'),
                       Image.open('assets/images/Labels/FH_l5.jpg'),Image.open('assets/images/Labels/FH_l6.jpg'),
                       Image.open('assets/images/Labels/FH_l7.jpg'),Image.open('assets/images/Labels/FH_l8.jpg'),
                       Image.open('assets/images/Labels/FH_l9.jpg'),Image.open('assets/images/Labels/FH_l10.jpg')]
        self.disp_imgs()

        left_button = tk.Button(self, text='<', bd=0, padx=0, pady=0, bg=self.bg_color, fg=self.fg_color,
                                font=('Arial', 18, 'bold'), command=lambda: self.swipe('left'))
        canvas.create_window(100, 370*12.3, anchor=tk.NW, window= left_button)
        
        right_button = tk.Button(self, text='>', bd=0, padx=0, pady=0, bg=self.bg_color, fg=self.fg_color,
                                 font=('Arial', 18, 'bold'), command=lambda: self.swipe('right'))
        canvas.create_window(self.screen_width-130, 370*12.3, anchor=tk.NW, window= right_button)
# Labels
        canvas.create_text(self.screen_width//2-320, 240, text='FALCON HEAVY',fill=self.fg_color, font=('Bahnschrift',72, 'bold'), anchor=tk.NW)
        canvas.create_text(self.screen_width//2, 370, text='OVER 5 MILLION LBS OF THRUST', fill=self.fg_color, font=('Bahnschrift',11))

        canvas.create_text(self.screen_width//2-400, 780, text='9', fill=self.fg_color, font=("Bahnschrift", 100))
        canvas.create_text(self.screen_width//2-30, 780, text='17', fill=self.fg_color, font=("Bahnschrift", 100))
        canvas.create_text(self.screen_width//2+400, 780, text='14', fill=self.fg_color, font=("Bahnschrift", 100))

        canvas.create_text(370, 870, text='TOTAL LAUNCHES', fill=self.fg_color, font=("Bahnschrift", 16))
        canvas.create_text(740, 870, text='TOTAL LANDINGS', fill=self.fg_color, font=("Bahnschrift", 16))
        canvas.create_text(1160, 870, text='TOTAL REFLIGHTS', fill=self.fg_color, font=("Bahnschrift", 16))

        canvas.create_text(177, 1150, text='FALCON HEAVY', fill=self.fg_color, font=("Bahnschrift", 16))
        canvas.create_text(210, 1190, text='OVERVIEW', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))
        
        canvas.create_text(125, 1320, text='HEIGHT', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(125, 1320+55, text='WIDTH', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(120, 1320+55*2, text='MASS', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(160, 1320+55*3, text='PAYLOAD TO LEO', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(160, 1320+55*4, text='PAYLOAD TO GTO', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(170, 1320+55*5, text='PAYLOAD TO MARS', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))

        canvas.create_text(560, 1320, text='70 m / 229.6 ft', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1320+55, text='12.2 m / 39.9 ft', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1320+55*2, text='549,054 kg / 1,207,920 lb', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1320+55*3, text='22,800 kg / 50,265 lb', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1320+55*4, text='8,300 kg / 18,300 lb', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 1320+55*5, text='4,020 kg / 8,860 lb', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))

        canvas.create_text(125, 2270, text='VIDEO', fill=self.fg_color, font=("Bahnschrift", 14, 'bold'))
        canvas.create_text(335, 2350, text='FALCON HEAVY FIRST\nFLIGHT', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))

        canvas.create_text(1060, 2770, text='UNMATCHED\nPERFORMANCE', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))
        text1 = ['With more than 5 million pounds of thrust at liftoff, Falcon Heavy is\n',
                'one of the most capable rockets flying. By comparison, the liftoff\n',
                'thrust of the Falcon Heavy equals approximately eighteen 747 aircraft\n',
                'at full power. Falcon Heavy can lift the equivalent of a fully loaded 737\n',
                'jetliner—complete with passengers, luggage and fuel—to orbit.']
        canvas.create_text(1140, 2900, text=f'{text1[0]}{text1[1]}{text1[2]}{text1[3]}{text1[4]}', 
                           fill=self.fg_color, font=("Bahnschrift", 12))
        
        text2 = ['Merlin is a family of rocket engines developed by SpaceX for use on its Falcon\n',
        '1, Falcon 9 and Falcon Heavy launch vehicles. Merlin engines use a rocket\n',
        'grade kerosene (RP-1) and liquid oxygen as rocket propellants in a gas-\n',
        'generator power cycle. The Merlin engine was originally designed for recovery\n',
        'and reuse.\n']
        canvas.create_text(130, 3300, text='ENGINES', fill=self.fg_color, font=("Bahnschrift", 11, 'bold'))
        canvas.create_text(185, 3340, text='MERLIN', fill=self.fg_color, font=("Bahnschrift", 36, 'bold'))

        canvas.create_text(140, 3450, text='SEA LEVEL', fill=self.fg_color, font=("Bahnschrift", 12))
        canvas.create_text(220, 3450, text='| VACUUM', fill='grey', font=("Bahnschrift", 12))
        
        canvas.create_text(390, 3550, text=f'{text2[0]}{text2[1]}{text2[2]}{text2[3]}{text2[4]}', 
                           fill=self.fg_color, font=("Bahnschrift", 12))
        
        canvas.create_text(150, 3680, text='PROPELLANT', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(130, 3680+50, text='THRUST', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 3680, text='LOX / RP-1', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))
        canvas.create_text(560, 3680+50, text='845 kN / 190,000 lbf', fill=self.fg_color, font=("Bahnschrift", 12, 'bold'))

        canvas.create_text(self.screen_width/2-100, 4900, text='For information about our launch services, contact', fill='grey', font=("Bahnschrift", 12))
        canvas.create_text(self.screen_width/2+165, 4900, text='sales@spacex.com', fill=self.fg_color, font=("Bahnschrift", 12))

        usr_gd = tk.Button(self, text='DOWNLOAD USER\'S GUIDS', bd=0, padx=5, pady=10, bg=self.bg_color, fg=self.fg_color,
                                font=('Arial',11, 'bold'), command= lambda: wb.open('https://www.spacex.com/media/falcon-users-guide-2021-09.pdf'))
        canvas.create_window(self.screen_width/2-130, 4930, anchor=tk.NW, window= usr_gd)
        usr_gd.bind('<Enter>', lambda event: usr_gd.config(bg=self.fg_color, fg=self.bg_color))
        usr_gd.bind('<Leave>', lambda event: usr_gd.config(bg=self.bg_color, fg=self.fg_color))

        # Bottom most frame and buttons
        canvas.create_text(self.screen_width//2-150, 5050, text="SpaceX © 2024", fill=self.fg_color, anchor=tk.SW)
        pp_button = tk.Button(canvas, text='PRIVACY POLICY', bd=0, bg=self.bg_color, fg=self.fg_color,
                               command=lambda: wb.open('https://www.spacex.com/media/privacy_policy_spacex.pdf'))
        canvas.create_window(self.screen_width//2-50, 5055, anchor=tk.SW, window=pp_button)
        sup_button = tk.Button(canvas, text='SUPPLIERS',bd=0,  bg=self.bg_color, fg=self.fg_color,
                                command=lambda: wb.open('https://www.spacex.com/supplier/'))
        canvas.create_window(self.screen_width//2+60, 5055, anchor=tk.SW, window=sup_button)
        canvas.create_text(1300, 5045, text="@ SudhanshuD\tSelf", fill=self.fg_color, anchor=tk.SW)

        # Write any code above
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox('all'))
        canvas.bind('<Configure>', self.on_canvas_configure)
# methods
    def on_mouse_wheel(self, event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def on_canvas_configure(self, event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    def disp_imgs(self):
        image = self.images[self.current_image_index].resize((self.screen_width, self.screen_height-250), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(image)
        canvas.create_image(0, 370*10.57, anchor=tk.NW, image=self.image)
    def swipe(self, dirn):
        if dirn == 'left':
            self.current_image_index = (self.current_image_index - 1) % len(self.images)
            self.disp_imgs()
            # canvas.delete('text')

        else:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.disp_imgs()
            # canvas.delete('text')
    
    #Lable frame calls
    def go_to_page2(self):
        from Falcon9 import Falcon_9
        self.master.switch_frame(Falcon_9)

    def go_to_page3(self):
        messagebox.showinfo('Same page', 'You are on the same page only')

    def go_to_page4(self):
        from Dragon import Dragon_page
        self.master.switch_frame(Dragon_page)

    def go_to_page5(self):
        from Starship import Starship_page
        self.master.switch_frame(Starship_page)

    def go_to_page7(self):
        from Rideshare import Rideshare_page
        self.master.switch_frame(Rideshare_page)