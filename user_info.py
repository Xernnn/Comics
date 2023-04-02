import tkinter as tk
from PIL import Image, ImageTk
import random
from lorem_text import lorem

class UserInfo:
    def __init__(self, window):
        self.window = window
        
        # self.user_data = {
        #     'avatar': 'images/orgasm.jpg',
        #     'username': 'Xern',
        #     'email': 'sonn.bi12-389@st.usth.edu.vn',
        #     'age': 20,
        #     'member_since': '28/11/2021',
        #     'user_role': 'administrator',
        #     'favorite': 'Spider-man',
        #     'comics_followed': 118,
        #     'comics_read': 135,
        #     'chapters_read': 2184
        # }
        
        # if user_data is None:
        user_data = {
            'avatar': 'images/orgasm.jpg',
            'username': lorem.words(1),
            'email': f"{lorem.words(1)}@{lorem.words(1)}.com",
            'age': random.randint(13, 99),
            'member_since': f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(2000, 2023)}",
            'user_role': random.choice(['Administrator', 'User', 'Moderator']),
            'favorite': lorem.words(random.randint(1, 3)),
            'comics_followed': random.randint(1, 200),
            'comics_read': random.randint(1, 300),
            'chapters_read': random.randint(1, 5000)
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
        avatar_image = Image.open(self.user_data['avatar'])
        avatar_image = avatar_image.resize((80, 80), Image.Resampling.LANCZOS)
        avatar_image_button = ImageTk.PhotoImage(avatar_image)

        avatar_label = tk.Label(self.user_info_window, image=avatar_image_button)
        avatar_label.image = avatar_image_button
        avatar_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), rowspan=6)
        
        # User's info
        username_label = tk.Label(self.user_info_window, text=f"Username: {self.user_data['username']}")
        username_label.grid(row=0, column=1, sticky=tk.W, pady=(10, 0))

        age_label = tk.Label(self.user_info_window, text=f"Age: {self.user_data['age']}")
        age_label.grid(row=1, column=1, sticky=tk.W)

        member_since_label = tk.Label(self.user_info_window, text=f"Member Since: {self.user_data['member_since']}")
        member_since_label.grid(row=2, column=1, sticky=tk.W)

        user_role_label = tk.Label(self.user_info_window, text=f"User Role: {self.user_data['user_role']}")
        user_role_label.grid(row=3, column=1, sticky=tk.W)

        favorite_label = tk.Label(self.user_info_window, text=f"Favorite: {self.user_data['favorite']}")
        favorite_label.grid(row=4, column=1, sticky=tk.W)

        comics_followed_label = tk.Label(self.user_info_window, text=f"Comics followed: {self.user_data['comics_followed']}")
        comics_followed_label.grid(row=5, column=1, sticky=tk.W)

        comics_read_label = tk.Label(self.user_info_window, text=f"Comics read: {self.user_data['comics_read']}")
        comics_read_label.grid(row=6, column=1, sticky=tk.W)

        chapters_read_label = tk.Label(self.user_info_window, text=f"Chapters read: {self.user_data['chapters_read']}")
        chapters_read_label.grid(row=7, column=1, sticky=tk.W)