import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from content import Content

class ComicDetails(tk.Toplevel):
    def __init__(self, master, comic):
        super().__init__(master)
        self.title("Comic Details")
        self.geometry("1000x600")
        self.config(bg="#2C2C2C")
        self.comic = comic
        self.create_widgets()

    def create_widgets(self):
        padding = 5
        cover_img = Image.open(requests.get(self.comic[8], stream=True).raw)
        cover_img.thumbnail((300, 600))
        cover_img = ImageTk.PhotoImage(cover_img)

        cover_label = tk.Label(
            self,
            image=cover_img,
            bg="#2C2C2C"
        )
        cover_label.image = cover_img
        cover_label.pack(side="left", padx=(20, 0), pady=20)

        details_frame = tk.Frame(self, bg="#2C2C2C")
        details_frame.pack(side="left", fill="both", expand=True, padx=(10, 20), pady=5)

        title_label = tk.Label(
            details_frame,
            text=self.comic[0],
            font=("Comic Sans MS", 20),
            fg="#F5F5F5",
            bg="#2C2C2C",
            wraplength=400,
            justify="center"
        )
        title_label.pack(padx=padding, pady=(0, 20))

        labels = [
            (f"Series: {self.comic[7]}", 12),
            (f"Volume: {self.comic[6]}", 12),
            (f"Author: {self.comic[1]}", 12),
            (f"Artist: {self.comic[2]}", 12),
            (f"Publisher: {self.comic[3]}", 12),
            (f"Publish Date: {self.comic[4]}", 12),
            (f"Genre: {self.comic[5]}", 12),
            # (f"Language: {self.comic[9]}", 12),
            (f"Synopsis: {self.comic[10]}", 12)
        ]

        for text, font_size in labels:
            label = tk.Label(
                details_frame,
                text=text,
                font=("Comic Sans MS", font_size),
                fg="#F5F5F5",
                bg="#2C2C2C",
                wraplength=600,
                justify="left"
            )
            label.pack(anchor="w", padx=padding, pady=5)
        

        # Create a new frame for the language label and flag
        language_frame = tk.Frame(details_frame, bg="#2C2C2C")
        language_frame.pack(anchor="w", padx=padding, pady=1)

        # Add the "Language:" label
        language_text_label = tk.Label(
            language_frame,
            text="Language:",
            font=("Comic Sans MS", 12),
            fg="#F5F5F5",
            bg="#2C2C2C"
        )
        language_text_label.pack(side="left")

        # Load and display the flag image for the language
        flag_img = Image.open(requests.get(self.comic[9], stream=True).raw)
        flag_img.thumbnail((30, 15))
        flag_img = ImageTk.PhotoImage(flag_img)

        language_flag_label = tk.Label(
            language_frame,
            image=flag_img,
            bg="#2C2C2C"
        )
        language_flag_label.image = flag_img
        language_flag_label.pack(side="left", padx=(5, 0))