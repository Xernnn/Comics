import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from content import Content

language_flags = {
    "English": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Flag_of_Great_Britain_%281707%E2%80%931800%29.svg/2560px-Flag_of_Great_Britain_%281707%E2%80%931800%29.svg.png",
    "Chinese": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/1280px-Flag_of_the_People%27s_Republic_of_China.svg.png",
    "French": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Flag_of_France_%28lighter_variant%29.svg/1280px-Flag_of_France_%28lighter_variant%29.svg.png",
    "Italian": "https://upload.wikimedia.org/wikipedia/en/thumb/0/03/Flag_of_Italy.svg/1280px-Flag_of_Italy.svg.png",
    "Japanese": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/1280px-Flag_of_Japan.svg.png",
    "Korean": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/1280px-Flag_of_South_Korea.svg.png",
    "Spanish": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Bandera_de_Espa%C3%B1a.svg/750px-Bandera_de_Espa%C3%B1a.svg.png",
    "Vietnamese": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Flag_of_Vietnam.svg/1280px-Flag_of_Vietnam.svg.png"
}

class ComicBox(tk.Frame):
    def __init__(self, master, comic):
        super().__init__(master, bg="#2C2C2C")
        self.comic = comic
        self.create_widgets()

    def create_widgets(self):
        cover_img = Image.open(requests.get(self.comic[8], stream=True).raw)
        cover_img.thumbnail((300, 600))
        cover_img = ImageTk.PhotoImage(cover_img)

        cover_button = tk.Button(
            self,
            image=cover_img,
            bg="#2C2C2C",
            borderwidth=0,
            highlightthickness=0,
            command=self.show_details
        )
        cover_button.image = cover_img
        cover_button.pack(padx=20, pady=20)

    def show_details(self):
        ComicDetails(self.master, self.comic)

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
        flag_url = language_flags.get(self.comic[9])
        if flag_url:
            flag_img = Image.open(requests.get(flag_url, stream=True).raw)
            flag_img.thumbnail((30, 15))
            flag_img = ImageTk.PhotoImage(flag_img)
        else:
            flag_img = None

        language_flag_label = tk.Label(
            language_frame,
            image=flag_img,
            bg="#2C2C2C"
        )
        language_flag_label.image = flag_img
        language_flag_label.pack(side="left", padx=(5, 0))