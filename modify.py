# modify.py
import tkinter as tk
from tkinter import ttk
import mysql.connector as sql

db = sql.connect(host="localhost",user="root",password="root",database="comics",port=3306,autocommit=True)
cursor = db.cursor(buffered=True)

class ModifySubMenu:
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
        submenu_texts = ["Add Comic", "Delete Comic", "Update Comic"]

        submenu_frame = tk.Frame(self.parent_frame, bg="#1A1918")
        submenu_frame.grid(row=self.index * 5, column=0, padx=10, pady=(self.button_padding[0] if self.index == 0 else self.button_padding[1]))

        main_button = tk.Label(
            submenu_frame,
            text="Modify",
            width=self.button_width,
            height=self.button_height,
            font=(self.button_font[0], self.button_font[1], "bold"),  # Add the "bold" attribute
            bg="#1A1918",
            fg="#F5F5F5",
            cursor="hand2",
            anchor="w"
        )
        main_button.grid(row=0, column=0, sticky="w")
        main_button.bind("<Button-1>", lambda e, f=submenu_frame: self.toggle_submenu(f))
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
            sub_button.bind("<Button-1>", lambda e, t=sub_label: self.modify_action(t))
            sub_button.bind("<Enter>", lambda e, b=sub_button: b.configure(bg="#3C3C3C", fg="#FFFFFF"))
            sub_button.bind("<Leave>", lambda e, b=sub_button: b.configure(bg="#1A1918", fg="#F5F5F5"))

            sub_button.grid_remove()

        self.submenu_frame = submenu_frame
        self.buttons = [main_button] + [sub_button for sub_button in submenu_frame.children.values()][1:]

    def toggle_submenu(self, event=None):
        any_visible = any(button.winfo_viewable() for button in self.buttons[1:])
        
        for button in self.buttons[1:]:
            if any_visible:
                button.grid_remove()
            else:
                button.grid()

    def modify_action(self, button_text):
        if button_text == "Add Comic":
            self.add_comic()
        elif button_text == "Delete Comic":
            self.delete_comic()
        elif button_text == "Update Comic":
            self.update_comic()
        else:
            return  # Do nothing if it's not a modify button

    def add_comic(self):
        add_window = tk.Toplevel(self.parent_frame)
        add_window.title("Add Comic")
        add_window.geometry("400x400")

        labels = ["Title", "Author", "Artist", "Publisher", "Publish Date", "Genre", "Issue Number", "Series", "Cover Image URL", "Language", "Synopsis"]
        entries = []

        for index, label in enumerate(labels):
            label_widget = tk.Label(add_window, text=label, anchor="w")
            label_widget.grid(row=index, column=0, padx=(10, 0), pady=(10, 0), sticky="w")

            entry_widget = tk.Entry(add_window, width=40)  # Change the width of the Entry widget
            entry_widget.grid(row=index, column=1, padx=(10, 0), pady=(10, 0), sticky="w")
            entries.append(entry_widget)

        submit_button = tk.Button(add_window, text="Submit", command=lambda: self.add_to_database(add_window, entries))
        submit_button.grid(row=len(labels), column=1, pady=(10, 0))
        
        add_window.bind('<Return>', lambda event: self.add_to_database(add_window, entries))

    def add_to_database(self, window, entries):
        comic_data = tuple(entry.get() for entry in entries)
        cursor.execute("""INSERT INTO comics(
            title, author, artist, publisher, public_date, genre,
            issue_number, series, cover_image, language, synopsis)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", comic_data)
        print("Comic", comic_data[0], "has been added")
        window.destroy()

    def delete_comic(self):
        delete_window = tk.Toplevel(self.parent_frame)
        delete_window.title("Delete Comic")
        delete_window.geometry("400x100")

        title_label = tk.Label(delete_window, text="Title", anchor="w")
        title_label.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="w")

        title_entry = tk.Entry(delete_window, width=40)  # Change the width of the Entry widget
        title_entry.grid(row=0, column=1, padx=(10, 20), pady=(10, 0), sticky="w")  # Add gap between the label and textbox

        submit_button = tk.Button(delete_window, text="Submit", command=lambda: self.delete_from_database(delete_window, title_entry.get()))
        submit_button.grid(row=1, column=1, pady=(10, 0))

        delete_window.bind('<Return>', lambda event: self.delete_from_database(delete_window, title_entry.get()))


    def delete_from_database(self, window, title):
        title_tuple = (title,)
        cursor.execute("DELETE FROM comics WHERE title=%s", title_tuple)
        print("Comic", title, "has been deleted")
        window.destroy()


    def update_comic(self):
        update_window = tk.Toplevel(self.parent_frame)
        update_window.title("Update Comic")
        update_window.geometry("400x100")

        title_label = tk.Label(update_window, text="Title", anchor="w")
        title_label.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="w")

        title_entry = tk.Entry(update_window, width=40)  # Change the width of the Entry widget
        title_entry.grid(row=0, column=1, padx=(10, 20), pady=(10, 0), sticky="w")  # Add gap between the label and textbox

        submit_button = tk.Button(update_window, text="Submit", command=lambda: self.fetch_comic_details(update_window, title_entry.get()))
        submit_button.grid(row=1, column=1, pady=(10, 0))

        update_window.bind('<Return>', lambda event: self.fetch_comic_details(update_window, title_entry.get()))


    def fetch_comic_details(self, window, title):
        title_tuple = (title,)
        cursor.execute("SELECT * from comics WHERE title=%s", title_tuple)
        comic_data = cursor.fetchone()

        if comic_data:
            window.destroy()
            self.display_update_form(title, comic_data)
        else:
            print("Comic not found")

    def display_update_form(self, original_title, comic_data):
        update_form = tk.Toplevel(self.parent_frame)
        update_form.title("Update Comic")
        update_form.geometry("400x350")

        labels = ["Title", "Author", "Artist", "Publisher", "Publish Date", "Genre", "Issue Number", "Series", "Cover Image", "Language", "Synopsis"]
        entries = []

        for index, label in enumerate(labels):
            tk.Label(update_form, text=label).grid(row=index, column=0, padx=(10, 0), pady=(10, 0))
            entry = tk.Entry(update_form)
            entry.insert(0, comic_data[index])
            entry.grid(row=index, column=1, padx=(0, 10), pady=(10, 0))
            entries.append(entry)

        submit_button = ttk.Button(update_form, text="Update", command=lambda: self.update_in_database(update_form, original_title, [entry.get() for entry in entries]))
        submit_button.grid(row=len(labels), column=1, pady=(10, 0))

    def update_in_database(self, window, original_title, new_comic_data):
        new_comic_data.append(original_title)
        updated_data_tuple = tuple(new_comic_data)

        cursor.execute("""UPDATE comics
            SET title=%s, author=%s, artist=%s, publisher=%s, public_date=%s, genre=%s, 
            issue_number=%s, series=%s, cover_image=%s, language=%s, synopsis=%s 
            WHERE title=%s """, updated_data_tuple)

        print("Comic", original_title, "has been updated")
        window.destroy()

    @staticmethod
    def comic_input(self):
        title = input(str("title: "))
        author = input(str("author: "))
        artist = input(str("artist: "))
        publisher = input(str("publisher: "))
        public_date = input(str("publisher_date: "))
        genre = input(str("genre: "))
        issue_number = input(str("issue_number: "))
        series = input(str("series: "))
        cover_image = input(str("cover_image: "))
        language = input(str("language: "))
        synopsis = input(str("synopsis: "))
        comic_data = (title, author, artist, publisher, public_date, genre, issue_number, series, cover_image, language, synopsis)
        return comic_data