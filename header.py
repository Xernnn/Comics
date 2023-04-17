import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from user_menu import UserMenu
from user_info import UserInfo
import mysql.connector as sql
import tkinter.messagebox as messagebox
import requests

db = sql.connect(host="localhost", user="root", password="root", database="comics", port=3306, autocommit=True)
cursor = db.cursor(buffered=True)


class Header(tk.Frame):
    def __init__(self, parent, go_to_homepage_callback, search_callback, toggle_left_menu, user_menu, user_info):
        super().__init__(parent, bg="#1A1918")
        self.parent = parent
        self.go_to_homepage_callback = go_to_homepage_callback
        self.search_callback = search_callback
        self.toggle_left_menu = toggle_left_menu
        self.user_menu = user_menu
        self.user_info = user_info
        self.create_header()

    def create_header(self):
        bg_color = "#1A1918"
        self.config(bg=bg_color)
        self.pack(fill=tk.X)
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

        # Add search filter options
        self.search_filter = tk.StringVar()
        self.search_filter.set("All")

        filter_options = [
            "All",
            "All",
            "Title",
            "Author",
            "Artist",
            "Series",
        ]

        filter_frame = tk.Frame(self.header_frame, bg="#2C2C2C")  # Set the background color to match the header
        filter_menu = ttk.OptionMenu(filter_frame, self.search_filter, *filter_options)
        filter_menu.pack(side=tk.LEFT, padx=5)

        filter_frame.pack(side=tk.RIGHT, padx=10)  # Pack filter_frame to the right of the search box

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

        # Bind the search icon click
        self.search_icon_label.bind("<Button-1>", self.search_comics)

        # Bind the Enter key press in the search_box
        self.search_box.bind("<Return>", self.search_comics)

    def search_comics(self, event):
        search_query = self.search_box.get().strip()
        if search_query and search_query != self.placeholder_text:
            option = self.search_filter.get()
            results = self.search(option, search_query)
            if results:
                self.show_results_window(results)
            else:
                messagebox.showerror("Error", "Sorry, your comic doesn't exist here.")
        elif not search_query or search_query == self.placeholder_text:
            messagebox.showerror("Error", "Please enter a search term.")

    def search(self, option, where):
        where = f"%{where}%"
        where = (where,)
        if option == "All":
            cursor.execute("SELECT * from comics WHERE title LIKE %s OR author LIKE %s OR artist LIKE %s OR series LIKE %s", where * 4)
        elif option == "Title":
            cursor.execute("SELECT * from comics WHERE title LIKE %s", where)
        elif option == "Author":
            cursor.execute("SELECT * from comics WHERE author LIKE %s", where)
        elif option == "Artist":
            cursor.execute("SELECT * from comics WHERE artist LIKE %s", where)
        elif option == "Series":
            cursor.execute("SELECT * from comics WHERE series LIKE %s", where)

        if cursor.rowcount > 0:
            return cursor.fetchall()

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
            if self.user_info.user_data['avatar'] == 'images/guest.png':
                avatar_image = Image.open(self.user_info.user_data['avatar'])
            else:
                avatar_image = Image.open(requests.get(self.user_info.user_data['avatar'], stream=True).raw)
            avatar_image = avatar_image.resize((35, 35), Image.Resampling.LANCZOS)
            avatar_image_button = ImageTk.PhotoImage(avatar_image)
            self.user_button.config(image=avatar_image_button)
            self.user_button.image = avatar_image_button

    def update_user_data(self, username):
        if self.user_menu.is_logged_in():
            s = "SELECT avatar, gmail, role, age, favorite FROM users WHERE username = %s"
            val = (username,)
            cursor.execute(s, val)
            result = cursor.fetchone()
            if result is not None:
                avatar, gmail, role, age, favorite = result
                self.user_info.user_data['avatar'] = avatar
                self.user_info.user_data['email'] = gmail
                self.user_info.user_data['user_role'] = role
                self.user_info.user_data['username'] = username
                self.user_info.user_data['favorite'] = favorite
                self.user_info.user_data['age'] = age

    def update(self, age, favorite, avatar):
        self.user_info.user_data['age'] = age
        self.user_info.user_data['favorite'] = favorite
        self.user_info.user_data['avatar'] = avatar
        user_data = {
            "age": self.user_info.user_data['age'],
            "favorite": self.user_info.user_data['favorite'],
            "avatar": self.user_info.user_data['avatar'],
            "username": self.user_info.user_data['username']
        }
        values = tuple(user_data.values())
        cursor.execute("UPDATE users SET age=%s, favorite=%s, avatar=%s WHERE username=%s", values)


    def update_content(self, results):
        print(f"Updating content with results: {results}")
        for widget in self.winfo_children():
            widget.destroy()

        # Display search results
        for result in results:
            # Create a widget for each search result and add it to the content area
            # For example, you can use a label with the title of the comic:
            comic_label = tk.Label(self, text=result[1], font=("Arial", 14))
            comic_label.pack(pady=10)

    def show_results_window(self, results):
        results_window = tk.Toplevel(self.parent)
        results_window.title("Search Results")
        results_window.iconbitmap('images/ch.ico')
        results_window.geometry("800x600")
        results_window.config(bg="#1A1918")

        # Set up a Frame to hold the comic boxes
        comic_boxes_frame = tk.Frame(results_window, bg="#1A1918")
        comic_boxes_frame.pack(fill=tk.BOTH, expand=True)

        # Create comic information boxes and add them to the grid
        row = 0
        column = 0
        max_columns = 2
        padding = 10

        for index, result in enumerate(results):
            comic_frame = ttk.Frame(comic_boxes_frame, borderwidth=1, relief="solid", width=10)
            comic_frame.grid(row=row, column=column, padx=padding, pady=padding, sticky="nsew")
            comic_frame.grid_propagate(False)

            title_label = ttk.Label(comic_frame, text=result[0], wraplength=300, justify="center", foreground="white",
                                    background="#2C2C2C", font=("Comic Sans MS", 16))
            title_label.pack(padx=padding, pady=padding)

            # Load and display the cover image
            print(result)
            cover_img = Image.open(requests.get(result[8], stream=True).raw)
            cover_img.thumbnail((100, 200))
            cover_img = ImageTk.PhotoImage(cover_img)

            cover_label = tk.Label(comic_frame, image=cover_img, bg="#2C2C2C")
            cover_label.image = cover_img
            cover_label.pack(side="left", padx=(10, 20), pady=5)

            # Create a new frame for the labels on the right side of the cover image
            details_frame = ttk.Frame(comic_frame)
            details_frame.pack(side="left", fill="both", expand=True)

            author_label = tk.Label(details_frame, text=f"Author: {result[1]}", font=("Comic Sans MS", 10),
                                    fg="#F5F5F5", bg="#2C2C2C", anchor="w", wraplength=220, justify="left")
            author_label.pack(anchor="w")

            artist_label = tk.Label(details_frame, text=f"Artist: {result[2]}", font=("Comic Sans MS", 10),
                                    fg="#F5F5F5", bg="#2C2C2C", anchor="w", wraplength=220, justify="left")
            artist_label.pack(anchor="w")

            series_label = tk.Label(details_frame, text=f"Series: {result[7]}", font=("Comic Sans MS", 10),
                                    fg="#F5F5F5", bg="#2C2C2C", anchor="w", wraplength=220, justify="left")
            series_label.pack(anchor="w")

            # Update the row and column for the next comic box
            column += 1
            if column >= max_columns:
                column = 0
                row += 1