import tkinter as tk
from PIL import Image, ImageTk
from Update import Update
import requests
import mysql.connector as sql

db = sql.connect(host="localhost",user="root",password="root",database="comics",port=3306,autocommit=True)
cursor = db.cursor(buffered=True)

class UserInfo:
    def __init__(self, window, cursor, update_user_icon_callback=None):
        self.window = window
        self.cursor = cursor
        self.update_user_icon_callback = update_user_icon_callback

        # if user_data is None:
        user_data = {
            'avatar': 'images/guest.png',
            'username': None,
            'email': None,
            'age': None,
            'user_role': None,
            'favorite': None,
            'comics_followed': None,
        }

        self.user_data = user_data

    def show_user_info(self, event=None):
        self.user_info_window = tk.Toplevel()
        self.user_info_window.title("User Info")

        # Center the window on the screen
        window_width = 400
        window_height = 300
        screen_width = self.user_info_window.winfo_screenwidth()
        screen_height = self.user_info_window.winfo_screenheight()

        x_position = int((screen_width / 2) - (window_width / 2))
        y_position = int((screen_height / 2) - (window_height / 2))

        self.user_info_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # User's avatar
        if self.user_data['avatar'] == 'images/guest.png':
            avatar_image = Image.open(self.user_data['avatar'])
        else:
            avatar_image = Image.open(requests.get(self.user_data['avatar'], stream=True).raw)
        avatar_image = avatar_image.resize((100, 100), Image.Resampling.LANCZOS)
        avatar_image_button = ImageTk.PhotoImage(avatar_image)

        avatar_label = tk.Label(self.user_info_window, image=avatar_image_button)
        avatar_label.image = avatar_image_button
        avatar_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), rowspan=6)

        # User's info
        username_label = tk.Label(self.user_info_window, text=f"Username: {self.user_data['username']}")
        username_label.grid(row=0, column=1, sticky=tk.W, pady=(10, 0))
        
        email_label = tk.Label(self.user_info_window, text=f"Email: {self.user_data['email']}")
        email_label.grid(row=1, column=1, sticky=tk.W)

        age_label = tk.Label(self.user_info_window, text=f"Age: {self.user_data['age']}")
        age_label.grid(row=2, column=1, sticky=tk.W)

        user_role_label = tk.Label(self.user_info_window, text=f"User Role: {self.user_data['user_role']}")
        user_role_label.grid(row=3, column=1, sticky=tk.W)

        favorite_label = tk.Label(self.user_info_window, text=f"Favorite: {self.user_data['favorite']}")
        favorite_label.grid(row=4, column=1, sticky=tk.W)

        comics_followed_label = tk.Label(self.user_info_window, text=f"Comics followed: {self.user_data['comics_followed']}")
        comics_followed_label.grid(row=5, column=1, sticky=tk.W)

        # Add a new column and configure it to expand
        self.user_info_window.columnconfigure(2, weight=1)

        # Button
        button = tk.Button(self.user_info_window, text="Update", command=self.update)
        button.grid(row=8, column=1, pady=(40, 20), sticky=tk.E + tk.W)
        button.configure(anchor='center')

    def update(self):
        update_window = Update(self.user_info_window)
        update_window.update_data_callback = self.update_user_data

    def update_user_data(self, age, favorite, avatar):
        self.user_data['age'] = age
        self.user_data['favorite'] = favorite
        self.user_data['avatar'] = avatar

        user_data = {
            "age": self.user_data['age'],
            "favorite": self.user_data['favorite'],
            "avatar": self.user_data['avatar'],
            "username": self.user_data['username']
        }
        values = tuple(user_data.values())

        self.cursor.execute("UPDATE users SET age=%s, favorite=%s, avatar=%s WHERE username=%s", values)

        # Call the update_user_icon method
        if self.update_user_icon_callback:
            self.update_user_icon_callback()

    def set_update_user_icon_callback(self, callback):
        self.update_user_icon_callback = callback


