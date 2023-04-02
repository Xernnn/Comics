import tkinter as tk

class ForgetPassword:
    def __init__(self, window):
        self.window = window

    def show_forget_password_window(self):
        self.forget_password_window = tk.Toplevel(self.window)
        self.forget_password_window.title("Forget Password")

        # Center the window on the screen
        window_width = 300
        window_height = 200
        screen_width = self.forget_password_window.winfo_screenwidth()
        screen_height = self.forget_password_window.winfo_screenheight()

        x_position = int((screen_width / 2) - (window_width / 2))
        y_position = int((screen_height / 2) - (window_height / 2))

        self.forget_password_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Create a frame to contain the widgets
        forget_password_frame = tk.Frame(self.forget_password_window)
        forget_password_frame.pack(pady=(40, 0))

        # Username and email labels and entry fields
        username_label = tk.Label(forget_password_frame, text="Username:")
        username_label.grid(row=0, column=0, pady=(0, 5), sticky=tk.W)

        self.username_entry = tk.Entry(forget_password_frame)
        self.username_entry.grid(row=0, column=1, pady=(0, 5), padx=(2, 0), sticky=tk.W)

        email_label = tk.Label(forget_password_frame, text="Email:")
        email_label.grid(row=1, column=0, pady=(5, 0), sticky=tk.W)

        self.email_entry = tk.Entry(forget_password_frame)
        self.email_entry.grid(row=1, column=1, pady=(5, 0), padx=(2, 0), sticky=tk.W)

        # Create a frame to contain the buttons
        button_frame = tk.Frame(forget_password_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        # Retrieve Password button
        self.retrieve_password_button = tk.Button(
            button_frame,
            text="Retrieve Password",
            command=self.retrieve_password
        )
        self.retrieve_password_button.grid(row=0, column=0, padx=(0, 10), pady=(0, 5))

    def retrieve_password(self):
        # You can add more logic here to handle actual password retrieval
        print("Password retrieved")
        self.forget_password_window.destroy()