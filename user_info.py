import tkinter as tk
from PIL import Image, ImageTk
from Update import Update
import requests
import mysql.connector as sql
from tkinter import ttk
from delete_user import Delete

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
        window_height = 400
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

        favorite_label = tk.Label(self.user_info_window, text=f"About me: {self.user_data['favorite']}")
        favorite_label.grid(row=4, column=1, sticky=tk.W)

        comics_followed_label = tk.Label(self.user_info_window, text=f"Comics followed: {self.user_data['comics_followed']}")
        comics_followed_label.grid(row=5, column=1, sticky=tk.W)

        # Add a new column and configure it to expand
        self.user_info_window.columnconfigure(2, weight=1)

        # Button
        button = tk.Button(self.user_info_window, text="Update", command=self.update)
        button.grid(row=6, column=1, pady=(10, 5), sticky=tk.E + tk.W)
        button.configure(anchor='center')
        
        button = tk.Button(self.user_info_window, text="Show Followed Comics", command=self.show_followed_comics)
        button.grid(row=7, column=1, pady=(10, 5), sticky=tk.E + tk.W)
        button.configure(anchor='center')

        
        if self.user_data['user_role'] == 'User':
            button = tk.Button(self.user_info_window, text="Delete Account", command=self.hehe)
            button.grid(row=8, column=1, pady=(10, 5), sticky=tk.E + tk.W)
            button.configure(anchor='center')
        else:
            button = tk.Button(self.user_info_window, text="Show User List", command=self.show)
            button.grid(row=10, column=1, pady=(10, 5), sticky=tk.E + tk.W)
            button.configure(anchor='center')
            
        if self.user_data['user_role'] == 'Admin':
            button = tk.Button(self.user_info_window, text="Delete user", command=self.delete_user)
            button.grid(row=10, column=1, pady=(20, 10), sticky=tk.E + tk.W)
            button.configure(anchor='center')

    def delete_user(self):
        Delete(self.user_info_window)

    def update(self):
        update_window = Update(self.user_info_window)
        update_window.update_data_callback = self.update_user_data

    def update_user_data(self, age, favorite, avatar):
        self.user_data['age'] = age
        self.user_data['favorite'] = favorite
        self.user_data['avatar'] = avatar

        user_data = {
            "age": self.user_data['age'],
            "about me": self.user_data['favorite'],
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

    def hehe(self):
        data = (self.user_data['username'], )
        cursor.execute("DELETE FROM users WHERE username = %s", data)

    def show(self):
        cursor.execute("SELECT * FROM users")
        datas = cursor.fetchall()

        # create a new Toplevel window
        tree_window = tk.Toplevel(self.user_info_window)
        tree_window.title("User List")
        tree_window.geometry("600x300")

        # create the treeview widget and configure columns
        my_tree = ttk.Treeview(tree_window)
        my_tree["columns"] = ("Username", "Password", "Avatar", "Gmail", "Role", "Age", "About me", "Comics_followed")

        my_tree.column("#0", width=30)
        my_tree.column("Username", width=100)
        my_tree.column("Password", width=100)
        my_tree.column("Avatar", width=100)
        my_tree.column("Gmail", width=150)
        my_tree.column("Role", width=50)
        my_tree.column("Age", width=30)
        my_tree.column("About me", width=150)
        my_tree.column("Comics_followed", width=120)
        
        my_tree.heading("#0", text="ID")
        my_tree.heading("Username", text="Username")
        my_tree.heading("Password", text="Password")
        my_tree.heading("Avatar", text="Avatar")
        my_tree.heading("Gmail", text="Gmail")
        my_tree.heading("Role", text="Role")
        my_tree.heading("Age", text="Age")
        my_tree.heading("About me", text="About me")
        my_tree.heading("Comics_followed", text="Comics followed")
        count = 0
        for user in datas:
            my_tree.insert("", "end", text=count, values=(user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7]))
            count = count + 1
        my_tree.pack()


        my_tree.pack()