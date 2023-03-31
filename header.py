import tkinter as tk
from PIL import Image, ImageTk
import os

class Header:
    def __init__(self, go_to_homepage_callback, search_callback):
        self.go_to_homepage_callback = go_to_homepage_callback
        self.search_callback = search_callback
        self.create_header()

    def create_header(self):
        self.header_frame = tk.Frame(
            self.details_frame,
            bg="#2C2C2C",
            relief=tk.GROOVE,
            height=60
        )
        self.header_frame.pack(fill=tk.X, pady=20, padx=20)

        # Configure grid weights
        # self.details_frame.grid_columnconfigure(1, weight=1)
        # self.details_frame.grid_rowconfigure(0, weight=0)

        # User image button
        self.user_icon_image = Image.open("images/orgasm.jpg")
        self.user_icon_image = self.user_icon_image.resize((20, 20), Image.Resampling.LANCZOS)
        self.user_icon_image_button = ImageTk.PhotoImage(self.user_icon_image)

        self.user_button = tk.Label(
            self.header_frame,
            image=self.user_icon_image_button,
            cursor="hand2",
            relief=tk.FLAT,
            bg="#2C2C2C"
        )
        self.user_button.bind("<Button-1>", self.show_user_menu)
        self.user_button.pack(side=tk.RIGHT, padx=(0, 20))

        self.logo_image = Image.open("images/orgasm.jpg")
        self.logo_image = self.logo_image.resize((180, 40), Image.Resampling.LANCZOS)
        self.logo_image_button = ImageTk.PhotoImage(self.logo_image)

        self.logo_button = tk.Button(
            self.header_frame,
            image=self.logo_image_button,
            cursor="hand2",
            relief=tk.FLAT,
            bg="#2C2C2C",
            command=self.go_to_homepage_callback 
        )
        self.logo_button.pack(side=tk.LEFT, padx=(0, 20))

        # Replace the search button with a label containing a magnifying glass icon
        self.search_icon_image = Image.open("images/orgasm.jpg")
        self.search_icon_image = self.search_icon_image.resize((20, 20), Image.Resampling.LANCZOS)
        self.search_icon_image_button = ImageTk.PhotoImage(self.search_icon_image)

        self.search_button = tk.Label(
            self.header_frame,
            image=self.search_icon_image_button,
            cursor="hand2",
            relief=tk.FLAT,
            bg="#2C2C2C"
        )
        self.search_button.bind("<Button-1>", self.search_manga)
        self.search_button.pack(side=tk.RIGHT, padx=(0, 20))
        
        self.search_box = tk.Entry(self.header_frame, width=30, font=("Arial", 12))
        self.search_box.pack(side=tk.RIGHT, padx=(0, 20))

        
        # Add menu image button
        self.menu_image = Image.open("images/orgasm.jpg")
        self.menu_image = self.menu_image.resize((20, 20), Image.Resampling.LANCZOS)
        self.menu_image_button = ImageTk.PhotoImage(self.menu_image)

        self.menu_button = tk.Label(
            self.header_frame,
            image=self.menu_image_button,
            cursor="hand2",
            relief=tk.FLAT,
            bg="#2C2C2C"
        )
        self.menu_button.bind("<Button-1>", self.toggle_left_menu)
        self.menu_button.pack(side=tk.LEFT, padx=(20, 0))
        
    
    def search_manga(self, event):
        search_query = self.search_box.get().strip()
        if search_query:
            self.search_callback(search_query)