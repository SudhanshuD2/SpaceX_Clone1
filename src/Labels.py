import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser as wb


class Label_Fr(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(bg='#101010')

        self.label_spaces()
    def label_spaces(self):
        bg_color = '#101010'
        fg_color = '#FFFFFF'

        try:
            img = Image.open('assets/images/logo.png')
            image = img.resize((230, 30), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            spacex_icon = tk.Label(self, image=photo,bd=0, background=bg_color)  #, background=bg_color, fg=fg_color, font=('Impact', 24, 'bold')
            spacex_icon.image = photo
            spacex_icon.grid(row=0, column=0,padx=(100, 0), pady=(30,10), sticky='e')
        except:
            print('handling now')

        Falcon9 = tk.Button(self, text='FALCON 9',background=bg_color,bd=0, fg=fg_color, font=('Arial', 11, 'bold'),
                        command=lambda: self.master.go_to_page2())
        Falcon9.grid(row=0, column=1, padx=10,pady=10, sticky='s')
        Falcon9.bind('<Enter>', lambda event: Falcon9.config(font=('Arial', 11, 'underline bold'), bg=bg_color))
        Falcon9.bind('<Leave>', lambda event: Falcon9.config(fg=fg_color, font=('Arial', 11, 'bold'), bg=bg_color))

        Falcon_heavy = tk.Button(self, text='FALCON HEAVY',background=bg_color,bd=0, fg=fg_color, font=('Arial', 11, 'bold'),
                                command=lambda: self.master.go_to_page3())
        Falcon_heavy.grid(row=0, column=2, padx=10,pady=10, sticky='s')
        Falcon_heavy.bind('<Enter>', lambda event: Falcon_heavy.config(font=('Arial', 11, 'underline bold'), bg=bg_color))
        Falcon_heavy.bind('<Leave>', lambda event: Falcon_heavy.config(fg=fg_color, font=('Arial', 11, 'bold'), bg=bg_color))

        Dragon = tk.Button(self, text='DRAGON',background=bg_color,bd=0, fg=fg_color, font=('Arial', 11, 'bold'),
                        command=lambda: self.master.go_to_page4())
        Dragon.grid(row=0, column=3, padx=9,pady=10, sticky='s')
        Dragon.bind('<Enter>', lambda event: Dragon.config(font=('Arial', 11, 'underline bold'), bg=bg_color))
        Dragon.bind('<Leave>', lambda event: Dragon.config(fg=fg_color, font=('Arial', 11, 'bold'), bg=bg_color))

        Starship = tk.Button(self, text='STARSHIP',background=bg_color,bd=0, fg=fg_color, font=('Arial', 11, 'bold'),
                            command= lambda: self.master.go_to_page5())
        Starship.grid(row=0, column=4, padx=9,pady=10, sticky='s')
        Starship.bind('<Enter>', lambda event: Starship.config(font=('Arial', 11, 'underline bold'), bg=bg_color))
        Starship.bind('<Leave>', lambda event: Starship.config(fg=fg_color, font=('Arial', 11, 'bold'), bg=bg_color))

        Human_SF = tk.Button(self, text='HUMAN SPACEFLIGHT',background=bg_color,bd=0, fg=fg_color, font=('Arial', 11, 'bold'))
        Human_SF.grid(row=0, column=5, padx=9,pady=10, sticky='s')
        Human_SF.bind('<Enter>', lambda event: Human_SF.config(font=('Arial', 11, 'underline bold'), bg=bg_color))
        Human_SF.bind('<Leave>', lambda event: Human_SF.config(fg=fg_color, font=('Arial', 11, 'bold'), bg=bg_color))

        Rideshare = tk.Button(self, text='RIDESHARE',background=bg_color,bd=0, fg=fg_color, font=('Arial', 11, 'bold'),
                              command= lambda: self.master.go_to_page7())
        Rideshare.grid(row=0, column=6, padx=9,pady=10, sticky='s')
        Rideshare.bind('<Enter>', lambda event: Rideshare.config(font=('Arial', 11, 'underline bold'), bg=bg_color))
        Rideshare.bind('<Leave>', lambda event: Rideshare.config(fg=fg_color, font=('Arial', 11, 'bold'), bg=bg_color))

        Starshield = tk.Button(self, text='STARSHIELD',background=bg_color,bd=0, fg=fg_color, font=('Arial', 11, 'bold'))
        Starshield.grid(row=0, column=7, padx=9,pady=10, sticky='s')
        Starshield.bind('<Enter>', lambda event: Starshield.config(font=('Arial', 11, 'underline bold'), bg=bg_color))
        Starshield.bind('<Leave>', lambda event: Starshield.config(fg=fg_color, font=('Arial', 11, 'bold'), bg=bg_color))

        Starlink = tk.Button(self, text='STARLINK',background=bg_color,bd=0, fg=fg_color, font=('Arial', 11, 'bold')
                            , command=lambda: wb.open('https://www.starlink.com/'))
        Starlink.grid(row=0, column=8, padx=9,pady=10, sticky='s')
        Starlink.bind('<Enter>', lambda event: Starlink.config(font=('Arial', 11, 'underline bold'), bg=bg_color))
        Starlink.bind('<Leave>', lambda event: Starlink.config(fg=fg_color, font=('Arial', 11, 'bold'), bg=bg_color))

        r1 = tk.Label(self, text='', background=bg_color, fg=bg_color, font=('Arial', 28))
        r1.grid(row=0, column=9, padx=50)

        shop = tk.Button(self, text='SHOP',border=0,background=bg_color,fg=fg_color,bd=0, font=('Arial', 11, 'bold'),
                        command=lambda: wb.open('https://shop.spacex.com/'))
        shop.grid(row=0, column=12, padx=5,pady=10, sticky='s')
        shop.bind('<Enter>', lambda event: shop.config(font=('Arial', 11, 'underline bold'), bg=bg_color))
        shop.bind('<Leave>', lambda event: shop.config(fg=fg_color, font=('Arial', 11, 'bold'), bg=bg_color))

        global menu_dd
        menu_dd = tk.Menu(self, tearoff=0,bd=0, bg=bg_color, fg=fg_color, font=('Vardana', 11))
        menu_dd.add_command(label=' '*50+'MISSION', command=lambda: self.dropdown('MISSION'))
        menu_dd.add_separator()
        menu_dd.add_command(label=' '*46+'LAUNCHES', command=lambda: self.dropdown('LAUNCHES'))
        menu_dd.add_separator()
        menu_dd.add_command(label=' '*47+'CAREERS', command=lambda: self.dropdown('CAREERS'))
        menu_dd.add_separator()
        menu_dd.add_command(label=' '*48+'UPDATES', command=lambda: self.dropdown('UPDATES'))
        menu_dd.add_separator()
        menu_dd.add_command(label=' '*54+'SHOP', command=lambda: self.dropdown('SHOP'))
        for i in range(0, 27):
            menu_dd.add_command(label=' ')

        global menu_posted
        menu_posted = tk.BooleanVar()
        menu_posted.set(False)

        global menu_b
        menu_b = tk.Button(self, text='≡', background=bg_color,bd=0, fg=fg_color, font=('Arial', 18),
                          command=self.toggle_menu)
        menu_b.grid(row=0, column=13, sticky='s', padx=10, pady=4)
        menu_b.bind('<Enter>', lambda event: menu_b.config(fg='#AAAAAA'))
        menu_b.bind('<Leave>', lambda event: menu_b.config(fg=fg_color))
        # menu_b.config(menu=menu_dd)

    def toggle_menu(self):
        if menu_posted.get():
            menu_posted.set(False)
            menu_dd.unpost()
            menu_b.config(text='≡', font=('Arial', 18))
        else:
            menu_b.config(text='x', font=('Comic Sans MS', 18, 'bold'))
            menu_posted.set(True)
            menu_dd.post(menu_b.winfo_rootx(), menu_b.winfo_rooty()+menu_b.winfo_height())

    def dropdown(self, optins):
        menu_posted.set(False)
        menu_b.config(text='≡')
        messagebox.showinfo('Information', f'Sorry {optins} under construction site!!')