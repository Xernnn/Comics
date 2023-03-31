import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
from lorem_text import lorem
import os

class Content:
    def __init__(self):
        self.create_content()

    def create_content(self):
        self.scroll_frame = tk.Frame(
            self.details_frame,
            bg="#1A1918"
        )
        self.scroll_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.scroll_frame, bg="#1A1918", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.scroll_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#1A1918")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Bind mouse wheel scrolling
        self.scrollable_frame.bind("<Enter>", lambda _: self.scrollable_frame.focus_set())
        self.scrollable_frame.bind("<MouseWheel>", self._on_mouse_wheel)

        # Comic data
        # comics = [
        #     {
        #         "title": "Spider-Man",
        #         "issue": "Amazing Spider-Man #1",
        #         "writer": "Dan Slott",
        #         "artist": "Humberto Ramos",
        #         "publisher": "Marvel Comics",
        #         "year": 2014,
        #         "cover": "C:/Users/Admin/OneDrive/Documents/University of Science and Technology Hanoi/Advance Python/Comic Information Management System/orgasm.jpg"
        #     },https://product.hstatic.net/200000343865/product/8_6afdb5e2d6aa4672b713460f8ec44d61_master.jpg
        #     {
        #         "title": "Batman",
        #         "issue": "Batman #404",
        #         "writer": "Frank Miller",
        #         "artist": "David Mazzucchelli",
        #         "publisher": "DC Comics",
        #         "year": 1987,
        #         "cover": "C:/Users/Admin/OneDrive/Documents/University of Science and Technology Hanoi/Advance Python/Comic Information Management System/orgasm.jpg"
        #     },
        #     {
        #         "title": "Watchmen",
        #         "issue": "#1",
        #         "writer": "Alan Moore",
        #         "artist": "Dave Gibbons",
        #         "publisher": "DC Comics",
        #         "year": 1986,
        #         "cover": "C:/Users/Admin/OneDrive/Documents/University of Science and Technology Hanoi/Advance Python/Comic Information Management System/orgasm.jpg"
        #     },
        #     {
        #         "title": "Saga",
        #         "issue": "#1",
        #         "writer": "Brian K. Vaughan",
        #         "artist": "Fiona Staples",
        #         "publisher": "Image Comics",
        #         "year": 2012,
        #         "cover": "C:/Users/Admin/OneDrive/Documents/University of Science and Technology Hanoi/Advance Python/Comic Information Management System/orgasm.jpg"
        #     },
        #     {
        #         "title": "The Walking Dead",
        #         "issue": "#1",
        #         "writer": "Robert Kirkman",
        #         "artist": "Tony Moore",
        #         "publisher": "Image Comics",
        #         "year": 2003,
        #         "cover": "C:/Users/Admin/OneDrive/Documents/University of Science and Technology Hanoi/Advance Python/Comic Information Management System/orgasm.jpg"
        #     },
        #     {
        #         "title": "X-Men",
        #         "issue": "Giant-Size X-Men #1",
        #         "writer": "Len Wein",
        #         "artist": "Dave Cockrum",
        #         "publisher": "Marvel Comics",
        #         "year": 1975,
        #         "cover": "C:/Users/Admin/OneDrive/Documents/University of Science and Technology Hanoi/Advance Python/Comic Information Management System/orgasm.jpg"
        #     }
        # ]
        comics = []
        for i in range(30):
            title = lorem.words(random.randint(1, 4))
            issue = f"Issue #{random.randint(1, 100)}"
            writer = lorem.words(random.randint(1, 3))
            artist = lorem.words(random.randint(1, 3))
            publisher = lorem.words(random.randint(1, 2))
            year = random.randint(1950, 2022)
            cover = "images/orgasm.jpg"
            comics.append({"title": title, "issue": issue, "writer": writer, "artist": artist, "publisher": publisher, "year": year, "cover": cover})

        # Display comic covers and information
        padding_x = 15
        padding_y = 10
        cover_width = 180
        cover_height = 225
        num_comics = len(comics)
        max_columns = 3
        rows = (num_comics + max_columns - 1) // max_columns

        content_width = max_columns * (cover_width + padding_x)
        content_height = rows * (cover_height + padding_y)
        
        for i in range(rows):
            for j in range(max_columns):
                index = i * max_columns + j
                if index < num_comics:
                    comic = comics[index]
                    # Comic frame
                    comic_frame = tk.Frame(
                        self.scrollable_frame,
                        bg="#1A1918",
                        highlightthickness=1,
                        highlightbackground="#505050",
                        highlightcolor="#505050",
                        width=cover_width + 2*padding_x
                    )
                    comic_frame.grid(row=i, column=j, padx=padding_x, pady=padding_y, sticky="nsew")

                    # Comic cover
                    cover = ImageTk.PhotoImage(Image.open(comic["cover"]).resize((cover_width, cover_height)))
                    cover_label = tk.Label(comic_frame, image=cover, bg="#1A1918")
                    cover_label.image = cover
                    cover_label.grid(row=0, column=0, padx=10)

                    # Comic details
                    details_frame = tk.Frame(comic_frame, bg="#1A1918")
                    details_frame.grid(row=0, column=1, sticky="nsew")

                    title_label = tk.Label(
                        details_frame, 
                        text=comic["title"], 
                        font=("TkDefaultFont", 14), 
                        fg="#F5F5F5", 
                        bg="#1A1918",
                        wraplength = cover_width - 20,
                        anchor="w"
                    )
                    title_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

                    issue_label = tk.Label(
                        details_frame, 
                        text=comic["issue"], 
                        font=("TkDefaultFont", 12), 
                        fg="#CCCCCC", 
                        bg="#1A1918"
                    )
                    issue_label.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")

                    writer_label = tk.Label(
                        details_frame, 
                        text="Writer: " + comic["writer"], 
                        font=("TkDefaultFont", 12), 
                        fg="#F5F5F5", 
                        bg="#1A1918"
                    )
                    writer_label.grid(row=2, column=0, padx=10, pady=(0, 5), sticky="w")

                    artist_label = tk.Label(
                        details_frame, 
                        text="Artist: " + comic["artist"], 
                        font=("TkDefaultFont", 12), 
                        fg="#F5F5F5", 
                        bg="#1A1918"
                    )
                    artist_label.grid(row=3, column=0, padx=10, pady=(0, 5), sticky="w")

                    publisher_label = tk.Label(
                        details_frame, 
                        text="Publisher: " + comic["publisher"], 
                        font=("TkDefaultFont", 12), 
                        fg="#F5F5F5", 
                        bg="#1A1918"
                        )
                    publisher_label.grid(row=4, column=0, padx=10, pady=(0, 5), sticky="w")

                    year_label = tk.Label(
                        details_frame, 
                        text="Year: " + str(comic["year"]), 
                        font=("TkDefaultFont", 12), 
                        fg="#F5F5F5", 
                        bg="#1A1918"
                    )
                    year_label.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="w")

                    # Add the comic frame to the scrollable frame
                    # comic_frame.grid(row=i, column=j, padx=padding_x, pady=padding_y, sticky="nsew")

        self.scrollable_frame.columnconfigure(list(range(max_columns)), weight=1)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def _on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1 * int(event.delta / 120), "units")