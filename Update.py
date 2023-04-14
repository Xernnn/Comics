import tkinter as tk
import tkinter.messagebox
import user_queries
import mysql.connector.errors


class Update:
    def __init__(self, window):
        self.window = window
        self.create_update_window()
        self.update_data = None

    def create_update_window(self):
        self.update_window = tk.Toplevel(self.window)
        self.update_window.title("Update")

        # Center the window on the screen
        window_width = 300
        window_height = 250
        screen_width = self.update_window.winfo_screenwidth()
        screen_height = self.update_window.winfo_screenheight()

        x_position = int((screen_width / 2) - (window_width / 2))
        y_position = int((screen_height / 2) - (window_height / 2))

        self.update_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Create a frame to contain the widgets
        update_frame = tk.Frame(self.update_window)
        update_frame.pack(pady=(40, 0))

        # Create labels and entry fields for username, email, and password
        age_label = tk.Label(update_frame, text="Age:")
        age_label.grid(row=0, column=0, pady=(0, 5), sticky=tk.W)

        self.age_entry = tk.Entry(update_frame)
        self.age_entry.grid(row=0, column=1, pady=(0, 5), padx=(2, 0), sticky=tk.W)

        membersince_label = tk.Label(update_frame, text="Member Since:")
        membersince_label.grid(row=1, column=0, pady=(0, 5), sticky=tk.W)

        self.membersince_entry = tk.Entry(update_frame)
        self.membersince_entry.grid(row=1, column=1, pady=(0, 5), padx=(2, 0), sticky=tk.W)

        favorite_label = tk.Label(update_frame, text="Favorite:")
        favorite_label.grid(row=2, column=0, pady=(0, 5), sticky=tk.W)

        self.favorite_entry = tk.Entry(update_frame, show="*")
        self.favorite_entry.grid(row=2, column=1, pady=(0, 5), padx=(2, 0), sticky=tk.W)

        # Create a frame to contain the buttons
        button_frame = tk.Frame(update_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=(10, 0))

        # Register button
        self.update_button = tk.Button(
            button_frame,
            text="Update",
            command=self.update_user
        )
        self.update_button.pack()

    def update_user(self):
        membersince = self.membersince_entry.get()
        favorite = self.favorite_entry.get()
        age = self.age_entry.get()
        if self.update_data_callback:
            self.update_data_callback(age, membersince, favorite)
        self.update_window.destroy()
