# sort.py
import tkinter as tk
import mysql.connector as sql

db = sql.connect(host="localhost",user="root",password="root",database="comics",port=3306,autocommit=True)
cursor = db.cursor(buffered=True)

class SortSubMenu:
    def __init__(self, parent_frame, content_obj, index, button_width, button_height, button_font, button_padding, action_callback):
        self.parent_frame = parent_frame
        self.content_obj = content_obj
        self.index = index
        self.button_width = button_width
        self.button_height = button_height
        self.button_font = button_font
        self.button_padding = button_padding
        self.action_callback = action_callback
        self.sort_options = ["Sort by Title (A-Z)", "Sort by Title (Z-A)", "Sort by Newest", "Sort by Oldest"]

        self.create_submenu()

    def create_submenu(self):
        submenu_texts = self.sort_options

        submenu_frame = tk.Frame(self.parent_frame, bg="#1A1918")
        submenu_frame.grid(row=self.index * 5, column=0, padx=10, pady=(self.button_padding[0] if self.index == 0 else self.button_padding[1]))

        main_button = tk.Label(
            submenu_frame,
            text="Sort",
            width=self.button_width,
            height=self.button_height,
            font=(self.button_font[0], self.button_font[1], "bold"),
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
            sub_button.grid_row = sub_index + 1
            sub_button.grid_column = 0
            sub_button.grid(row=sub_button.grid_row, column=sub_button.grid_column, sticky="w")
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
                button.grid(row=button.grid_row, column=button.grid_column, sticky="w")

    def sort_action(self, text):
        print("Sort action:", text)
        if text == "Sort by Title (A-Z)":
            self.order_by = "title ASC"
        elif text == "Sort by Title (Z-A)":
            self.order_by = "title DESC"
        elif text == "Sort by Newest":
            self.order_by = "public_date DESC"
        elif text == "Sort by Oldest":
            self.order_by = "public_date ASC"
        order_by = (self.order_by,)
        cursor.execute("INSERT INTO sort(order_by)  VALUES(%s)", order_by)
        # Call the sort_and_update_content function
        self.action_callback(self.order_by)
        