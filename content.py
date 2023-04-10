import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import mysql.connector as sql
from sort import SortSubMenu
import os 

db = sql.connect(host="localhost",user="root",password="root",database="comics",port=3306,autocommit=True)
cursor = db.cursor(buffered=True)

class Content(tk.Frame):
    def __init__(self, details_frame, show_details_callback=None):
        super().__init__(details_frame)
        self.details_frame = details_frame
        # self.content_area = tk.Frame(...)
        self.comics = []
        self.show_details_callback = show_details_callback
        self.title_frame = None

        # Set up the content frame
        self.create_content()

        # Generate and display comics
        cursor.execute("select * from sort")
        temp = cursor.fetchall() 
        if len(temp) == 0:
            order_by = "title ASC"
        else: 
            order_by = temp[0][0]
            print(temp[0][0])
        cursor.execute("delete from sort")
        self.comics = self.generate_comics(order_by)
        self.display_comics(self.comics)

    def filter_comics(self, comic, search_query):
        # Check if any of the comic's attributes contain the search_query
        for attribute in comic:
            if search_query in str(attribute).lower():
                return True
        return False

    def clear_content(self):
        # Clear the content by setting the comics list to an empty list
        self.comics = []

    def add_content(self, new_content):
        # Add new_content to the comics list
        self.comics = new_content

        # Update the display
        self.display_comics(self.comics)

    def create_content(self):
        self.scroll_frame = tk.Frame(
            self.details_frame,
            bg="#2C2C2C"
        )

        self.scroll_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.scroll_frame, bg="#1A1918", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.scroll_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#1A1918")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.scroll_frame.grid_rowconfigure(0, weight=1)
        self.scroll_frame.grid_columnconfigure(0, weight=1)

        # Bind mouse wheel scrolling
        self.scrollable_frame.bind("<Enter>", lambda _: self.scrollable_frame.focus_set())
        self.scrollable_frame.bind("<MouseWheel>", self._on_mouse_wheel)
        
        self.sort_menu = SortSubMenu(self.scrollable_frame, self, 0, 20, 1, ("TkDefaultFont", 12), (10, 5), self.sort_and_update_content)

    def generate_comics(self, order_by):            
        query = "SELECT * from comics"
        query += f" ORDER BY {order_by}"
        cursor.execute(query)
        comics = cursor.fetchall()
        comics = list(comics)
        return comics

    def display_comics(self, comics_to_display):
        from comics import ComicDetails

        max_columns = 5  # Define max_columns here
        padding = 10

        # Remove any existing content
        for child in self.scrollable_frame.winfo_children():
            child.destroy()

        # Update the "All Titles" label text
        if self.title_frame is not None:
            all_titles_label = self.title_frame.winfo_children()[0]
            all_titles_label.configure(text=f"All Titles: {len(comics_to_display)}")
        else:
            # Add a title frame
            self.title_frame = tk.Frame(self.details_frame, bg="#2C2C2C")

            all_titles_label = tk.Label(
                self.title_frame,
                text=f"All Titles: {len(comics_to_display)}",
                font=("TkDefaultFont", 14),
                fg="#F5F5F5",
                bg="#2C2C2C",
                anchor="w"
            )
            all_titles_label.pack(side="left", padx=5, pady=5)
            self.title_frame.pack(fill="x", padx=10, pady=10)

        # Display the comics
        for i, comic in enumerate(self.comics):
            style = ttk.Style()
            style.configure('ComicFrame.TFrame', background='#2C2C2C')
            comic_frame = ttk.Frame(
                self.scrollable_frame,
                borderwidth=1,
                relief="solid",
                style="ComicFrame.TFrame",
                width=220)

            comic_frame.grid(row=i // max_columns, column=i % max_columns, padx=padding, pady=padding, sticky="nsew")
            comic_frame.grid_propagate(False)

            title_label = ttk.Label(
                comic_frame, 
                text=comic[0], 
                wraplength=300, 
                justify="center", 
                foreground="white", 
                background="#2C2C2C", 
                font=("Comic Sans MS", 16)
                )
            title_label.pack(padx=padding, pady=padding)

            # Load and display the cover image
            cover_img = Image.open(requests.get(comic[8], stream=True).raw)
            cover_img.thumbnail((100, 200))
            cover_img = ImageTk.PhotoImage(cover_img)

            cover_label = tk.Label(
                comic_frame,
                image=cover_img,
                bg="#2C2C2C"
            )
            cover_label.image = cover_img
            cover_label.pack(side="left", padx=(10, 20), pady=5)

            # Create a new frame for the labels on the right side of the cover image
            details_frame = ttk.Frame(comic_frame, style='ComicFrame.TFrame')
            details_frame.pack(side="left", fill="both", expand=True)

            # Bind the click event to the cover_label
            cover_label.bind("<Button-1>", lambda e, comic=comic: self.show_details(comic))
            cover_label.bind("<Enter>", lambda e: e.widget.config(cursor="hand2"))

            # Display comic details
            author_label = tk.Label(
                details_frame,
                text=f"Author: {comic[1]}",
                font=("Comic Sans MS", 10),
                fg="#F5F5F5",
                bg="#2C2C2C",
                anchor="w",
                wraplength=220,
                justify="left"
            )
            author_label.pack(anchor="w")

            artist_label = tk.Label(
                details_frame,
                text=f"Artist: {comic[2]}",
                font=("Comic Sans MS", 10),
                fg="#F5F5F5",
                bg="#2C2C2C",
                anchor="w",
                wraplength=220,
                justify="left"
            )
            artist_label.pack(anchor="w")

            genre_label = tk.Label(
                details_frame,
                text=f"Genre: {comic[5]}",
                font=("Comic Sans MS", 10),
                fg="#F5F5F5",
                bg="#2C2C2C",
                anchor="w",
                wraplength=220,
                justify="left"
            )
            genre_label.pack(anchor="w")
            
            # Display "Language:" text
            language_text_label = tk.Label(
                details_frame,
                text="Language:",
                font=("Comic Sans MS", 10),
                fg="#F5F5F5",
                bg="#2C2C2C",
                anchor="w",
                wraplength=220,
                justify="left"
            )
            language_text_label.pack(side="left", pady=5)  # Adjust the pady value to set the vertical gap

            # Load and display the flag image for the language
            language = comic[9]
            flag_path = f"images/flags/{language}.png"
            print(flag_path)
            
            try:
                flag_img = Image.open(flag_path)
                flag_img.thumbnail((20, 10))
                flag_img = ImageTk.PhotoImage(flag_img)
            except FileNotFoundError:
                print(language)
                flag_img = None

            language_flag_label = tk.Label(
                details_frame,
                image=flag_img,
                bg="#2C2C2C",
                anchor="w",
                justify="left"
            )
            if flag_img:
                language_flag_label.image = flag_img
            language_flag_label.pack(side="left", pady=5)  # Adjust the pady value to set the vertical gap

        for i in range(max_columns):
            self.scrollable_frame.columnconfigure(i, weight=1)

    def _on_mouse_wheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def search_comic(self, search_query):
        search_results = [comic for comic in self.comics if self.filter_comics(comic, search_query)]
        self.display_comics(search_results)

    def show_details(self, comic):
        if self.show_details_callback:
            self.show_details_callback(comic)

    def search_and_update_content(self, search_query):
        search_query = search_query.lower()
        search_results = [comic for comic in self.comics if self.filter_comics(comic, search_query)]
        self.display_comics(search_results)

    def sort_and_update_content(self, order_by):
        # Check the order type (ascending or descending)
        if order_by == "title_desc":
            order_by = "title DESC"
        elif order_by == "release_date_asc":
            order_by = "release_date"

        # Fetch the sorted data from the database
        cursor.execute(f"SELECT * FROM comics ORDER BY {order_by}")
        print(f"SELECT * FROM comics ORDER BY {order_by}")
        sorted_data = cursor.fetchall()

        # Show the sorted data in a pop-up window
        self.show_sort_results(sorted_data)

        # Update the content with the sorted data
        self.clear_content()
        self.add_content(sorted_data)

    def show_sort_results(self, sorted_data):
        sort_window = tk.Toplevel(self)
        sort_window.title("Sorted Results")

        sort_results_listbox = tk.Listbox(sort_window, width=100, height=20)
        sort_results_listbox.pack(padx=10, pady=10)

        for comic in sorted_data:
            sort_results_listbox.insert(tk.END, comic[0])  # Assuming comic[0] is the title of the comic

        close_button = tk.Button(sort_window, text="Close", command=sort_window.destroy)
        close_button.pack(pady=10)

