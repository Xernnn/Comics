import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from user_menu import UserMenu
from user_info import UserInfo
import mysql.connector as sql

db = sql.connect(host="localhost",user="root",password="root",database="comics",port=3306,autocommit=True)
cursor = db.cursor(buffered=True)

class Header(tk.Frame):
    def __init__(self, root, go_to_homepage_callback, search_callback, toggle_left_menu, user_menu, user_info):
        super().__init__(root)
        self.go_to_homepage_callback = go_to_homepage_callback
        self.search_callback = search_callback
        self.toggle_left_menu = toggle_left_menu
        self.user_menu = user_menu
        self.user_info = user_info
        self.create_header()

    def create_header(self):
        bg_color = "#1A1918"
        self.config(bg=bg_color)  # Set the background color of the Header
        self.pack(fill=tk.X)  # Remove pady and padx here
        self.header_frame = tk.Frame(
            self,
            bg="#2C2C2C",
            relief=tk.GROOVE,
            height=60
        )
        self.header_frame.pack(fill=tk.X, pady=20, padx=20)

        # User image button
        self.user_icon_image = Image.open("images/guest.png")
        self.user_icon_image = self.user_icon_image.resize((35, 35), Image.Resampling.LANCZOS)
        self.user_icon_image_button = ImageTk.PhotoImage(self.user_icon_image)

        self.user_button = tk.Label(
            self.header_frame,
            image=self.user_icon_image_button,
            cursor="hand2",
            relief=tk.FLAT,
            bg="#2C2C2C"
        )
        self.user_button.bind("<Button-1>", self.show_user_window)
        self.user_button.pack(side=tk.RIGHT, padx=(0, 20))

        # Add menu image button
        self.menu_image = Image.open("images/menu.jpg")
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
        self.menu_button.pack(side=tk.LEFT, padx=(10, 0))

        self.logo_image = Image.open("images/logo.jpg")
        self.logo_image = self.logo_image.resize((140, 40), Image.Resampling.LANCZOS)
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
        
        # Search box
        self.search_box = tk.Entry(self.header_frame, width=25, font=("Times New Roman", 12), bg="#3E3E3E", fg="#FFFFFF")
        self.search_box.pack(side=tk.RIGHT, padx=(0, 20))
        
        # Replace the search button with a label containing a magnifying glass icon
        self.search_icon_image = Image.open("images/search.png")
        self.search_icon_image = self.search_icon_image.resize((20, 20), Image.Resampling.LANCZOS)
        self.search_icon_image_button = ImageTk.PhotoImage(self.search_icon_image)

        self.search_icon_label = tk.Label(
            self.search_box,
            image=self.search_icon_image_button,
            cursor="hand2",
            relief=tk.FLAT,
            bg="#2C2C2C"
        )
        
        # Calculate the x position of the search icon based on the search_box width
        search_icon_x = self.search_box.winfo_reqwidth() - 25
        self.search_icon_label.place(x=search_icon_x, y=-2)
        self.search_icon_label.bind("<Button-1>", self.search_comics)

        # Set placeholder text and events
        self.placeholder_text = "Search"
        self.search_box.insert(0, self.placeholder_text)
        self.search_box.bind("<FocusIn>", self.clear_placeholder_text)
        self.search_box.bind("<FocusOut>", self.add_placeholder_text)
        self.search_box.bind("<Return>", self.search_comics)
        
    def search_comics(self, event):
        search_query = self.search_box.get().strip()
        if search_query and search_query != self.placeholder_text:
            self.search_callback(search_query)

    def clear_placeholder_text(self, event):
        if self.search_box.get() == self.placeholder_text:
            self.search_box.delete(0, tk.END)

    def add_placeholder_text(self, event):
        if self.search_box.get() == "":
            self.search_box.insert(0, self.placeholder_text)

    def show_user_window(self, event):
        if self.user_menu.is_logged_in():
            self.user_info.show_user_info()
        else:
            self.user_menu.show_user_menu(event)
            
    def update_user_icon(self):
        if self.user_menu.is_logged_in():
            avatar_image = Image.open(self.user_info.user_data['avatar'])
            avatar_image = avatar_image.resize((35, 35), Image.Resampling.LANCZOS)
            avatar_image_button = ImageTk.PhotoImage(avatar_image)
            self.user_button.config(image=avatar_image_button)
            self.user_button.image = avatar_image_button