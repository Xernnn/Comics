import tkinter as tk

class LeftMenu:
    def __init__(self, details_frame, master=None, content=None):
        self.master = master
        self.content = content
        self.details_frame = details_frame
        self.menu_visible = False
        self.create_left_menu()
    
    def toggle_left_menu(self, event):
        if self.menu_visible:
            self.hide_left_menu()
        else:
            self.left_menu_frame.place(x=0, y=66, width=250, height=1000)
            self.left_menu_frame.lift()
        self.menu_visible = not self.menu_visible


    def hide_left_menu(self):
        self.left_menu_frame.place_forget()

    def create_left_menu(self):
        self.left_menu_frame = self.create_button_frame(x=0, y=1000, width=4560, height=1000)
        self.left_menu_frame.place_forget()

    def create_button_frame(self, x, y, width, height):
        button_frame = tk.Frame(
            self.details_frame,
            bg="#1A1918",
            relief=tk.GROOVE
        )
        button_frame.place(x=x, y=y, width=width, height=height)

        button_texts = [
            ("Sort by Title", "Sort by Release", "Sort by Rating", "Sort by Views"),
            ("Modify Title", "Modify Issue", "Modify Writer", "Modify Artist")
        ]

        button_width = 24  # Adjust the desired button width
        button_height = 2  # Adjust the desired button height

        buttons_frame = tk.Frame(button_frame, bg="#1A1918")
        buttons_frame.place(relx=0.5, rely=0.5, anchor="center")

        button_font = ("Arial", 12)  # Adjust the desired button font size
        button_padding = (5, 5)  # Adjust the desired padding between buttons

        for part_index, part_button_texts in enumerate(button_texts):
            for index, button_text in enumerate(part_button_texts):
                button = tk.Button(
                    button_frame,
                    text=button_text,
                    command=lambda t=button_text: self.sidebar_action(t),
                    width=button_width,
                    height=button_height,
                    font=button_font,
                    bg="#3C3C3C",
                    fg="#F5F5F5"
                )
                button.grid(
                    row=index + 5 * part_index,
                    column=0,
                    padx=5,
                    pady=(button_padding[0] if index == 0 else button_padding[1])  # Use the appropriate padding value based on the index
                )  # Center the buttons horizontally
                button.bind("<Enter>", lambda e, b=button: b.configure(bg="#5C5C5C"))  # Hover effect
                button.bind("<Leave>", lambda e, b=button: b.configure(bg="#3C3C3C"))  # Hover effect
        
        return button_frame

                
    def sidebar_action(self, button_text):
        if button_text == "Sort by Title":
            # sorted_comics = sorted(self.content.comics, key=lambda x: x["title"])
            print("Sorted by title")
        elif button_text == "Sort by Release":
            # sorted_comics = sorted(self.content.comics, key=lambda x: x["year"])
            print("Sorted by Release")
        elif button_text == "Sort by Rating":
            # Assuming you have a "rating" key in your comic dictionary
            # sorted_comics = sorted(self.content.comics, key=lambda x: x["rating"], reverse=True)
            print("Sorted by Rating")
        elif button_text == "Sort by Views":
            # Assuming you have a "views" key in your comic dictionary
            # sorted_comics = sorted(self.content.comics, key=lambda x: x["views"], reverse=True)
            print("Sorted by Views")
        else:
            return  # Do nothing if it's not a sorting button

        # self.content.display_comics(sorted_comics)

        
