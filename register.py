import tkinter as tk
import tkinter.messagebox
import user_queries
import mysql.connector.errors

class Register:
    def __init__(self, window):
        self.window = window
        self.create_register_window()

    def create_register_window(self):
        self.register_window = tk.Toplevel(self.window)
        self.register_window.title("Register")

        # Center the window on the screen
        window_width = 300
        window_height = 250
        screen_width = self.register_window.winfo_screenwidth()
        screen_height = self.register_window.winfo_screenheight()

        x_position = int((screen_width / 2) - (window_width / 2))
        y_position = int((screen_height / 2) - (window_height / 2))

        self.register_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Create a frame to contain the widgets
        register_frame = tk.Frame(self.register_window)
        register_frame.pack(pady=(40, 0))

        # Create labels and entry fields for username, email, and password
        username_label = tk.Label(register_frame, text="Username:")
        username_label.grid(row=0, column=0, pady=(0, 5), sticky=tk.W)

        self.username_entry = tk.Entry(register_frame)
        self.username_entry.grid(row=0, column=1, pady=(0, 5), padx=(2, 0), sticky=tk.W)

        email_label = tk.Label(register_frame, text="Email:")
        email_label.grid(row=1, column=0, pady=(0, 5), sticky=tk.W)

        self.email_entry = tk.Entry(register_frame)
        self.email_entry.grid(row=1, column=1, pady=(0, 5), padx=(2, 0), sticky=tk.W)

        password_label = tk.Label(register_frame, text="Password:")
        password_label.grid(row=2, column=0, pady=(0, 5), sticky=tk.W)

        self.password_entry = tk.Entry(register_frame, show="*")
        self.password_entry.grid(row=2, column=1, pady=(0, 5), padx=(2, 0), sticky=tk.W)
        
        # Add the following lines in the create_register_window method, after the password_entry creation

        confirm_password_label = tk.Label(register_frame, text="Confirm Password:")
        confirm_password_label.grid(row=3, column=0, pady=(0, 5), sticky=tk.W)

        self.confirm_password_entry = tk.Entry(register_frame, show="*")
        self.confirm_password_entry.grid(row=3, column=1, pady=(0, 5), padx=(2, 0), sticky=tk.W)

        # Avatar label and entry field

        avatar_label = tk.Label(register_frame, text="Avatar Image Link:")
        avatar_label.grid(row=4, column=0, pady=(0, 5), sticky=tk.W)

        self.avatar_entry = tk.Entry(register_frame)
        self.avatar_entry.grid(row=4, column=1, pady=(0, 5), padx=(2, 0), sticky=tk.W)

        # Create a frame to contain the buttons
        button_frame = tk.Frame(register_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=(10, 0))

        # Register button
        self.register_button = tk.Button(
            button_frame,
            text="Register",
            command=self.register_user
        )
        self.register_button.pack()

    def register_user(self):
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            error_msg = "Passwords do not match. Please re-enter your passwords."
            tk.messagebox.showerror("Error", error_msg)
            self.password_entry.delete(0, tk.END)
            self.confirm_password_entry.delete(0, tk.END)
            return
        try:
            user_data = {
                "username": self.username_entry.get(),
                "password": self.password_entry.get(),
                "gmail": self.email_entry.get(),
                "avatar": self.avatar_entry.get()
            }
            user_queries.add(user_data)
        except mysql.connector.errors.IntegrityError:
            error_msg = "This username is already used by someone else."
            tk.messagebox.showerror("Error", error_msg)
            self.password_entry.delete(0, tk.END)
            self.confirm_password_entry.delete(0, tk.END)
        # You can add more logic here to handle user registration
        print("User registered")
        self.register_window.destroy()
