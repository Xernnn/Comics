import tkinter as tk
import tkinter.messagebox
import user_queries
import mysql.connector.errors
import mysql.connector as sql

class Delete:
    def __init__(self, window):
        self.window = window
        self.create_delete_window()

    def create_delete_window(self):
        self.delete_window = tk.Toplevel(self.window)
        self.delete_window.iconbitmap('images/ch.ico')
        self.delete_window.title("Delete")

        # Center the window on the screen
        window_width = 300
        window_height = 250
        screen_width = self.delete_window.winfo_screenwidth()
        screen_height = self.delete_window.winfo_screenheight()

        x_position = int((screen_width / 2) - (window_width / 2))
        y_position = int((screen_height / 2) - (window_height / 2))

        self.delete_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Create a frame to contain the widgets
        register_frame = tk.Frame(self.delete_window)
        register_frame.pack(pady=(40, 0))

        # Create labels and entry fields for username, email, and password
        username_label = tk.Label(register_frame, text="Username:")
        username_label.grid(row=0, column=0, pady=(0, 5), sticky=tk.W)

        self.username_entry = tk.Entry(register_frame)
        self.username_entry.grid(row=0, column=1, pady=(0, 5), padx=(2, 0), sticky=tk.W)

        # Create a frame to contain the buttons
        button_frame = tk.Frame(register_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=(10, 0))

        # Register button
        self.register_button = tk.Button(
            button_frame,
            text="Delete",
            command=self.delete_user
        )
        self.register_button.pack()

    def delete_user(self):
        db = sql.connect(host="localhost", user="root", password="root", database="comics", port=3306, autocommit=True)
        cursor = db.cursor(buffered=True)
        username = self.username_entry.get()
        data = (username,)
        cursor.execute("DELETE FROM users WHERE username = %s", data)
        self.delete_window.destroy()
