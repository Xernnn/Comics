# sort.py
import tkinter as tk
import mysql.connector as sql

db = sql.connect(host="localhost",user="root",password="root",database="comics",port=3306,autocommit=True)
cursor = db.cursor(buffered=True)

class SortSubMenu:
    def __init__(self, parent_frame, index, button_width, button_height, button_font, button_padding, action_callback):
        self.parent_frame = parent_frame
        self.index = index
        self.button_width = button_width
        self.button_height = button_height
        self.button_font = button_font
        self.button_padding = button_padding
        self.action_callback = action_callback

        self.create_submenu()

    def create_submenu(self):
        submenu_texts = ["Sort by Title (A-Z)", "Sort by Release", "Sort by Rating", "Sort by Views"]

        submenu_frame = tk.Frame(self.parent_frame, bg="#1A1918")
        submenu_frame.grid(row=self.index * 5, column=0, padx=10, pady=(self.button_padding[0] if self.index == 0 else self.button_padding[1]))

        main_button = tk.Label(
            submenu_frame,
            text="Sort",
            width=self.button_width,
            height=self.button_height,
            font=(self.button_font[0], self.button_font[1], "bold"),  # Add the "bold" attribute
            bg="#1A1918",
            fg="#F5F5F5",
            cursor="hand2",
            anchor="w"
        )
        main_button.grid(row=0, column=0, sticky="w")
        main_button.bind("<Button-1>", lambda e: self.toggle_submenu())
        main_button.bind("<Enter>", lambda e, b=main_button: b.configure(bg="#3C3C3C", fg="#FFFFFF"))
        main_button.bind("<Leave>", lambda e, b=main_button: b.configure(bg="#1A1918", fg="#F5F5F5"))

        for sub_index, sub_label in enumerate(submenu_texts):
            sub_button = tk.Label(
                submenu_frame,
                text=sub_label,
                width=self.button_width,
                height=self.button_height,
                font=self.button_font,
                bg="#1A1918",
                fg="#F5F5F5",
                cursor="hand2",
                anchor="w"
            )
            sub_button.grid(row=sub_index + 1, column=0, sticky="w")
            sub_button.bind("<Button-1>", lambda e, t=sub_label: self.sort_action(t))
            sub_button.bind("<Enter>", lambda e, b=sub_button: b.configure(bg="#3C3C3C", fg="#FFFFFF"))
            sub_button.bind("<Leave>", lambda e, b=sub_button: b.configure(bg="#1A1918", fg="#F5F5F5"))

            sub_button.grid_remove()

        self.submenu_frame = submenu_frame
        self.buttons = [main_button] + [sub_button for sub_button in submenu_frame.children.values()][1:]

    def toggle_submenu(self):
        any_visible = any(button.winfo_viewable() for button in self.buttons[1:])
        
        for button in self.buttons[1:]:
            if any_visible:
                button.grid_remove()
            else:
                button.grid()

                
    def sort_action(self, button_text):
        if button_text == "Sort by Title (A-Z)":
            print("Sorted by Title")
        elif button_text == "Sort by Release":
            print("Sorted by Release")
        elif button_text == "Sort by Rating":
            print("Sorted by Rating")
        elif button_text == "Sort by Views":
            print("Sorted by Views")
        else:
            return  # Do nothing if it's not a sorting button
