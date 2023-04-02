import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import os
import mysql.connector as sql


db = sql.connect(host="localhost",user="root",password="root",database="comics",port=3306,autocommit=True)
cursor = db.cursor(buffered=True)

class Content(tk.Frame):
    def __init__(self, details_frame, show_details_callback=None):
        super().__init__(details_frame)
        self.details_frame = details_frame
        self.comics = []
        self.show_details_callback = show_details_callback

        # Set up the content frame
        self.create_content()

        # Generate and display comics
        self.comics = self.generate_comics(50)
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

    def generate_comics(self, num_comics):
        cursor.execute("SELECT * from comics")
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
        if hasattr(self, 'title_frame'):
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
            flag_img = Image.open(requests.get(comic[9], stream=True).raw)
            flag_img.thumbnail((20, 10))
            flag_img = ImageTk.PhotoImage(flag_img)

            language_flag_label = tk.Label(
                details_frame,
                image=flag_img,
                bg="#2C2C2C",
                anchor="w",
                justify="left"
            )
            language_flag_label.image = flag_img
            language_flag_label.pack(side="left", pady=5)  # Adjust the pady value to set the vertical gap

            
        for i in range(max_columns):
            self.scrollable_frame.columnconfigure(i, weight=1)

    def _on_mouse_wheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def search_comic(self, search_query):
        search_query = search_query.lower()
        search_results = [comic for comic in self.comics if search_query in comic["title"].lower()]
        self.display_comics(search_results)
        
    def show_details(self, comic):
        if self.show_details_callback:
            self.show_details_callback(comic)
            
